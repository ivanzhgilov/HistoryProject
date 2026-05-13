import { CLASSES, SCROLL } from "../config.js";
import { animateScrollToTop, on } from "../utils.js";

export function initScrollToTopButton() {
  const button = document.createElement("button");
  button.className = "scroll-top-btn";
  button.setAttribute("aria-label", "Наверх");
  button.textContent = "↑";
  document.body.appendChild(button);

  const sync = () => {
    button.classList.toggle(CLASSES.visible, window.scrollY > SCROLL.topButtonThreshold);
  };

  on(window, "scroll", sync, { passive: true });
  on(button, "click", () => animateScrollToTop(SCROLL.topButtonDurationMs));
  sync();
}
