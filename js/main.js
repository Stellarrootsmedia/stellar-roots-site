/* ============================================================
   Stellar Roots Media — interactions
   ============================================================ */
(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* Form delivery inbox. Change this to your preferred address.
     First submission triggers a one-time FormSubmit activation email —
     click it once or nothing is delivered. Make sure the mailbox exists. */
  var CONTACT_ENDPOINT = "https://formsubmit.co/ajax/contact@stellarrootsmedia.com";

  /* ---------- header scroll ---------- */
  var header = $(".site-header");
  window.addEventListener("scroll", function () {
    header.classList.toggle("is-scrolled", window.scrollY > 10);
  }, { passive: true });

  /* ---------- mobile nav ---------- */
  var nav = $(".nav"), toggle = $(".nav-toggle");
  if (toggle) toggle.addEventListener("click", function () {
    var open = nav.getAttribute("data-open") === "true";
    nav.setAttribute("data-open", String(!open));
    toggle.setAttribute("aria-expanded", String(!open));
  });
  $$(".nav-links a").forEach(function (a) {
    a.addEventListener("click", function () { nav.setAttribute("data-open", "false"); });
  });

  /* ---------- FAQ accordion ---------- */
  $$(".faq-q").forEach(function (q) {
    q.addEventListener("click", function () {
      var open = q.getAttribute("aria-expanded") === "true";
      var ans = q.nextElementSibling;
      q.setAttribute("aria-expanded", String(!open));
      ans.style.maxHeight = open ? "0" : ans.scrollHeight + 24 + "px";
    });
  });

  /* ---------- contact form (delivers via FormSubmit, no backend) ---------- */
  var form = $("#contact-form");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = $("#cf-name").value.trim();
    var email = $("#cf-email").value.trim();
    var business = $("#cf-business").value.trim();
    var message = $("#cf-msg").value.trim();
    var msg = $("#form-msg");
    if (name.length < 2) { msg.textContent = "Please enter your name."; msg.className = "form-msg"; return; }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { msg.textContent = "Please enter a valid email."; msg.className = "form-msg"; return; }
    var btn = form.querySelector("button"), orig = btn.textContent;
    btn.disabled = true; btn.textContent = "Sending…"; msg.textContent = ""; msg.className = "form-msg";
    fetch(CONTACT_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify({
        name: name, email: email, business: business, message: message,
        _subject: "New growth-plan inquiry — stellarrootsmedia.com",
        _template: "table"
      })
    }).then(function (r) { return r.json(); }).then(function () {
      msg.textContent = "Got it — we'll be in touch within one business day. 🚀";
      msg.className = "form-msg ok"; form.reset();
    }).catch(function () {
      msg.textContent = "That didn't go through — email contact@stellarrootsmedia.com and we'll jump on it.";
      msg.className = "form-msg";
    }).finally(function () { btn.disabled = false; btn.textContent = orig; });
  });

  /* ---------- scroll reveal ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    $$(".reveal:not(.in)").forEach(function (el) { io.observe(el); });
  } else {
    $$(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- footer year ---------- */
  var yr = $("#year"); if (yr) yr.textContent = new Date().getFullYear();
})();
