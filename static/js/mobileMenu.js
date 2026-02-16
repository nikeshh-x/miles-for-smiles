const btn = document.getElementById("mobileMenuBtn");
const menu = document.getElementById("mobileMenu");
if (btn && menu) {
  btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });
}

const links = document.querySelectorAll("#navLinks a[data-section]");
const sections = Array.from(links)
  .map((l) => document.getElementById(l.dataset.section))
  .filter(Boolean);
if (sections.length) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const id = entry.target.id;
        const link = document.querySelector(
          `#navLinks a[data-section="${id}"]`
        );
        if (!link) return;
        if (entry.isIntersecting) {
          links.forEach((a) =>
            a.classList.remove("text-blue-600", "border-blue-600")
          );
          links.forEach((a) => a.classList.add("text-gray-700"));
          link.classList.remove("text-gray-700");
          link.classList.add("text-blue-600", "border-blue-600");
        }
      });
    },
    { rootMargin: "-40% 0px -60% 0px", threshold: 0.1 }
  );

  sections.forEach((sec) => observer.observe(sec));
}
