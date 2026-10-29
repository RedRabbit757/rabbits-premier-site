/* Shared site behavior: mobile nav, scroll reveals, pricing estimators, quote form. */
(function () {
  const PHONE = "7574102347";
  const EMAIL = "rabbits.premier@gmail.com";
  const money = (cents) => "$" + (cents / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const num = (el) => { const v = parseFloat(el && el.value); return isFinite(v) && v > 0 ? v : 0; };

  // ---------- mobile nav ----------
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  // ---------- scroll reveals ----------
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { threshold: 0.15 });
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

  // ---------- lighting labor estimator ----------
  // Base $2.83/ft; each story above the first adds 50% of the base rate, applied only to that story's footage.
  // Each story's charge = footage x exact rate, rounded to cents. Removal = 75% of installation labor.
  const light = document.getElementById("calc-lighting");
  if (light) {
    const BASE_CENTS = 283;
    const inputs = [...light.querySelectorAll("input[data-story]")];
    const removal = light.querySelector("#light-removal");
    const render = () => {
      let install = 0;
      inputs.forEach((inp) => {
        const story = parseInt(inp.dataset.story, 10);
        const rate = BASE_CENTS * (1 + 0.5 * (story - 1));
        const charge = Math.round(num(inp) * rate);
        install += charge;
        light.querySelector(`[data-out-story="${story}"]`).textContent = money(charge);
      });
      const rem = removal.checked ? Math.round(install * 0.75) : 0;
      light.querySelector("[data-out='install']").textContent = money(install);
      light.querySelector("[data-out='removal']").textContent = removal.checked ? money(rem) : "—";
      light.querySelector("[data-out='total']").textContent = money(install + rem);
    };
    light.addEventListener("input", render);
    render();
  }

  // ---------- pressure washing estimator ----------
  // Concrete $0.40/sq ft, deck flooring $0.50/sq ft, privacy fence $3/linear ft per side; $200 minimum once per visit.
  const wash = document.getElementById("calc-wash");
  if (wash) {
    const render = () => {
      const concrete = Math.round(num(wash.querySelector("#wash-concrete")) * 40);
      const deck = Math.round(num(wash.querySelector("#wash-deck")) * 50);
      const fence = Math.round(num(wash.querySelector("#wash-fence")) * 300);
      const sub = concrete + deck + fence;
      const total = sub > 0 ? Math.max(sub, 20000) : 0;
      wash.querySelector("[data-out='concrete']").textContent = money(concrete);
      wash.querySelector("[data-out='deck']").textContent = money(deck);
      wash.querySelector("[data-out='fence']").textContent = money(fence);
      wash.querySelector("[data-out='min']").textContent = sub > 0 && sub < 20000 ? "Visit minimum applies" : "—";
      wash.querySelector("[data-out='total']").textContent = money(total);
    };
    wash.addEventListener("input", render);
    render();
  }

  // ---------- quote form ----------
  const form = document.getElementById("quote-form");
  if (form) {
    const params = new URLSearchParams(location.search);
    const type = params.get("type");
    if (type === "commercial") {
      const r = form.querySelector("input[name='property'][value='Commercial']");
      if (r) r.checked = true;
    }
    const svc = params.get("service");
    if (svc) {
      const box = form.querySelector(`input[name='services'][value='${CSS.escape(svc)}']`);
      if (box) box.checked = true;
    }
    const commercialNote = document.getElementById("commercial-note");
    const syncType = () => {
      const v = (form.querySelector("input[name='property']:checked") || {}).value;
      commercialNote.hidden = !(v === "Commercial" || v === "Property management");
    };
    form.addEventListener("change", syncType);
    syncType();

    const compose = () => {
      const fd = new FormData(form);
      const services = fd.getAll("services");
      const lines = [
        `Name: ${fd.get("name") || ""}`,
        `Preferred contact: ${fd.get("contact") || ""}`,
        `Phone: ${fd.get("phone") || ""}`,
        `Email: ${fd.get("email") || ""}`,
        `Property address: ${fd.get("address") || ""}`,
        `City: ${fd.get("city") || ""}`,
        `Property type: ${fd.get("property") || ""}`,
        `Services: ${services.length ? services.join(", ") : "Not sure yet"}`,
        "",
        "Scope / details:",
        fd.get("scope") || "",
      ];
      return { subject: `Quote request - ${fd.get("property") || "Residential"} - ${fd.get("city") || ""}`, body: lines.join("\n") };
    };
    const status = document.getElementById("form-status");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const { subject, body } = compose();
      const photosNote = "\n\nPhotos: I'll attach photos to this email if I have them.";
      location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body + photosNote)}`;
      status.textContent = "Your email app should open with the request filled in — just press send.";
    });
    const textBtn = document.getElementById("send-text");
    if (textBtn) textBtn.addEventListener("click", () => {
      if (!form.reportValidity()) return;
      const { body } = compose();
      location.href = `sms:${PHONE}?&body=${encodeURIComponent("Quote request\n" + body)}`;
      status.textContent = "Your messaging app should open with the request filled in.";
    });
  }
})();
