---
description: Process every posting in jobs/inbox/ following jobs/JOBS.md
---

Process all job postings currently in `jobs/inbox/`.

Follow the detailed workflow in **`jobs/JOBS.md`** exactly. For each posting:

1. Read the posting and the CV (`jobs/cv/cv.md`).
2. Decide **ready** vs **blocked** using the language rule in `CLAUDE.md`.
3. Create a packet folder named `YYYY-MM-DD-company-role` inside `jobs/ready/`
   or `jobs/blocked/`, containing `application.md`, `cover-letter.md`, and a
   `cover-letter.docx` built with `jobs/tools/build_letter.py`.
4. Try to make a PDF via LibreOffice headless (detect the OS path). If
   LibreOffice isn't installed, skip the PDF and keep the docx.
5. Add one row to `jobs/tracker.md`.
6. Archive the raw posting to `jobs/processed/<same-name>.txt` and remove it
   from `jobs/inbox/`.

When done, print a short summary: how many ready, how many blocked, and where
each packet landed.

Only write inside `jobs/`.
