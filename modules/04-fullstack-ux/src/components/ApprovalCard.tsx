"use client";

import type { PendingApproval } from "@/hooks/useAgentStream";

interface ApprovalCardProps {
  approval: PendingApproval;
  disabled?: boolean;
  onApprove: () => void;
  onReject: () => void;
}

export function ApprovalCard({
  approval,
  disabled = false,
  onApprove,
  onReject,
}: ApprovalCardProps) {
  return (
    <div className="rounded-xl border border-amber-500/40 bg-amber-950/30 p-4 shadow-lg">
      <div className="mb-2 flex items-center justify-between">
        <span className="text-xs font-semibold uppercase tracking-wider text-amber-300">
          Human-in-the-Loop · Confirmación Requerida
        </span>
        <span className="text-xs text-slate-400">Thread: {approval.threadId}</span>
      </div>
      <p className="text-sm text-slate-200">{approval.reason}</p>
      <pre className="mt-2 overflow-x-auto rounded bg-slate-900 p-2 text-xs text-amber-200">
        {approval.action}
      </pre>
      <div className="mt-4 flex gap-3">
        <button
          type="button"
          disabled={disabled}
          onClick={onApprove}
          className="rounded-lg bg-emerald-600 px-4 py-2 text-sm font-medium text-white hover:bg-emerald-500 disabled:opacity-50"
        >
          Aprobar ejecución
        </button>
        <button
          type="button"
          disabled={disabled}
          onClick={onReject}
          className="rounded-lg bg-rose-700 px-4 py-2 text-sm font-medium text-white hover:bg-rose-600 disabled:opacity-50"
        >
          Rechazar
        </button>
      </div>
    </div>
  );
}
