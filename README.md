# Workout Journal

My running and cycling journal: each session's numbers, what went wrong, and what to fix next.

**Read it here:** https://workout.larjun.me/

## Structure

```
docs/index.md          current focus + session index (home page)
docs/focus/            living notes per sport: goals, recurring mistakes, what's improving
docs/sessions/YYYY/    one short entry per session (front matter holds the key numbers)
docs/weekly/           weekly reviews: did the goals work? adjust them
docs/tags.md           browse sessions by tag
mkdocs.yml             site config and navigation
docs/stylesheets/      theme colours (built around #00ffae)
```

The site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed to GitHub Pages automatically on every push to `main`.

## Preview locally

```bash
pip install mkdocs-material
mkdocs serve
```

Then open http://127.0.0.1:8000.

## Adding a session

1. Add `docs/sessions/YYYY/YYYY-MM-DD-run.md` (or `-ride.md`) using the template on the home page, with front matter.
2. Add it to the session index in `docs/index.md` and to `nav` in `mkdocs.yml`.
3. Update the relevant focus file if goals or patterns changed.

*Not medical advice.*
