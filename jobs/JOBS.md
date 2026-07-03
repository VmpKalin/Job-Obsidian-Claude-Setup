# JOBS.md — Detailed workflow rules

This file is the step-by-step recipe the assistant follows when processing
jobs. `CLAUDE.md` points here. Everything the assistant writes stays inside
`jobs/`.

---

## Inputs and outputs at a glance

```
jobs/
├── inbox/      ← you drop raw job postings here (one file per job)
├── cv/         ← the applicant's CV (cv.md)
├── ready/      → finished packets, language is NOT a blocker
├── blocked/    → finished packets, a required language is missing
├── processed/  → the original posting text, archived as .txt
├── tracker.md  → one table row per posting
└── tools/
    └── build_letter.py   ← builds cover-letter.docx (standard library only)
```

---

## Processing one posting (what `/job-process` does)

For **each** file in `jobs/inbox/`:

### 1. Read the posting
Pull out: company name, role title, the posting URL (usually the first line),
key requirements, and any **required spoken language**.

### 2. Read the CV
Open `jobs/cv/cv.md` to know the applicant's skills and spoken languages.

### 3. Decide: ready or blocked
- No language required, or the applicant already has it → this packet is
  **ready**.
- A required language the applicant does **not** have → this packet is
  **blocked** (note which language).

### 4. Choose a packet folder name
Use this pattern (lowercase, dashes, today's date):

```
YYYY-MM-DD-company-role
```

Example: `2026-07-03-acme-cloud-backend-engineer`

The packet folder goes in `jobs/ready/` or `jobs/blocked/` depending on step 3.

### 5. Build the packet
Inside the packet folder create:

- **`application.md`** — a short summary: company, role, URL, match notes,
  language decision, and next steps.
- **`cover-letter.md`** — the cover-letter body in plain text/markdown,
  tailored to the posting using the CV.
- **`cover-letter.docx`** — generated from the body by running:

  ```
  python3 jobs/tools/build_letter.py \
      --body "jobs/ready/<folder>/cover-letter.md" \
      --out  "jobs/ready/<folder>/cover-letter.docx"
  ```

  The builder wraps the body in a simple letterhead (applicant name + contact
  line) and uses only Python's standard library — nothing to install.

### 6. Make a PDF (optional, cross-platform)
Convert the `.docx` to PDF using **LibreOffice in headless mode**. The exact
path to LibreOffice depends on the operating system:

| OS      | Command / path                                                        |
|---------|-----------------------------------------------------------------------|
| Windows | `"C:\Program Files\LibreOffice\program\soffice.exe" --headless ...`   |
| macOS   | `/Applications/LibreOffice.app/Contents/MacOS/soffice --headless ...` |
| Linux   | `libreoffice --headless ...` (or `soffice`)                           |

Full conversion command (same flags on every OS):

```
<soffice> --headless --convert-to pdf --outdir "<packet folder>" \
          "<packet folder>/cover-letter.docx"
```

**If LibreOffice is not installed, skip the PDF and keep the `.docx`.** The
packet is still complete without the PDF.

### 7. Log it
Add one row to `jobs/tracker.md`:

`| date | company | role | url | language ok? | status | folder |`

- `language ok?` = ✅ if not a blocker, ❌ (+ missing language) if blocked.
- `status` = `ready` or `blocked`.

### 8. Archive the original
Move the raw posting out of `jobs/inbox/` into `jobs/processed/` as a `.txt`
file, named the same as the packet folder. The inbox ends up empty.

---

## Naming rules quick reference
- Folders & files: lowercase, words separated by `-`.
- Dates: `YYYY-MM-DD`.
- One packet folder per posting; one tracker row per posting; one archived
  `.txt` per posting.
