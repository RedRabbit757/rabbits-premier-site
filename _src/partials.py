"""Shared header/footer for every page. Run build.py after editing anything in _src/."""

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services &amp; Pricing"),
    ("about.html", "About"),
    ("service-areas.html", "Service Areas"),
    ("policies.html", "Policies"),
]

SITE = "https://rabbits-premier.com"

def page_url(fname):
    return SITE + "/" + ("" if fname == "index.html" else fname)

def head(title, description, extra="", fname="index.html"):
    url = page_url(fname)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="theme-color" content="#0f2419" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{SITE}/img/crest.png" />
  <link rel="icon" type="image/png" href="img/favicon-64.png" />
  <link rel="apple-touch-icon" href="img/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(active):
    links = "\n".join(
        f'      <a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a>' for href, label in NAV
    )
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Rabbit's Premier Property Care home">
      <img src="img/crest-256.png" alt="" width="44" height="44" />
      <span>Rabbit's Premier<small>Property Care</small></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
{links}
      <a class="btn btn-gold" href="quote.html">Request a Quote</a>
    </nav>
  </div>
</header>
"""

CONTACT_STRIP = """<section class="contact-strip" aria-labelledby="contact-title">
  <div class="wrap">
    <div>
      <p class="eyebrow" style="color:var(--gold-soft)">Free estimates</p>
      <h2 id="contact-title">Let's get your property <em>looking its best.</em></h2>
      <p>Call, text, or email Billy for a free estimate. Open every day, 6 a.m.–6 p.m. Eastern.</p>
    </div>
    <div class="contact-actions">
      <a class="big" href="tel:+17574102347"><span><small>Call</small>757-410-2347</span><span aria-hidden="true">→</span></a>
      <a class="big" href="sms:+17574102347"><span><small>Text</small>757-410-2347</span><span aria-hidden="true">→</span></a>
      <a class="big" href="mailto:rabbits.premier@gmail.com"><span><small>Email</small>rabbits.premier@gmail.com</span><span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
"""

def footer(scripts='<script src="site.js"></script>'):
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="brandline"><img src="img/crest-256.png" alt="Rabbit's Premier Property Care crest" width="56" height="56" />Rabbit's Premier Property Care</div>
        <p>Owner-operated property care for homeowners in Portsmouth, Norfolk, Chesapeake, Virginia Beach, and Suffolk, Virginia. Commercial properties by on-site assessment.</p>
        <p style="margin-top:10px"><strong style="color:var(--gold-soft)">Insured</strong> · Free estimates</p>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li>Owner: Billy C. Hernandez</li>
          <li><a href="tel:+17574102347">Call or text: 757-410-2347</a></li>
          <li><a href="mailto:rabbits.premier@gmail.com">rabbits.premier@gmail.com</a></li>
          <li>900 Commonwealth Pl, Suite 200<br />Virginia Beach, VA 23464</li>
        </ul>
      </div>
      <div>
        <h3>Hours</h3>
        <ul>
          <li>Every day</li>
          <li>6 a.m.–6 p.m. Eastern</li>
        </ul>
        <h3 style="margin-top:18px">We accept</h3>
        <p>Cash, Cash App, Venmo, PayPal, card, check</p>
      </div>
      <div>
        <h3>Explore</h3>
        <ul>
          <li><a href="services.html">Services &amp; Pricing</a></li>
          <li><a href="services.html#faq">FAQ</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="service-areas.html">Service Areas</a></li>
          <li><a href="policies.html">Policies</a></li>
          <li><a href="quote.html">Request a Quote</a></li>
          <li><a href="quote.html?type=commercial">Commercial quotes</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© 2026 Rabbit's Premier Property Care. Published prices are for residential work.</span>
      <span>Work is performed on-site at your property.</span>
    </div>
  </div>
</footer>
<nav class="callbar" aria-label="Quick contact">
  <a href="tel:+17574102347">Call</a>
  <a href="sms:+17574102347">Text</a>
  <a class="q" href="quote.html">Free quote</a>
</nav>
{scripts}
</body>
</html>
"""

BUSINESS_LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "@id": "https://rabbits-premier.com/#business",
  "name": "Rabbit's Premier Property Care",
  "url": "https://rabbits-premier.com/",
  "logo": "https://rabbits-premier.com/img/crest.png",
  "image": "https://rabbits-premier.com/img/crest.png",
  "description": "Owner-operated residential property care: lawn care and yard cleanup, seasonal and decorative lighting installation, pressure washing, painting, and drywall repair. Commercial properties by on-site assessment and custom quote.",
  "telephone": "+1-757-410-2347",
  "email": "rabbits.premier@gmail.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "900 Commonwealth Pl, Suite 200",
    "addressLocality": "Virginia Beach",
    "addressRegion": "VA",
    "postalCode": "23464",
    "addressCountry": "US"
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "06:00",
    "closes": "18:00"
  }],
  "areaServed": [
    {"@type": "City", "name": "Portsmouth", "containedInPlace": {"@type": "State", "name": "Virginia"}},
    {"@type": "City", "name": "Norfolk", "containedInPlace": {"@type": "State", "name": "Virginia"}},
    {"@type": "City", "name": "Chesapeake", "containedInPlace": {"@type": "State", "name": "Virginia"}},
    {"@type": "City", "name": "Virginia Beach", "containedInPlace": {"@type": "State", "name": "Virginia"}},
    {"@type": "City", "name": "Suffolk", "containedInPlace": {"@type": "State", "name": "Virginia"}}
  ],
  "paymentAccepted": "Cash, Cash App, Venmo, PayPal, Credit Card, Check",
  "currenciesAccepted": "USD"
}
</script>
"""
