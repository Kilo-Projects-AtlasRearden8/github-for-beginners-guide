#!/usr/bin/env python3
"""Verify the static site: internal links resolve, copyright line exact, README credit."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

errors = []

# 1. All chapter HTML files exist
chapters = [
    "00-welcome.html", "01-creating-an-account.html", "02-repositories.html",
    "03-commits.html", "04-issues.html", "05-pull-requests.html",
    "06-releases.html", "07-github-pages.html", "08-first-repo-checklist.html",
    "09-glossary.html", "index.html", "LICENSE.html",
]
for c in chapters:
    p = os.path.join(SITE, c)
    if not os.path.exists(p):
        errors.append(f"missing file: {c}")

# 2. Internal links resolve
html_files = [f for f in os.listdir(SITE) if f.endswith(".html")]
existing = set(html_files)
link_re = re.compile(r'href="([^"]+)"')
for f in html_files:
    with open(os.path.join(SITE, f), encoding="utf-8") as fh:
        content = fh.read()
    for m in link_re.finditer(content):
        href = m.group(1)
        # Skip external, anchor-only, fragment, css, js links
        if href.startswith("http") or href.startswith("mailto") or href.startswith("#"):
            continue
        if href.lower().endswith((".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico")):
            continue
        # Strip fragment
        target = href.split("#")[0]
        # Handle ../LICENSE.html -> LICENSE.html
        if target.startswith("../"):
            target = target[3:]
        if target not in existing:
            errors.append(f"broken link in {f}: -> {href}")

# 3. No leftover .md links
for f in html_files:
    with open(os.path.join(SITE, f), encoding="utf-8") as fh:
        content = fh.read()
    if re.search(r'\.md[")]', content):
        errors.append(f"unconverted .md link in {f}")

# 4. LICENSE copyright line exact
with open(os.path.join(ROOT, "LICENSE"), encoding="utf-8") as fh:
    lic = fh.read()
expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
if expected not in lic:
    errors.append("LICENSE missing exact copyright line")
# ensure it's on its own line properly
lines = [l for l in lic.splitlines() if l.strip() == expected]
if len(lines) != 1:
    errors.append(f"LICENSE copyright line count = {len(lines)} (expected 1)")

# 5. README credits Asdale Dynamics
with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
    readme = fh.read()
if "Asdale Dynamics" not in readme:
    errors.append("README does not credit Asdale Dynamics")
if expected not in readme:
    errors.append("README missing exact copyright line")

# 6. No .github/workflows
if os.path.exists(os.path.join(ROOT, ".github", "workflows")):
    errors.append(".github/workflows exists (should not)")

# 7. No secrets-ish patterns in site/docs
secret_patterns = [r"sk-", r"ghp_", r"API[_-]?KEY", r"password\s*=\s*['\"]"]
for root, _, files in os.walk(ROOT):
    if "/.git" in root or root.endswith(".git"):
        continue
    for fn in files:
        if fn.endswith(".gitignore"):
            continue
        p = os.path.join(root, fn)
        if os.path.basename(p) in ("verify_site.py", "build_site.py"):
            continue
        try:
            with open(p, encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except Exception:
            continue
        for pat in secret_patterns:
            if re.search(pat, content, re.I):
                errors.append(f"possible secret pattern {pat} in {p}")

if errors:
    print("VERIFICATION FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"VERIFICATION PASSED: {len(html_files)} HTML files, all internal links resolve, copyright/credit OK, no secrets, no workflows.")
