# GitHub for Beginners

A plain-English, step-by-step beginner manual for GitHub: creating an account, repositories, commits, issues, pull requests, releases, and publishing a free static site with GitHub Pages. **No command line required.**

## Who this is for

Anyone new to GitHub — no programming experience needed. You only need a web browser.

This guide was prepared by **Asdale Dynamics, LLC**, an Indiana LLC founded by Dylan Asdale, a registered nurse turned AI author. Asdale Dynamics publishes beginner-friendly AI education, books, guides, and practical tools, explained plainly "like a friend would."

Dylan's book, *The Massive AI Manual*, and his hub site at **dylanasdale.github.io** explain AI in plain English, step by step, never condescending.

## What's inside

| Section | What you'll learn |
|---|---|
| Welcome | What GitHub is and how to use this manual |
| Creating a GitHub Account | Sign up, confirm your email, set up your profile, enable two-factor authentication |
| Repositories | Create a repo, add and edit files, upload files, write a README |
| Commits | Save changes, view history, write good commit messages, undo mistakes |
| Issues | Track bugs, ideas, and tasks; label, assign, close, and reopen |
| Pull Requests | Create branches, propose changes, review, and merge |
| Releases | Tag and publish versioned releases with downloadable files |
| GitHub Pages | Publish a free static website from a repository |
| First-Repo Checklist | A step-by-step checklist for your first repository |
| Glossary | Plain-English definitions of GitHub terms |

## Read it

- **Markdown:** read the manual in `docs/`, starting with [`docs/00-welcome.md`](docs/00-welcome.md).
- **Static HTML site:** open `site/index.html` in your browser, or open any chapter directly in `site/`.

## Build the site (optional)

The HTML site in `site/` is generated from the Markdown in `docs/`. To rebuild it:

```bash
python3 build_site.py
```

This requires Python 3 and the `markdown` package (`pip install markdown`). The build script writes `style.css`, `script.js`, and one HTML file per chapter into `site/`.

## Credit

Prepared by **Asdale Dynamics, LLC** — beginner-friendly AI education, books, and guides.
Dylan Asdale, registered nurse turned AI author and founder of Asdale Dynamics, LLC (Indiana, formed October 2026).

## License

This manual and site are released under the [MIT License](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC.
