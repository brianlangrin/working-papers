#!/usr/bin/env python3
"""Generate docs/index.html listing all PDFs in the papers/ directory."""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PAPERS_DIR = REPO_ROOT / "docs" / "papers"
OUTPUT_FILE = REPO_ROOT / "docs" / "index.html"

PAPERS_BASE_URL = "papers/"


def get_papers():
    """Return a sorted list of PDF filenames found in the papers/ directory."""
    if not PAPERS_DIR.exists():
        return []
    return sorted(
        f.name
        for f in PAPERS_DIR.iterdir()
        if f.suffix.lower() == ".pdf" and f.is_file()
    )


def paper_title(filename):
    """Convert a filename like my-paper.pdf to a human-readable title."""
    stem = Path(filename).stem
    return stem.replace("-", " ").replace("_", " ").title()


def render_html(papers):
    if papers:
        items = "\n".join(
            f'    <li><a href="{PAPERS_BASE_URL}{name}">{paper_title(name)}</a></li>'
            for name in papers
        )
        list_content = items
    else:
        list_content = '    <li class="empty">No papers have been added yet.</li>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Working Papers</title>
  <style>
    body {{
      font-family: Georgia, serif;
      max-width: 800px;
      margin: 40px auto;
      padding: 0 20px;
      color: #333;
      line-height: 1.6;
    }}
    h1 {{ border-bottom: 2px solid #333; padding-bottom: 10px; }}
    ul {{ list-style: none; padding: 0; }}
    li {{
      padding: 10px 0;
      border-bottom: 1px solid #eee;
    }}
    li:last-child {{ border-bottom: none; }}
    a {{ color: #0066cc; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .empty {{ color: #888; font-style: italic; }}
  </style>
</head>
<body>
  <h1>Working Papers</h1>
  <ul id="paper-list">
{list_content}
  </ul>
  <p><small>Papers are listed as they are added to the repository.</small></p>
</body>
</html>
"""


def main():
    papers = get_papers()
    html = render_html(papers)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"Generated {OUTPUT_FILE} with {len(papers)} paper(s).")


if __name__ == "__main__":
    main()
