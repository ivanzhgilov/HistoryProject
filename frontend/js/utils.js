export const qs = (s, r = document) => r.querySelector(s);
export const qsa = (s, r = document) => Array.from(r.querySelectorAll(s));
export const on = (t, e, h, o) => t.addEventListener(e, h, o);
export const getCurrentPage = () => {
  const last = window.location.pathname.split("/").filter(Boolean).pop() || "index";
  return last.endsWith(".html") ? last.slice(0, -5) : last;
};

export function animateScrollToTop(durationMs) {
  const startY = window.scrollY;
  if (startY <= 0) return;
  const startTime = performance.now();
  const ease = (x) => 1 - Math.pow(1 - x, 3);
  const step = (now) => {
    const p = Math.min((now - startTime) / durationMs, 1);
    window.scrollTo(0, Math.round(startY * (1 - ease(p))));
    if (p < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}
