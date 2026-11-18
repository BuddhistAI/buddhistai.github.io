---
title: "Share a skill or any file you give to AI"
date: 2026-11-18
author: NT (with Claude)
journeys: [share-know-how]
pages: [https://buddhistai.github.io/ (hero "For AI developers" box, "Art, practice and teaching" cards, Contribute section, the paste-a-link helper), https://github.com/BuddhistAI/buddhist-prompt-library (README, Share form), buddhist-skills README, CONTRIBUTING, SKILLS.md]
state: built
---

# Share a skill or any file you give to AI

## Problem

Translators, teachers and practitioners ([Translator](https://github.com/BuddhistAI/knowledge-base/blob/main/ux/personas/translator.md)) often do not have a skill. They have files they give to AI: a `CLAUDE.md`, project instructions, a style guide for their teacher's voice, a glossary, a prompt. Today the homepage and the Share form talk about "a skill". The form is in buddhist-skills. NT decided (2026-11-18, project chat) that buddhist-skills holds only the released skills: for each task, the **top performance** and **best value** skill (see [handbook status](https://buddhistai.github.io/knowledge-base/handbook/status.html)). Shared files sit in `buddhist-skills/community/`, and challengers sit in `buddhist-skills/drafts/`, next to the released skills. A visitor cannot tell measured from unmeasured. The first upload form was made for a translator who wanted to share a Claude file about his teacher's style.

NT asked: "How can people share other parts of their setup like their md files?" NT chose the name **prompt library** (2026-11-18, this thread) after a short look at how other fields share these files ("awesome-…" lists and "dotfiles" repos are developer words; "prompt library" is the term Anthropic, OpenAI and Notion use).

## Change

### A. Where things live

1. New repo **BuddhistAI/buddhist-prompt-library** holds everything shared and not measured. README title "Buddhist prompt library" (no emoji). First line: "Files that people give to AI for Buddhist work, shared so others can learn from them and use them." Second line: "Also skills and workflows that have no score yet." Then the list of kinds.
2. The one existing entry, `community/personal-ai-setup-english/shoukei-matsumoto-my-dharma/`, is copied unchanged (CARD.md with `authors`, SOURCE.md, `my-dharma.md`) to the same folder path at the root of the new repo. `task:` in CARD.md becomes `topic:`.
3. Challengers (`buddhist-skills/drafts/`) move to the task's **workshop repo** (one repo per skill, made from template-skill-repo), as `variants/<name>/`: the TOC GEPA draft to [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan) (already there as `variants/gepa-v1`), Drupchen-method drafts to the new [translation-tibetan-to-french](https://github.com/BuddhistAI/translation-tibetan-to-french). CONTRIBUTING "From challenger to promoted skill" says: "Put your challenger in the task's workshop repo as a variant, or in your own repo."
4. buddhist-skills keeps `skills/`, `shared/` and the router skill `ask-buddhistai`. `community/README.md`, `drafts/README.md` and a `README.md` in each moved entry folder (today one: `community/personal-ai-setup-english/shoukei-matsumoto-my-dharma/`) stay as one-line pointers: "This moved to <link to the same entry>."
5. Knowledge-base Papers do not change: research papers and guides for people to read stay Papers pages. Everything else shared goes to the prompt library.

### B. The Share form (moves to the prompt library)

- Title: **Share your files**. Description: "Share a skill or any file you give to AI: a Claude file, project instructions, a style guide, a glossary or a prompt. Paste a link or upload your files. No git or code needed. You need a free GitHub account."
- First text block, before the fields: "**Everything in this form is public at once**, before anyone reviews it. Do not upload private or restricted material." Then: "To change or remove your entry or your picture later, comment on your issue. A maintainer does it, usually within a few days." Then: "A maintainer adds your entry to the prompt library and credits you. GitHub sends you a message when it is added, with a link." Then: "Is it a skill for a task that has a benchmark? A maintainer also adds it to that task's repo so it can be scored, with your name."
- Field label "A short name for your file" (placeholder "Translation style of Khenpo X").
- Field "What is it?", options and the `kind` each becomes:

| Option | `kind` |
| --- | --- |
| A personal AI file (like CLAUDE.md or ChatGPT custom instructions) | personal |
| Project instructions (from a Claude Project or a custom GPT) | project-instructions |
| A style guide | style-guide |
| A glossary | glossary |
| A prompt | prompt |
| A skill (SKILL.md) | skill |
| A workflow (several steps) | workflow |
| Other | other |

- Other fields stay: language, what it does, link or files, notes, name, picture, license, permission.
- buddhist-skills keeps a stub `share.yml` named "Share your files (moved)": a text block "This form has moved. Open **[Share your files](https://github.com/BuddhistAI/buddhist-prompt-library/issues/new?template=share.yml)**." and one optional field "Anything else? (optional)" (GitHub needs one real field). Its `config.yml` also gets a "Share your files" link to the new form. Old links still land somewhere useful.
- The Language field help adds: "If it is not for one Buddhist language, give the language it is written in."
- Maintainer steps: close the issue with the pull request (`Closes #<issue>`) and post the link to the entry in the issue, so the author gets the message and the link. If a shared skill's task has a benchmark but no workshop repo yet, it stays in the prompt library and the maintainer notes it on the task's Skills board card.

### C. The prompt library README

- "Use an entry", browser first: "Open the file and click **Copy raw file** (two squares, top right). In Claude.ai: paste it into a Project's instructions. In ChatGPT: paste it into a GPT's instructions or at the start of a chat. If you use Claude Code on your computer, a `CLAUDE.md` goes in your project folder and a skill folder goes in `~/.claude/skills/`."
- "All entries" table shows plain labels for `kind` (Personal AI file, Project instructions, Style guide, Glossary, Prompt, Skill, Workflow, Other).
- Layout rule: folder `<topic>-<language>/<author>-<short-name>/`. `<topic>` is a task ID for skills and workflows when one fits; if none fits yet, a short name, and the maintainer renames the folder when a task ID exists. For other kinds it is a short name such as `personal-ai-setup`, `style-guide`, `glossary`. Translation folders are `translation-<source>-to-<target>`, and `language` and `target-language` in CARD.md match the folder name (check.py enforces this).
- Link or copy: for a link, the entry copies the files at one commit, and SOURCE.md records the repo and the commit. To update, the author opens a new Share issue or a pull request. The README and the form say this.
- Changing or removing an entry: the author comments on the issue (or opens one); a maintainer does it. `<language>` is the Buddhist language the file is for; if it is for no one language, the language it is written in.
- CARD.md fields: `title`, `kind`, `file` (needed for kinds other than skill, workflow, prompt), `topic`, `language`, `target-language` (translation only), `authors`, `github`, `avatar`, `contact`, `license`, `version`, `shared`.
- Repo files: README, CODE_OF_CONDUCT, LICENSE, CODEOWNERS, `templates/` (CARD, skill, workflow), `scripts/build.py` (writes the README list), `scripts/check.py` (checks folders and cards; language names fetched from buddhist-skills `languages.json`), CI `check` and `egm` workflows, label `community-share`.

### D. Homepage

1. Hero box "For AI developers", line under the link field: "No repo? **Share your files**: a skill, project instructions, a Claude file, a style guide or a prompt. Needs a free GitHub account ([make one](https://github.com/signup)). The form is public." Link to the new form.
2. Contribute section box: heading **No GitHub repo? Share a skill or any file you give to AI.** Text: "The prompt library holds files people give to AI: your CLAUDE.md, project instructions, a style guide, a glossary or a prompt. Drag your files into a short form. You need a free GitHub account, and the form is public. Your name and picture are optional." Button **Share your files**.
3. "Art, practice and teaching" cards (Visual AI, Personal setups): links **Open the prompt library** (to the repo) and **Share yours** (to the form), with a small line under them: "Sharing needs a free GitHub account ([make one](https://github.com/signup)). The form is public." Translators who skip the "For AI developers" box see these. The "Community" badge stays: it still means "shared, not measured".
4. Paste-a-link helper (the Contribute form that shows "Found" and four steps). For a **skill**, Submit now opens the prompt library Share form (query `template=share.yml&title=Share: <link>&link=<url>&name=<link>&notes=Task: <task>` (plus "please open a task request" for a new task); the form's name field has id `name`, not `title`). Today it opens a blank issue in buddhist-skills. Skill steps: 1 "You send the form: the Share form opens with your link filled in." 2 "Listed by a maintainer". 3 "Measured, for free: if its task has a benchmark, a maintainer adds it as a variant in the task's workshop repo and runs it at least 3 times. Or open a pull request with your variant there yourself." 4 "On the leaderboard: a row with your name, the model and the data version." The old step "A GitHub Action runs it" is removed (no such Action exists). TOC task line: "A maintainer runs it on TOC extraction, Tibetan 2.0.0 (85 passages), and the result goes on the leaderboard." This holds for every task choice, "A new task, not listed" included (the maintainer then also opens a task request; the task line says so). Models and benchmark data keep their current routes. Words: "it stays in the prompt library", note "A maintainer lists it in the prompt library, usually within a few days. Scored when its task has a benchmark.", step 2 "Listed by a maintainer: it shows in the prompt library, unmeasured, so others can try it.", task line "No benchmark yet. A maintainer lists your entry in the prompt library, and it is scored once a benchmark exists."
5. Contributors job (`scripts/update_contributors.py`): reads `[^/]+/[^/]+/CARD.md` in buddhist-prompt-library (`templates/` has no CARD.md at that depth), and the fallback link for people without a GitHub page goes to the prompt library. **Order:** create the `community-share` label in the prompt library; push the prompt library with the entry; then the script; then remove the moved files from `community/` and `drafts/` in buddhist-skills and keep the pointer READMEs. The [Skills board](https://github.com/orgs/BuddhistAI/projects/1) allows only one auto-add rule on the free plan (it watches buddhist-skills), so maintainers add prompt library Share issues to the board by hand until NT decides on a paid plan or a small Action. Handbook architecture (boards and forms tables) and how-to change to match.

### E. buddhist-skills

`build.py` writes one line in SKILLS.md: "Shared files and skills with no score yet are in the [prompt library](…). Challengers are in each task's workshop repo." `skills_lib.py`, `check.py`, `templates/` (CARD and workflow move), README, CONTRIBUTING, CODEOWNERS, `docs/design.md` decision 12, CHANGELOG and `ask-buddhistai` (points to the prompt library) change to match.

## Journeys and pages

share-know-how, before → after:

| # | Before | After |
| --- | --- | --- |
| 1 | Homepage: "No repo? Upload your files." | Homepage: hero line "No repo? Share your files…", Contribute box, or "Share yours" on the Art, practice and teaching cards |
| 2 | Share form in buddhist-skills ("Share a skill") | Share form in buddhist-prompt-library ("Share your files"), with setup kinds first, and clear notes on the GitHub account and that it is public |
| 3 | Maintainer adds a `community/` entry in buddhist-skills, or a Papers page | Maintainer adds a prompt library entry, or a Papers page for papers and guides to read. A skill for a task with a benchmark is also added as a variant in its workshop repo |
| 4 | Author finds it in buddhist-skills `community/` | GitHub tells the author; they find it in the prompt library list and their name in the contributors row |

New "Done when": "the entry is listed in the prompt library (or a Papers page in the knowledge base) and the author sees their name on it and in the contributors row (or the entry without a name, if they asked not to be shown)." Update `ux/journeys/share-know-how.md` in knowledge-base in the same change.

## Files

buddhist-prompt-library (all new, see C); buddhistai.github.io `index.html` and `scripts/update_contributors.py`; buddhist-skills (see E); toc-extraction-tibetan `variants/gepa-v1/VARIANT.md` (adds the scores from the draft); translation-tibetan-to-french (new); buddhist-benchmarks README line 69 and `tasks/translation/harness/run.py` usage line; knowledge-base journey, handbook (architecture, conventions, how-to, status, leaderboard-app), governance, glossary, `learn/write-your-first-skill.md`, experiment PLAN link (as a LOG note, since PLAN is frozen), design `VOICE.md`.

## Not in scope

- Sharing without a GitHub account (still open, see [Status](https://buddhistai.github.io/knowledge-base/handbook/status.html)).
- A search or filter page for the prompt library.
- Measuring shared files. Style guides and Claude files have no benchmark.

## Goldfish review

- 2026-11-18, round 1: Translator and Skill builder personas (journey standard), EGM `comprehension` and `design_critic`, as fresh subagents. Findings: 2 Blockers (drafts not explained; contributors script order) and 15 Major (GitHub account and public form not said; browser use of entries; translators skip the developer box; old form links; drafts route; scoring of uploaded skills; Done-when; migration; tooling; check.py inputs; Papers vs library; helper strings). All fixed in this version (sections A to E).
- 2026-11-18, round 2: same reviewers. 2 Major (the helper's Submit still went to buddhist-skills; a markdown-only stub form is not valid on GitHub) and 3 Minor (no workshop repo yet; how the author gets the link; Language help). All fixed in this version.
- Round 2 personas (Translator, Skill builder): 4 Major (GitHub note missing on hero and cards; how to change or remove an entry; translation folder rule; link vs copy; broken link to the moved entry) and 3 Minor (copy raw file; project instructions in hero line; Done-when without a name). All fixed in this version.
- 2026-11-18, round 3: all four reviewers. Translator and comprehension clean. 2 Major (the helper still promised an automatic scoring Action that does not exist; the Skills board auto-add would miss the new repo's Share issues) and 3 Minor (repeated words; form field id `title` clashes with the issue title; "repo" in the Contribute heading). All fixed.
- 2026-11-18, round 4: all four reviewers. Translator, comprehension and design critic clean. 1 Major (skill builder: a skill sent with "A new task" still went to the request form) and 2 Minor (keep pointer READMEs in the order; link the board). All fixed.
- 2026-11-18, round 5: all four reviewers. Translator, comprehension and design critic clean. 1 Major (skill builder: the task choice was lost on Submit) and 2 Minor ("workshop repo" unexplained in the helper; blank issues skip the label). All fixed after the round.
- Result: 5 rounds, the maximum. Rounds 4 and 5 each had one Major, both fixed, so the rule "two clean rounds in a row" was not met. No open Blocker or Major. Known limit accepted: Share issues from the prompt library are added to the Skills board by hand (free plan, one auto-add rule).
- Later (NT, 2026-11-18): the prompt library README became a catalog grouped by kind, listing hosted entries and entries kept in the author's own repo (card with `link:`), rebuilt by an Action on every push.
