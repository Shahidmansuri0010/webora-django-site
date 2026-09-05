(function () {
  "use strict";

  /* ---------- Sticky navbar background on scroll ---------- */
  var navbar = document.querySelector(".navbar");
  function updateNavbar() {
    if (!navbar) return;
    if (window.scrollY > 12) {
      navbar.classList.add("is-scrolled");
    } else {
      navbar.classList.remove("is-scrolled");
    }
  }
  updateNavbar();
  window.addEventListener("scroll", updateNavbar, { passive: true });

  /* ---------- Mobile menu toggle ---------- */
  var toggle = document.querySelector(".navbar-toggle");
  var mobileMenu = document.querySelector(".mobile-menu");
  if (toggle && mobileMenu) {
    toggle.addEventListener("click", function () {
      document.body.classList.toggle("nav-open");
      var expanded = document.body.classList.contains("nav-open");
      toggle.setAttribute("aria-expanded", expanded ? "true" : "false");
    });
    mobileMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
      });
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in-view"); });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var question = item.querySelector(".faq-question");
    var answer = item.querySelector(".faq-answer");
    if (!question || !answer) return;

    question.addEventListener("click", function () {
      var isOpen = item.classList.contains("is-open");

      // Close all siblings within the same list for a clean single-open accordion
      var list = item.closest(".faq-list");
      if (list) {
        list.querySelectorAll(".faq-item.is-open").forEach(function (openItem) {
          if (openItem !== item) {
            openItem.classList.remove("is-open");
            var openAnswer = openItem.querySelector(".faq-answer");
            if (openAnswer) openAnswer.style.maxHeight = null;
            openItem.querySelector(".faq-question").setAttribute("aria-expanded", "false");
          }
        });
      }

      if (isOpen) {
        item.classList.remove("is-open");
        answer.style.maxHeight = null;
        question.setAttribute("aria-expanded", "false");
      } else {
        item.classList.add("is-open");
        answer.style.maxHeight = answer.scrollHeight + "px";
        question.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* ---------- Active nav link highlighting ---------- */
  var currentPath = window.location.pathname.replace(/\/$/, "") || "/";
  document.querySelectorAll(".navbar-links a, .mobile-menu a").forEach(function (link) {
    var linkPath = link.getAttribute("data-path");
    if (linkPath && (linkPath === currentPath || (linkPath !== "/" && currentPath.startsWith(linkPath)))) {
      link.classList.add("active");
    }
  });
})();
