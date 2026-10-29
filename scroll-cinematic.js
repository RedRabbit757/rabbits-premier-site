/* ============================================================
   Scroll engine — canvas frame-sequence scrub sections
   Config lives in window.SCRUB_SECTIONS (see index.html).
   Sections with lazy:true start preloading when they near the viewport.
   ============================================================ */
function initScrub(cfg) {
  const section = document.querySelector(cfg.section);
  const canvas  = section.querySelector("canvas");
  const ctx     = canvas.getContext("2d", { alpha: false });
  const lines   = [...section.querySelectorAll(".reveal-line")];
  const bar     = section.querySelector(".progress i");
  const loader  = section.querySelector(".loader");
  const bgFill  = cfg.bg || "#0b1a12";
  const images = [];
  let loaded = 0, started = false, current = -1;

  function preload() {
    if (started) return;
    started = true;
    for (let i = 0; i < cfg.frameCount; i++) {
      const img = new Image();
      img.decoding = "async";
      img.onload = img.onerror = () => {
        loaded++;
        if (i === 0 || current < 0) draw(Math.max(current, 0));
        if (loader) {
          loader.textContent = `Loading ${Math.round((loaded / cfg.frameCount) * 100)}%`;
          if (loaded === cfg.frameCount) loader.style.opacity = "0";
        }
      };
      img.src = cfg.framePath(i + 1);
      images[i] = img;
    }
  }

  function draw(index) {
    // fall back to the nearest loaded frame so fast scrolling never shows a blank
    let img = images[index], k = index;
    while (k > 0 && !(img && img.complete && img.naturalWidth)) img = images[--k];
    if (!img || !img.complete || !img.naturalWidth) return;
    const cw = canvas.clientWidth, ch = canvas.clientHeight;
    const ir = img.naturalWidth / img.naturalHeight, cr = cw / ch;
    let dw, dh, dx, dy;
    if (ir > cr) { dh = ch; dw = ch * ir; dx = (cw - dw) * (cfg.focusX ?? 0.5); dy = 0; }
    else         { dw = cw; dh = cw / ir; dx = 0; dy = (ch - dh) / 2; }
    ctx.fillStyle = bgFill; ctx.fillRect(0, 0, cw, ch);
    ctx.drawImage(img, dx, dy, dw, dh);
  }

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width  = canvas.clientWidth  * dpr;
    canvas.height = canvas.clientHeight * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw(current < 0 ? 0 : current);
  }

  function update() {
    const rect = section.getBoundingClientRect();
    if (!started && rect.top < window.innerHeight * 2.5) preload();
    if (rect.bottom < -window.innerHeight || rect.top > window.innerHeight) return;
    const scrollable = rect.height - window.innerHeight;
    const p = Math.min(Math.max(-rect.top / scrollable, 0), 1);
    const idx = Math.min(cfg.frameCount - 1, Math.floor(p * (cfg.frameCount - 1)));
    if (idx !== current) { current = idx; draw(idx); }
    if (bar) bar.style.width = (p * 100).toFixed(2) + "%";
    for (const el of lines) {
      const a = parseFloat(el.dataset.in), b = parseFloat(el.dataset.out);
      // first line starts fully visible; last line holds at the end
      const holdStart = a <= 0, holdEnd = b >= 1;
      const fade = 0.07;
      let o;
      if (p < a) o = holdStart ? 1 : 0;
      else if (p > b) o = holdEnd ? 1 : 0;
      else {
        const fin = holdStart ? 1 : Math.min(1, (p - a) / fade);
        const fout = holdEnd ? 1 : Math.min(1, (b - p) / fade);
        o = Math.min(fin, fout);
      }
      el.style.opacity = o.toFixed(3);
      el.style.transform = `translateY(${(1 - o) * 28}px)`;
      el.classList.toggle("live", o > 0.6);
      el.setAttribute("aria-hidden", o < 0.05 ? "true" : "false");
    }
  }

  if (!cfg.lazy) preload();
  window.addEventListener("resize", resize);
  resize();
  return { update, resize };
}

document.addEventListener("DOMContentLoaded", () => {
  const scrubs = (window.SCRUB_SECTIONS || [])
    .filter(c => document.querySelector(c.section))
    .map(initScrub);

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let lenis = null;
  if (window.Lenis && !reduce) {
    lenis = new Lenis({ lerp: 0.09, smoothWheel: true });
    window.__lenis = lenis;
  }
  function raf(t) { if (lenis) lenis.raf(t); scrubs.forEach(s => s.update()); requestAnimationFrame(raf); }
  requestAnimationFrame(raf);

  const hints = document.querySelectorAll(".scroll-hint");
  window.addEventListener("scroll", () => {
    hints.forEach(h => h.style.opacity = window.scrollY > 60 ? "0" : "1");
  }, { passive: true });
});
