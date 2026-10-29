"""Assemble the static pages: python _src/build.py  (writes *.html into the site root)."""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from partials import head, header, footer, page_url, CONTACT_STRIP, BUSINESS_LD

HOME_SCRIPTS = """<script>
  window.SCRUB_SECTIONS = [
    { section: "#hero", frameCount: 120, bg: "#2a2017", focusX: 0.5,
      framePath: (i) => `frames/mascot/frame_${String(i).padStart(4, "0")}.jpg` },
    { section: "#work-reel", frameCount: 96, bg: "#0b1a12", lazy: true,
      framePath: (i) => `frames/work/frame_${String(i).padStart(4, "0")}.jpg` }
  ];
</script>
<script src="https://unpkg.com/lenis@1.3.21/dist/lenis.min.js"></script>
<script src="scroll-cinematic.js"></script>
<script src="site.js"></script>"""

PAGES = [
    ("index.html", "Rabbit's Premier Property Care | Lawn Care, Lighting & Pressure Washing",
     "Owner-operated property care in Portsmouth, Norfolk, Chesapeake, Virginia Beach, and Suffolk, VA. Lawn care from $75 per visit, lighting, pressure washing, painting, and drywall. Free estimates.",
     '<link rel="preload" as="image" href="frames/mascot/frame_0001.jpg" />\n' + BUSINESS_LD, HOME_SCRIPTS, True),
    ("services.html", "Services & Pricing | Rabbit's Premier Property Care",
     "Published residential prices for lawn care, seasonal and decorative lighting, pressure washing, painting, and drywall in Portsmouth, Norfolk, Chesapeake, Virginia Beach, and Suffolk, VA.",
     "", None, True),
    ("about.html", "About | Rabbit's Premier Property Care",
     "Rabbit's Premier Property Care is owned and operated by Billy C. Hernandez, serving homeowners in five Virginia cities with clear, published pricing.",
     "", None, True),
    ("service-areas.html", "Service Areas | Rabbit's Premier Property Care",
     "Rabbit's Premier Property Care serves Portsmouth, Norfolk, Chesapeake, Virginia Beach, and Suffolk, Virginia.",
     "", None, True),
    ("policies.html", "Policies | Rabbit's Premier Property Care",
     "Deposit, cancellation, rescheduling, and satisfaction promise policies for Rabbit's Premier Property Care.",
     "", None, True),
    ("quote.html", "Request a Free Quote | Rabbit's Premier Property Care",
     "Request a free estimate for lawn care, lighting, pressure washing, painting, drywall, or hardscaping. Commercial properties receive an on-site assessment and custom quote.",
     "", None, False),
]

def faq_ld(body):
    items = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", body, re.S)
    strip = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s)).strip()
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items]}
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2, ensure_ascii=False) + "\n</script>\n"

for fname, title, desc, extra, scripts, strip_contact in PAGES:
    with open(os.path.join(HERE, "pages", fname), encoding="utf-8") as f:
        body = f.read()
    if fname == "services.html":
        extra += faq_ld(body)
    out = head(html.escape(title, quote=True), html.escape(desc, quote=True), extra, fname) + header(fname) + body
    if strip_contact:
        out += CONTACT_STRIP
    out += footer(scripts) if scripts else footer()
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print("wrote", fname)

urls = "\n".join(f"  <url><loc>{page_url(p[0])}</loc></url>" for p in PAGES)
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
print("wrote sitemap.xml")
