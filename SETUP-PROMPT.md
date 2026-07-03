# The prompt that generated this repo

> **This is the exact prompt used to generate this sample repository — paste it
> into Claude Code in an empty folder to recreate it.**

---

# Build a clean public sample of the "AI Job Application Assistant" (Obsidian + Claude Code)

I'm creating a PUBLIC sample repository to share this workflow with others. You are running in a NEW EMPTY folder — build everything from scratch here. Do NOT look for or copy any of my real files; this is a standalone demo.

Everything must be FAKE / placeholder. No real names, emails, phones, or real personal data anywhere. This will go on public Git.

## What to build

A minimal but complete working example of the job-application workflow, plus fake sample data so someone can clone it, run one command, and see it work.

### 1. Folder structure

```
./
├── CLAUDE.md            # the rules file (the "operating system")
├── README.md            # explains the idea + how to use, in simple language
├── .claude/commands/    # the slash commands
│   ├── job-intake.md
│   ├── job-process.md
│   └── job-stats.md
└── jobs/
    ├── inbox/           # where postings are dropped
    ├── cv/              # the applicant's CV lives here (fake sample CV)
    ├── ready/           # finished packets, language not a blocker
    ├── blocked/         # finished packets, a required language is missing
    ├── processed/       # raw postings archived here after processing (.txt)
    ├── tracker.md       # table log of every posting
    └── JOBS.md          # detailed workflow rules
```

### 2. CLAUDE.md — the rules file
Write it in clear, simple English so a non-technical reader learns from it. It should explain, at the top, in plain words: "This file is the instructions the AI follows. It is not code — it is a description of what to do." Then define: the write boundary (only write inside `jobs/`), the applicant profile placeholder, the language rule, and a pointer to `jobs/JOBS.md` for the detailed workflow.

### 3. Fake sample data (this is the important part — make it realistic but clearly fake)
- `jobs/cv/cv.md` — a FAKE applicant. Name: "Alex Sample". Email: "alex.sample@example.com". Phone: "+00 000 000 000". A believable but invented profile: e.g. "Backend developer, Python and JavaScript, 3 years experience." Location: "Sample City".
- `jobs/inbox/` — put TWO fake job postings as separate files, invented companies (e.g. "Acme Cloud" and "Globex Software"), realistic-looking descriptions, one with no language requirement, one that requires a language the applicant doesn't have (to demonstrate the `blocked/` sort). Put a fake URL at the top of each.

### 4. The letter template + builder
- A small Python script (standard library only, no installs) that builds a `cover-letter.docx` from a plain-text body inserted into a simple letterhead (fake name + fake contact line).
- Cross-platform PDF note: document that the docx is converted to PDF via LibreOffice headless, and that the command detects the OS (Windows / macOS / Linux path). If LibreOffice isn't installed, keep the docx and skip the PDF.

### 5. Run the demo once (so the repo shows real output)
After building everything, actually RUN `/job-process` on the two fake postings so the repo contains example output: two packet folders with markdown + cover-letter.docx (+ PDF if LibreOffice is available), the tracker filled with two fake rows, and the raw postings archived as .txt. This way anyone cloning the repo sees a working example, not empty folders.

### 6. README.md — for humans, simple language
Explain in plain words: the core idea (text instructions replace code; the AI is the "compiler" from human language to action), the four parts (rules file, input/output folders, commands, execution), how to install (Obsidian + Claude Code), how to run it, and that all data here is fake sample data to replace with your own. Mention the same works with OpenAI Codex (rules file is AGENTS.md there). Keep it friendly and non-technical.

### 7. Save THIS prompt as an example
Save the full text of this prompt (the message you are reading now) into the repo as `SETUP-PROMPT.md`, with a short note at the top saying "This is the exact prompt used to generate this sample repository — paste it into Claude Code in an empty folder to recreate it." So people can see how the whole thing was created from one description.

## Before building
Confirm the fake identity values you'll use (Alex Sample etc.), show me the folder plan, then build it all and run the demo. Keep everything fake and public-safe.
