# NV2 Lab Manual — Project Notes

Sphinx + MyST (Markdown) documentation site for the NV2 experimental setup (Quantum Engineering
Group). Deployed to GitHub Pages automatically on every push to `main` via
[.github/workflows/sphinx.yml](.github/workflows/sphinx.yml).

## Layout

- Source pages: `docs/source/**/*.md` — organized into `background/`, `system_overview/`,
  `calibration/`, `experiments/`, `appendix/`.
- Each section has an `index.md` with a summary table + a `` ```{toctree}``` `` block listing its
  pages. **When adding a new page, add it to both** — a page missing from the toctree builds fine
  but is orphaned (Sphinx warns "document isn't included in any toctree") and won't show in the
  sidebar.
- Images live in `docs/source/_static/images/`, referenced with relative paths like
  `../_static/images/foo.png`.
- `docs/build/` is git-ignored (CI rebuilds it fresh on every deploy).

## Building & previewing locally

```bash
cd "/Users/alexungar/Documents/research/NV2 docs" && .venv/bin/sphinx-build -b html docs/source docs/build/html
```

This is incremental (fast after the first run). Read the warnings it prints — common ones are
`image file not readable` (figure directive points at an image that doesn't exist yet) and
`document isn't included in any toctree` (page not linked from its section's `index.md`).

To view the result, serve the build directory over local HTTP and open it in a browser:

```bash
cd "/Users/alexungar/Documents/research/NV2 docs/docs/build/html" && python3 -m http.server 8123 --bind 127.0.0.1
```

Then open http://127.0.0.1:8123/. Rebuild + refresh after each edit (no live-reload —
`sphinx-autobuild` doesn't work in this sandboxed environment because subprocess dev-servers here
can't resolve the working directory; plain `sphinx-build` + a background `http.server` is the
working alternative). `sphinx-autobuild` is still listed in `docs/requirements-dev.txt` for use in
a normal (non-sandboxed) terminal, where live-reload does work.

## Content conventions

- Each page starts with a single `# Title` (required — a missing title breaks its toctree entry).
- Figures use the MyST directive:
  ```
  ```{figure} ../_static/images/name.png
  :alt: Short description
  :width: 80%
  :align: center

  Caption text.
  ```
  ```
  For side-by-side multi-panel figures, see the raw-HTML pattern in
  [docs/source/index.md](docs/source/index.md).
- Cross-references between pages use `` {doc}`../section/page` `` (relative path, no `.md`
  extension).
- Citations use footnote syntax: `text[^Label]` with `[^Label]: full reference` at the bottom of
  the page.
- Many sections still have incomplete content marked with `*Add: ...*` — these are placeholders
  for data/details not yet written up, not errors.
- Component pages typically end with a "Key Parameters" table (`| Parameter | Value | Notes |`).

## Publishing

Once changes look right in the local preview, commit and push to `main` (with the user's
confirmation) — GitHub Actions rebuilds and deploys to GitHub Pages automatically. No manual
deploy step.
