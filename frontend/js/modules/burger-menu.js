import { CLASSES, SELECTORS } from "../config.js";
import { on, qs, qsa } from "../utils.js";

export function initBurgerMenu() {
  const burger = qs(SELECTORS.burgerButton);
  const menu = qs(SELECTORS.mobileMenu);
  const overlay = qs(SELECTORS.menuOverlay);
  const closeButton = qs(SELECTORS.menuCloseButton);
  const links = qsa(SELECTORS.mobileMenuLinks);
  if (!burger || !menu || !overlay || !closeButton) return;

  const open = () => {
    document.body.classList.add(CLASSES.menuOpen);
    overlay.hidden = false;
    menu.hidden = false;
  };
  const close = () => {
    document.body.classList.remove(CLASSES.menuOpen);
    overlay.hidden = true;
    menu.hidden = true;
  };

  on(burger, "click", () => (document.body.classList.contains(CLASSES.menuOpen) ? close() : open()));
  on(closeButton, "click", close);
  on(overlay, "click", close);
  links.forEach((l) => on(l, "click", close));
  on(document, "keydown", (e) => e.key === "Escape" && close());
}
