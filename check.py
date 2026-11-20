#!/usr/bin/env python3
"""Check that every post follows the Tech Explainer rules.

Posts live at topics/<topic>/<post>.html.

Rules:
  1. No more than 1,000 words inside <main>.
  2. At least one <img> inside <main>, and every image file exists.
  3. The post is linked from index.html.

Run:  python3 check.py
"""

import html
import re
import sys
from pathlib import Path

MAX_WORDS = 1000
ROOT = Path(__file__).resolve().parent
TOPICS = ROOT / "topics"


def check_page(page: Path, index_html: str) -> tuple[list[str], int, int]:
    problems = []
    source = page.read_text(encoding="utf-8")

    match = re.search(r"<main>(.*?)</main>", source, re.S)
    if not match:
        return ["no <main> section found"], 0, 0
    body = match.group(1)

    # Rule 1: word count of the visible text.
    text = re.sub(r"<!--.*?-->", " ", body, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    words = [w for w in html.unescape(text).split() if re.search(r"\w", w)]
    if len(words) > MAX_WORDS:
        problems.append(f"{len(words)} words (limit is {MAX_WORDS})")

    # Rule 2: at least one image, and every image file exists.
    sources = re.findall(r"<img\b[^>]*\bsrc=\"([^\"]+)\"", body)
    if not sources:
        problems.append("no image (needs at least one <img>)")
    for src in sources:
        if not (page.parent / src).resolve().exists():
            problems.append(f"image file missing: {src}")

    # Rule 3: linked from the home page.
    if f'href="{page.relative_to(ROOT).as_posix()}"' not in index_html:
        problems.append("not linked from index.html")

    return problems, len(words), len(sources)


def main() -> int:
    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    pages = sorted(TOPICS.glob("*/*.html"))
    if not pages:
        print("No posts found in topics/<topic>/")
        return 1

    failed = 0
    for page in pages:
        problems, words, images = check_page(page, index_html)
        status = "FAIL" if problems else "ok  "
        print(f"{status} {page.relative_to(TOPICS).as_posix():<44} {words:>4} words, {images} image(s)")
        for problem in problems:
            print(f"       - {problem}")
        failed += bool(problems)

    print()
    print(f"{len(pages) - failed} of {len(pages)} posts pass.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
