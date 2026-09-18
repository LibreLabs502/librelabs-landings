// LibreLabs — landing del laboratorio
(function () {
  "use strict";

  // --- Navbar con sombra al hacer scroll ---
  var nav = document.getElementById("nav");
  var onScroll = function () {
    if (!nav || typeof window.scrollY === "undefined") return;
    if (document.body.getAttribute("data-nav-bound") === "1") return;
    nav.classList.toggle("is-scrolled", window.scrollY > 8);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // --- Menú móvil ---
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("menu");
  if (toggle && menu) {
    document.body.setAttribute("data-nav-bound", "1");
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Cerrar menú de navegación" : "Abrir menú de navegación");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a[href^='#']")) {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("open")) {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // --- Reveal al hacer scroll ---
  var reveals = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window) || reveals.length === 0) {
    reveals.forEach(function (el) { el.classList.add("in"); });
    return;
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );

  reveals.forEach(function (el) { io.observe(el); });
})();