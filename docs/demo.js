(function () {
  const compare = document.getElementById("compare");
  const slider = document.getElementById("slider");
  const handle = document.getElementById("handle");
  const paneBefore = document.getElementById("pane-before");
  const paneAfter = document.getElementById("pane-after");
  const themeToggle = document.getElementById("theme-toggle");
  const logoDay = document.querySelector(".logo-day");
  const logoNight = document.querySelector(".logo-night");

  let dragging = false;
  let activePointerId = null;
  let scrollBound = false;

  const narrowMq = window.matchMedia("(max-width: 480px)");

  function isVertical() {
    return narrowMq.matches;
  }

  function defaultPos() {
    return isVertical() ? 50 : 70;
  }

  function setTheme(theme) {
    const next = theme === "night" ? "night" : "light";
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem("openbook-demo-theme", next);
    } catch (_) {
      /* private mode */
    }
    if (themeToggle) {
      const night = next === "night";
      themeToggle.setAttribute("aria-pressed", night ? "true" : "false");
      themeToggle.textContent = night ? "Day" : "Night";
    }
    if (logoDay && logoNight) {
      logoDay.hidden = next === "night";
      logoNight.hidden = next !== "night";
    }
  }

  if (themeToggle) {
    let stored = "light";
    try {
      stored = localStorage.getItem("openbook-demo-theme") || "light";
    } catch (_) {
      stored = "light";
    }
    setTheme(stored);
    themeToggle.addEventListener("click", () => {
      const cur = document.documentElement.getAttribute("data-theme");
      setTheme(cur === "night" ? "light" : "night");
    });
  }

  if (!compare || !slider || !handle) {
    return;
  }

  function setPos(pct) {
    const v = Math.max(0, Math.min(100, pct));
    compare.style.setProperty("--pos", v + "%");
    slider.value = String(Math.round(v));
    handle.setAttribute("aria-valuenow", String(Math.round(v)));
    handle.setAttribute(
      "aria-label",
      isVertical()
        ? "Reveal OpenBook Brief below the status dump"
        : "Reveal OpenBook Brief over the status dump"
    );
  }

  function posFromClient(clientX, clientY) {
    const rect = compare.getBoundingClientRect();
    if (isVertical()) {
      return ((clientY - rect.top) / rect.height) * 100;
    }
    return ((clientX - rect.left) / rect.width) * 100;
  }

  function startDrag(e) {
    if (e.pointerType === "mouse" && e.button !== 0) return;
    dragging = true;
    activePointerId = e.pointerId;
    compare.classList.add("is-dragging");
    document.body.style.cursor = isVertical() ? "ns-resize" : "ew-resize";
    document.body.style.userSelect = "none";
    try {
      handle.setPointerCapture(e.pointerId);
    } catch (_) {
      /* older browsers */
    }
    setPos(posFromClient(e.clientX, e.clientY));
    e.preventDefault();
  }

  function moveDrag(e) {
    if (!dragging) return;
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    setPos(posFromClient(e.clientX, e.clientY));
    e.preventDefault();
  }

  function endDrag(e) {
    if (!dragging) return;
    if (activePointerId !== null && e.pointerId !== activePointerId) return;
    dragging = false;
    activePointerId = null;
    compare.classList.remove("is-dragging");
    document.body.style.cursor = "";
    document.body.style.userSelect = "";
    try {
      if (e && e.pointerId != null) handle.releasePointerCapture(e.pointerId);
    } catch (_) {
      /* ignore */
    }
  }

  function scrollMax(win) {
    const doc = win.document;
    const el = doc.scrollingElement || doc.documentElement;
    return Math.max(1, el.scrollHeight - win.innerHeight);
  }

  function syncScroll() {
    try {
      const a = paneAfter.contentWindow;
      const b = paneBefore.contentWindow;
      if (!a || !b || !a.document || !b.document) return;
      if (scrollBound) return;
      if (a.document.readyState !== "complete" || b.document.readyState !== "complete") {
        return;
      }
      scrollBound = true;

      let lock = false;
      let raf = 0;

      const bind = (from, to) => {
        from.addEventListener(
          "scroll",
          () => {
            if (lock || dragging) return;
            if (raf) cancelAnimationFrame(raf);
            raf = requestAnimationFrame(() => {
              raf = 0;
              if (dragging) return;
              lock = true;
              const next = (from.scrollY / scrollMax(from)) * scrollMax(to);
              if (Math.abs(to.scrollY - next) > 1) {
                to.scrollTo({ top: next, left: 0, behavior: "instant" });
              }
              // Hold the lock one more frame so the peer scroll event is ignored
              requestAnimationFrame(() => {
                lock = false;
              });
            });
          },
          { passive: true }
        );
      };
      bind(a, b);
      bind(b, a);
    } catch (_) {
      /* file:// cross-frame may be restricted; slider still works */
    }
  }

  slider.addEventListener("input", () => setPos(Number(slider.value)));

  handle.addEventListener("pointerdown", startDrag);
  handle.addEventListener("pointermove", moveDrag);
  handle.addEventListener("pointerup", endDrag);
  handle.addEventListener("pointercancel", endDrag);
  handle.addEventListener("lostpointercapture", endDrag);

  handle.addEventListener("keydown", (e) => {
    const cur = Number(handle.getAttribute("aria-valuenow") || 70);
    if (e.key === "ArrowLeft") setPos(cur - 3);
    if (e.key === "ArrowRight") setPos(cur + 3);
    if (e.key === "Home") setPos(0);
    if (e.key === "End") setPos(100);
  });

  paneBefore.addEventListener("load", syncScroll);
  paneAfter.addEventListener("load", syncScroll);
  // srcdoc iframes may already be complete
  syncScroll();
  function applyLayout() {
    const stored = Number(slider.value);
    const fallback = defaultPos();
    if (!stored || (isVertical() && stored === 70) || (!isVertical() && stored === 50)) {
      setPos(fallback);
    } else {
      setPos(stored);
    }
  }

  narrowMq.addEventListener("change", applyLayout);
  applyLayout();
})();
