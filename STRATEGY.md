# Stellar Roots Media — Website Strategy & Build Report

_Source of truth: the 2026 pitch deck (StellarRootsPD26-1.pdf). Older site content is secondary._

---

## 1. Business summary (extracted from the deck — verified, not invented)

- **What it is:** Austin, TX creative + performance marketing agency. Core offering = premium **video creative** + **strategically managed Meta advertising** that generates leads for **established, high-ticket service businesses.**
- **Positioning:** "Anyone can generate an ad. Very few brands build real trust." → homepage line: **"Made to stand out. Built to perform."**
- **System:** Capture → Create → Advertise → Deliver lead (client then Contact → Qualify → Sell). Homepage frames it as **Create · Launch · Optimize**. "We handle the marketing. You handle the customer."
- **Packages (exact, from deck slide "Simple by design."):**
  | Package | Price | Includes |
  |---|---|---|
  | **Ad Sprint** | $3,000/mo | Managed Meta ads, performance creative, Meta Instant Lead Forms, direct lead delivery, testing + optimization, reporting (no organic, no capture) |
  | **Growth Engine** (flagship) | $4,000/mo | Everything in Ad Sprint + quarterly professional capture, up to 8 organic posts/mo, fresh creative quarterly, compounding brand equity, search + AI visibility |
  | **Growth + Authority** | $7,500/mo | Everything in Growth Engine + Google Ads (high-intent), Google Business Profile + reputation, review generation/response, 1 high-intent search asset/mo, long-term SEO/local, quarterly authority planning |
- **Terms:** $2,500 setup fee (waived at 6-mo commit); else 3-mo minimum + setup, then month-to-month, 30 days' notice. **Ad spend separate**, ~$1,500–$3,000+/mo to Meta.
- **Documented results:** $2.84 avg cost/lead (Meta, lifetime); 103.4% YoY revenue increase (client); +2,776% organic impressions, +69.7% follower growth (IG); 5.0★ Google.
- **Real testimonials:** Dwayne Clark (Summit Tech), Jim McCullick (Networking Austin), DeeDee Patterson (Whiskey Towers), Adriana May (Lonestar Organizing).
- **Client brands (logos on current site):** Buc-ee's, Fairmont Austin, Harlem Globetrotters, Icelandic Glacial, Whiskey Towers, Networking Austin.

---

## 2. Visual / brand direction (implemented)

Retro-futuristic **mission-control**: 1970s NASA graphics × modern creative studio.
- **Palette:** Deep Space Navy `#101B2B`, Cosmic Cream `#F3EBDD`, Launch Orange `#E87842` (primary accent), Orbit Blue `#8DAFC1`, Earth Sage `#71836D`, Moon Dust `#C5B9A5`.
- **Type:** Space Grotesk (oversized editorial headlines), **Space Mono** (mission-control labels, uppercase/tracked), Inter (body).
- **Details:** alternating navy/cream bands, orbital rings, corner brackets on the hero video, film grain, monospace coordinate/label tags, restrained motion. All colors are CSS variables in `css/styles.css` `:root`.

---

## 3. Sitemap + SEO keyword map (recommended)

Currently built as a **single conversion-focused homepage**. For full SEO coverage, expand to these indexable pages (distinct intent each — no cannibalization). _Search volumes/difficulty must be validated in Google Search Console / Ahrefs / Keyword Planner — not invented here._

| URL | Primary keyword (intent) | H1 | Title tag | Conversion goal |
|---|---|---|---|---|
| `/` | brand + creative & Meta ads Austin (mixed) | Made to stand out. Built to perform. | Video Creative & Meta Ads Agency in Austin, TX | Book a strategy call |
| `/meta-ads-austin/` | *meta ads management austin* / *facebook ads agency austin* (commercial) | Meta Ads Management in Austin | Meta Ads Management Austin | Ad Meta Advertising | Book a call |
| `/video-production-austin/` | *video production for businesses austin* / *video advertising* (commercial) | Video Creative Production, Austin | Business Video Production & Ad Creative — Austin | Book a call |
| `/work/` | portfolio / *creative advertising agency austin* (consideration) | Selected Work | Our Work — Video & Ad Creative | See work → book |
| `/pricing/` | *marketing agency pricing / packages* (commercial) | Packages & Pricing | Pricing — Retainers from $3,000/mo | Book a call |
| `/about/` | brand/trust (navigational) | About Stellar Roots Media | About — Austin Creative & Performance Studio | Trust → book |
| `/insights/` | informational blog hub (see §7) | Insights | Insights on Video Ads & Meta Advertising | Nurture → book |
| `/contact/` | *book strategy call* (transactional) | Book a Strategy Call | Contact — Book a Strategy Call | Lead |

**Do not** create separate near-duplicate city pages for suburbs (doorway-page risk) — one strong Austin page + genuine local signals instead.

---

## 4. On-page + technical SEO — status

**Done on the homepage build:** one `<h1>`, logical H2/H3, crawlable HTML content (not locked behind JS/video), descriptive alt text, unique title + meta description, semantic landmarks, clean anchor structure, `robots.txt` (allows Google + AI crawlers), `sitemap.xml`, `llms.txt`, Open Graph/Twitter, `theme-color`, responsive, lazy images, mobile nav, accessible FAQ.

**Structured data (implemented, validates):** `ProfessionalService`/`Organization`, `WebSite`, `FAQPage`, `AggregateRating` + 4 real `Review`s, `OfferCatalog` with the 3 real packages. Matches visible content.

**Pending (needs your accounts/hosting — I can't do from here):**
- Google Search Console + GA4 install and sitemap submission (needs property access).
- `LocalBusiness` + link to your **Google Business Profile** (need the GBP URL).
- `BreadcrumbList` + per-service `Service` pages once the subpages above exist.
- `VideoObject` — intentionally **omitted** until real hosted video exists (no fake markup).
- Core Web Vitals/image compression pass once on final hosting.

---

## 5. Generative Engine Optimization (GEO) — done

`llms.txt` states who/where/what/for-whom/how/pricing/results in plain facts; FAQ answers real buyer questions in crawlable HTML; entities (Austin, Meta ads, video, packages) are explicit and consistent across page text + schema. No fabricated authority, no "GEO hacks," no promised citations.

---

## 6. Local SEO
Austin is established consistently (title, H-tags, address region, coordinates, schema `areaServed`/address). **Need from you:** Google Business Profile URL to connect + NAP consistency check. No fake office address used.

---

## 7. 6-month content plan (commercial-intent, lean to maintain)
1. *How much do Meta ads cost for a service business?* 2. *Facebook lead forms vs. landing pages — what converts?* 3. *What makes a video ad actually perform (with examples)?* 4. *How to tell if a marketing agency is worth $3k–$7.5k/mo.* 5. *Meta ads vs. Google ads for high-ticket services.* 6. *A quarter of content from one capture day — how it works.*
Each = one indexable `/insights/` post supporting a service page. One per month; original, experience-based, tied to real work.

---

## 8. Missing assets & decisions needing your approval
1. **Video footage** — hero showreel + Selected Work reels are styled **placeholders**. Send MP4s (or Vimeo/YouTube links) + poster frames and I'll drop them in.
2. **Per-client work details/outcomes** — descriptions are conservative/generic to avoid inventing results. Confirm real project details/metrics per client, or keep generic.
3. **Contact inbox** — form + email use `contact@stellarrootsmedia.com`. Confirm it exists (or switch to your Gmail); first FormSubmit submission needs one activation click.
4. **Google Business Profile URL** (for LocalBusiness + local SEO).
5. **GA4 + Search Console** access (analytics + sitemap submission).
6. **Platform decision** — see §9.

---

## 9. Platform note (important)
Your stack is **WordPress + Elementor + SiteGround**. What I built here is a **standalone static homepage** (HTML/CSS/JS) — I did **not** touch your live site. Two paths:
- **A) Ship static** (fastest): deploy this to Netlify/Vercel as a staging link for approval, then optionally as the live site.
- **B) Port to Elementor:** use this as the pixel/copy reference and rebuild in your WordPress theme (global colors/fonts as above, reusable sections). Needs your WP/staging access; I won't change the live site without approval.
Recommended: review the static version first (approve design/copy), then decide A vs B.

---

## 10. Build report — what's completed vs. outstanding
- ✅ Homepage: 10-section conversion architecture, real packages/results/testimonials/clients, mission-control design, SEO + structured data, working contact form wiring.
- ⏳ Needs your input: video assets, GBP URL, contact inbox confirmation.
- ⏳ Needs credentials/hosting: GA4, Search Console, sitemap submission, Core Web Vitals pass, Elementor port (if chosen).
- ⚠️ Unverified: keyword volumes/difficulty (validate in a keyword tool); any per-client campaign metrics beyond the deck's documented figures.
