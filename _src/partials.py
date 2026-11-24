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
  <meta name="msvalidate.01" content="1C28F9B61F359751F5F616C6C31BF697" />
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
  <link rel="stylesheet" href="styles.css?v=2026-11-10" />
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
      <a class="big" href="tel:+17577658212"><span><small>Call</small>757-765-8212</span><span aria-hidden="true">→</span></a>
      <a class="big" href="sms:+17577658212"><span><small>Text</small>757-765-8212</span><span aria-hidden="true">→</span></a>
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
          <li><a href="tel:+17577658212">Call or text: 757-765-8212</a></li>
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
  <a href="tel:+17577658212">Call</a>
  <a href="sms:+17577658212">Text</a>
  <a class="q" href="quote.html">Free quote</a>
</nav>
{scripts}
</body>
</html>
"""

# Structured data for the homepage (GEO audit 2026-11-22). Built as a dict so it is always valid JSON.
# Google Business Profile added 2026-11-24. Add Bing Places, Angi, Facebook, Nextdoor and Yelp URLs to "sameAs" once they exist;
# add "geo" from the verified Google pin. Never put placeholder values in here.
_SITE = "https://rabbits-premier.com/"
_BIZ = _SITE + "#business"


def _city(name):
    slug = name.replace(" ", "_") + ",_Virginia"
    return {"@type": "City", "name": name, "sameAs": "https://en.wikipedia.org/wiki/" + slug,
            "containedInPlace": {"@type": "State", "name": "Virginia"}}


def _offer(name, service_type, spec):
    return {"@type": "Offer", "itemOffered": {"@type": "Service", "name": name, "serviceType": service_type},
            "priceSpecification": dict({"priceCurrency": "USD"}, **spec)}


_LD = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": _SITE + "#website", "url": _SITE, "name": "Rabbit's Premier Property Care",
         "inLanguage": "en-US", "publisher": {"@id": _BIZ}},
        {"@type": "Person", "@id": _SITE + "#owner", "name": "Billy C. Hernandez", "jobTitle": "Owner and Operator",
         "url": _SITE + "about.html", "worksFor": {"@id": _BIZ},
         "knowsAbout": ["Lawn care", "Yard cleanup", "Seasonal and decorative lighting installation", "Pressure washing",
                        "Painting", "Drywall repair", "Hardscaping"]},
        {"@type": "HomeAndConstructionBusiness", "@id": _BIZ,
         "name": "Rabbit's Premier Property Care",
         "alternateName": "Rabbit's Lawn & Garden Care",
         "url": _SITE,
         "logo": {"@type": "ImageObject", "url": _SITE + "img/crest.png", "width": 1024, "height": 993},
         "image": [_SITE + "img/crest.png", _SITE + "img/work/P12-1000004078.jpg",
                   _SITE + "img/work/P11-1000004094.jpg", _SITE + "img/work/P2-1000002238.jpg"],
         "description": ("Owner-operated residential property care in Portsmouth, Norfolk, Chesapeake, Virginia Beach, and "
                         "Suffolk, Virginia: lawn care and yard cleanup, seasonal and decorative lighting installation, "
                         "pressure washing, painting, drywall repair, and hardscaping by estimate. Commercial properties by "
                         "on-site assessment and custom quote. Formerly Rabbit's Lawn & Garden Care. Insured. Free estimates."),
         "founder": {"@id": _SITE + "#owner"},
         "telephone": "+1-757-765-8212",
         "email": "rabbits.premier@gmail.com",
         "address": {"@type": "PostalAddress", "streetAddress": "900 Commonwealth Pl, Suite 200",
                     "addressLocality": "Virginia Beach", "addressRegion": "VA", "postalCode": "23464",
                     "addressCountry": "US"},
         # Google Business Profile (the King's share link 2026-11-24, resolved to its stable cid address).
         "hasMap": "https://www.google.com/maps?cid=5067193554226828321",
         "sameAs": ["https://www.google.com/maps?cid=5067193554226828321"],
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                                                      "Saturday", "Sunday"],
                                        "opens": "06:00", "closes": "18:00"}],
         "areaServed": [_city(c) for c in ("Portsmouth", "Norfolk", "Chesapeake", "Virginia Beach", "Suffolk")],
         "priceRange": "Lawn visits from $75; published residential rates",
         "paymentAccepted": "Cash, Cash App, Venmo, PayPal, Credit Card, Check",
         "currenciesAccepted": "USD",
         "hasOfferCatalog": {
             "@type": "OfferCatalog", "name": "Residential services and published prices",
             "url": _SITE + "services.html",
             "itemListElement": [
                 _offer("Routine lawn maintenance: mowing, edging, and trimming", "Lawn care",
                        {"@type": "UnitPriceSpecification", "price": 75,
                         "unitText": "per visit (most average properties; size-dependent)"}),
                 _offer("Leaf cleanup: raking/blowing and bagging", "Yard cleanup",
                        {"@type": "PriceSpecification", "minPrice": 150, "description": "Starting at $150 per visit"}),
                 _offer("Seasonal and decorative lighting installation", "Outdoor lighting installation",
                        {"@type": "UnitPriceSpecification", "price": 2.83, "unitCode": "FOT",
                         "unitText": "per linear foot, first-story labor; +50% of base per additional story; lights and materials separate"}),
                 _offer("Concrete pressure washing: driveways, walkways, patios", "Pressure washing",
                        {"@type": "UnitPriceSpecification", "price": 0.40, "unitCode": "FTK",
                         "unitText": "per sq. ft.; $200 standalone visit minimum"}),
                 _offer("House exterior soft wash", "Pressure washing",
                        {"@type": "PriceSpecification", "minPrice": 300,
                         "description": "One-story from $300; two-story from $450"}),
                 _offer("Interior painting: walls and ceilings", "House painting",
                        {"@type": "UnitPriceSpecification", "price": 2, "unitCode": "FTK",
                         "unitText": "per sq. ft. of painted surface, labor only; $350 job minimum"}),
                 _offer("Drywall repair", "Drywall repair",
                        {"@type": "PriceSpecification", "minPrice": 250,
                         "description": "Standalone repair minimum $250; new drywall $2.50 per sq. ft., $500 minimum"}),
                 {"@type": "Offer", "itemOffered": {"@type": "Service",
                                                    "name": "Hardscaping: patios, walkways, retaining walls, fire pits",
                                                    "serviceType": "Hardscaping"},
                  "description": "Scope and price set at an on-site estimate."},
             ]},
         },
    ],
}

import json as _json
BUSINESS_LD = ('<script type="application/ld+json">\n' + _json.dumps(_LD, indent=2, ensure_ascii=False)
               + "\n</script>\n")
