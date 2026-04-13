# Working Papers

A repository for hosting PDF working papers on GitHub, with an automatically generated index page served via GitHub Pages.

## Browse Papers

The working papers index is available at:
**https://brianlangrin.github.io/working-papers/**

## Adding a Paper

1. Add your PDF file to the `docs/papers/` directory.
2. Commit and push to the `main` branch.
3. The GitHub Actions workflow will automatically regenerate `docs/index.html` to include the new paper.

Paper filenames become their display titles (e.g. `my-research-paper.pdf` → *My Research Paper*).

## Repository Structure

```
docs/            # GitHub Pages site
  papers/        # PDF working papers (served at .../papers/<filename>.pdf)
  index.html     # Auto-generated index of all papers
scripts/
  generate_index.py  # Script to regenerate docs/index.html
.github/
  workflows/
    generate-index.yml  # CI workflow triggered on changes to docs/papers/
```

## Regenerating the Index Locally

```bash
python3 scripts/generate_index.py
```

## GitHub Pages Setup

Go to **Settings → Pages** and set the source to **Deploy from a branch**, selecting `main` and the `/docs` folder.
