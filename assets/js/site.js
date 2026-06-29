/* VIPER 2026 — small, dependency-free UI behaviours */
(function () {
  "use strict";

  // Mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { links.classList.remove("open"); });
    });
  }

  // Generic tab switcher: elements with [data-tab-group] hold buttons [data-tab]
  // and panels [data-panel]; matching values toggle .active.
  document.querySelectorAll("[data-tab-group]").forEach(function (group) {
    var buttons = group.querySelectorAll("[data-tab]");
    var scope = group.getAttribute("data-tab-scope")
      ? document.querySelector(group.getAttribute("data-tab-scope"))
      : document;
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var key = btn.getAttribute("data-tab");
        buttons.forEach(function (b) { b.classList.toggle("active", b === btn); });
        scope.querySelectorAll("[data-panel]").forEach(function (p) {
          p.classList.toggle("active", p.getAttribute("data-panel") === key);
        });
      });
    });
  });
})();
