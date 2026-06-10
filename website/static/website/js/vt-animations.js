(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initReveal() {
    var nodes = document.querySelectorAll(".vt-reveal");
    if (!nodes.length) return;

    if (reduceMotion) {
      nodes.forEach(function (el) {
        el.classList.add("vt-reveal--visible");
      });
      return;
    }

    nodes.forEach(function (el) {
      var d = parseInt(el.getAttribute("data-reveal-delay") || "0", 10);
      if (d) el.style.setProperty("--vt-delay", d + "ms");
    });

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("vt-reveal--visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -6% 0px", threshold: 0.06 }
    );

    nodes.forEach(function (el) {
      observer.observe(el);
    });
  }

  function initContactForm() {
    var form = document.querySelector("[data-contact-form]");
    if (!form) return;

    form.addEventListener("submit", function () {
      var btn = form.querySelector("[type='submit']");
      if (btn) {
        btn.disabled = true;
        btn.setAttribute("aria-busy", "true");
      }
    });

    var fields = form.querySelectorAll("input[required], textarea[required]");
    fields.forEach(function (field) {
      field.addEventListener("blur", function () {
        var errorId = field.id + "-error";
        var existing = document.getElementById(errorId);
        if (field.validity.valid) {
          if (existing) existing.remove();
          field.removeAttribute("aria-invalid");
          return;
        }
        if (!existing) {
          existing = document.createElement("p");
          existing.id = errorId;
          existing.className = "vt-form-error";
          existing.setAttribute("role", "alert");
          field.parentNode.appendChild(existing);
        }
        existing.textContent = field.validationMessage;
        field.setAttribute("aria-invalid", "true");
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      initReveal();
      initContactForm();
    });
  } else {
    initReveal();
    initContactForm();
  }
})();
