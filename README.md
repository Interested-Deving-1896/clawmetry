# clawmetry

[![Built with Ona](https://ona.com/build-with-ona.svg)](https://app.ona.com/#https://github.com/Interested-Deving-1896/clawmetry) [![KDE Eco](https://img.shields.io/badge/KDE%20Eco-certified-brightgreen?logo=kde&logoColor=white&style=flat-square)](https://eco.kde.org/) [![Blue Angel](https://img.shields.io/badge/Blue%20Angel-DE--UZ%20215-0055a4?style=flat-square)](https://www.blauer-engel.de/en/certification/criteria)


<!-- AI:start:what-it-does -->
_Description pending._
<!-- AI:end:what-it-does -->

## Architecture

<!-- AI:start:architecture -->
_Architecture documentation pending._
<!-- AI:end:architecture -->

## Install


```bash
pip install clawmetry     # then: clawmetry
```

Or the one-liner: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

Needs Python 3.8+ on macOS, Linux or Windows, and at least one agent runtime on
the same machine. Docker instructions: [docs/DOCKER.md](docs/DOCKER.md).

Or let the agent set it up for you. The [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
skill teaches Claude Code, Codex, Cursor, Gemini CLI, Copilot or OpenCode to
install ClawMetry, report what the agents on the machine are doing and spending,
stop one session on request, and hold risky tool calls for approval:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Usage

<!-- Add usage examples here. This section is yours — the AI will not modify it. -->

## Configuration

<!-- Document configuration options here. This section is yours — the AI will not modify it. -->

## CI

<!-- AI:start:ci -->
_CI documentation pending._
<!-- AI:end:ci -->

## Mirror chain

<!-- AI:start:mirror-chain -->
This repo is maintained in [`Interested-Deving-1896/clawmetry`](https://github.com/Interested-Deving-1896/clawmetry) and mirrored through:

```
Interested-Deving-1896/clawmetry  ──►  OpenOS-Project-OSP/clawmetry  ──►  OpenOS-Project-Ecosystem-OOC/clawmetry
```

Changes flow downstream automatically via the hourly mirror chain in
[`fork-sync-all`](https://github.com/Interested-Deving-1896/fork-sync-all).
Direct commits to OSP or OOC are detected and opened as PRs back to `Interested-Deving-1896`.
<!-- AI:end:mirror-chain -->

## Contributors

<!-- AI:start:contributors -->
| Contributor | Commits |
|---|---|
| [@vivekchand](https://github.com/vivekchand) | 3795 |
| [@github-actions[bot]](https://github.com/apps/github-actions) | 578 |
| [@dependabot[bot]](https://github.com/apps/dependabot) | 101 |
| [@dumko2001](https://github.com/dumko2001) | 17 |
| [@JaiCodes77](https://github.com/JaiCodes77) | 10 |
| [@claude](https://github.com/claude) | 4 |
| [@mvanhorn](https://github.com/mvanhorn) | 3 |
| [@ummtushar](https://github.com/ummtushar) | 2 |
| [@mrbrazzi](https://github.com/mrbrazzi) | 2 |
| [@Interested-Deving-1896](https://github.com/Interested-Deving-1896) | 2 |
| [@Aaqibhafeezkhan](https://github.com/Aaqibhafeezkhan) | 1 |
| [@JF10R](https://github.com/JF10R) | 1 |
| [@RijulTP](https://github.com/RijulTP) | 1 |
| [@ruzeynalov](https://github.com/ruzeynalov) | 1 |
| [@XanderLuciano](https://github.com/XanderLuciano) | 1 |
| [@drathava847-beep](https://github.com/drathava847-beep) | 1 |
| [@gypsy5oul](https://github.com/gypsy5oul) | 1 |
| [@sudabg](https://github.com/sudabg) | 1 |
| [@vincent067](https://github.com/vincent067) | 1 |
<!-- AI:end:contributors -->

## Origins

<!-- AI:start:origins -->
_Original project — no upstream influences recorded._
<!-- AI:end:origins -->

## Resources

<!-- AI:start:resources -->
_No additional resource files found._
<!-- AI:end:resources -->

## Accessibility

<!-- AI:start:accessibility -->
This repo uses automated accessibility auditing via `check-accessibility.yml`.

Checks include: CODEOWNERS ownership coverage, README screen-reader compatibility,
WCAG 2.1 AA HTML compliance, audio overview (espeak-ng), and Braille output (liblouis).




Run the [Check Accessibility](https://github.com/Interested-Deving-1896/clawmetry/actions/workflows/check-accessibility.yml)
workflow to generate the first report and accessibility artifacts.
See the [W3C Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/)
for the underlying accessibility reference.
<!-- AI:end:accessibility -->

## License

<!-- AI:start:license -->
[MIT](https://github.com/Interested-Deving-1896/clawmetry/blob/main/LICENSE) © 2026 [Interested-Deving-1896](https://github.com/Interested-Deving-1896)
<!-- AI:end:license -->
