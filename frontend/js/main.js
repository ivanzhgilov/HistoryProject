import { initActiveMenu } from "./modules/active-menu.js";
import { initBurgerMenu } from "./modules/burger-menu.js";
import { initRevealAnimation } from "./modules/reveal.js";
import { initSmoothAnchors } from "./modules/smooth-anchors.js";
import { initScrollToTopButton } from "./modules/scroll-top.js";

document.addEventListener("DOMContentLoaded", () => {
  initActiveMenu();
  initBurgerMenu();
  initRevealAnimation();
  initSmoothAnchors();
  initScrollToTopButton();
});
