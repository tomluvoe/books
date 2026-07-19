# 📚 Dashboard

**165 unique books · 167 reads · 2005–2026 · 59 with imported reviews**

## Books per year

- 2005: █ 1
- 2006: ██████████ 10
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
- 2026: █ 1

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
