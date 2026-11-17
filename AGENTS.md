# Notes for agents working in this repo

## Start here (every BuddhistAI repo)

- Read the maintainer handbook first: https://buddhistai.github.io/knowledge-base/handbook/ (source: BuddhistAI/knowledge-base `handbook/`). Follow its rules and conventions.
- Check the Development board for cards assigned to you: https://github.com/orgs/BuddhistAI/projects/3. Status and next steps: `handbook/status.md`.
- Rules: plain English for non-native readers, no idioms. "Buddhist tasks", not only texts. "Top performance" and "Best value". Neutral credits: WeBuddhist is one contributor among others. Never invent data, scores, votes or links. Never edit generated files by hand.
- buddhist-benchmarks stays clean (short `result.json`, outputs, scores). Provenance records (`buddhistai/provenance@1`) live in the skill's own repo.
- When you change something the handbook describes, update the handbook in the same pull request.
- This repo: the homepage at https://buddhistai.github.io/: one self-contained `index.html` served by GitHub Pages from `main`. Scores on it are copied from the leaderboard; never type a score that is not there. No build step and no CI: open the page at 360px wide and in dark mode before pushing.
