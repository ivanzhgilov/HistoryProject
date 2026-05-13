import { CLASSES, SELECTORS } from "../config.js";
import { qsa } from "../utils.js";

export function initRevealAnimation() {
  const items = qsa(SELECTORS.revealItems);
  if (!items.length) return;

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add(CLASSES.visible);
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -30px 0px" }
  );

  items.forEach((item) => observer.observe(item));
}
