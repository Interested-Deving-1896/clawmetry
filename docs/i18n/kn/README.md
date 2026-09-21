<!-- i18n-src:b22579578775 -->
> ಕನ್ನಡ translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**ಒಂದು ಏಜೆಂಟ್ ಯಾವುದೇ ಪ್ರಗತಿಯಿಲ್ಲದೆ ನೂರು ಟೂಲ್ ಕಾಲ್‌ಗಳನ್ನು ಮಾಡಬಹುದು.** ClawMetry
ನಿಮ್ಮ ಕೋಡಿಂಗ್ ಏಜೆಂಟ್‌ಗಳು ಈಗಾಗಲೇ ಬರೆಯುವ ಸೆಷನ್ ಫೈಲ್‌ಗಳನ್ನು ಓದುತ್ತದೆ, ಮತ್ತು ಟೈಮ್‌ಲೈನ್,
ಟೂಲ್ ಕಾಲ್‌ಗಳು ಮತ್ತು ರನ್‌ಟೈಮ್ ಬಹಿರಂಗಪಡಿಸುವ ಯಾವುದೇ ಟೋಕನ್ ಮತ್ತು ವೆಚ್ಚ ದತ್ತಾಂಶವನ್ನು ಒಂದೇ
ವೀಕ್ಷಣೆಯಲ್ಲಿ ಇಡುತ್ತದೆ — ಇದರಿಂದ ಕೆಲಸ ಮಾಡುತ್ತಿರುವ ದೀರ್ಘ ರನ್ ಮತ್ತು ಸಿಲುಕಿಕೊಂಡಿರುವ ರನ್
ಇವುಗಳ ನಡುವಿನ ವ್ಯತ್ಯಾಸವನ್ನು ನೀವು ಗುರುತಿಸಬಹುದು.

**32 AI ಏಜೆಂಟ್ ರನ್‌ಟೈಮ್‌ಗಳೊಂದಿಗೆ** ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ — Claude Code, OpenAI Codex, Hermes, OpenClaw ಮತ್ತು ಇನ್ನೂ 28. ನಿಮ್ಮ ಇಡೀ ಏಜೆಂಟ್ ಫ್ಲೀಟ್‌ಗೆ ಒಂದೇ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್. ([ಪೂರ್ಣ ಪಟ್ಟಿ](SUPPORTED_RUNTIMES.txt), ಕ್ಯಾಟಲಾಗ್‌ನಿಂದ ಜನರೇಟ್ ಮಾಡಲಾಗಿದೆ.)

> 🌐 **ಇದನ್ನು ಈ ಭಾಷೆಗಳಲ್ಲಿ ಓದಿ:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [ಇನ್ನಷ್ಟು →](docs/i18n/)

ಒಂದು ಕಮಾಂಡ್. ಶೂನ್ಯ ಕಾನ್ಫಿಗ್. ಎಲ್ಲವನ್ನೂ ಸ್ವಯಂ-ಪತ್ತೆ ಮಾಡುತ್ತದೆ.

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** ನಲ್ಲಿ ತೆರೆಯುತ್ತದೆ. ಶೂನ್ಯ ಕಾನ್ಫಿಗ್: ನಿಮ್ಮ ಬಳಿ ಈಗಾಗಲೇ ಇರುವ ಏಜೆಂಟ್
ರನ್‌ಟೈಮ್‌ಗಳನ್ನು ಇದು ಕಂಡುಹಿಡಿಯುತ್ತದೆ, ಅವುಗಳನ್ನು ಕೇವಲ-ಓದುವ ರೀತಿಯಲ್ಲಿ ಓದುತ್ತದೆ, ಮತ್ತು ಅವು ಹೇಗೆ
ಚಲಿಸುತ್ತವೆ ಎಂಬುದರ ಬಗ್ಗೆ ಏನನ್ನೂ ಬದಲಾಯಿಸುವುದಿಲ್ಲ.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುವ ಮೊದಲು

| | |
|---|---|
| **ಇದು ಏನು ಮಾಡುತ್ತದೆ** | ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗಳು ಈಗಾಗಲೇ ಬರೆಯುವ ಸೆಷನ್ ಫೈಲ್‌ಗಳು ಮತ್ತು ಲಾಗ್‌ಗಳನ್ನು ಓದುತ್ತದೆ. SDK ಇಲ್ಲ, ಕೋಡ್ ಬದಲಾವಣೆ ಇಲ್ಲ, ನಿಮ್ಮ ಆಪ್‌ನಲ್ಲಿ ಇನ್‌ಸ್ಟ್ರುಮೆಂಟೇಶನ್ ಇಲ್ಲ. |
| **ನೀವು ಏನನ್ನು ನೋಡುತ್ತೀರಿ** | ಸೆಷನ್ ಟೈಮ್‌ಲೈನ್, ಟೂಲ್-ಬೈ-ಟೂಲ್ ರಿಪ್ಲೇ, ಟೋಕನ್ ಮತ್ತು ವೆಚ್ಚ ವಿಭಜನೆ, ಮತ್ತು ಟ್ರಾಜೆಕ್ಟರಿ ಸಿಗ್ನಲ್‌ಗಳು (ಲೂಪಿಂಗ್, ಪುನರಾವರ್ತಿತ ವೈಫಲ್ಯಗಳು) — ಪ್ರತಿ ರನ್‌ಟೈಮ್‌ಗೆ. |
| **ಏನು ಉಚಿತ** | `pip install clawmetry` **OpenClaw, NVIDIA NemoClaw, Goose ಮತ್ತು Qwen Code** ಅನ್ನು ಯಾವುದೇ ಖಾತೆ, ಕೀ ಅಥವಾ ನೆಟ್‌ವರ್ಕ್ ಕಾಲ್ ಇಲ್ಲದೆ ಓದುತ್ತದೆ. ಉಳಿದ 28 — Claude Code, Codex, Cursor ಮತ್ತು ಇತರವು — ಅನ್ನು ಕ್ಲೋಸ್ಡ್-ಸೋರ್ಸ್ `clawmetry-pro` ಕಂಪ್ಯಾನಿಯನ್ ಓದುತ್ತದೆ, ಇದು 7-ದಿನದ ಟ್ರಯಲ್ ಅಥವಾ ಪ್ಲಾನ್‌ನೊಂದಿಗೆ ಬರುತ್ತದೆ — ನಿಖರವಾದ ವಿಭಜನೆಗಾಗಿ [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) ನೋಡಿ. |
| **ಹೇಗೆ ಪ್ರಾರಂಭಿಸುವುದು** | `pip install clawmetry && clawmetry`, ನಂತರ localhost:8900 ಅನ್ನು ತೆರೆಯಿರಿ. ಈ ಯಂತ್ರದಲ್ಲಿ ಇನ್ನೂ ಯಾವುದೇ ಏಜೆಂಟ್‌ಗಳಿಲ್ಲವೇ? `clawmetry --sample` ಮೂರು ಲೇಬಲ್ ಮಾಡಿದ ಸಿಂಥೆಟಿಕ್ ಸೆಷನ್‌ಗಳಲ್ಲಿ ತೆರೆಯುತ್ತದೆ. |
| **ನಿಮ್ಮ ಯಂತ್ರದಿಂದ ಏನು ಹೊರಹೋಗುತ್ತದೆ** | ನೀವು `clawmetry connect` ಅನ್ನು ರನ್ ಮಾಡದ ಹೊರತು ಯಾವುದೇ ಸೆಷನ್ ದತ್ತಾಂಶ ಇಲ್ಲ. ಡೀಫಾಲ್ಟ್ ಆಗಿ ಎರಡು ವಿಷಯಗಳು ಚಲಿಸುತ್ತವೆ, ಎರಡೂ ಆಪ್ಟ್-ಔಟ್ ಮಾಡಬಹುದಾದವು ಮತ್ತು ಯಾವುದೂ ಸೆಷನ್ ವಿಷಯವನ್ನು ಹೊಂದಿಲ್ಲ: ಅನಾಮಧೇಯ ಇನ್‌ಸ್ಟಾಲ್ ಪಿಂಗ್ ಮತ್ತು PyPI ಆವೃತ್ತಿ ಪರಿಶೀಲನೆ. ಪ್ರತಿ ಗಮ್ಯಸ್ಥಾನವನ್ನು [docs/EGRESS.md](docs/EGRESS.md) ನಲ್ಲಿ ಪಟ್ಟಿ ಮಾಡಲಾಗಿದೆ, ಕಾಮೆಂಟ್‌ಗಳನ್ನು ಓದುವ ಬದಲು ವೈರ್ ಕ್ಯಾಪ್ಚರ್‌ನಿಂದ ಮರುನಿರ್ಮಿಸಲಾಗಿದೆ. |

ನೀವು ಔಟ್‌ಪುಟ್‌ ಅನ್ನು ನಿರ್ಣಯಿಸುವ ಮೊದಲು ತಿಳಿದಿರಬೇಕಾದ ಎರಡು ಮಿತಿಗಳು: ರನ್‌ಟೈಮ್‌ಗಳು ಬಹಳ
ವಿಭಿನ್ನವಾದ ದತ್ತಾಂಶವನ್ನು ಬಹಿರಂಗಪಡಿಸುತ್ತವೆ (ಕೆಲವು ಯಾವುದೇ ವೆಚ್ಚವನ್ನು ಪ್ರಕಟಿಸುವುದಿಲ್ಲ —
[ಮ್ಯಾಟ್ರಿಕ್ಸ್](docs/compatibility.md) ಯಾವುದು ಎಂಬುದನ್ನು, ಪ್ರತಿ ರನ್‌ಟೈಮ್‌ಗೆ ಹೇಳುತ್ತದೆ), ಮತ್ತು ಒಂದು
ಕ್ರಿಯೆಯನ್ನು ಗಮನಿಸುವುದು ಅದನ್ನು ತಡೆಯಲು ಸಾಧ್ಯವಾಗುವುದಕ್ಕೆ ಸಮನಾಗಿಲ್ಲ ([ಯಾವ ನಿಯಂತ್ರಣಗಳು
ನಿಜವಾದವು, ಪ್ರತಿ ರನ್‌ಟೈಮ್‌ಗೆ](docs/APPROVALS.md)).


## 32 ಏಜೆಂಟ್ ರನ್‌ಟೈಮ್‌ಗಳೊಂದಿಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ

**ಓಪನ್ ಸೋರ್ಸ್ ಆಪ್‌ನಲ್ಲಿ ಉಚಿತ:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**ಪಾವತಿಸಿದ ಪ್ಲಾನ್‌ನಲ್ಲಿ:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

ಪ್ರತಿ ರನ್‌ಟೈಮ್‌ಗೆ ಅದೇ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ಸಿಗುತ್ತದೆ. ಒಂದೇ ಬಾರಿ ಹಲವಾರು ಚಲಾಯಿಸಿ ಮತ್ತು ಹೆಡರ್
ಸ್ವಿಚರ್ ಪ್ರತಿ ಟ್ಯಾಬ್ ಅನ್ನು ಅವುಗಳಲ್ಲಿ ಒಂದಕ್ಕೆ ಮರುಗುರಿಪಡಿಸುತ್ತದೆ.

SDK ಬಳಸಿ ನಿಮ್ಮ ಸ್ವಂತ ಏಜೆಂಟ್ ಅನ್ನು ನಿರ್ಮಿಸಿದ್ದೀರಾ? ಇಂಟರ್‌ಸೆಪ್ಟರ್ ಅದರ LLM ಕಾಲ್‌ಗಳನ್ನೂ
ಟ್ರ್ಯಾಕ್ ಮಾಡುತ್ತದೆ. [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md) ನೋಡಿ.

## ನಿಮಗೆ ಏನು ಸಿಗುತ್ತದೆ

- **ಸೆಷನ್‌ಗಳು ಮತ್ತು ಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಟ್‌ಗಳು**: ಪ್ರತಿ ಏಜೆಂಟ್ ಏನು ಮಾಡಿತು, ಟರ್ನ್-ಬೈ-ಟರ್ನ್, ರಿಪ್ಲೇ ಸಮೇತ
- **ವೆಚ್ಚ ಮತ್ತು ಟೋಕನ್‌ಗಳು**: ಪ್ರತಿ ರನ್‌ಟೈಮ್, ಮಾಡೆಲ್, ಸೆಷನ್ ಮತ್ತು ದಿನಕ್ಕೆ, ಅಸಂಗತತೆ ಫ್ಲ್ಯಾಗ್‌ಗಳೊಂದಿಗೆ
- **ಫ್ಲೋ**: ಚಾನೆಲ್‌ಗಳು, ಮಾಡೆಲ್‌ಗಳು ಮತ್ತು ಟೂಲ್‌ಗಳ ಮೂಲಕ ಚಲಿಸುವ ಸಂದೇಶಗಳ ಲೈವ್ ರೇಖಾಚಿತ್ರ
- **ಬ್ರೈನ್**: ಸಂಭವಿಸಿದಂತೆ ಚಿಂತನೆ ಮತ್ತು ಟೂಲ್-ಕಾಲ್ ಈವೆಂಟ್ ಸ್ಟ್ರೀಮ್
- **ಕಾಂಟೆಕ್ಸ್ಟ್ ಬ್ಲೋಔಟ್**: ಪ್ರತಿ ಪ್ರೊವೈಡರ್‌ಗೆ ಗಾತ್ರ ನಿಗದಿಪಡಿಸಿದ ವಿಂಡೋ ಬಳಕೆ, ಕಂಪ್ಯಾಕ್ಷನ್ ವಿರುದ್ಧ ಬಲವಂತದ ಓವರ್‌ಫ್ಲೋ, ಜೊತೆಗೆ ನಾವು *ನೋಡಲಾಗದ*ದ್ದರ ಪ್ರತಿ-ರನ್‌ಟೈಮ್ ನಕ್ಷೆ ([ಹೇಗೆ](docs/CONTEXT_BLOWOUT.md))
- **ಮೆಮೊರಿ ಮತ್ತು ಕೌಶಲ್ಯಗಳು**: ಪ್ರತಿ ರನ್‌ಟೈಮ್ ನಿಜವಾಗಿ ಲೋಡ್ ಮಾಡಿದ ಫೈಲ್‌ಗಳು ಮತ್ತು ಕೌಶಲ್ಯಗಳು
- **ಆರೋಗ್ಯ ಮತ್ತು ಲಾಗ್‌ಗಳು**: ಡಿಸ್ಕ್, ಮೆಮೊರಿ, ದೋಷ ದರಗಳು, ದರ ಮಿತಿಗಳು, ಲೈವ್ ಲಾಗ್ ಸ್ಟ್ರೀಮ್
- **ಎಚ್ಚರಿಕೆಗಳು**: ಬಜೆಟ್ ಮಿತಿಗಳು, ದೋಷ ಸ್ಪೈಕ್‌ಗಳು, ಏಜೆಂಟ್-ಆಫ್‌ಲೈನ್, Slack, Discord, PagerDuty, Telegram, Email ಗೆ ಮಾರ್ಗನಿರ್ದೇಶಿಸಲಾಗಿದೆ
- **ಅನುಮೋದನೆಗಳು**: ಅಪಾಯಕಾರಿ ಟೂಲ್ ಕಾಲ್‌ಗಳನ್ನು ಅವು ಚಲಾಯಿಸುವ *ಮೊದಲು* ವಿರಮಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಫೋನ್‌ನಿಂದ ಅನುಮೋದಿಸಿ ([ಹೇಗೆ](docs/APPROVALS.md))

## ಕಾಂಟೆಕ್ಸ್ಟ್ ಬ್ಲೋಔಟ್, ಮತ್ತು ಗಮನಿಸುವುದರ ವೆಚ್ಚ ಏನು

ಯಾವುದೇ ಏಜೆಂಟ್-ಹೋಲಿಕೆ ಟೂಲ್ ಅನ್ನು ನಂಬುವ ಮೊದಲು ಉತ್ತರಿಸಬೇಕಾದ ಎರಡು ಪ್ರಶ್ನೆಗಳು.

**ಇದು ರನ್‌ಟೈಮ್‌ಗಳಾದ್ಯಂತ ಕಾಂಟೆಕ್ಸ್ಟ್-ವಿಂಡೋ ಬ್ಲೋಔಟ್ ಅನ್ನು ಹೇಗೆ ನಿಭಾಯಿಸುತ್ತದೆ?**

ಬಳಕೆಯ ಶೇಕಡಾವಾರು ಪ್ರಮಾಣ ಅದು ಯಾವುದನ್ನು ಭಾಗಿಸುತ್ತದೆ ಎಂಬುದರಷ್ಟೇ ಪ್ರಾಮಾಣಿಕವಾಗಿರುತ್ತದೆ.
ClawMetry ಪ್ರತಿ ಪ್ರೊವೈಡರ್‌ಗೆ ವಿಂಡೋ ಗಾತ್ರವನ್ನು [ನೀವು ಓದಬಹುದಾದ ಮತ್ತು PR
ಮಾಡಬಹುದಾದ ಟೇಬಲ್](clawmetry/context_windows.py) ನಿಂದ ನಿಗದಿಪಡಿಸುತ್ತದೆ, ಇದು Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama ಮತ್ತು GLM ಅನ್ನು ಒಳಗೊಂಡಿದೆ. ಇದು ಒಬ್ಬ ವೆಂಡರ್‌ನ
ಅಳತೆಗೋಲಿನಿಂದ ಎಲ್ಲಾ 32 ರನ್‌ಟೈಮ್‌ಗಳನ್ನು ಅಳೆಯುವುದಿಲ್ಲ. ಇದು ಮುಖ್ಯವಾಗುತ್ತದೆ: 300K
GPT-5 ಟರ್ನ್ ಅನ್ನು Anthropic ನ 200K ವಿರುದ್ಧ ಸ್ಕೋರ್ ಮಾಡಿದಾಗ ">100%, blown" ಎಂದು
ಓದುತ್ತದೆ, ಆದರೆ ಅದು ವಾಸ್ತವವಾಗಿ GPT-5 ನ 400K ಯ 75% ರಷ್ಟಿದೆ. ಅದೇ ಅಳತೆಗೋಲು
ನಿಜವಾಗಿಯೂ ಓವರ್‌ಫ್ಲೋ ಆದ 130K DeepSeek ಟರ್ನ್ ಅನ್ನು ಆರಾಮದಾಯಕ 65% ಎಂದು ಮರೆಮಾಚುತ್ತದೆ.

ಪ್ರತಿ ವಿಂಡೋ ತನ್ನ ಮೂಲದೊಂದಿಗೆ ಬರುತ್ತದೆ: `model_table`, `explicit_marker`,
`observed_floor`, ಅಥವಾ ನಮಗೆ ಮಾಡೆಲ್ ತಿಳಿದಿಲ್ಲದಿದ್ದಾಗ ಪ್ರಾಮಾಣಿಕ `default`. ಊಹೆಯ ಮೇಲೆ
ನಿರ್ಮಿಸಲಾದ ಗೇಜ್ ಎಂದಿಗೂ ಲುಕಪ್‌ನಿಂದ ನಿರ್ಮಿಸಿದ ಒಂದೇ ಅಧಿಕಾರದೊಂದಿಗೆ ರೆಂಡರ್ ಆಗುವುದಿಲ್ಲ.

ClawMetry ಕೆಲವು ರನ್‌ಟೈಮ್‌ಗಳಲ್ಲಿ ಮಾತ್ರ ಕಂಪ್ಯಾಕ್ಷನ್ ಈವೆಂಟ್‌ಗಳನ್ನು ನೋಡಬಲ್ಲದು. ಆದ್ದರಿಂದ
`GET /api/context-coverage` ಪ್ರತಿ ರನ್‌ಟೈಮ್‌ಗೆ, ಶೂನ್ಯ ಎಂದರೆ **"ಶುದ್ಧವಾಗಿ ಓಡಿತು" ಅಥವಾ
"ನಾವು ಕುರುಡರಾಗಿದ್ದೇವೆ"** ಎಂಬುದನ್ನು ವರದಿ ಮಾಡುತ್ತದೆ. ನಿಜವಾಗಿ ಕುರುಡು ಎಂದರ್ಥವಿರುವ `0` ಹಾಗೆಯೇ ಹೇಳುತ್ತದೆ.
[ಪೂರ್ಣ ವಿವರ](docs/CONTEXT_BLOWOUT.md)

**ಇನ್‌ಸ್ಟ್ರುಮೆಂಟೇಶನ್ ಎಷ್ಟು ವೆಚ್ಚವಾಗುತ್ತದೆ?**

| ಮಾರ್ಗ | ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗೆ ಸೇರಿಸಲಾಗಿದೆ | ಡೀಫಾಲ್ಟ್? |
|---|---|---|
| ಸೆಷನ್-ಫೈಲ್ ಟೈಲಿಂಗ್ (ಎಲ್ಲಾ 32 ರನ್‌ಟೈಮ್‌ಗಳು) | **0**. ಪ್ರತ್ಯೇಕ ಪ್ರಕ್ರಿಯೆ, ನಿಮ್ಮ ಏಜೆಂಟ್‌ನಲ್ಲಿ ClawMetry ಕೋಡ್ ಇಲ್ಲ | ಆನ್ |
| HTTP ಇಂಟರ್‌ಸೆಪ್ಟರ್ (`CLAWMETRY_INTERCEPT=1`) | ಪ್ರತಿ LLM ಕಾಲ್‌ಗೆ **+0.44 ms**, ಅಥವಾ 5s ಕಾಲ್‌ನ 0.009% | ಆಫ್ |
| ಪ್ರಿ-ಟೂಲ್ ಹುಕ್ ಗೇಟ್ (ಬೆಚ್ಚಗಿನ ಕ್ಯಾಷೆ) | 36 ms ಇಂಟರ್ಪ್ರಿಟರ್ ಫ್ಲೋರ್‌ಗಿಂತ ಹೆಚ್ಚಾಗಿ, ಪ್ರತಿ ಗೇಟ್ ಮಾಡಿದ ಟೂಲ್ ಕಾಲ್‌ಗೆ **+44 ms** | ಆಫ್ |
| ಎನ್‌ಫೋರ್ಸ್‌ಮೆಂಟ್ ಪ್ರಾಕ್ಸಿ | ಪ್ರತಿ LLM ಕಾಲ್‌ಗೆ **+9.7 ms** | ಆಫ್ |

ಡೀಮನ್ ಹೋಸ್ಟ್ ವೆಚ್ಚ: **2,762 ಈವೆಂಟ್/ಸೆಕೆಂಡ್** ಇಂಜೆಸ್ಟ್, ಡಿಸ್ಕ್‌ನಲ್ಲಿ **710 ಬೈಟ್ಸ್/ಈವೆಂಟ್**
(100k ಈವೆಂಟ್‌ಗಳಿಗೆ 67.7 MB), ಮತ್ತು ಬಿಡುವಿಲ್ಲದ ಇನ್‌ಸ್ಟಾಲ್‌ನಲ್ಲಿ ಸ್ಥಿರವಾಗಿ **ಒಂದು ಕೋರ್‌ನ
~12%**. ಆ ಕೊನೆಯ ಸಂಖ್ಯೆ ನಮ್ಮ ಸ್ವಂತ ಹೇಳಿಕೆಯಾದ 5-10% ಬಜೆಟ್‌ಗಿಂತ ಹೆಚ್ಚಾಗಿದೆ, ಆದ್ದರಿಂದ
ಇದನ್ನು ಪುಟದಿಂದ ಬಿಟ್ಟುಬಿಡುವ ಬದಲು ಬೆನ್ನಟ್ಟಬೇಕಾದ ದೋಷವಾಗಿ ಪ್ರಕಟಿಸಲಾಗಿದೆ.

Apple M2 Pro ನಲ್ಲಿ `benchmarks/overhead.py` ನೊಂದಿಗೆ ಅಳೆಯಲಾಗಿದೆ. ಹಾರ್ನೆಸ್ ಪ್ರತಿ
ಸ್ಥಿತಿಯನ್ನು ಪ್ರತ್ಯೇಕ ಪ್ರಕ್ರಿಯೆಯಲ್ಲಿ ಚಲಾಯಿಸುತ್ತದೆ, ಅವುಗಳ ಕ್ರಮವನ್ನು ಪರ್ಯಾಯಗೊಳಿಸುತ್ತದೆ, ಮತ್ತು
**ಸುತ್ತುಗಳು ಅದರ ಚಿಹ್ನೆಯ ಬಗ್ಗೆ ಒಪ್ಪದಿದ್ದಾಗ ಸಂಖ್ಯೆಯನ್ನು ಮುದ್ರಿಸಲು ನಿರಾಕರಿಸುತ್ತದೆ**. ಇದನ್ನು ನಿಮ್ಮ
ಸ್ವಂತ ಯಂತ್ರದಲ್ಲಿ ಒಂದು ನಿಮಿಷದಲ್ಲಿ ರನ್ ಮಾಡಿ:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

ಹುಕ್ ಗೇಟ್‌ಗಳು ಮತ್ತು ಎನ್‌ಫೋರ್ಸ್‌ಮೆಂಟ್ ಪ್ರಾಕ್ಸಿ ಸೇರಿದಂತೆ ಪ್ರತಿ ಮಾರ್ಗವನ್ನೂ ಅಳೆಯಲಾಗಿದೆ,
ಮತ್ತು ಹಾರ್ನೆಸ್ CI ಯಲ್ಲಿ Linux, macOS ಮತ್ತು Windows ನಲ್ಲಿ ಚಲಿಸುತ್ತದೆ. ತಿಳಿದಿರಬೇಕಾದ
ಎರಡು ಫಲಿತಾಂಶಗಳು: Windows ನಲ್ಲಿ ಪ್ರಾಕ್ಸಿ Linux ಗಿಂತ ಸುಮಾರು ಏಳು ಪಟ್ಟು ಹೆಚ್ಚು ವೆಚ್ಚವಾಗುತ್ತದೆ,
ಮತ್ತು ಡೀಮನ್ ಪ್ರಸ್ತುತ ಒಂದು ಕೋರ್‌ನ ಸುಮಾರು 12% ಅನ್ನು ಉಳಿಸಿಕೊಳ್ಳುತ್ತದೆ, ನಮ್ಮ ಸ್ವಂತ 5-10%
ಬಜೆಟ್‌ಗಿಂತ ಹೆಚ್ಚಾಗಿ. ಕಚ್ಚಾ JSON, ವಿಧಾನ, ಮತ್ತು ಇನ್ನೂ ಅಳೆಯದಿರುವುದು
[docs/OVERHEAD.md](docs/OVERHEAD.md) ನಲ್ಲಿದೆ.

## ಬೆಲೆ ನಿಗದಿ

| ಪ್ಲಾನ್ | ಇದು ಏನನ್ನು ಒಳಗೊಳ್ಳುತ್ತದೆ | ಬೆಲೆ |
|---|---|---|
| **ಉಚಿತ** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, ಪೂರ್ಣ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್, ಸ್ಥಳೀಯ ಮಾತ್ರ | $0 |
| **ಸ್ಟಾರ್ಟರ್** | ಮೇಲಿನ ಪ್ರತಿಯೊಂದು ಇತರ ರನ್‌ಟೈಮ್, ಫ್ಲೀಟ್ ವೀಕ್ಷಣೆ, ಕ್ಲೌಡ್ ಸಿಂಕ್ | ಪ್ರತಿ ನೋಡ್‌ಗೆ / ತಿಂಗಳಿಗೆ $9 |
| **Pro** | ಸ್ಟಾರ್ಟರ್ + ನಿಯಂತ್ರಣ ಮತ್ತು ಮೌಲ್ಯಮಾಪನ: ಅನುಮೋದನೆಗಳು, ಟೂಲ್-ಅಪಾಯ ನೀತಿಗಳು, ಇವಾಲ್‌ಗಳು, ಅಸಂಗತತೆ ಪತ್ತೆ, ವೆಚ್ಚ ಆಪ್ಟಿಮೈಜರ್, OTel ಎಕ್ಸ್‌ಪೋರ್ಟ್, ಟ್ಯಾಂಪರ್-ಎವಿಡೆಂಟ್ ಆಡಿಟ್ ಲಾಗ್ | ಪ್ರತಿ ನೋಡ್‌ಗೆ / ತಿಂಗಳಿಗೆ $19 |

ವಾರ್ಷಿಕ ಪ್ಲಾನ್‌ಗಳು, Enterprise ಮತ್ತು ಪ್ರಸ್ತುತ ಸಂಖ್ಯೆಗಳು
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** ನಲ್ಲಿ ಲಭ್ಯವಿದೆ. ಸ್ವಯಂ-ಹೋಸ್ಟ್ ಮಾಡಿದ ಲೈಸೆನ್ಸ್
ಕೀಗಳು ಕ್ಲೌಡ್ ಇಲ್ಲದೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ (`clawmetry license`). ನಿಖರವಾದ ಉಚಿತ/ಪಾವತಿ ವಿಭಜನೆ
[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) ನಲ್ಲಿದೆ.

## ನಿಮ್ಮ ದತ್ತಾಂಶ ನಿಮ್ಮ ಯಂತ್ರದಲ್ಲೇ ಇರುತ್ತದೆ

ClawMetry ಸ್ಥಳೀಯ ಸೆಷನ್ ಫೈಲ್‌ಗಳು ಮತ್ತು ಲಾಗ್‌ಗಳನ್ನು ಓದುತ್ತದೆ. **ನೀವು `clawmetry connect`
ಅನ್ನು ರನ್ ಮಾಡದ ಹೊರತು ಯಾವುದೇ ಸೆಷನ್ ದತ್ತಾಂಶ ನಿಮ್ಮ ಬಾಕ್ಸ್‌ನಿಂದ ಹೊರಹೋಗುವುದಿಲ್ಲ** — ಯಾವುದೇ
ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಪ್ರತ್ಯುತ್ತರಗಳು, ಟೂಲ್ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು, ಫೈಲ್ ವಿಷಯಗಳು ಅಥವಾ ಲಾಗ್ ಲೈನ್‌ಗಳಿಲ್ಲ. ನೀವು
ಕನೆಕ್ಟ್ ಮಾಡಿದಾಗ, ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ ಅನ್ನು ಎಂದಿಗೂ ನಿಮ್ಮ ಯಂತ್ರವನ್ನು ಬಿಡದ ಕೀಯೊಂದಿಗೆ ಎಂಡ್-ಟು-ಎಂಡ್
ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಲಾಗುತ್ತದೆ, ಮತ್ತು ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಡಿಕ್ರಿಪ್ಟ್ ಮಾಡಲಾಗುತ್ತದೆ. ಒಂದು ನೋಡ್‌ಗೆ
ಕೀ ಇಲ್ಲದಿದ್ದರೆ, ಅಪ್‌ಲೋಡ್ ಅನ್ನು ಸ್ಪಷ್ಟ ಪಠ್ಯದಲ್ಲಿ ಕಳುಹಿಸುವ ಬದಲು ಬಿಟ್ಟುಬಿಡಲಾಗುತ್ತದೆ, ಮತ್ತು
ಯಾವುದೇ ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆ ಅದನ್ನು ಆಫ್ ಮಾಡಲು ಸಾಧ್ಯವಿಲ್ಲ.

ನೀವು ಕನೆಕ್ಟ್ ಮಾಡುವ ಮೊದಲು ಡೀಫಾಲ್ಟ್ ಆಗಿ ಎರಡು ವಿಷಯಗಳು ಚಲಿಸುತ್ತವೆ, ಎರಡೂ ಆಪ್ಟ್-ಔಟ್
ಮಾಡಬಹುದಾದವು ಮತ್ತು ಯಾವುದೂ ಸೆಷನ್ ದತ್ತಾಂಶವನ್ನು ಹೊಂದಿಲ್ಲ: ಅನಾಮಧೇಯ ಇನ್‌ಸ್ಟಾಲ್ ಪಿಂಗ್ ಮತ್ತು
PyPI ವಿರುದ್ಧ ಆವೃತ್ತಿ ಪರಿಶೀಲನೆ. ಡೀಫಾಲ್ಟ್ ಇನ್‌ಸ್ಟಾಲ್ ಸ್ಟಾರ್ಟಪ್ ಬ್ಯಾನರ್ ಲೈನ್‌ಗಾಗಿ ನಿಮ್ಮ
ಸಾರ್ವಜನಿಕ IP ಅನ್ನು ಒಮ್ಮೆ ಲುಕಪ್ ಮಾಡುತ್ತದೆ. ಪ್ರತಿ ಗಮ್ಯಸ್ಥಾನ, ಅದು ಏನನ್ನು ಹೊಂದಿದೆ ಮತ್ತು
ಅದನ್ನು ಹೇಗೆ ಸ್ವಿಚ್ ಆಫ್ ಮಾಡುವುದು ಎಂಬುದನ್ನು
[docs/EGRESS.md](docs/EGRESS.md) ನಲ್ಲಿ ಪಟ್ಟಿ ಮಾಡಲಾಗಿದೆ; ಸ್ವಯಂ-ಹೋಸ್ಟ್, ಮರುನಿರ್ದೇಶಿತ ಮತ್ತು
ಏರ್-ಗ್ಯಾಪ್ಡ್ ಇನ್‌ಸ್ಟಾಲ್‌ಗಳು ಯಾವುದೇ ಐಚ್ಛಿಕ ಔಟ್‌ಬೌಂಡ್ ಕಾಲ್‌ಗಳನ್ನು ಮಾಡುವುದಿಲ್ಲ.

ಡಿಕ್ರಿಪ್ಷನ್ ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ನಡೆಯುತ್ತದೆ, ನಾವು ನಿಮಗೆ ನೀಡುವ ಕೋಡ್‌ನಲ್ಲಿ. ಇದು ಹಿಂದೆ
ಒಂದು ಭರವಸೆಯಾಗಿತ್ತು; ಈಗ ಇದು ನೀವು ಪರಿಶೀಲಿಸಬಹುದಾದ ವಿಷಯ. ನಿಮ್ಮ ಕೀಯನ್ನು ಸ್ಪರ್ಶಿಸುವ ಪ್ರತಿ
ಲೈನ್ ಒಂದೇ ಓದಬಹುದಾದ ಫೈಲ್‌ನಲ್ಲಿ ವಾಸಿಸುತ್ತದೆ, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
ಇದು ವೀಲ್‌ನ ಒಳಗೆ ಶಿಪ್ ಆಗುತ್ತದೆ ಮತ್ತು ಯಥಾವತ್ತಾಗಿ ಸರ್ವ್ ಮಾಡಲಾಗುತ್ತದೆ, Subresource
Integrity ಹ್ಯಾಶ್‌ನೊಂದಿಗೆ ಪಿನ್ ಮಾಡಲಾಗಿದೆ. ಬ್ರೌಸರ್ ನಾವು ಪ್ರಕಟಿಸಿದ್ದನ್ನೇ ಚಲಾಯಿಸುತ್ತದೆ ಎಂದು
ದೃಢೀಕರಿಸಲು:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

ಇದು ಏನನ್ನು ಸಾಬೀತುಪಡಿಸುವುದಿಲ್ಲ: ಫೈಲ್ ಅನ್ನು ಲೋಡ್ ಮಾಡುವ ಪುಟವನ್ನು ನಾವು ಸರ್ವ್ ಮಾಡುತ್ತೇವೆ,
ಆದ್ದರಿಂದ ನಾವು ಬೇರೆ ಪುಟವನ್ನೇ ಸರ್ವ್ ಮಾಡಬಹುದು. Integrity ಹ್ಯಾಶ್‌ಗಳು ರಾಜಿಯಾದ CDN ನಿಂದ
ನಿಮ್ಮನ್ನು ರಕ್ಷಿಸುತ್ತವೆ, ವೆಂಡರ್‌ನಿಂದಲ್ಲ. ನೀವು ಪಡೆಯುವುದೇನೆಂದರೆ ಯಾವುದೇ ಬದಲಾವಣೆ
ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿರಬೇಕು, ಪುಟದ ಮೂಲದಲ್ಲಿ ಗೋಚರಿಸಬೇಕು, ಮತ್ತು ಯಾರಾದರೂ ಪಡೆಯಬಹುದಾದ PyPI
ಯಲ್ಲಿನ ಆರ್ಟಿಫ್ಯಾಕ್ಟ್‌ಗಿಂತ ಭಿನ್ನವಾಗಿರಬೇಕು. ಸ್ವಯಂ-ಹೋಸ್ಟಿಂಗ್ ಅಥವಾ ಸ್ಥಳೀಯ-ಮಾತ್ರ ಉಳಿಯುವುದು
ಈ ಅವಲಂಬನೆಯನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕುತ್ತದೆ.

## ಇನ್‌ಸ್ಟಾಲ್

```bash
pip install clawmetry     # ನಂತರ: clawmetry
```

ಅಥವಾ ಒಂದು-ಸಾಲಿನ: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS, Linux ಅಥವಾ Windows ನಲ್ಲಿ Python 3.8+ ಬೇಕು, ಮತ್ತು ಅದೇ ಯಂತ್ರದಲ್ಲಿ ಕನಿಷ್ಠ ಒಂದು
ಏಜೆಂಟ್ ರನ್‌ಟೈಮ್ ಬೇಕು. Docker ಸೂಚನೆಗಳು: [docs/DOCKER.md](docs/DOCKER.md).

ಅಥವಾ ಏಜೆಂಟ್ ಅನ್ನೇ ನಿಮಗಾಗಿ ಇದನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಲು ಬಿಡಿ. [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
ಕೌಶಲ್ಯ Claude Code, Codex, Cursor, Gemini CLI, Copilot ಅಥವಾ OpenCode ಗೆ ClawMetry ಅನ್ನು
ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು, ಯಂತ್ರದಲ್ಲಿನ ಏಜೆಂಟ್‌ಗಳು ಏನು ಮಾಡುತ್ತಿವೆ ಮತ್ತು ಖರ್ಚು ಮಾಡುತ್ತಿವೆ ಎಂಬುದನ್ನು
ವರದಿ ಮಾಡಲು, ವಿನಂತಿಯ ಮೇರೆಗೆ ಒಂದು ಸೆಷನ್ ಅನ್ನು ನಿಲ್ಲಿಸಲು, ಮತ್ತು ಅನುಮೋದನೆಗಾಗಿ ಅಪಾಯಕಾರಿ
ಟೂಲ್ ಕಾಲ್‌ಗಳನ್ನು ಹಿಡಿದಿಡಲು ಕಲಿಸುತ್ತದೆ:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## ದಾಖಲೆಗಳು

| | |
|---|---|
| [Runtime compatibility](docs/compatibility.md) | ಪ್ರತಿ ಅಡಾಪ್ಟರ್ ಏನನ್ನು ಓದುತ್ತದೆ, ಮತ್ತು ರನ್‌ಟೈಮ್ ಅನ್ನು ಹೇಗೆ ಸೇರಿಸುವುದು |
| [Context blowout](docs/CONTEXT_BLOWOUT.md) | ಪ್ರತಿ-ಪ್ರೊವೈಡರ್ ವಿಂಡೋಗಳು, ಕಂಪ್ಯಾಕ್ಷನ್ ವಿರುದ್ಧ ಓವರ್‌ಫ್ಲೋ, ಪ್ರತಿ-ರನ್‌ಟೈಮ್ ಕವರೇಜ್ |
| [Overhead](docs/OVERHEAD.md) | ಇನ್‌ಸ್ಟ್ರುಮೆಂಟೇಶನ್ ಎಷ್ಟು ವೆಚ್ಚವಾಗುತ್ತದೆ, ಅಳೆಯಲಾಗಿದೆ, ಅದನ್ನು ಮರುಉತ್ಪಾದಿಸಲು ಹಾರ್ನೆಸ್ ಸಮೇತ |
| [Entitlements](docs/ENTITLEMENTS.md) | ಉಚಿತ vs ಪಾವತಿ, ಟಯರ್ ಮ್ಯಾಟ್ರಿಕ್ಸ್, ಲೈಸೆನ್ಸ್ CLI |
| [Approvals & policies](docs/APPROVALS.md) | ಪೂರ್ವ-ಎಕ್ಸಿಕ್ಯೂಶನ್ ಗೇಟಿಂಗ್, ಅಪಾಯ ಸ್ಕೋರಿಂಗ್, ಫೋನ್ ಅನುಮೋದನೆಗಳು |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | ಎಲ್ಲಿಯಾದರೂ ಟ್ರೇಸ್‌ಗಳನ್ನು ಎಕ್ಸ್‌ಪೋರ್ಟ್ ಮಾಡಿ, ಎಲ್ಲಿಂದಲಾದರೂ OTLP ಇಂಜೆಸ್ಟ್ ಮಾಡಿ |
| [Bring your own agent](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain ಅಂತ್ಯದಿಂದ ಅಂತ್ಯ, ರನ್ ಮಾಡಬಹುದಾದ ಉದಾಹರಣೆಗಳೊಂದಿಗೆ |
| [SDK tracking](docs/SDK_TRACKING.md) | ನೀವೇ ನಿರ್ಮಿಸಿದ ಏಜೆಂಟ್‌ಗಳಿಗೆ ವೆಚ್ಚ ಅಟ್ರಿಬ್ಯೂಷನ್ |
| [Chat channels](docs/CHANNELS.md) | ಫ್ಲೋನಲ್ಲಿ ತೋರಿಸಲಾದ ಚಾಟ್ ಅಡಾಪ್ಟರ್‌ಗಳು |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | ಸ್ಯಾಂಡ್‌ಬಾಕ್ಸ್ಡ್ NVIDIA NemoClaw ಸೆಟಪ್‌ಗಳು |
| [Docker](docs/DOCKER.md) | ಇಮೇಜ್, ಕಂಪೋಸ್, ವಾಲ್ಯೂಮ್ ಮೌಂಟ್‌ಗಳು |
| [Architecture](ARCHITECTURE.md) · [Development](docs/DEVELOPMENT.md) | ಇದು ಒಳಗೆ ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ; ಮೂಲದಿಂದ ಚಲಾಯಿಸುವುದು |
| [Telemetry](docs/TELEMETRY.md) | ಅನಾಮಧೇಯ ಇನ್‌ಸ್ಟಾಲ್ ಮತ್ತು ಡೆಸ್ಕ್‌ಟಾಪ್-ಓಪನ್ ಪಿಂಗ್‌ಗಳು, ಮತ್ತು ಅವುಗಳನ್ನು ಹೇಗೆ ಆಫ್ ಮಾಡುವುದು |

## ಸ್ಕ್ರೀನ್‌ಶಾಟ್‌ಗಳು

ಕೆಳಗಿನ ಪ್ರತಿಯೊಂದು ಸಂಖ್ಯೆಯೂ ಒಂದೇ ನಿಜವಾದ ಯಂತ್ರದಿಂದ, ಕೇವಲ-ಓದುವ ರೀತಿಯಲ್ಲಿ, ಏನನ್ನೂ
ಬಿತ್ತದೆ ಬಂದಿದೆ.

**ಏನಾದರೂ ತಪ್ಪಾದಾಗ ಅದು ನಿಮಗೆ ಹೇಳುತ್ತದೆ, ಕೇವಲ ಏನಾಯಿತು ಎಂದಲ್ಲ.**
ಮೇಲ್ಭಾಗದಲ್ಲಿ ಎರಡು ಅಸಂಗತತೆ ಬ್ಯಾನರ್‌ಗಳು: ದೈನಂದಿನ ಸರಾಸರಿಯ 7 ಪಟ್ಟು ಖರ್ಚು ಚಲಿಸುತ್ತಿದೆ,
ಮತ್ತು 4.2 ಪಟ್ಟು ವೆಚ್ಚ ಸ್ಪೈಕ್. ಅವುಗಳ ಕೆಳಗೆ, ಇತ್ತೀಚಿನ 667 ಸೆಷನ್‌ಗಳಲ್ಲಿ 324 ಒಂದು ವ್ಯರ್ಥ
ಸಂಕೇತವನ್ನು ಹೊಂದಿವೆ, ಕಾರಣದಿಂದ ಪಟ್ಟಿ ಮಾಡಲಾಗಿದೆ.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**ಹಣ ಎಲ್ಲಿ ಹೋಯಿತು ಎಂಬುದನ್ನು, ಪ್ರತಿ ವಿಂಡೋದಲ್ಲಿ ಇದು ತೋರಿಸುತ್ತದೆ.**
ಇಂದು $252.47, ಈ ವಾರ $513.15, ಈ ತಿಂಗಳು $1,312.92, ಪ್ರತಿಯೊಂದೂ ಅದರ ಹಿಂದಿನ ಟೋಕನ್‌ಗಳು
ಮತ್ತು ನಿಮ್ಮ ಚಂದಾದಾರಿಕೆ ಈಗಾಗಲೇ ಎಷ್ಟು ಆವರಿಸುತ್ತದೆ ಎಂಬುದರೊಂದಿಗೆ. ಅದರ ಕೆಳಗೆ, ಸುಮಾರು
$1,128/ತಿಂಗಳು ಚೇತರಿಸಬಹುದಾದ ಎಂದು ಐಟಂ ಮಾಡಲಾಗಿದೆ ಮತ್ತು ಕ್ಯಾಷೆ ಮರುಬಳಕೆಯಿಂದ ಈಗಾಗಲೇ
$17,256/ತಿಂಗಳು ಉಳಿತಾಯವಾಗಿದೆ.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**ಒಂದು ಸಂದೇಶ ಹೇಗೆ ಉತ್ತರವಾಗುತ್ತದೆ ಎಂಬುದನ್ನು ಇದು ಚಿತ್ರಿಸುತ್ತದೆ.**
ಲೈವ್ ಫ್ಲೋ ರೇಖಾಚಿತ್ರ: ನೀವು, ಅದು ಬಂದ ಚಾನೆಲ್, ಗೇಟ್‌ವೇ, ಈಗ ಉತ್ತರಿಸುತ್ತಿರುವ ಮಾಡೆಲ್, ಮತ್ತು
ಅದು ತಲುಪಿದ ಪ್ರತಿ ಟೂಲ್. ಕೆಲಸ ಅವುಗಳ ಮೂಲಕ ಚಲಿಸುತ್ತಿದ್ದಂತೆ ನೋಡ್‌ಗಳು ಬೆಳಗುತ್ತವೆ.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**ಯಂತ್ರದ ಮೇಲಿನ ಪ್ರತಿ ಏಜೆಂಟ್, ಒಂದೇ ಟೇಬಲ್‌ನಲ್ಲಿ.**
ಅದು ಏನನ್ನು ಚಲಾಯಿಸುತ್ತದೆ, ಕಳೆದ 24 ಗಂಟೆಗಳಲ್ಲಿ ಮತ್ತು ಅದರ ಜೀವಿತಾವಧಿಯಲ್ಲಿ ಅದು ಎಷ್ಟು
ವೆಚ್ಚವಾಗುತ್ತದೆ, ಅದನ್ನು ಕೊನೆಯದಾಗಿ ಯಾವಾಗ ನೋಡಲಾಯಿತು, ಅದನ್ನು ಯಾರು ಹೊಂದಿದ್ದಾರೆ, ಮತ್ತು
ಚಂದಾದಾರಿಕೆ ಬಿಲ್ ಅನ್ನು ಆವರಿಸುತ್ತಿದೆಯೇ. ಇಲ್ಲಿ 14 ಏಜೆಂಟ್‌ಗಳು, 3 ಸೆಷನ್‌ಗಳು ಕೆಲಸ ಮಾಡುತ್ತಿವೆ,
13 ಶಾಂತವಾಗಿವೆ.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**ಒಂದು ಟರ್ನ್‌ನ ಸಮಯ ಮತ್ತು ಹಣ ಎಲ್ಲಿ ಹೋಯಿತು ಎಂಬುದನ್ನು, ಟೂಲ್-ಬೈ-ಟೂಲ್ ಇದು ತೋರಿಸುತ್ತದೆ.**
ನಿಜವಾದ ಸೆಷನ್‌ನ ಒಂದು ಟರ್ನ್: $1.16 ಗೆ 11.2 ನಿಮಿಷಗಳಲ್ಲಿ 11 ಟೂಲ್‌ಗಳು. ಪ್ರತಿ Bash
ಕಾಲ್ ಮತ್ತು ಮಾಡೆಲ್ ಕಾಲ್ ಟೈಮ್‌ಲೈನ್‌ನಲ್ಲಿ ತನ್ನದೇ ಬಾರ್ ಪಡೆಯುತ್ತದೆ, ಆದ್ದರಿಂದ 4.1 ನಿಮಿಷ ಚಲಿಸಿದ
ಕಮಾಂಡ್ ಮತ್ತು 226ms ಚಲಿಸಿದ ಕಮಾಂಡ್ ಅನ್ನು ಒಂದೇ ನೋಟದಲ್ಲಿ ಬೇರ್ಪಡಿಸಬಹುದು.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**ಇದು ಕೆಲಸವನ್ನು ಗ್ರೇಡ್ ಮಾಡುತ್ತದೆ, ಕೇವಲ ಖರ್ಚನ್ನಲ್ಲ.**
ಈ ವಾರ A: 54 ಟಾಸ್ಕ್‌ಗಳು ಶುದ್ಧವಾಗಿ ಹಿಂತಿರುಗಿದವು, 2 ಒರಟಾದವು $48.57 ವೆಚ್ಚವಾಯಿತು, ಮತ್ತು
ನಿರ್ಣಯಿಸಲು ಸಾಕಷ್ಟು ಚಟುವಟಿಕೆ ಇಲ್ಲದ ರನ್‌ಗಳನ್ನು ಗೆಲುವು ಎಂದು ಎಣಿಸುವ ಬದಲು ಗ್ರೇಡ್‌ನಿಂದ
ಬಿಟ್ಟುಬಿಡಲಾಗಿದೆ. ಪ್ರತಿ ಒರಟಾದ ರನ್ ಅದರ ಟ್ರೇಸ್‌ಗೆ ಲಿಂಕ್ ಮಾಡುತ್ತದೆ.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**ಕಾಂಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ ಏಕೆ ತುಂಬುತ್ತಲೇ ಇರುತ್ತದೆ ಎಂಬುದನ್ನು ಇದು ತೋರಿಸುತ್ತದೆ.**
ಇತ್ತೀಚಿನ ಟರ್ನ್‌ನಲ್ಲಿ 1M-ಟೋಕನ್ ವಿಂಡೋದ 715K, 83.3% ಪೀಕ್, ಓವರ್‌ಫ್ಲೋ ಬದಲು ಎಲ್ಲಾ 4
ಕಂಪ್ಯಾಕ್ಷನ್‌ಗಳು ಪೂರ್ವಭಾವಿಯಾಗಿ ಚಾಲಿತವಾಗಿವೆ, ಮತ್ತು ಅದರ ಹಿಂದಿನ ಪ್ರತಿ ಟರ್ನ್‌ನ ಬಳಕೆ.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**ನೀವು ಏನನ್ನೂ ಕಾನ್ಫಿಗರ್ ಮಾಡದೆ ಪತ್ತೆಹಚ್ಚುವಿಕೆ ಚಲಿಸುತ್ತದೆ.**
ಅಂತರ್ನಿರ್ಮಿತ ಪತ್ತೆಕಾರರು ಇನ್‌ಸ್ಟಾಲ್‌ನಿಂದಲೇ ಆನ್ ಆಗಿರುತ್ತಾರೆ: ಏಜೆಂಟ್ ಶಾಂತವಾಯಿತು, ಟೆಲಿಮೆಟ್ರಿ
ಫೀಡ್ ನಿಂತಿತು, ವೆಚ್ಚ ಸ್ಪೈಕ್, ಟೋಕನ್ ಬರ್ಸ್ಟ್, ದೋಷಗಳು ಏರುತ್ತಿವೆ, ದೋಷ ಸ್ಪೈಕ್, ಬಜೆಟ್
ಮಿತಿ, ಬೆದರಿಕೆ ಸಹಿ ಹೊಂದಿಕೆಯಾಯಿತು, ಭದ್ರತಾ ಟೂಲ್ ಶೋಧನೆ, ಭದ್ರತಾ ಸ್ಥಾನ ಬದಲಾಯಿತು. ನಿಮ್ಮ
ಸ್ವಂತ ನಿಯಮಗಳು ಮೇಲ್ಭಾಗದಲ್ಲಿ ಐಚ್ಛಿಕವಾಗಿವೆ.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**ಅಪಾಯಕಾರಿ ಕಾಲ್ ಅನ್ನು ಹಿಡಿದಿಡುವುದು ಆಪ್ಟ್-ಇನ್ ಆಗಿದೆ, ಮತ್ತು ಆಫ್ ಆಗಿ ಶಿಪ್ ಆಗುತ್ತದೆ.**
ರಿಕರ್ಸಿವ್ ಡಿಲೀಟ್‌ಗಳು, ಫೋರ್ಸ್ ಪುಶ್‌ಗಳು, sudo, ಸೀಕ್ರೆಟ್‌ಗಳು, ಪ್ಯಾಕೇಜ್ ಇನ್‌ಸ್ಟಾಲ್‌ಗಳು ಮತ್ತು
ಔಟ್‌ಬೌಂಡ್ ಕಾಲ್‌ಗಳು ಪ್ರತಿಯೊಂದೂ ನೀವು ಆನ್ ಮಾಡಬಹುದಾದ ನಿಯಮವನ್ನು ಪಡೆಯುತ್ತವೆ. ನೀವು ಆನ್
ಮಾಡುವವರೆಗೆ, ClawMetry ವೀಕ್ಷಿಸುತ್ತದೆ ಮತ್ತು ಏನನ್ನೂ ಬದಲಾಯಿಸುವುದಿಲ್ಲ. ಒಂದನ್ನು ಆನ್
ಮಾಡಿದ ನಂತರ, ಹೊಂದಿಕೆಯಾಗುವ ಕಾಲ್‌ಗಳು ಒಪ್ಪಿಗೆ ಅಥವಾ ನಿರಾಕರಣೆಗಾಗಿ ಇಲ್ಲಿ (ಅಥವಾ ನಿಮ್ಮ ಫೋನ್‌ನಲ್ಲಿ)
ಕಾಯುತ್ತವೆ.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

ಇನ್ನಷ್ಟು, ಪ್ರತಿ ರನ್‌ಟೈಮ್‌ಗೆ: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## ಮನ್ನಣೆ

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## ಸ್ಟಾರ್ ಇತಿಹಾಸ

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## ಲೈಸೆನ್ಸ್

MIT · [@vivekchand](https://github.com/vivekchand) ನಿರ್ಮಿಸಿದ್ದಾರೆ · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
