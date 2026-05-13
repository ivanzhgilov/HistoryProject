import { SELECTORS } from "../config.js";
import { on, qsa } from "../utils.js";

export function initSmoothAnchors() {
  qsa(SELECTORS.anchorLinks).forEach((anchor) => {
    on(anchor, "click", (event) => {
      const href = anchor.getAttribute("href");
      if (!href || href.length < 2) return;

      const target = document.querySelector(href);
      if (!target) return;

      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
}
