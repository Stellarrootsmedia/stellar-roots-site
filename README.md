# Stellar Roots Media — Website

A fast, modern, SEO- and AI-citation-optimized static site. No build step, no framework — plain HTML/CSS/JS. Built around the offerings in the 2026 pitch deck (The Orbit).

**Theme:** dark cosmic "growth engine" — near-black `#08080F`, stellar violet→blue gradient `#8B6CFF → #4E86FF`, star-gold `#F6C66B`. Fonts **Space Grotesk** + **Inter**. All colors are CSS variables at the top of `css/styles.css`.

## Files
```
index.html         one page — all content + JSON-LD structured data
css/styles.css     design system (edit :root variables to re-skin)
js/main.js         nav, FAQ, contact form, scroll reveal
assets/logo-black.png   your logo (auto-inverted to white on the dark theme via CSS)
robots.txt sitemap.xml llms.txt site.webmanifest
```

## Run locally
Open `index.html` directly in a browser, or:
```bash
cd "Stellar Roots Website" && python3 .claude/serve.py   # http://localhost:4322
```

## Edit your content
Everything is plain HTML in `index.html`, clearly sectioned (Approach, The Orbit, Engine,
Services, Results, Reviews, Pricing, Peace of Mind, FAQ, Contact). To change offerings or
pricing, edit that section's markup.

### A few things to finish
- **Contact inbox:** the form + email links point to `contact@stellarrootsmedia.com`
  (in `js/main.js` → `CONTACT_ENDPOINT`, and the mailto links in `index.html`). Make sure
  that mailbox exists, or change it to your Gmail. First submission triggers a one-time
  FormSubmit activation email — click it once or nothing gets delivered.
- **Reviews:** the testimonial cards use your real client names with placeholder
  "Verified Google review" text. Paste the actual Google review quotes into the `q`
  paragraphs in the Reviews section when ready (or link the cards to your Google profile).
- **Pricing inclusions:** the per-plan bullet lists are a sensible starting point — adjust
  them to match exactly what each tier includes.
- **Book a call:** buttons currently scroll to the contact form. To use Calendly instead,
  change the `href="#contact"` on the "Book a call" buttons to your Calendly link.
- **Add real photos:** drop capture stills / client ad frames into `assets/` and reference
  them in the hero, engine, or results sections for extra impact.

## SEO & AI citation (already built in)
- JSON-LD: ProfessionalService/Organization, WebSite, FAQPage, OfferCatalog (pricing),
  AggregateRating (5.0).
- llms.txt summary for AI answer engines; robots.txt allows AI crawlers; sitemap.xml.
- Open Graph/Twitter meta, canonical, semantic HTML, one `<h1>`, lazy fonts.

## Deploy
Push to GitHub, then connect the repo to Netlify or Vercel for a free live URL, and point
`stellarrootsmedia.com` at it. (See ~/Documents/topflight-master-build-guide.md for the
exact GitHub + deploy commands.)
