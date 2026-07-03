# AI Job Application Assistant — a working sample

A tiny, complete example of a job-application workflow you run with **Obsidian**
(to see and edit the files) and **Claude Code** (the AI that does the work). You
drop a job posting into a folder, run one command, and get a tailored cover
letter — sorted automatically by whether you meet the language requirement.

> **All data in this repo is fake sample data.** "Alex Sample", the companies,
> the emails and phone numbers — everything is invented and safe to make public.
> Replace it with your own details to actually use it.

---

## The core idea (in one minute)

Normally, software is **code**: precise instructions a computer runs. This
project works differently. The instructions are written in **plain English**, in
ordinary text files. The AI reads those files and does the work.

> **Text instructions replace code. The AI is the "compiler" that turns human
> language into action.**

That means you can open every file, read it like a note, and understand exactly
what will happen — no programming required. Want to change the behaviour? Change
the words.

---

## The four parts

1. **The rules file — `CLAUDE.md`**
   The "operating system." Plain-English rules the AI always follows: where it's
   allowed to write, who the applicant is, and the language rule. (Detailed
   workflow lives in `jobs/JOBS.md`.)

2. **Input & output folders — `jobs/`**
   - `inbox/` — you drop job postings here.
   - `cv/` — your CV lives here (`cv.md`).
   - `ready/` — finished packets where language is **not** a blocker.
   - `blocked/` — finished packets where a required language is **missing**.
   - `processed/` — the original postings, archived as `.txt`.
   - `tracker.md` — a table logging every posting.

3. **The commands — `.claude/commands/`**
   Short slash commands you type in Claude Code:
   - `/job-intake` — add a new posting to the inbox.
   - `/job-process` — process everything in the inbox.
   - `/job-stats` — summarise the tracker.

4. **Execution**
   Claude Code reads a posting, compares it to your CV, writes a tailored cover
   letter, builds a `.docx` (and a PDF if LibreOffice is installed), sorts the
   packet into `ready/` or `blocked/`, and logs it. A small Python helper
   (`jobs/tools/build_letter.py`, standard library only) builds the `.docx`.

---

## What's already in this sample

The demo has **already been run**, so you can see real output immediately:

- `jobs/ready/2026-07-03-acme-cloud-backend-engineer/` — a full packet
  (`application.md`, `cover-letter.md`, `cover-letter.docx`). Acme Cloud needs
  no extra language, so it's **ready**.
- `jobs/blocked/2026-07-03-globex-software-backend-developer/` — a full packet
  that landed in **blocked** because the posting requires German (C1), which the
  sample applicant doesn't have.
- `jobs/tracker.md` — two rows, one for each.
- `jobs/processed/` — the two original postings, archived as `.txt`.

*(PDFs were skipped in this run because LibreOffice wasn't installed — the
assistant kept the `.docx`, exactly as designed.)*

---

## How to install

1. **Obsidian** (free) — <https://obsidian.md>. Open this folder as a "vault" so
   you can read and edit the notes comfortably.
2. **Claude Code** — Anthropic's CLI. Install it and run it from inside this
   folder. See <https://docs.claude.com/claude-code>.

That's it — no other dependencies. The cover-letter builder uses only Python 3's
standard library. PDF export is optional and needs
[LibreOffice](https://www.libreoffice.org) if you want it.

---

## How to run it

1. Put your real details in `jobs/cv/cv.md`.
2. Drop a job posting into `jobs/inbox/` (URL on the first line), or use
   `/job-intake` to add one.
3. In Claude Code, run **`/job-process`**.
4. Look in `jobs/ready/` or `jobs/blocked/` for your packet, and check
   `jobs/tracker.md`.
5. Run **`/job-stats`** any time for a quick summary.

To replay the included demo, copy one of the files from `jobs/processed/` back
into `jobs/inbox/` (rename it to end in `.md`) and run `/job-process` again.

---

## Using OpenAI Codex instead

The same setup works with **OpenAI Codex**. The only difference is the name of
the rules file: Codex reads **`AGENTS.md`** instead of `CLAUDE.md`. Copy
`CLAUDE.md` to `AGENTS.md` and everything else works the same way.

---

## Make it your own

Replace the fake data:
- `jobs/cv/cv.md` — your real CV.
- The letterhead defaults in `jobs/tools/build_letter.py` (or pass `--name` and
  `--contact`).
- The applicant profile block in `CLAUDE.md`.

Then start dropping real postings into `jobs/inbox/`.

---

*See `SETUP-PROMPT.md` for the exact prompt used to generate this whole sample.*
