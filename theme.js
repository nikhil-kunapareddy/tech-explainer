// Light and dark theme button.
// Remembers the reader's choice. With no choice saved, it follows the computer's setting.
(function () {
  var root = document.documentElement;

  var saved = null;
  try { saved = localStorage.getItem("theme"); } catch (e) {}
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);

  function currentTheme() {
    var chosen = root.getAttribute("data-theme");
    if (chosen) return chosen;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  var ICON = 'width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
             'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"';
  var SUN = '<svg ' + ICON + '><circle cx="12" cy="12" r="4"/>' +
            '<path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var MOON = '<svg ' + ICON + '><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';

  document.addEventListener("DOMContentLoaded", function () {
    var button = document.getElementById("theme-toggle");
    if (!button) return;

    // Light mode shows a moon (click for dark). Dark mode shows a sun (click for light).
    function updateButton() {
      var dark = currentTheme() === "dark";
      var label = dark ? "Switch to light mode" : "Switch to dark mode";
      button.innerHTML = dark ? SUN : MOON;
      button.setAttribute("aria-label", label);
      button.title = label;
    }

    button.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
      updateButton();
    });

    updateButton();
  });
})();
