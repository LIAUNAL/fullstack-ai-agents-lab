"use client";

import { useCallback, useState } from "react";

export interface PendingApproval {
  threadId: string;
  action: string;
  reason: string;
}

interface StreamOptions {
  threadId: string;
  message: string;
  approved?: boolean | null;
}

const BACKEND_URL =
  process.env.NEXT_PUBLIC_BACKEND_URL ?? "http://localhost:8000";

export function useAgentStream() {
  const [stage, setStage] = useState<string>("idle");
  const [toolOutput, setToolOutput] = useState<string>("");
  const [answer, setAnswer] = useState<string>("");
  const [pendingApproval, setPendingApproval] =
    useState<PendingApproval | null>(null);
  const [isStreaming, setIsStreaming] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const sendMessage = useCallback(
    async ({ threadId, message, approved = null }: StreamOptions) => {
      setIsStreaming(true);
      setError(null);
      setStage("connecting");
      if (approved === null) {
        setAnswer("");
        setToolOutput("");
      }

      try {
        const response = await fetch(`${BACKEND_URL}/chat/stream`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            thread_id: threadId,
            message,
            approved,
          }),
        });

        if (!response.ok || !response.body) {
          throw new Error(`Error del backend: ${response.status}`);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = "";
        let currentEvent = "message";

        while (true) {
          const { value, done } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split("\n");
          buffer = lines.pop() ?? "";

          for (const rawLine of lines) {
            const line = rawLine.trim();
            if (line.startsWith("event:")) {
              currentEvent = line.slice(6).trim();
            } else if (line.startsWith("data:")) {
              const payload = JSON.parse(line.slice(5).trim());
              if (currentEvent === "status") {
                setStage(payload.stage ?? "working");
                if (payload.output) setToolOutput(payload.output);
              } else if (currentEvent === "approval_required") {
                setPendingApproval({
                  threadId: payload.thread_id,
                  action: payload.action,
                  reason: payload.reason,
                });
                setStage("waiting_approval");
              } else if (currentEvent === "token") {
                setStage("responding");
                setAnswer((prev) => prev + (payload.content ?? ""));
              } else if (currentEvent === "done") {
                setStage(payload.status ?? "completed");
              }
            }
          }
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : "Error desconocido");
        setStage("error");
      } finally {
        setIsStreaming(false);
      }
    },
    []
  );

  const resolveApproval = useCallback(
    async (approved: boolean) => {
      if (!pendingApproval) return;
      const current = pendingApproval;
      setPendingApproval(null);
      await sendMessage({
        threadId: current.threadId,
        message: current.action,
        approved,
      });
    },
    [pendingApproval, sendMessage]
  );

  return {
    stage,
    toolOutput,
    answer,
    pendingApproval,
    isStreaming,
    error,
    sendMessage,
    resolveApproval,
  };
}
