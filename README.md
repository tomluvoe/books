# Reading Library

Migrated from the **Books** Google Calendar (2005–2026): **166 unique books, 168 reads, 59 imported reviews**. Plain Markdown + YAML frontmatter is the source of truth; `library.yaml` is a generated compact index (regenerate or edit either — just pick one master).

## Structure
- `Books/` — one note per book. Frontmatter schema: `title, author[], dates_read[], language, domains[], rating, status, tags, source` (+ `year_published, isbn, pages` after enrichment). Re-reads = multiple `dates_read`.
- `MOCs/` — one Map of Content per domain (17 domains). Study plans and reading paths live here.
- `Dashboard.md` — stats + Dataview queries (requires the Dataview community plugin).
- `library.yaml` — flat index for agents/scripts that don't want to walk the vault.
- `_scripts/enrich_openlibrary.py` — adds ISBN, publish year, page count, subjects from Open Library.

## AI workflows
Drop this folder into a Claude Project (or point your agent framework at it). Useful skills to build, FinAgent-style:
1. **Librarian** — answer "what did I think of X", find books by theme, dedupe against the vault before recommending.
2. **Recommender** — reads `library.yaml` + reviews, proposes next reads per MOC, appends to the MOC's "Reading paths" section.
3. **Curriculum builder** — given a target domain (e.g. monetary history), builds a sequenced study plan as a new MOC note, linking owned books and gap-filling with new ones.
4. **Logger** — on "finished X today", creates the note, updates `library.yaml`, prompts for a rating and review.
