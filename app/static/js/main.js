// Мобильное меню (бургер)
const burger = document.querySelector(".burger");
const links = document.querySelector(".nav-links");
if (burger && links) {
  burger.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    burger.setAttribute("aria-expanded", String(open));
  });
}

// Плавное появление элементов при прокрутке
const revealItems = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  revealItems.forEach((el) => observer.observe(el));
} else {
  revealItems.forEach((el) => el.classList.add("visible"));
}

// Фильтр проектов по технологиям
const chips = document.querySelectorAll(".chip");
const cards = document.querySelectorAll(".card[data-tags]");
chips.forEach((chip) => {
  chip.addEventListener("click", () => {
    chips.forEach((c) => c.classList.remove("active"));
    chip.classList.add("active");
    const filter = chip.dataset.filter;
    cards.forEach((card) => {
      const tags = card.dataset.tags.split("|");
      const show = filter === "*" || tags.includes(filter);
      card.classList.toggle("hidden", !show);
      if (show) card.classList.add("visible");
    });
  });
});
