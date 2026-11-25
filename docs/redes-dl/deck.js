(function () {
  const e = React.createElement;
  const RF = window.ReactFlow;
  const ReactFlowComp = RF.default || RF.ReactFlow;
  const { Background, Controls, Handle, Position, ReactFlowProvider } = RF;

  const PHASE_META = {
    empatizar: { label: "1. Empatizar", color: "#00A8E0" },
    definir: { label: "2. Definir", color: "#E9572B" },
    idear: { label: "3. Idear", color: "#4DB922" },
    prototipar: { label: "4. Prototipar", color: "#FF8A00" },
    evaluar: { label: "5. Evaluar", color: "#3763A9" },
    portada: { label: "Bloque · 60 min/clase", color: "#0D1B33" }
  };

  function MiniNode({ data }) {
    return e(
      "div",
      { className: "rf-mini-node", style: { borderColor: data.color || "#3763A9" } },
      e(Handle, { type: "target", position: Position.Left, style: { background: data.color || "#3763A9" } }),
      e("strong", null, data.label),
      e("span", null, data.sub || ""),
      e(Handle, { type: "source", position: Position.Right, style: { background: data.color || "#3763A9" } })
    );
  }

  const nodeTypes = { mini: MiniNode };

  function InteractiveDiagram({ diagram }) {
    const [note, setNote] = React.useState(
      diagram.defaultNote || "Haz clic en cualquier nodo del diagrama para ver su explicación."
    );
    return e(
      React.Fragment,
      null,
      e(
        "div",
        { className: "diagram-box" },
        e(
          ReactFlowProvider,
          null,
          e(
            ReactFlowComp,
            {
              style: { width: "100%", height: "100%" },
              nodes: diagram.nodes.map((n) => ({ ...n, type: "mini" })),
              edges: diagram.edges,
              nodeTypes,
              fitView: true,
              fitViewOptions: { padding: 0.18 },
              minZoom: 0.35,
              maxZoom: 1.5,
              onNodeClick: (_, node) => {
                if (node.data && node.data.detail) setNote(node.data.detail);
              }
            },
            e(Background, { gap: 16, color: "#E2E8F0" }),
            e(Controls, null)
          )
        )
      ),
      e("div", { className: "diagram-note" }, note)
    );
  }

  function DeckApp({ config }) {
    const storageKey = "deck-redes-" + config.id;
    const slides = config.slides;
    const [idx, setIdx] = React.useState(() => {
      try {
        const s = Number(localStorage.getItem(storageKey));
        if (Number.isFinite(s) && s >= 0 && s < slides.length) return s;
      } catch (_) {}
      return 0;
    });
    const [focus, setFocus] = React.useState(false);

    const go = React.useCallback(
      (next) => {
        const clamped = Math.max(0, Math.min(next, slides.length - 1));
        setIdx(clamped);
        try {
          localStorage.setItem(storageKey, String(clamped));
        } catch (_) {}
      },
      [slides.length, storageKey]
    );

    React.useEffect(() => {
      const onKey = (ev) => {
        if (ev.key === "ArrowRight" || ev.key === "PageDown") {
          ev.preventDefault();
          go(idx + 1);
        } else if (ev.key === "ArrowLeft" || ev.key === "PageUp") {
          ev.preventDefault();
          go(idx - 1);
        } else if (ev.key === "Home") {
          ev.preventDefault();
          go(0);
        } else if (ev.key === "End") {
          ev.preventDefault();
          go(slides.length - 1);
        } else if (ev.key.toLowerCase() === "f") {
          ev.preventDefault();
          setFocus((p) => !p);
        }
      };
      window.addEventListener("keydown", onKey);
      return () => window.removeEventListener("keydown", onKey);
    }, [go, idx, slides.length]);

    React.useEffect(() => {
      document.body.classList.toggle("focus-mode", focus);
      return () => document.body.classList.remove("focus-mode");
    }, [focus]);

    React.useEffect(() => {
      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise().catch(() => {});
      }
    }, [idx]);

    const slide = slides[idx];
    const phase = PHASE_META[slide.phase] || PHASE_META.portada;

    return e(
      "div",
      { className: "deck-shell" },
      e(
        "aside",
        { className: "deck-rail" },
        e("div", { className: "rail-brand" }, "Redes Neuronales y DL · SIA 18373"),
        e("h1", { className: "rail-title-main" }, config.title),
        e("a", { className: "rail-back", href: "../index.html" }, "← Volver al Path Curricular"),
        slides.map((s, i) => {
          const p = PHASE_META[s.phase] || PHASE_META.portada;
          return e(
            "button",
            {
              key: i,
              type: "button",
              className: "rail-item" + (i === idx ? " active" : ""),
              style: { borderLeftColor: p.color },
              onClick: () => go(i)
            },
            e("span", { className: "r-phase" }, p.label),
            s.navTitle || s.title
          );
        })
      ),
      e(
        "main",
        { className: "deck-stage" },
        e(
          "article",
          { className: "slide-card", style: { borderTopColor: phase.color } },
          e(
            "div",
            { className: "slide-head" },
            e("span", { className: "phase-pill", style: { background: phase.color } }, phase.label),
            e("span", { className: "slide-time" }, slide.time || "Primeros 60 min · Cápsula + Worked Example")
          ),
          e("h2", { className: "slide-title" }, slide.title),
          slide.lead && e("p", { className: "slide-lead" }, slide.lead),
          slide.equation && e("div", { className: "eq-box" }, slide.equation),
          slide.boxes &&
            e(
              "div",
              { className: "slide-grid" },
              slide.boxes.map((b, bi) =>
                e(
                  "div",
                  { key: bi, className: "info-box" },
                  e("h4", null, b.heading),
                  e("ul", null, b.items.map((it, ii) => e("li", { key: ii }, it)))
                )
              )
            ),
          slide.diagram && e(InteractiveDiagram, { key: idx, diagram: slide.diagram })
        )
      ),
      e(
        "footer",
        { className: "deck-footer" },
        e(
          "div",
          { className: "nav-btns" },
          e("button", { type: "button", className: "nav-btn", disabled: idx === 0, onClick: () => go(idx - 1) }, "← Anterior"),
          e("button", { type: "button", className: "nav-btn primary", disabled: idx === slides.length - 1, onClick: () => go(idx + 1) }, "Siguiente →"),
          e("button", { type: "button", className: "nav-btn", onClick: () => setFocus((p) => !p) }, focus ? "Mostrar menú (f)" : "Modo enfoque (f)")
        ),
        e("span", { className: "counter" }, String(idx + 1).padStart(2, "0") + " / " + String(slides.length).padStart(2, "0"))
      )
    );
  }

  window.renderRedesDeck = function (config) {
    ReactDOM.createRoot(document.getElementById("root")).render(e(DeckApp, { config }));
  };
})();
