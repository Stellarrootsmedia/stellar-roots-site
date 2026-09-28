#!/usr/bin/env python3
"""Build the service pages from shared header/footer in index.html.
Run from the site root:  python3 scripts/build_pages.py
Edit page content in the PAGES dict below, then re-run and push."""
import re, json, html, os

SITE = "https://stellarrootsmedia.com/"
idx = open("index.html").read()

def grab(pattern):
    return re.search(pattern, idx, re.S).group(0)

def rootify(block):
    # make links/assets work from a sub-folder page
    block = re.sub(r'(src|href|srcset)="(assets|css|js)/', r'\1="/\2/', block)
    block = block.replace('href="meta-ads-austin/"', 'href="/meta-ads-austin/"').replace('href="video-production-austin/"', 'href="/video-production-austin/"')
    block = re.sub(r'href="#(?!contact|top)([\w-]+)"', r'href="/#\1"', block)
    block = block.replace('href="#top"', 'href="/"')
    return block

HEADER = rootify(grab(r'<header class="site-header">.*?</header>'))
FOOTER = rootify(grab(r'<footer class="site-footer">.*?</footer>'))
CONTACT = rootify(grab(r'<!-- FINAL CTA.*?</section>'))
MARQUEE = rootify(grab(r'<div class="logo-marquee".*?</div>\s*</div>'))
CSSV = re.search(r'styles\.css\?v=(\d+)', idx).group(1)

def faq_html(faqs):
    return "\n".join(f'          <div class="faq-item"><button class="faq-q" aria-expanded="false">{q}<span class="mark">+</span></button><div class="faq-a"><div>{a}</div></div></div>' for q, a in faqs)

def page(slug, title, desc, crumb, service_name, service_type, body, faqs):
    url = SITE + slug + "/"
    clean = lambda t: html.unescape(re.sub(r"<[^>]+>", "", t))
    ld = [
        {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": service_name,
         "serviceType": service_type, "url": url, "description": clean(desc),
         "provider": {"@type": ["ProfessionalService", "Organization"], "@id": SITE + "#org", "name": "Stellar Roots Media", "url": SITE, "telephone": "+1-512-730-0132"},
         "areaServed": [{"@type": "City", "name": "Austin", "containedInPlace": {"@type": "State", "name": "Texas"}}, {"@type": "Country", "name": "United States"}]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in faqs]},
    ]
    ld_html = "\n".join('  <script type="application/ld+json">\n  ' + json.dumps(x, indent=2, ensure_ascii=False).replace("\n", "\n  ") + "\n  </script>" for x in ld)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-79V9W46W92"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-79V9W46W92');
  </script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="{url}" />
  <meta name="theme-color" content="#101b2b" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Stellar Roots Media" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}assets/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Stellar Roots Media logo" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="{SITE}assets/og-image.jpg" />
  <link rel="icon" type="image/png" sizes="64x64" href="/assets/favicon-64.png" />
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="preload" href="/assets/fonts/space-grotesk-500-700.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="/assets/fonts/inter-400-600.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="/css/styles.css?v={CSSV}" />
{ld_html}
</head>
<body>
  <div class="starlayer" aria-hidden="true"></div>
  <a class="sr-only" href="#contact">Skip to contact</a>
  {HEADER}

  <main id="top">
{body}

    <section class="band" id="faq" aria-labelledby="faq-title">
      <div class="container">
        <div class="section-head center reveal">
          <span class="kicker center">Questions</span>
          <h2 class="display" id="faq-title">Good to know.</h2>
        </div>
        <div class="faq">
{faq_html(faqs)}
        </div>
      </div>
    </section>

    {CONTACT}
  </main>

  {FOOTER}

  <script src="/js/main.js"></script>
</body>
</html>
'''

def hero(crumb, kicker, h1, lead):
    return f'''    <section class="band hero page-hero" aria-labelledby="page-title">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><span aria-current="page">{crumb}</span></nav>
        <span class="kicker">{kicker}</span>
        <h1 id="page-title">{h1}</h1>
        <p class="lead">{lead}</p>
        <div class="hero-actions">
          <a class="btn btn--primary" href="#contact">Book a Strategy Call</a>
          <a class="btn btn--ghost" href="#proof">See the results</a>
        </div>
      </div>
    </section>'''

RECEIPTS = '''        <div class="receipts reveal">
          <span class="kicker">A few recent screenshots from our current campaigns</span>
          <figure class="receipt">
            <figcaption><span class="k">Local business group · member leads</span><span>Lifetime · 819 leads</span></figcaption>
            <div class="shot"><img src="/assets/results/networking-lifetime.png" alt="Meta Ads Manager, local business group member lead campaign, lifetime: 819 Meta leads at $2.77 per lead, $8.00 daily budget, $2,268.45 spent, 111,933 impressions" loading="lazy" width="1907" height="101"></div>
          </figure>
          <figure class="receipt">
            <figcaption><span class="k">High-ticket retail · form leads</span><span>Lifetime · still running</span></figcaption>
            <div class="shot"><img src="/assets/results/premier-lifetime.png" alt="Meta Ads Manager, high-ticket retail form lead campaign, lifetime: 145 form leads at $24.74 per lead, $15.00 daily budget, $3,587.67 spent, 84,370 impressions, 31,620 reach" loading="lazy" width="1672" height="76"></div>
          </figure>
          <p class="receipts-note">◦ Unedited from Meta Ads Manager — two of the campaigns we're running right now. Full exports on your strategy call.</p>
        </div>'''

FRAMES = '''        <div class="creative-grid reveal">
          <figure class="frame"><img src="/assets/work/retail.webp" alt="Retail showroom client ad frame" loading="lazy" width="660" height="1173"><figcaption class="tag">Retail Showroom</figcaption></figure>
          <figure class="frame"><img src="/assets/work/spirits.webp" alt="Spirits brand client ad frame" loading="lazy" width="660" height="1173"><figcaption class="tag">Spirits</figcaption></figure>
          <figure class="frame"><img src="/assets/work/hospitality.webp" alt="Hospitality client ad frame" loading="lazy" width="660" height="1173"><figcaption class="tag">Hospitality</figcaption></figure>
          <figure class="frame"><img src="/assets/work/homeservices.webp" alt="Home services client ad frame" loading="lazy" width="660" height="1173"><figcaption class="tag">Home Services</figcaption></figure>
          <figure class="frame"><img src="/assets/work/founder.webp" alt="Founder interview client ad frame" loading="lazy" width="660" height="1173"><figcaption class="tag">Founder Interview</figcaption></figure>
        </div>
        <p class="creative-note">◦ Every frame is a real client. Nothing here is stock, templated, or generated.</p>'''

# ---------------------------------------------------------------- META ADS
meta_faqs = [
    ("Do I need a website or landing page?", "Not necessarily. We use Meta's Instant Lead Forms, so people can request information without ever leaving Facebook or Instagram — and the lead is delivered straight to your team. Our local business group campaign has collected 819 leads this way with no landing page at all."),
    ("Is ad spend included?", "No. Your ad budget is paid directly to Meta and stays in your account — you own it. Our fee covers strategy, creative, campaign management and reporting. We'll recommend a budget on your strategy call."),
    ("Do you make the ads too, or just run them?", "Both — that's the point. Meta rewards ads people actually stop for, so we capture and produce the creative ourselves: founder stories, product and lifestyle video, and scroll-stopping ad cuts. No stock footage, no templates."),
    ("How fast will leads start coming in?", "After onboarding and a capture session, campaigns launch quickly and lead flow can begin within the first weeks. From there we test and optimize every cycle so results compound."),
    ("Do you work with businesses outside Austin?", "Yes. We're based in Austin, Texas and run campaigns for clients locally and across the U.S."),
]
meta_body = hero("Meta Ads Management", "Meta ads management",
    'Austin Meta ads that bring <em class="accent">real leads.</em>',
    "Facebook and Instagram campaigns built on premium creative — engineered to put qualified opportunities in front of your team, not vanity metrics.") + f'''

    <section class="band band--cream" id="included" aria-labelledby="inc-title">
      <div class="container">
        <div class="section-head reveal">
          <span class="kicker">What's included</span>
          <h2 class="display" id="inc-title">Everything it takes to run <em class="accent">Meta ads well.</em></h2>
          <p>Strategy, creative, launch, and optimization — handled end to end by one team, so nothing gets lost between the people making the ads and the people running them.</p>
        </div>
        <div class="fronts">
          <article class="front reveal"><span class="no">01 · Strategy</span><h3>Built around your numbers.</h3><p>Campaign structure, audiences, and offers planned around how your business actually makes money — whether that's a few high-ticket sales or a steady stream of local customers.</p></article>
          <article class="front reveal"><span class="no">02 · Creative</span><h3>Ads people stop for.</h3><p>Performance video and static creative we capture and produce ourselves — real owners, real products, filmed on location. Fresh angles tested continuously.</p></article>
          <article class="front reveal"><span class="no">03 · Leads</span><h3>Delivered to your team.</h3><p>Meta Instant Lead Forms capture interest without a landing page, and leads go straight to your team. Then we test, optimize, and report — plainly and honestly.</p></article>
        </div>
      </div>
    </section>

    <section class="band" id="proof" aria-labelledby="proof-title">
      <div class="container">
        <div class="section-head center reveal">
          <span class="kicker center">The proof</span>
          <h2 class="display" id="proof-title">Results on every kind of <em class="accent">campaign.</em></h2>
          <p>High-ticket brands that need fewer, better buyers. Local businesses that run on volume. Same system — tuned to your economics.</p>
        </div>
        <div class="ctypes reveal">
          <article class="ctype"><span class="no">For high-ticket</span><h3>Quality over quantity.</h3><p>Qualified buyers ready to spend — where a single sale can pay for the month.</p></article>
          <article class="ctype"><span class="no">For local business</span><h3>Volume that compounds.</h3><p>A steady stream of leads at a low cost per lead, delivered straight to your team.</p></article>
        </div>
{RECEIPTS}
      </div>
    </section>

    <section class="band band--cream" id="process" aria-labelledby="process-title">
      <div class="container">
        <div class="section-head reveal">
          <span class="kicker">How a lead reaches you</span>
          <h2 class="display" id="process-title">We handle the marketing. <em class="accent">You handle the customer.</em></h2>
          <p>We generate and deliver the opportunity — your team takes it from there.</p>
        </div>
        <div class="process">
          <div class="pstep"><span class="n">i</span><h3>Capture</h3><p>We film your business, your people, and your proof.</p></div>
          <div class="pstep"><span class="n">ii</span><h3>Create</h3><p>Footage becomes ad creative built to stop the scroll.</p></div>
          <div class="pstep"><span class="n">iii</span><h3>Advertise</h3><p>Targeted Facebook &amp; Instagram campaigns go live.</p></div>
          <div class="pstep"><span class="n">iv</span><h3>Deliver</h3><p>Instant Lead Forms send new leads straight to your team.</p></div>
          <div class="pstep"><span class="n">v</span><h3>Optimize</h3><p>We test, report, and sharpen performance every cycle.</p></div>
        </div>
      </div>
    </section>'''

# ---------------------------------------------------------------- VIDEO
video_faqs = [
    ("How much of my time does a shoot take?", "Very little. We compress production into efficient capture sessions — usually one session covers a large batch of content. We handle planning, filming, editing, and delivery."),
    ("Where do you film?", "On location at your business — your showroom, kitchen, job site, or office — because real places and real people build more trust than a studio backdrop. We're based in Austin and travel for clients across the U.S."),
    ("What do I actually get?", "A library of finished content from each shoot: founder and owner interviews, product and how-to videos, lifestyle footage, and ad cuts formatted for Facebook, Instagram, and your website."),
    ("Can the video be used for more than ads?", "Yes — that's how it keeps paying off. The same footage powers your ads, organic social posts, your website, and the content that helps you rank on Google and get recommended by AI search."),
    ("Do you use stock footage or AI-generated video?", "No. Every frame is your real business, filmed on location. That authenticity is what makes people trust — and choose — you."),
]
video_body = hero("Video Production", "Video production &amp; ad creative",
    'Austin video production that <em class="accent">earns trust.</em>',
    "Real owners, real products, filmed on location — then edited into ads, social content, and brand stories that keep working long after the shoot.") + f'''

    <section class="band band--cream" id="proof" aria-labelledby="work-title">
      <div class="container">
        <div class="section-head reveal">
          <span class="kicker">The work</span>
          <h2 class="display" id="work-title">Filmed on location. <em class="accent">Built to perform.</em></h2>
          <p>A few frames from real client ads across the kinds of businesses we serve.</p>
        </div>
{FRAMES}
      </div>
    </section>

    <section class="band" id="what-we-film" aria-labelledby="film-title">
      <div class="container">
        <div class="section-head reveal">
          <span class="kicker">What we film</span>
          <h2 class="display" id="film-title">Every kind of story <em class="accent">that sells.</em></h2>
        </div>
        <div class="fronts">
          <article class="front reveal"><span class="no">01 · People</span><h3>Founder &amp; owner interviews.</h3><p>The fastest way to build trust is to put a real face on your business. We make you comfortable on camera and pull out the stories customers remember.</p></article>
          <article class="front reveal"><span class="no">02 · Product</span><h3>Product &amp; how-to video.</h3><p>Show exactly what you sell and why it's better — product close-ups, demonstrations, and how-to content that answers buyers' questions before they ask.</p></article>
          <article class="front reveal"><span class="no">03 · Ads</span><h3>Performance ad creative.</h3><p>Vertical cuts, strong hooks, and clear offers for Facebook and Instagram — made by the same team that runs your campaigns, so creative and results stay connected.</p></article>
        </div>
        <p class="pull reveal">One shoot. <span class="accent">Every front.</span></p>
        <p style="text-align:center;color:var(--muted);max-width:60ch;margin:1.2rem auto 0">The same footage powers your ads, organic social, and website — and builds the search presence (SEO), AI visibility (GEO), and brand equity that keep working after a campaign ends.</p>
      </div>
    </section>

    <section class="band band--cream" id="process" aria-labelledby="process-title">
      <div class="container">
        <div class="section-head reveal">
          <span class="kicker">How a shoot works</span>
          <h2 class="display" id="process-title">You show up. <em class="accent">We handle the rest.</em></h2>
        </div>
        <figure class="bts reveal">
          <img src="/assets/work/bts-interview-1400.webp" srcset="/assets/work/bts-interview-800.webp 800w, /assets/work/bts-interview-1400.webp 1400w, /assets/work/bts-interview-2000.webp 2000w" sizes="(max-width: 1240px) 100vw, 1180px" alt="Evan Lopez, founder of Stellar Roots Media, interviewing a client on location" loading="lazy" width="2000" height="1125">
          <figcaption>◦ Evan Lopez, founder · client interview, filmed on location</figcaption>
        </figure>
        <div class="process">
          <div class="pstep"><span class="n">i</span><h3>Plan</h3><p>Strategy, story angles, and a shot list built around your goals.</p></div>
          <div class="pstep"><span class="n">ii</span><h3>Capture</h3><p>One efficient session, on location at your business.</p></div>
          <div class="pstep"><span class="n">iii</span><h3>Edit</h3><p>Ads, reels, founder stories, and website video.</p></div>
          <div class="pstep"><span class="n">iv</span><h3>Launch</h3><p>Content goes live in your ads and organic channels.</p></div>
        </div>
      </div>
    </section>

    <section class="band band--tight" aria-label="Clients and reviews">
      <div class="container">
        <div class="section-head center reveal">
          <span class="kicker center">Trusted by brands that want results</span>
        </div>
      </div>
      {MARQUEE}
      <div class="container">
        <div class="tgrid" style="margin-top:2.4rem">
          <div class="tcard"><p class="q">“Evan was so creative with different shots of our products to make our ‘How To’ videos really pop!”</p><div class="who"><div class="av">DP</div><div><b>DeeDee Patterson</b><span>Whiskey Towers</span></div></div></div>
          <div class="tcard"><p class="q">“I love these guys!! Evan is so creative and has such a positive way to deliver your vision. He really gets it and makes it happen.”</p><div class="who"><div class="av">AM</div><div><b>Adriana May</b><span>Lonestar Organizing</span></div></div></div>
        </div>
      </div>
    </section>'''

PAGES = [
    ("meta-ads-austin", "Meta Ads Management in Austin, TX | Stellar Roots Media",
     "Facebook &amp; Instagram lead campaigns for Austin businesses — premium creative, Instant Lead Forms delivered to your team, and unedited reporting.",
     "Meta Ads Management", "Meta Ads Management", "Facebook and Instagram advertising management", meta_body, meta_faqs),
    ("video-production-austin", "Video Production in Austin, TX | Stellar Roots Media",
     "Austin video production for businesses — founder interviews, product and lifestyle video, and ad creative filmed on location and built to perform.",
     "Video Production", "Video Production &amp; Ad Creative", "Video production", video_body, video_faqs),
]

for slug, title, desc, crumb, sname, stype, body, faqs in PAGES:
    os.makedirs(slug, exist_ok=True)
    open(f"{slug}/index.html", "w").write(page(slug, title, desc, crumb, html.unescape(sname), stype, body, faqs))
    print("built", slug)
