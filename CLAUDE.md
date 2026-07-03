# CLAUDE.md — The Rules File (the "operating system")

## Read this first, in plain words

**This file is the instructions the AI follows. It is not code — it is a
description of what to do, written in ordinary English.**

When you open this project in Claude Code, the AI reads this file before it
does anything. Think of it as the "operating system" for a little assistant:
it does not contain programming, it contains *rules*. You can read every line
and understand exactly how the assistant will behave. If you want to change how
it works, you change the words here — not any code.

(If you use OpenAI Codex instead of Claude Code, the same idea applies but the
file is named `AGENTS.md`. The content is the same.)

---

## Who the assistant is helping

The assistant helps **one applicant** apply for jobs. All details live in
`jobs/cv/cv.md`. In this public sample the applicant is a placeholder:

- **Name:** Alex Sample
- **Email:** alex.sample@example.com
- **Phone:** +00 000 000 000
- **Location:** Sample City
- **Profile:** Backend developer — Python and JavaScript, 3 years experience
- **Languages spoken:** English (native)

> Replace the CV with your own real details when you use this for yourself.

---

## The rules

### 1. Write boundary (very important)
The assistant may **only create or change files inside the `jobs/` folder.**
It must never edit anything outside `jobs/` — not this file, not the commands,
not the README. If a task seems to need writing outside `jobs/`, the assistant
stops and asks the human first.

### 2. The language rule
Some job postings require a spoken language (for example German). The applicant
speaks the languages listed in the CV. For each posting:

- If the posting requires **no language**, or a language the applicant
  **already has**, the finished packet goes into `jobs/ready/`.
- If the posting requires a language the applicant **does not have**, the
  finished packet is still built, but goes into `jobs/blocked/` and the tracker
  notes which language is missing. Nothing is thrown away — "blocked" just
  means "a language is in the way."

### 3. Everything is logged
Every posting the assistant processes gets one row in `jobs/tracker.md`, and
the original posting text is archived as a `.txt` file in `jobs/processed/`.

### 4. The detailed workflow lives in one place
The step-by-step process (how to read a posting, how to build a cover letter,
how to name folders) is written in **`jobs/JOBS.md`**. When processing jobs,
the assistant follows `jobs/JOBS.md` exactly.

---

## The commands

Three slash commands drive the workflow (defined in `.claude/commands/`):

- `/job-intake` — help drop a new posting into `jobs/inbox/`.
- `/job-process` — process everything in `jobs/inbox/` following `jobs/JOBS.md`.
- `/job-stats` — summarise the tracker (how many ready, blocked, etc.).
