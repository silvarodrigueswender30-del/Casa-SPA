function initCasaStats() {
  const nodes = document.querySelectorAll(".casa-stats__number[data-count]");
  if (!nodes.length) return;

  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const animate = (el, delay = 0) => {
    if (el.dataset.animated === "true") return;

    const target = parseFloat(el.dataset.count);
    const decimals = parseInt(el.dataset.decimal || "0", 10);

    if (Number.isNaN(target)) return;

    el.dataset.animated = "true";

    if (reduced || typeof gsap === "undefined") {
      el.textContent = target.toFixed(decimals);
      return;
    }

    const obj = { val: 0 };
    gsap.to(obj, {
      val: target,
      duration: 1.8,
      delay,
      ease: "power2.out",
      onUpdate: () => {
        el.textContent = obj.val.toFixed(decimals);
      },
      onComplete: () => {
        el.textContent = target.toFixed(decimals);
      },
    });
  };

  if (!("IntersectionObserver" in window)) {
    nodes.forEach(animate);
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = Array.from(nodes).indexOf(entry.target);
          animate(entry.target, index * 0.15);
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.4, rootMargin: "-10% 0px -10% 0px" },
  );

  nodes.forEach((el) => observer.observe(el));
}

document.addEventListener("DOMContentLoaded", initCasaStats);
