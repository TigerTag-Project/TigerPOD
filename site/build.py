"""Build the TigerPOD showcase site (GitHub Pages) into `_site/`.

One static page per language, all from `template.html` and `i18n/<lang>.json`:
English at the root, the others under `/<lang>/`. Every page is complete HTML in
its own language (what a search engine, an AI crawler or a reader without
JavaScript sees) with `hreflang` links between them, JSON-LD in its language
and a sitemap listing them all.

The pictures in `site/assets/` are web-sized copies of the repository's own
photos in `assets/`; the white TigerTag logo is taken from `assets/` as is.

Usage:
    python site/build.py                 # build into _site/
    python site/build.py --check         # only check the translations
    python site/build.py --out DIR --url https://example.org/path/
"""

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SITE_URL = "https://tigertag-project.github.io/TigerPOD/"
REPO_URL = "https://github.com/TigerTag-Project/TigerPOD"

# The eleven languages of the TigerTag sites, in the same order. `pt` (Brazil)
# and `pt-pt` (Portugal) are separate dictionaries on purpose.
LANGS = ["en", "fr", "de", "es", "it", "zh", "pt", "pt-pt", "pl", "ru", "nl"]
HTML_LANG = {"zh": "zh-Hans", "pt": "pt-BR", "pt-pt": "pt-PT"}
OG_LOCALE = {"en": "en_US", "fr": "fr_FR", "de": "de_DE", "es": "es_ES", "it": "it_IT",
             "zh": "zh_CN", "pt": "pt_BR", "pt-pt": "pt_PT", "pl": "pl_PL", "ru": "ru_RU", "nl": "nl_NL"}

# Repository file -> published path under assets/.
ASSETS = {
    # White logo on the dark theme; the black (contouring) one is in site/assets/.
    "assets/logo_tigertag_head.svg": "logo-tigertag-white.svg",
}

# The shells and the kit, exactly as linked from the README.
MAKERWORLD_MINI = "https://makerworld.com/fr/models/3190348-tigerpod-mini-for-openspool-tigertag-rfid-filament"
MAKERWORLD_ORIGINAL = "https://makerworld.com/fr/models/1289152-tigertag-io-open-spool-pod-for-rfid-filament"

# Crawlers of search and answer engines, welcomed by name in robots.txt: the
# project is meant to be read and cited. Listing them is an explicit opt-in.
AI_AGENTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
             "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot",
             "Amazonbot", "Bytespider", "Meta-ExternalAgent", "cohere-ai", "DuckAssistBot", "MistralAI-User"]

ORG_ID = "https://tigersystem.io/#organization"
# The photos of the colour gallery (site/assets/pods/), as in the README.
POD_COLOURS = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "gold", "copper",
               "silver", "grey", "black", "white", "glow"]
POD_FINISHES = ["silk-red", "silk-pink", "silk-yellow", "silk-blue", "silk-black", "silk-gold", "silk-copper",
                "silk-silver", "galaxy-purple", "marble", "rainbow-linear", "rainbow-multi",
                "glow-green-dark", "glow-blue-dark", "glow-red-dark"]
STEPS = 5
FAQ_COUNT = 8

PLACEHOLDER = re.compile(r"\{\{([a-z0-9_@]+)\}\}")


def asset_version(name):
    """Short sha256 of a published site file, appended to its URL as ?v=."""
    return hashlib.sha256((HERE / name).read_bytes()).hexdigest()[:10]


def page_date():
    """Last change to the site or the README, as an ISO date."""
    try:
        date = subprocess.run(["git", "log", "-1", "--format=%cI", "--", "site", "README.md", "llms.txt"],
                              cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()[:10]
    except (OSError, subprocess.CalledProcessError):
        date = ""
    return date or datetime.now(timezone.utc).date().isoformat()


def load_dictionaries():
    """Every language, checked against English: same keys, none empty."""
    dicts = {}
    for lang in LANGS:
        path = HERE / "i18n" / f"{lang}.json"
        if not path.exists():
            raise SystemExit(f"error: missing translation {path.relative_to(REPO)}")
        dicts[lang] = json.loads(path.read_text(encoding="utf-8"))
    reference = list(dicts["en"])
    problems = []
    for lang, words in dicts.items():
        missing = [k for k in reference if k not in words]
        extra = [k for k in words if k not in dicts["en"]]
        empty = [k for k, v in words.items() if not isinstance(v, str) or not v.strip()]
        for label, keys in (("missing", missing), ("unknown", extra), ("empty", empty)):
            if keys:
                problems.append(f"{lang}.json: {label} key(s): {', '.join(keys)}")
    template_keys = set(PLACEHOLDER.findall((HERE / "template.html").read_text(encoding="utf-8")))
    unused = [k for k in template_keys if not k.startswith("@") and k not in dicts["en"]]
    if unused:
        problems.append(f"template.html uses unknown key(s): {', '.join(sorted(unused))}")
    if problems:
        raise SystemExit("error: translations do not match en.json\n  " + "\n  ".join(problems))
    return dicts


def page_path(lang):
    return "" if lang == "en" else f"{lang}/"


def jsonld(lang, words, site_url, url, date):
    inlang = HTML_LANG.get(lang, lang)
    image = site_url + "assets/og.jpg"
    org = {"@context": "https://schema.org", "@type": "Organization", "@id": ORG_ID, "name": "TigerTag Corp",
           "url": "https://tigersystem.io", "logo": site_url + "assets/apple-touch-icon.png",
           "email": "tigertag@tigertag.io",
           "sameAs": ["https://github.com/TigerTag-Project", "https://wiki.tigersystem.io",
                      "https://tigertag-project.github.io/TigerTag-RFID-Guide/"]}
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": "TigerPOD", "url": url,
               "inLanguage": inlang, "description": words["meta_description"], "publisher": {"@id": ORG_ID}}
    product = {"@context": "https://schema.org", "@type": "Product", "name": "TigerPOD",
               "description": words["meta_description"], "image": image, "url": url,
               "brand": {"@type": "Brand", "name": "TigerTag"}, "manufacturer": {"@id": ORG_ID},
               "category": "NFC reader and writer for 3D-printing filament spools",
               "isRelatedTo": {"@type": "Product", "name": "TigerPOD Mini", "url": MAKERWORLD_MINI}}
    design = {"@context": "https://schema.org", "@type": "CreativeWork",
              "name": "TigerPOD open hardware design", "description": words["shells_lead"],
              "inLanguage": inlang, "url": REPO_URL, "image": image, "dateModified": date,
              "license": "https://creativecommons.org/licenses/by/4.0/",
              "author": {"@type": "Person", "name": "Benoit Michaut"}, "publisher": {"@id": ORG_ID},
              "workExample": [{"@type": "CreativeWork", "name": "TigerPOD Mini", "url": MAKERWORLD_MINI},
                              {"@type": "CreativeWork", "name": "TigerPOD (original)", "url": MAKERWORLD_ORIGINAL}]}
    howto = {"@context": "https://schema.org", "@type": "HowTo", "name": words["build_title"],
             "description": words["build_lead"], "inLanguage": inlang, "image": image,
             "supply": [{"@type": "HowToSupply", "name": words[k]} for k in ("part_reader", "part_tags", "part_shell")],
             "step": [{"@type": "HowToStep", "position": i, "name": words[f"step{i}_title"],
                       "text": words[f"step{i}_text"], "url": f"{url}#step{i}"} for i in range(1, STEPS + 1)]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": inlang,
           "mainEntity": [{"@type": "Question", "name": words[f"faq{i}_q"],
                           "acceptedAnswer": {"@type": "Answer", "text": words[f"faq{i}_a"]}}
                          for i in range(1, FAQ_COUNT + 1)]}
    # `</` never appears inside a <script> block.
    return "\n".join('<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False).replace("</", "<\\/") + "</script>"
                     for j in (org, website, product, design, howto, faq))


def pod_row(names, base, alt):
    """One gallery row: the last photo carries the row's description, the others are its duplicates."""
    return "\n".join(
        f'      <img src="{base}assets/pods/{name}.webp" alt="{html.escape(alt) if i == len(names) - 1 else ""}" '
        f'width="240" height="240" loading="lazy">' for i, name in enumerate(names))


def render(template, lang, words, dicts, site_url, date):
    base = "" if lang == "en" else "../"
    url = site_url + page_path(lang)

    alternates = [f'<link rel="alternate" hreflang="{HTML_LANG.get(l, l)}" href="{site_url}{page_path(l)}">' for l in LANGS]
    alternates.append(f'<link rel="alternate" hreflang="x-default" href="{site_url}">')

    menu = []
    for l in LANGS:
        current = ' aria-current="true"' if l == lang else ""
        menu.append(f'          <li><a href="{base}{page_path(l)}" hreflang="{HTML_LANG.get(l, l)}" '
                    f'lang="{HTML_LANG.get(l, l)}" data-lang="{l}"{current}>{html.escape(dicts[l]["lang_name"])}</a></li>')

    special = {
        "@lang": lang,
        "@htmllang": HTML_LANG.get(lang, lang),
        "@oglocale": OG_LOCALE[lang],
        "@oglocalealt": "\n".join(f'<meta property="og:locale:alternate" content="{OG_LOCALE[l]}">' for l in LANGS if l != lang),
        "@url": url,
        "@siteurl": site_url,
        "@base": base,
        "@langpath": page_path(lang),
        "@alternates": "\n".join(alternates),
        "@langmenu": "\n".join(menu),
        "@jsonld": jsonld(lang, words, site_url, url, date),
        "@podcolours": pod_row(POD_COLOURS, base, words["colours_alt"]),
        "@podfinishes": pod_row(POD_FINISHES, base, words["finishes_alt"]),
        "@mini": MAKERWORLD_MINI,
        "@original": MAKERWORLD_ORIGINAL,
        # Content hashes: a new site.css / site.js gets a new URL, so no browser
        # keeps the previous one from its cache.
        "@vcss": asset_version("site.css"),
        "@vjs": asset_version("site.js"),
    }

    def fill(match):
        key = match.group(1)
        if key in special:
            return special[key]
        return html.escape(words[key], quote=True)

    return PLACEHOLDER.sub(fill, template)


def build(out, site_url):
    dicts = load_dictionaries()
    template = (HERE / "template.html").read_text(encoding="utf-8")
    date = page_date()
    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)

    for lang in LANGS:
        target = out / page_path(lang) / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(template, lang, dicts[lang], dicts, site_url, date), encoding="utf-8")

    for name in ("site.css", "site.js"):
        shutil.copy2(HERE / name, out / name)
    for source, published in ASSETS.items():
        shutil.copy2(REPO / source, out / "assets" / published)
    # Web-sized pictures made for the site (site/assets/), from the README's photos.
    shutil.copytree(HERE / "assets", out / "assets", dirs_exist_ok=True)
    shutil.copy2(HERE / "og.jpg", out / "assets" / "og.jpg")
    # The machine-readable description of the project, at the site root too.
    shutil.copy2(REPO / "llms.txt", out / "llms.txt")

    urls = "\n".join(
        "  <url><loc>{}</loc><lastmod>{}</lastmod>{}</url>".format(
            site_url + page_path(lang), date,
            "".join(f'<xhtml:link rel="alternate" hreflang="{HTML_LANG.get(l, l)}" href="{site_url}{page_path(l)}"/>' for l in LANGS))
        for lang in LANGS)
    (out / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{urls}\n</urlset>\n", encoding="utf-8")
    robots = ["User-agent: *", "Allow: /", ""]
    for agent in AI_AGENTS:
        robots += [f"User-agent: {agent}", "Allow: /", ""]
    robots += [f"Sitemap: {site_url}sitemap.xml"]
    (out / "robots.txt").write_text("\n".join(robots) + "\n", encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"built {len(LANGS)} languages into {out}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(REPO / "_site"))
    parser.add_argument("--url", default=SITE_URL)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", help="comma-separated languages, for a quick local preview")
    args = parser.parse_args()
    if args.only:
        LANGS[:] = [l for l in LANGS if l in args.only.split(",")]
    if args.check:
        load_dictionaries()
        print(f"translations OK: {len(LANGS)} languages")
        return
    url = args.url if args.url.endswith("/") else args.url + "/"
    build(Path(args.out), url)


if __name__ == "__main__":
    sys.exit(main())
