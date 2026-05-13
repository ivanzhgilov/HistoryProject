import { CLASSES, SELECTORS } from "../config.js";
import { getCurrentPage, qsa } from "../utils.js";

export function initActiveMenu() {
  const current = getCurrentPage();
  qsa(SELECTORS.navLink).forEach((link) => {
    const isActive = link.getAttribute("data-page") === current;
    link.classList.toggle(CLASSES.active, isActive);
  });
}
