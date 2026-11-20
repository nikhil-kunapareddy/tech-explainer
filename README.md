# Tech Explainer

Computer science explained in simple words, in the spirit of *Thing Explainer*.

Live site: https://techexplainer.duckdns.org/

## Rules for every post

1. No more than 1,000 words.
2. At least one picture.

## How the site is organized

- The home page lists **topics** (like Web Development).
- Clicking a topic opens its list of **subtopics**.
- Each subtopic is one **post**.

## Files

- `index.html`: home page with topics and subtopics
- `topics/<topic>/<post>.html`: one page per post
- `images/`: pictures for the posts
- `template.html`: copy this to start a new post
- `style.css`: a few lines of styling, kept close to plain HTML, with light and dark colors
- `theme.js`: the light/dark button
- `check.py`: checks every post against the rules

## Add a post

1. Copy `template.html` to `topics/<topic>/<post>.html` and fill it in.
2. Put the picture in `images/`.
3. In `index.html`, add a link to the post inside its topic's `<details>` block.
4. Run `python3 check.py`.

## View the site locally

Run `python3 -m http.server 8000` in this folder, then open http://127.0.0.1:8000.

## Publishing

The site is hosted on GitHub Pages from the `main` branch. Every push to `main` updates the live site within a few minutes. `.nojekyll` tells GitHub to serve the files as they are, without running them through Jekyll.

The domain `techexplainer.duckdns.org` comes from DuckDNS and points to GitHub Pages at `185.199.108.153`. The `CNAME` file tells GitHub which site to serve for that name, so don't delete it.
