# STATUS

## What was built

A beginner manual for GitHub, delivered as Markdown docs plus a generated static HTML site.

**Docs (`docs/`):** 10 chapters in plain English, step by step, no command line required:
- `00-welcome.md` — What GitHub is and how to use the manual
- `01-creating-an-account.md` — Sign up, confirm email, profile, two-factor authentication
- `02-repositories.md` — Create a repo, add/edit/upload files, README
- `03-commits.md` — Save changes, view history, commit messages, undo mistakes
- `04-issues.md` — Track bugs, ideas, tasks; label, assign, close, reopen
- `05-pull-requests.md` — Branches, propose changes, review, merge
- `06-releases.md` — Tag and publish versioned releases
- `07-github-pages.md` — Publish a free static site with GitHub Pages
- `08-first-repo-checklist.md` — First-repo checklist
- `09-glossary.md` — Plain-English GitHub terms

**Static site (`/`):** `build_site.py` converts the Markdown to a polished, navigable HTML site in `site/` with shared CSS, chapter navigation, client-side search filter, and skip-to-content link.

**Other files:**
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — credits Asdale Dynamics, LLC and Dylan Asdale; includes exact copyright line
- `build_site.py` — site generator
- `verify_site.py` — link/requirements verifier
- `site-template-script.js` — client-side search template (copied to `site/script.js`)

**Credit:** Asdale Dynamics, LLC is credited in `README.md`, every doc footer, the site header, and the site footer. Prepared for Dylan Asdale, registered nurse turned AI author and founder of Asdale Dynamics, LLC (Indiana, formed October 2026).

## How to run it

Open the static site in a browser:

```
site/index.html
```

Or open any chapter directly, e.g. `site/00-welcome.html`.

To rebuild the site from the Markdown:

```
python3 build_site.py
```

Requires Python 3 and the `markdown` package:

```
pip install markdown
```

## Verification results

`python3 verify_site.py` → PASSED

- 12 HTML files generated (10 chapters + index + LICENSE)
- All internal links resolve (no broken links)
- No leftover `.md` links in generated HTML
- `LICENSE` contains the exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC and includes the exact copyright line
- No `.github/workflows` directory (by design)
- No secrets, API keys, or personal data in files

## Known gaps

- No automated test framework; verification is a custom Python script (`verify_site.py`)
- Site search is client-side filtering only (no backend index)
- The site is not published anywhere (by design — never push, never create remote repos)
- Build requires the third-party `markdown` Python package
- Git history is empty until committed (see below)
