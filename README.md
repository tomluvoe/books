# Reading Library

Leisure reading log (originally **Books** Google Calendar, 2005–2026), plus retrospective backfills. **169 unique books, 171 reads, 59 imported reviews**. Plain Markdown + YAML frontmatter is the source of truth; `library.yaml` is a generated compact index (regenerate or edit either — just pick one master).

## Structure
- `Context.md` — **reader profile**: degrees, what formal education already covers, series completion, pre-library caveats. Agents should read this before “gap” recommendations.
- `Books/` — one note per book. Frontmatter schema: `title, author[], dates_read[], language, domains[], rating, status, tags, source` (+ optional `date_precision: approximate`, `subtitle`, and after enrichment `year_published, isbn, pages`). Re-reads = multiple `dates_read`.
- `MOCs/` — one Map of Content per domain (17 domains). Study plans and reading paths live here.
- `Dashboard.md` — stats + Dataview queries (requires the Dataview community plugin).
- `library.yaml` — flat index for agents/scripts that don't want to walk the vault.
- `scripts/enrich_openlibrary.py` — adds ISBN, publish year, page count, subjects from Open Library.

## Status values
- `read` — finished (`dates_read` set; counts toward read totals)
- `reading` — started, not finished (no `dates_read` until done; listed on Dashboard / Context)
- `paused` — abandoned or on hold (optional; same non-counting rule as `reading`)

## AI workflows
Drop this folder into a Claude Project (or point your agent framework at this vault). Useful skills to build, FinAgent-style:
1. **Librarian** — answer "what did I think of X", find books by theme, dedupe against the vault before recommending; always consult `Context.md`.
2. **Recommender** — reads `Context.md` + `library.yaml` + reviews, proposes next reads per MOC, appends to the MOC's "Reading paths" section. Avoid intro material in degree fields.
3. **Curriculum builder** — given a target domain (e.g. monetary history), builds a sequenced study plan as a new MOC note, linking owned books and gap-filling with new ones — on top of degree foundations, not instead of them.
4. **Logger** — on "finished X today", creates the note, updates `library.yaml`, prompts for a rating and review.
