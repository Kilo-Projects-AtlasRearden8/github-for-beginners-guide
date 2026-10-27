#!/usr/bin/env python3
"""Build the static HTML site from the Markdown docs."""
import os
import re
import sys

import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
SITE = os.path.join(ROOT, "site")

# Ordered chapters: (filename, display title)
CHAPTERS = [
    ("00-welcome.md", "Welcome to GitHub for Beginners"),
    ("01-creating-an-account.md", "Creating a GitHub Account"),
    ("02-repositories.md", "Repositories"),
    ("03-commits.md", "Commits"),
    ("04-issues.md", "Issues"),
    ("05-pull-requests.md", "Pull Requests"),
    ("06-releases.md", "Releases"),
    ("07-github-pages.md", "GitHub Pages"),
    ("08-first-repo-checklist.md", "First-Repo Checklist"),
    ("09-glossary.md", "Glossary"),
]

MD_EXTENSIONS = [
    "extra",
    "toc",
    "sane_lists",
    "attr_list",
    "md_in_html",
]

LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\.md\)')


def md_to_html(text):
    """Convert markdown text to HTML, rewriting .md links to .html."""
    def repl(match):
        label, target = match.group(1), match.group(2)
        return f"[{label}]({target}.html)"
    text = LINK_RE.sub(repl, text)
    html = markdown.markdown(text, extensions=MD_EXTENSIONS)
    return html


CSS = """
:root {
  --ink: #1f2937;
  --muted: #6b7280;
  --brand: #2f6f8f;
  --brand-dark: #1f4e63;
  --accent: #d97706;
  --bg: #f7fafc;
  --surface: #ffffff;
  --border: #e5e7eb;
  --code-bg: #eef2f5;
  --nav-bg: #ffffff;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }

body {
  margin: 0;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
  font-size: 16px;
  line-height: 1.7;
  color: var(--ink);
  background: var(--bg);
}

a { color: var(--brand); text-decoration: underline; text-underline-offset: 2px; }
a:hover { color: var(--brand-dark); }

.skip {
  position: absolute; left: -9999px; top: auto; width: 1px; height: 1px;
  overflow: hidden;
}

/* Header */
header {
  background: var(--brand-dark);
  color: #fff;
  padding: 1.25rem 1.5rem;
}
.header-inner { max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; gap: 0.5rem; }
.site-title { margin: 0; font-size: 1.5rem; font-weight: 700; letter-spacing: 0.2px; }
.site-title a { color: #fff; text-decoration: none; }
.site-sub { font-size: 0.95rem; color: #cbd5e1; margin: 0; }
.site-credit { font-size: 0.85rem; color: #94a3b8; margin-top: 0.25rem; }

/* Layout */
.wrap { max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }
main { display: flex; gap: 2rem; padding: 2rem 0; }

/* Navigation */
nav.sidebar {
  flex: 0 0 260px;
  position: sticky;
  top: 1.5rem;
  height: fit-content;
}
nav.sidebar h2 {
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin: 0 0 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border);
}
.search {
  width: 100%;
  padding: 0.55rem 0.75rem;
  font-size: 0.95rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: #fff;
  margin-bottom: 1rem;
  outline: none;
}
.search:focus { border-color: var(--brand); }
ul.chapters { list-style: none; padding: 0; margin: 0; }
ul.chapters li { margin: 0.35rem 0; }
ul.chapters a {
  display: block;
  padding: 0.5rem 0.75rem;
  border-radius: 8px;
  color: var(--ink);
  text-decoration: none;
  border: 1px solid transparent;
}
ul.chapters a:hover { background: #eef2f7; border-color: var(--border); }
ul.chapters a.active { background: var(--brand); color: #fff; border-color: var(--brand); }

/* Content */
article {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem 2.5rem;
}
article h1 {
  font-size: 2rem;
  margin-top: 0;
  border-bottom: 2px solid var(--border);
  padding-bottom: 0.5rem;
}
article h2 { font-size: 1.4rem; margin-top: 1.75rem; }
article h3 { font-size: 1.15rem; margin-top: 1.5rem; }
article p { margin: 0 0 1rem; }
article ul, article ol { margin: 0.5rem 0 1rem 1.25rem; padding-left: 1rem; }
article li { margin: 0.35rem 0; }
article code { background: var(--code-bg); padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.9em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
article pre { background: var(--code-bg); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; overflow-x: auto; }
article pre code { padding: 0; background: transparent; font-size: 0.9em; }
article table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
article th, article td { border: 1px solid var(--border); padding: 0.5rem 0.75rem; text-align: left; }
article th { background: #f3f4f6; }
article blockquote {
  border-left: 4px solid var(--brand);
  margin: 1rem 0;
  padding: 0.75rem 1.25rem;
  background: #f0f7fa;
  color: #334155;
}
article hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }

.toc {
  background: #f8fafc;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}
.toc h3 { margin-top: 0; font-size: 1rem; }
.toc ul { list-style: none; padding-left: 0; margin: 0.5rem 0 0; }
.toc li { margin: 0.25rem 0; }
.toc a { text-decoration: none; color: var(--ink); }
.toc a:hover { color: var(--brand); }

.nav-links {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
  display: flex;
  gap: 1rem;
  justify-content: space-between;
  font-size: 0.95rem;
}
.nav-links a { text-decoration: none; color: var(--brand); }
.nav-links a:hover { text-decoration: underline; }

/* Footer */
footer {
  background: var(--brand-dark);
  color: #cbd5e1;
  padding: 2rem 1.5rem;
  font-size: 0.9rem;
}
.footer-inner { max-width: 1100px; margin: 0 auto; border-top: 1px solid #334155; padding-top: 1.5rem; }
footer a { color: #93c5fd; }
.small { font-size: 0.85rem; color: #94a3b8; }

@media (max-width: 768px) {
  main { flex-direction: column; padding: 1rem 0; }
  nav.sidebar { position: static; width: 100%; }
  article { padding: 1.25rem 1.5rem; }
}
"""

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — GitHub for Beginners</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a href="#content" class="skip">Skip to content</a>

<header>
  <div class="header-inner">
    <h1 class="site-title"><a href="index.html">GitHub for Beginners</a></h1>
    <p class="sub">A plain-English, step-by-step beginner manual — no command line required.</p>
    <p class="credit">Prepared by <strong>Asdale Dynamics, LLC</strong> — beginner-friendly AI education, books, and guides.</p>
  </div>
</header>

<div class="wrap">
<main>
  <nav class="sidebar" aria-label="Chapters">
    <h2>Contents</h2>
    <input type="text" class="search" id="chapterSearch" placeholder="Filter chapters…">
    <ul class="chapters" id="chapterList">{chapter_list}</ul>
  </nav>

  <article id="content">{body}</article>
</main>
</div>

<footer>
  <div class="footer-inner">
    <p>Copyright (c) 2026 Asdale Dynamics, LLC. Released under the <a href="../LICENSE.html">MIT License</a>.</p>
    <p class="small">Credit: Asdale Dynamics, LLC — Dylan Asdale, registered nurse turned AI author and founder.</p>
  </div>
</footer>

<script src="script.js"></script>
</body>
</html>
"""


def chapter_list_html(current_file):
    items = []
    for fname, title in CHAPTERS:
        href = fname.replace(".md", ".html")
        active = ' class="active"' if fname == current_file else ""
        items.append(f'<li><a href="{href}"{active}>{title}</a></li>')
    return "\n".join(items)


def build():
    os.makedirs(SITE, exist_ok=True)

    # Copy CSS
    with open(os.path.join(SITE, "style.css"), "w") as f:
        f.write(CSS)

    # Build chapter pages
    for fname, title in CHAPTERS:
        with open(os.path.join(DOCS, fname), encoding="utf-8") as f:
            md_text = f.read()

        body_html = md_to_html(md_text)
        # Extract first H1 as title override if present
        m = re.search(r"<h1>(.*?)</h1>", body_html, re.S)
        if m:
            page_title = re.sub(r"<[^>]+>", "", m.group(1))
        else:
            page_title = title

        chapter_html = chapter_list_html(fname)
        page = PAGE_TEMPLATE.format(
            title=page_title,
            chapter_list=chapter_html,
            body=body_html,
        )

        out_name = fname.replace(".md", ".html")
        with open(os.path.join(SITE, out_name), "w", encoding="utf-8") as f:
            f.write(page)

        print(f"built {out_name}")

    # Script
    with open(os.path.join(ROOT, "site-template-script.js"), encoding="utf-8") as f:
        script = f.read()
    with open(os.path.join(SITE, "script.js"), "w", encoding="utf-8") as f:
        f.write(script)
    print("built script.js")

    # Index page (redirects to welcome)
    index = PAGE_TEMPLATE.format(
        title="Welcome",
        chapter_list=chapter_list_html("00-welcome.md"),
        body=('<p class="sub">Start with <a href="00-welcome.html">Welcome to GitHub for Beginners</a>.</p>'),
    )
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(index)
    print("built index.html")

    # LICENSE page
    with open(os.path.join(ROOT, "LICENSE"), encoding="utf-8") as f:
        lic = f.read()
    lic_html = "<pre>" + lic.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") + "</pre>"
    lic_page = PAGE_TEMPLATE.format(
        title="MIT License",
        chapter_list=chapter_list_html("00-welcome.md"),
        body=lic_html,
    )
    with open(os.path.join(SITE, "LICENSE.html"), "w", encoding="utf-8") as f:
        f.write(lic_page)
    print("built LICENSE.html")


if __name__ == "__main__":
    build()
    print("Done.")
