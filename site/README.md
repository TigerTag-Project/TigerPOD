# The TigerPOD site

The showcase site of the TigerPOD, published on GitHub Pages:
<https://tigertag-project.github.io/TigerPOD/>

It presents the Pod and sends readers to what the README provides: the print files on
MakerWorld, the build steps and parts, the electronics kit on the TigerTag shop, Tiger
Studio Manager and the SDKs. It is static HTML, one page per language, built by
[`build.py`](build.py) and published by [`pages.yml`](../.github/workflows/pages.yml)
on every push to `main` that touches `site/`, `assets/`, `llms.txt` or `README.md`.
Pull requests run the same build and checks without deploying.

It shares its architecture and look with the
[TigerTag protocol site](https://tigertag-project.github.io/TigerTag-RFID-Guide/)
([source](https://github.com/TigerTag-Project/TigerTag-RFID-Guide/tree/main/site)).

## Files

| File | Contents |
|---|---|
| [`template.html`](template.html) | The page. Every `{{key}}` is replaced by the text of that key in the page's language; `{{@…}}` keys are filled by `build.py` (language menu, `hreflang` links, JSON-LD, colour gallery, MakerWorld links). |
| [`i18n/en.json`](i18n/en.json) | The English text, which is the reference: every other language has exactly its keys. |
| `i18n/<lang>.json` | `fr`, `de`, `es`, `it`, `zh` (Simplified Chinese), `pt` (Brazil), `pt-pt` (Portugal), `pl`, `ru`, `nl`. |
| [`site.css`](site.css), [`site.js`](site.js) | The look (dark by default, light on request) and the theme / language buttons. Each page loads them with `?v=` and a hash of the file's content, so a new version is never hidden by a browser cache. |
| [`seo_check.py`](seo_check.py) | Checks the built pages for search and answer engines. |
| [`assets/`](assets/) | Web-sized copies (WebP, a short silent MP4) of the repository's own photos in [`../assets/`](../assets/), the black TigerTag logo for the light theme, the favicon and the touch icon. |

## Editing

- **Change a text**: edit `i18n/en.json`, then the same key in every other language.
- **Add a text**: add the key to every `i18n/*.json` file and use `{{key}}` in `template.html`.
  The build refuses a language that misses a key, has an unknown one or an empty value.
- **Facts only**: every statement on the page comes from the README. A new fact goes to
  the README and `llms.txt` first. No prices.
- **Check and preview**:

  ```bash
  python3 site/build.py --check
  python3 site/build.py --out _site && python3 site/seo_check.py _site
  python3 -m http.server 8000 --directory _site
  python3 site/build.py --only en   # English only, while translations are pending
  ```

`seo_check.py` checks every page: title and description length, one `h1`, canonical
and `hreflang`, sharing cards, `alt` text, JSON-LD types (`Organization`, `WebSite`,
`Product`, `CreativeWork`, `HowTo`, `FAQPage`), the FAQ and build steps they mirror,
in-page links, sitemap, robots and `llms.txt`.

The English page is the root (`/`), every other language has its own folder (`/fr/`,
`/zh/`…). A language chosen in the menu is remembered, and the English root forwards to
it on the next visit.
