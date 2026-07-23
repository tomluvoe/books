# 📚 Dashboard

**169 finished · 171 reads · 1 currently reading · ~2001–2026 · 59 with imported reviews**

See also [[Context]] for education background and recommendation rules (degree foundations vs leisure log).

## Currently reading

```dataview
TABLE join(author, ", ") AS Author, join(domains, ", ") AS Domains
FROM "Books"
WHERE status = "reading"
SORT file.name ASC
```

## Did not finish (DNF)

```dataview
TABLE join(author, ", ") AS Author, join(domains, ", ") AS Domains
FROM "Books"
WHERE status = "dnf" OR status = "paused"
SORT file.name ASC
```

## Books per year

- ~2001: █ 1 *(approx. — Relativity)*
- ~2002: █ 1 *(approx. — Nineteen Eighty-Four)*
- 2005: █ 1
- 2006: ███████████ 11
- 2007: ████████████████ 16
- 2008: ████████ 8
- 2009: ████████ 8
- 2010: ███████████████ 15
- 2011: ██████████ 10
- 2012: ██████████ 10
- 2013: █████████████ 13
- 2014: ██ 2
- 2015: ████ 4
- 2016: ███████ 7
- 2017: ██████ 6
- 2018: ██████████████ 14
- 2019: ████████ 8
- 2020: █████ 5
- 2021: █████████ 9
- 2022: ██████ 6
- 2023: ███████ 7
- 2024: ███ 3
- 2025: ████ 4
- 2026: ██ 2

## All books (Dataview)

```dataview
TABLE join(author, ", ") AS Author, dates_read AS Finished, rating AS "★", join(domains, ", ") AS Domains
FROM "Books"
SORT min(dates_read) DESC
```

## Unrated (fill these in)

```dataview
LIST FROM "Books" WHERE !rating SORT file.name ASC
```

## Approximate dates (retrospective)

```dataview
TABLE dates_read AS "Approx finished", author AS Author
FROM "Books"
WHERE date_precision = "approximate"
SORT min(dates_read) ASC
```
