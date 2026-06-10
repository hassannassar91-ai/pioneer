(function () {
  "use strict";

  var header = document.querySelector("[data-header]");
  var toggle = document.querySelector("[data-nav-toggle]");
  var mobileNav = document.querySelector("[data-mobile-nav]");
  var backdrop = document.querySelector("[data-nav-backdrop]");
  var closeBtn = document.querySelector("[data-nav-close]");
  var navLinks = document.querySelectorAll("[data-nav-link]");
  var focusableSelector = 'a[href], button:not([disabled]), textarea, input, select, [tabindex]:not([tabindex="-1"])';
  var lastFocus = null;

  function setHeaderState() {
    if (!header) return;
    if (window.scrollY > 24) {
      header.classList.remove("vt-header-top");
      header.classList.add("vt-header-scrolled");
    } else {
      header.classList.add("vt-header-top");
      header.classList.remove("vt-header-scrolled");
    }
  }

  function trapFocus(panel) {
    var focusable = panel.querySelectorAll(focusableSelector);
    if (!focusable.length) return;
    var first = focusable[0];
    var last = focusable[focusable.length - 1];
    panel.addEventListener("keydown", function (e) {
      if (e.key !== "Tab") return;
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });
  }

  function openNav() {
    if (!mobileNav || !toggle) return;
    lastFocus = document.activeElement;
    mobileNav.classList.remove("hidden");
    mobileNav.setAttribute("aria-hidden", "false");
    toggle.setAttribute("aria-expanded", "true");
    document.body.classList.add("vt-drawer-open");
    var panel = mobileNav.querySelector("[data-nav-panel]");
    if (panel) {
      trapFocus(panel);
      var firstLink = panel.querySelector("[data-nav-link]");
      if (firstLink) firstLink.focus();
    }
  }

  function closeNav() {
    if (!mobileNav || !toggle) return;
    mobileNav.classList.add("hidden");
    mobileNav.setAttribute("aria-hidden", "true");
    toggle.setAttribute("aria-expanded", "false");
    document.body.classList.remove("vt-drawer-open");
    if (lastFocus) lastFocus.focus();
  }

  if (toggle) toggle.addEventListener("click", openNav);
  if (closeBtn) closeBtn.addEventListener("click", closeNav);
  if (backdrop) backdrop.addEventListener("click", closeNav);
  navLinks.forEach(function (link) {
    link.addEventListener("click", closeNav);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && mobileNav && !mobileNav.classList.contains("hidden")) {
      closeNav();
    }
  });

  window.addEventListener("scroll", setHeaderState, { passive: true });
  setHeaderState();
})();
