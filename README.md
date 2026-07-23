# Reading Library

Leisure reading log (originally **Books** Google Calendar, 2005–2026), plus retrospective backfills. **171 unique books, 173 reads, 59 imported reviews**. Plain Markdown + YAML frontmatter is the source of truth; `library.yaml` is a generated compact index (regenerate or edit either — just pick one master).

## Structure
- `Context.md` — **reader profile**: degrees, work/AI practice level, intellectual taste (challenge ≠ cheerleading), DNF, series completion. Agents must read this before recommending.
- `Gaps and Study Paths.md` — **full domain gap map** + ordered paths (A–G). Source of truth for “what’s missing” and curricula.
- `Books/` — one note per book. Frontmatter schema: `title, author[], dates_read[], language, domains[], rating, status, tags, source` (+ optional `date_precision: approximate`, `subtitle`, and after enrichment `year_published, isbn, pages`). Re-reads = multiple `dates_read`.
- `MOCs/` — one Map of Content per domain (17 domains). Short path pointers live here; detail in `Gaps and Study Paths.md`.
- `Dashboard.md` — stats + Dataview queries (requires the Dataview community plugin).
- `library.yaml` — flat index for agents/scripts that don't want to walk the vault.
- `scripts/enrich_openlibrary.py` — adds ISBN, publish year, page count, subjects from Open Library.

## Status values
- `read` — finished (`dates_read` set; counts toward read totals)
- `reading` — started, not finished (no `dates_read` until done; listed on Dashboard / Context)
- `paused` — abandoned or on hold (optional; same non-counting rule as `reading`)
- `dnf` — did not finish; not a gap to re-push (see `Context.md`)

## AI workflows
Drop this folder into a Claude Project (or point your agent framework at this vault). Useful skills to build, FinAgent-style:
1. **Librarian** — answer "what did I think of X", find books by theme, dedupe against the vault; always consult `Context.md` + `Gaps and Study Paths.md`.
2. **Recommender** — reads Context + Gaps paths + `library.yaml` + reviews; proposes next step on an active path. **Challenge the reader; never cheerlead.** No intro material in degree fields; no practical AI books; no audience-flattery AI/society books.
3. **Curriculum builder** — extend paths in `Gaps and Study Paths.md` or MOC pointers; build on degree + work foundations.
4. **Logger** — on "finished X today", creates the note, updates `library.yaml`, prompts for a rating and review; update path checkboxes if relevant.
