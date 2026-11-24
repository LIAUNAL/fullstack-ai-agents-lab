"use client";

import { FormEvent, useState } from "react";
import { ApprovalCard } from "@/components/ApprovalCard";
import { useAgentStream } from "@/hooks/useAgentStream";

export default function HomePage() {
  const [input, setInput] = useState("");
  const [threadId] = useState("lab-session-01");
  const {
    stage,
    toolOutput,
    answer,
    pendingApproval,
    isStreaming,
    error,
    sendMessage,
    resolveApproval,
  } = useAgentStream();

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isStreaming) return;
    await sendMessage({ threadId, message: input.trim() });
    setInput("");
  };

  return (
    <main className="mx-auto flex min-h-screen max-w-3xl flex-col gap-6 px-4 py-10">
      <header className="space-y-1 border-b border-slate-800 pb-4">
        <h1 className="text-2xl font-bold tracking-tight">
          Full-Stack AI Agents Lab
        </h1>
        <p className="text-sm text-slate-400">
          Módulo 4 · Streaming SSE + Estado de herramientas + Human-in-the-Loop
        </p>
      </header>

      <form onSubmit={handleSubmit} className="flex gap-3">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ej: Consultar estado o Deploy model to production..."
          className="flex-1 rounded-lg border border-slate-700 bg-slate-900 px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:border-sky-500 focus:outline-none"
        />
        <button
          type="submit"
          disabled={isStreaming}
          className="rounded-lg bg-sky-600 px-5 py-2.5 text-sm font-medium text-white hover:bg-sky-500 disabled:opacity-50"
        >
          {isStreaming ? "Ejecutando..." : "Enviar"}
        </button>
      </form>

      <section className="rounded-xl border border-slate-800 bg-slate-900/60 p-4">
        <div className="flex items-center justify-between text-xs text-slate-400">
          <span>Estado del agente (Pensamiento / Herramientas)</span>
          <span className="rounded-full bg-slate-800 px-2.5 py-0.5 font-mono text-sky-300">
            {stage}
          </span>
        </div>
        {toolOutput && (
          <p className="mt-2 font-mono text-xs text-emerald-300">{toolOutput}</p>
        )}
      </section>

      {pendingApproval && (
        <ApprovalCard
          approval={pendingApproval}
          disabled={isStreaming}
          onApprove={() => resolveApproval(true)}
          onReject={() => resolveApproval(false)}
        />
      )}

      {error && (
        <div className="rounded-lg border border-rose-500/40 bg-rose-950/40 p-3 text-sm text-rose-300">
          {error}
        </div>
      )}

      <section className="min-h-32 rounded-xl border border-slate-800 bg-slate-900 p-5">
        <h2 className="mb-2 text-xs font-semibold uppercase tracking-wider text-slate-400">
          Respuesta Final
        </h2>
        <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-100">
          {answer || "Envía una consulta para iniciar el stream SSE."}
        </p>
      </section>
    </main>
  );
}
