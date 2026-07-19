#!/usr/bin/env python3
"""Enrich book notes with Open Library metadata (ISBN, first-publish year, pages, subjects).

Run from the vault root on a machine with internet access:
    pip install requests python-frontmatter
    python _scripts/enrich_openlibrary.py

Idempotent: skips notes that already have an isbn field.
"""
import glob, time, requests, frontmatter

for path in glob.glob("Books/*.md"):
    post = frontmatter.load(path)
    if post.get("isbn"):
        continue
    title = post.get("title", "")
    author = (post.get("author") or [""])[0]
    try:
        r = requests.get("https://openlibrary.org/search.json",
                         params={"title": title, "author": author, "limit": 1},
                         timeout=15).json()
        if not r.get("docs"):
            print(f"MISS  {title}")
            continue
        d = r["docs"][0]
        if d.get("first_publish_year"): post["year_published"] = d["first_publish_year"]
        if d.get("isbn"):               post["isbn"] = d["isbn"][0]
        if d.get("number_of_pages_median"): post["pages"] = d["number_of_pages_median"]
        if d.get("subject"):            post["ol_subjects"] = d["subject"][:8]
        frontmatter.dump(post, path)
        print(f"OK    {title} ({d.get('first_publish_year','?')})")
    except Exception as e:
        print(f"ERR   {title}: {e}")
    time.sleep(1)  # be polite to the API
