<!-- i18n-src:b22579578775 -->
> ਪੰਜਾਬੀ translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**ਇੱਕ ਏਜੰਟ ਬਿਨਾਂ ਕਿਸੇ ਤਰੱਕੀ ਦੇ ਸੌ ਟੂਲ ਕਾਲਾਂ ਕਰ ਸਕਦਾ ਹੈ।** ClawMetry
ਤੁਹਾਡੇ ਕੋਡਿੰਗ ਏਜੰਟਾਂ ਵੱਲੋਂ ਪਹਿਲਾਂ ਤੋਂ ਲਿਖੀਆਂ ਸੈਸ਼ਨ ਫ਼ਾਈਲਾਂ ਪੜ੍ਹਦਾ ਹੈ, ਅਤੇ ਟਾਈਮਲਾਈਨ,
ਟੂਲ ਕਾਲਾਂ ਅਤੇ ਰਨਟਾਈਮ ਵੱਲੋਂ ਦਿਖਾਏ ਗਏ ਟੋਕਨ ਤੇ ਲਾਗਤ ਡੇਟਾ ਨੂੰ ਇੱਕ ਹੀ
ਵਿਊ ਵਿੱਚ ਲੈ ਆਉਂਦਾ ਹੈ — ਤਾਂ ਜੋ ਤੁਸੀਂ ਕੰਮ ਕਰ ਰਹੇ ਲੰਬੇ ਰਨ ਅਤੇ ਅਟਕੇ ਹੋਏ ਰਨ ਵਿੱਚ ਫ਼ਰਕ ਦੱਸ ਸਕੋ।

**32 AI ਏਜੰਟ ਰਨਟਾਈਮਾਂ** ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ — Claude Code, OpenAI Codex, Hermes, OpenClaw ਅਤੇ 28 ਹੋਰ। ਤੁਹਾਡੇ ਪੂਰੇ ਏਜੰਟ ਫਲੀਟ ਲਈ ਇੱਕ ਹੀ ਡੈਸ਼ਬੋਰਡ। ([ਪੂਰੀ ਸੂਚੀ](SUPPORTED_RUNTIMES.txt), ਕੈਟਾਲਾਗ ਤੋਂ ਤਿਆਰ ਕੀਤੀ ਗਈ।)

> 🌐 **ਇਸਨੂੰ ਇਹਨਾਂ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਪੜ੍ਹੋ:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [ਹੋਰ →](docs/i18n/)

ਇੱਕ ਕਮਾਂਡ। ਕੋਈ ਕੌਂਫ਼ਿਗ ਨਹੀਂ। ਸਭ ਕੁਝ ਆਪਣੇ ਆਪ ਲੱਭ ਲੈਂਦਾ ਹੈ।

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** 'ਤੇ ਖੁੱਲ੍ਹਦਾ ਹੈ। ਕੋਈ ਕੌਂਫ਼ਿਗ ਨਹੀਂ ਚਾਹੀਦੀ: ਇਹ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ
ਏਜੰਟ ਰਨਟਾਈਮਾਂ ਨੂੰ ਲੱਭ ਲੈਂਦਾ ਹੈ, ਉਹਨਾਂ ਨੂੰ ਸਿਰਫ਼-ਪੜ੍ਹਨ ਲਈ ਪੜ੍ਹਦਾ ਹੈ, ਅਤੇ ਉਹਨਾਂ ਦੇ ਚੱਲਣ ਦੇ ਤਰੀਕੇ ਵਿੱਚ ਕੁਝ ਨਹੀਂ ਬਦਲਦਾ।

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

| | |
|---|---|
| **ਇਹ ਕੀ ਕਰਦਾ ਹੈ** | ਤੁਹਾਡੇ ਏਜੰਟਾਂ ਵੱਲੋਂ ਪਹਿਲਾਂ ਤੋਂ ਲਿਖੀਆਂ ਸੈਸ਼ਨ ਫ਼ਾਈਲਾਂ ਅਤੇ ਲੌਗ ਪੜ੍ਹਦਾ ਹੈ। ਕੋਈ SDK ਨਹੀਂ, ਕੋਈ ਕੋਡ ਬਦਲਾਅ ਨਹੀਂ, ਤੁਹਾਡੀ ਐਪ ਵਿੱਚ ਕੋਈ ਇੰਸਟਰੂਮੈਂਟੇਸ਼ਨ ਨਹੀਂ। |
| **ਤੁਸੀਂ ਕੀ ਵੇਖਦੇ ਹੋ** | ਸੈਸ਼ਨ ਟਾਈਮਲਾਈਨ, ਟੂਲ-ਦਰ-ਟੂਲ ਰੀਪਲੇ, ਟੋਕਨ ਤੇ ਲਾਗਤ ਦਾ ਵੇਰਵਾ, ਅਤੇ ਟ੍ਰੈਜੈਕਟਰੀ ਸੰਕੇਤ (ਲੂਪਿੰਗ, ਵਾਰ-ਵਾਰ ਅਸਫਲਤਾਵਾਂ) — ਹਰ ਰਨਟਾਈਮ ਲਈ। |
| **ਕੀ ਮੁਫ਼ਤ ਹੈ** | `pip install clawmetry` **OpenClaw, NVIDIA NemoClaw, Goose ਅਤੇ Qwen Code** ਨੂੰ ਬਿਨਾਂ ਕਿਸੇ ਖਾਤੇ, ਕੁੰਜੀ ਜਾਂ ਨੈੱਟਵਰਕ ਕਾਲ ਦੇ ਪੜ੍ਹਦਾ ਹੈ। ਬਾਕੀ 28 — Claude Code, Codex, Cursor ਅਤੇ ਹੋਰ — ਕਲੋਜ਼ਡ-ਸੋਰਸ `clawmetry-pro` ਕੰਪੈਨੀਅਨ ਵੱਲੋਂ ਪੜ੍ਹੇ ਜਾਂਦੇ ਹਨ, ਜੋ 7-ਦਿਨ ਦੇ ਟ੍ਰਾਇਲ ਜਾਂ ਕਿਸੇ ਪਲਾਨ ਨਾਲ ਆਉਂਦਾ ਹੈ — ਸਹੀ ਵੰਡ ਲਈ [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) ਵੇਖੋ। |
| **ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰੀਏ** | `pip install clawmetry && clawmetry`, ਫਿਰ localhost:8900 ਖੋਲ੍ਹੋ। ਇਸ ਮਸ਼ੀਨ 'ਤੇ ਹਾਲੇ ਕੋਈ ਏਜੰਟ ਨਹੀਂ? `clawmetry --sample` ਤਿੰਨ ਲੇਬਲ ਵਾਲੇ ਨਕਲੀ ਸੈਸ਼ਨਾਂ ਨਾਲ ਖੁੱਲ੍ਹਦਾ ਹੈ। |
| **ਤੁਹਾਡੀ ਮਸ਼ੀਨ ਤੋਂ ਕੀ ਬਾਹਰ ਜਾਂਦਾ ਹੈ** | ਕੋਈ ਸੈਸ਼ਨ ਡੇਟਾ ਨਹੀਂ, ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ `clawmetry connect` ਨਹੀਂ ਚਲਾਉਂਦੇ। ਦੋ ਚੀਜ਼ਾਂ ਮੂਲ ਰੂਪ ਵਿੱਚ ਚੱਲਦੀਆਂ ਹਨ, ਦੋਵੇਂ ਅਪਟ-ਆਊਟ ਅਤੇ ਦੋਵਾਂ ਵਿੱਚ ਕੋਈ ਸੈਸ਼ਨ ਸਮੱਗਰੀ ਨਹੀਂ: ਇੱਕ ਅਗਿਆਤ ਇੰਸਟਾਲ ਪਿੰਗ ਅਤੇ ਇੱਕ PyPI ਵਰਜਨ ਚੈੱਕ। ਹਰ ਟਿਕਾਣਾ [docs/EGRESS.md](docs/EGRESS.md) ਵਿੱਚ ਸੂਚੀਬੱਧ ਹੈ, ਜੋ ਟਿੱਪਣੀਆਂ ਪੜ੍ਹਨ ਦੀ ਬਜਾਏ ਇੱਕ ਵਾਇਰ ਕੈਪਚਰ ਤੋਂ ਬਣਾਈ ਗਈ ਹੈ। |

ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਜਾਣਨ ਲਾਇਕ ਦੋ ਸੀਮਾਵਾਂ: ਰਨਟਾਈਮ ਬਹੁਤ
ਵੱਖੋ-ਵੱਖਰਾ ਡੇਟਾ ਦਿਖਾਉਂਦੇ ਹਨ (ਕੁਝ ਕੋਈ ਲਾਗਤ ਬਿਲਕੁਲ ਨਹੀਂ ਦੱਸਦੇ — [ਮੈਟ੍ਰਿਕਸ](docs/compatibility.md)
ਹਰ ਰਨਟਾਈਮ ਲਈ ਦੱਸਦਾ ਹੈ ਕਿ ਕਿਹੜਾ), ਅਤੇ ਕਿਸੇ ਕਾਰਵਾਈ ਨੂੰ ਵੇਖਣਾ ਉਸਨੂੰ
ਰੋਕ ਸਕਣ ਦੇ ਬਰਾਬਰ ਨਹੀਂ ਹੁੰਦਾ ([ਹਰ ਰਨਟਾਈਮ ਲਈ ਕਿਹੜੇ ਕੰਟਰੋਲ ਅਸਲੀ ਹਨ](docs/APPROVALS.md))।


## 32 ਏਜੰਟ ਰਨਟਾਈਮਾਂ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ

**ਓਪਨ ਸੋਰਸ ਐਪ ਵਿੱਚ ਮੁਫ਼ਤ:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**ਪੇਡ ਪਲਾਨ 'ਤੇ:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

ਹਰ ਰਨਟਾਈਮ ਨੂੰ ਇੱਕੋ ਡੈਸ਼ਬੋਰਡ ਮਿਲਦਾ ਹੈ। ਕਈਆਂ ਨੂੰ ਇੱਕੱਠੇ ਚਲਾਓ ਅਤੇ
ਹੈਡਰ ਸਵਿੱਚਰ ਹਰ ਟੈਬ ਨੂੰ ਉਹਨਾਂ ਵਿੱਚੋਂ ਇੱਕ 'ਤੇ ਮੁੜ-ਸਕੋਪ ਕਰ ਦਿੰਦਾ ਹੈ।

ਆਪਣਾ ਏਜੰਟ ਕਿਸੇ SDK 'ਤੇ ਬਣਾਇਆ ਹੈ? ਇੰਟਰਸੈਪਟਰ ਉਸ ਦੀਆਂ LLM ਕਾਲਾਂ ਵੀ
ਟਰੈਕ ਕਰਦਾ ਹੈ। ਵੇਖੋ [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)।

## ਤੁਹਾਨੂੰ ਕੀ ਮਿਲਦਾ ਹੈ

- **ਸੈਸ਼ਨ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ**: ਹਰ ਏਜੰਟ ਨੇ ਕੀ ਕੀਤਾ, ਵਾਰੀ-ਦਰ-ਵਾਰੀ, ਰੀਪਲੇ ਨਾਲ
- **ਲਾਗਤ ਅਤੇ ਟੋਕਨ**: ਰਨਟਾਈਮ, ਮਾਡਲ, ਸੈਸ਼ਨ ਅਤੇ ਦਿਨ ਦੇ ਹਿਸਾਬ ਨਾਲ, ਵਿਗਾੜ ਦੇ ਸੰਕੇਤਾਂ ਨਾਲ
- **ਫ਼ਲੋ**: ਚੈਨਲਾਂ, ਮਾਡਲਾਂ ਅਤੇ ਟੂਲਾਂ ਰਾਹੀਂ ਲੰਘਦੇ ਸੁਨੇਹਿਆਂ ਦਾ ਲਾਈਵ ਡਾਇਗ੍ਰਾਮ
- **ਬ੍ਰੇਨ**: ਹੋ ਰਹੀ ਸੋਚ-ਵਿਚਾਰ ਅਤੇ ਟੂਲ-ਕਾਲ ਈਵੈਂਟ ਸਟ੍ਰੀਮ
- **ਸੰਦਰਭ ਬਲੋਆਊਟ**: ਹਰ ਪ੍ਰੋਵਾਈਡਰ ਮੁਤਾਬਕ ਵਿੰਡੋ ਵਰਤੋਂ, ਕੰਪੈਕਸ਼ਨ ਬਨਾਮ ਜ਼ਬਰਦਸਤੀ ਓਵਰਫਲੋ, ਨਾਲ ਹੀ ਹਰ ਰਨਟਾਈਮ ਲਈ ਇਹ ਨਕਸ਼ਾ ਕਿ ਅਸੀਂ *ਕੀ ਨਹੀਂ* ਵੇਖ ਸਕਦੇ ([ਕਿਵੇਂ](docs/CONTEXT_BLOWOUT.md))
- **ਮੈਮਰੀ ਅਤੇ ਸਕਿੱਲ**: ਉਹ ਫ਼ਾਈਲਾਂ ਅਤੇ ਸਕਿੱਲਾਂ ਜੋ ਹਰ ਰਨਟਾਈਮ ਨੇ ਅਸਲ ਵਿੱਚ ਲੋਡ ਕੀਤੀਆਂ
- **ਸਿਹਤ ਅਤੇ ਲੌਗ**: ਡਿਸਕ, ਮੈਮਰੀ, ਗਲਤੀ ਦਰਾਂ, ਰੇਟ ਲਿਮਿਟ, ਲਾਈਵ ਲੌਗ ਸਟ੍ਰੀਮ
- **ਅਲਰਟ**: ਬਜਟ ਕੈਪ, ਗਲਤੀ ਦੇ ਵਾਧੇ, ਏਜੰਟ-ਔਫ਼ਲਾਈਨ, Slack, Discord, PagerDuty, Telegram, Email ਵੱਲ ਭੇਜੇ ਗਏ
- **ਮਨਜ਼ੂਰੀਆਂ**: ਜੋਖਮ ਭਰੀਆਂ ਟੂਲ ਕਾਲਾਂ ਨੂੰ *ਚੱਲਣ ਤੋਂ ਪਹਿਲਾਂ* ਰੋਕੋ ਅਤੇ ਆਪਣੇ ਫ਼ੋਨ ਤੋਂ ਮਨਜ਼ੂਰ ਕਰੋ ([ਕਿਵੇਂ](docs/APPROVALS.md))

## ਸੰਦਰਭ ਬਲੋਆਊਟ, ਅਤੇ ਨਿਗਰਾਨੀ ਦੀ ਲਾਗਤ

ਕਿਸੇ ਵੀ ਏਜੰਟ-ਤੁਲਨਾ ਟੂਲ 'ਤੇ ਭਰੋਸਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਜਾਣਨ ਲਾਇਕ ਦੋ ਸਵਾਲ।

**ਇਹ ਵੱਖ-ਵੱਖ ਰਨਟਾਈਮਾਂ ਵਿੱਚ ਸੰਦਰਭ-ਵਿੰਡੋ ਬਲੋਆਊਟ ਨੂੰ ਕਿਵੇਂ ਸੰਭਾਲਦਾ ਹੈ?**

ਵਰਤੋਂ ਪ੍ਰਤੀਸ਼ਤਤਾ ਓਨੀ ਹੀ ਸੱਚੀ ਹੁੰਦੀ ਹੈ ਜਿੰਨਾ ਉਹ ਅੰਕ ਜਿਸ ਨਾਲ ਇਹ ਵੰਡੀ ਜਾਂਦੀ ਹੈ। ClawMetry
ਹਰ ਪ੍ਰੋਵਾਈਡਰ ਲਈ ਵਿੰਡੋ ਨੂੰ [ਇੱਕ ਟੇਬਲ ਜਿਸਨੂੰ ਤੁਸੀਂ ਪੜ੍ਹ ਸਕਦੇ ਹੋ ਅਤੇ
PR ਕਰ ਸਕਦੇ ਹੋ](clawmetry/context_windows.py) ਤੋਂ ਸਾਈਜ਼ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama ਅਤੇ GLM ਸ਼ਾਮਲ ਹਨ। ਇਹ 32
ਰਨਟਾਈਮਾਂ ਨੂੰ ਇੱਕੋ ਵੈਂਡਰ ਦੇ ਪੈਮਾਨੇ ਨਾਲ ਨਹੀਂ ਮਾਪਦਾ। ਇਹ ਮਾਅਨੇ ਰੱਖਦਾ ਹੈ: Anthropic ਦੇ
200K ਦੇ ਮੁਕਾਬਲੇ ਗਿਣਿਆ ਗਿਆ 300K GPT-5 ਵਾਰੀ ">100%, ਬਲੋਨ" ਪੜ੍ਹਿਆ ਜਾਂਦਾ ਹੈ ਜਦੋਂ ਕਿ ਇਹ ਅਸਲ ਵਿੱਚ
GPT-5 ਦੇ 400K ਦਾ 75% ਹੀ ਹੈ। ਇਹੀ ਪੈਮਾਨਾ ਅਸਲ ਵਿੱਚ ਓਵਰਫਲੋ ਹੋਈ 130K DeepSeek ਵਾਰੀ ਨੂੰ
ਇੱਕ ਆਰਾਮਦਾਇਕ 65% ਵਜੋਂ ਲੁਕਾ ਦਿੰਦਾ ਹੈ।

ਹਰ ਵਿੰਡੋ ਆਪਣੇ ਸਰੋਤ ਨਾਲ ਆਉਂਦੀ ਹੈ: `model_table`, `explicit_marker`,
`observed_floor`, ਜਾਂ ਜਦੋਂ ਸਾਨੂੰ ਮਾਡਲ ਦਾ ਪਤਾ ਨਹੀਂ ਹੁੰਦਾ ਤਾਂ ਇੱਕ ਇਮਾਨਦਾਰ `default`। ਇੱਕ
ਅੰਦਾਜ਼ੇ 'ਤੇ ਬਣਿਆ ਗੇਜ ਕਦੇ ਵੀ ਲੁੱਕਅੱਪ 'ਤੇ ਬਣੇ ਗੇਜ ਵਾਂਗ ਪ੍ਰਮਾਣਿਕਤਾ ਨਾਲ ਨਹੀਂ ਦਿਖਾਈ ਦਿੰਦਾ।

ClawMetry ਸਿਰਫ਼ ਕੁਝ ਰਨਟਾਈਮਾਂ 'ਤੇ ਕੰਪੈਕਸ਼ਨ ਈਵੈਂਟ ਵੇਖ ਸਕਦਾ ਹੈ। ਇਸ ਲਈ
`GET /api/context-coverage` ਹਰ ਰਨਟਾਈਮ ਲਈ ਦੱਸਦਾ ਹੈ ਕਿ ਕੀ **ਜ਼ੀਰੋ ਦਾ ਮਤਲਬ
"ਸਾਫ਼ ਚੱਲਿਆ" ਹੈ ਜਾਂ "ਸਾਨੂੰ ਦਿਖਾਈ ਨਹੀਂ ਦਿੰਦਾ"**। ਜਿਸ `0` ਦਾ ਅਸਲ ਵਿੱਚ ਮਤਲਬ ਅੰਨ੍ਹਾਪਣ ਹੈ, ਉਹ ਇਹੀ ਦੱਸਦਾ ਹੈ।
[ਪੂਰਾ ਵੇਰਵਾ](docs/CONTEXT_BLOWOUT.md)

**ਇੰਸਟਰੂਮੈਂਟੇਸ਼ਨ ਦੀ ਲਾਗਤ ਕੀ ਹੈ?**

| ਰਾਹ | ਤੁਹਾਡੇ ਏਜੰਟ ਵਿੱਚ ਜੋੜਿਆ ਗਿਆ | ਮੂਲ? |
|---|---|---|
| ਸੈਸ਼ਨ-ਫ਼ਾਈਲ ਟੇਲਿੰਗ (ਸਾਰੇ 32 ਰਨਟਾਈਮ) | **0**। ਵੱਖਰੀ ਪ੍ਰਕਿਰਿਆ, ਤੁਹਾਡੇ ਏਜੰਟ ਵਿੱਚ ਕੋਈ ClawMetry ਕੋਡ ਨਹੀਂ | ਚਾਲੂ |
| HTTP ਇੰਟਰਸੈਪਟਰ (`CLAWMETRY_INTERCEPT=1`) | ਹਰ LLM ਕਾਲ 'ਤੇ **+0.44 ms**, ਭਾਵ 5s ਦੀ ਕਾਲ ਦਾ 0.009% | ਬੰਦ |
| ਪ੍ਰੀ-ਟੂਲ ਹੁੱਕ ਗੇਟ (ਵਾਰਮ ਕੈਸ਼) | ਹਰ ਗੇਟਿਡ ਟੂਲ ਕਾਲ 'ਤੇ **+44 ms**, 36 ms ਦੇ ਇੰਟਰਪ੍ਰੇਟਰ ਫ਼ਲੋਰ ਤੋਂ ਵੱਧ | ਬੰਦ |
| ਐਨਫ਼ੋਰਸਮੈਂਟ ਪ੍ਰੌਕਸੀ | ਹਰ LLM ਕਾਲ 'ਤੇ **+9.7 ms** | ਬੰਦ |

ਡੀਮਨ ਹੋਸਟ ਲਾਗਤ: ਇੰਜੈਸਟ **2,762 ਈਵੈਂਟ/ਸੈਕਿੰਡ**, ਡਿਸਕ 'ਤੇ **710 ਬਾਈਟ/ਈਵੈਂਟ**
(1 ਲੱਖ ਈਵੈਂਟ ਲਈ 67.7 MB), ਅਤੇ ਇੱਕ ਵਿਅਸਤ ਇੰਸਟਾਲ 'ਤੇ ਲਗਾਤਾਰ **ਇੱਕ ਕੋਰ ਦਾ ~12%**।
ਇਹ ਆਖਰੀ ਅੰਕ ਸਾਡੇ ਆਪਣੇ ਦੱਸੇ ਗਏ 5-10% ਬਜਟ ਤੋਂ ਵੱਧ ਹੈ, ਇਸ ਲਈ ਇਸਨੂੰ ਸਫ਼ੇ ਤੋਂ
ਹਟਾਉਣ ਦੀ ਬਜਾਏ ਹੱਲ ਕੀਤੇ ਜਾਣ ਵਾਲੇ ਇੱਕ ਬੱਗ ਵਜੋਂ ਪ੍ਰਕਾਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ।

Apple M2 Pro 'ਤੇ `benchmarks/overhead.py` ਨਾਲ ਮਾਪਿਆ ਗਿਆ। ਹਾਰਨੈੱਸ
ਹਰ ਸ਼ਰਤ ਨੂੰ ਇੱਕ ਵੱਖਰੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਚਲਾਉਂਦਾ ਹੈ, ਉਹਨਾਂ ਦੇ ਕ੍ਰਮ ਨੂੰ ਬਦਲਦਾ ਹੈ, ਅਤੇ **ਜਦੋਂ
ਰਾਊਂਡ ਇਸਦੇ ਚਿੰਨ੍ਹ 'ਤੇ ਸਹਿਮਤ ਨਹੀਂ ਹੁੰਦੇ ਤਾਂ ਕੋਈ ਅੰਕ ਨਹੀਂ ਛਾਪਦਾ**। ਇਸਨੂੰ ਆਪਣੀ
ਮਸ਼ੀਨ 'ਤੇ ਇੱਕ ਮਿੰਟ ਵਿੱਚ ਚਲਾਓ:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

ਹਰ ਰਾਹ ਮਾਪਿਆ ਗਿਆ ਹੈ, ਹੁੱਕ ਗੇਟ ਅਤੇ ਐਨਫ਼ੋਰਸਮੈਂਟ ਪ੍ਰੌਕਸੀ ਸਮੇਤ,
ਅਤੇ ਹਾਰਨੈੱਸ CI ਵਿੱਚ Linux, macOS ਅਤੇ Windows 'ਤੇ ਚੱਲਦਾ ਹੈ। ਜਾਣਨ ਲਾਇਕ ਦੋ ਨਤੀਜੇ: ਪ੍ਰੌਕਸੀ
Windows 'ਤੇ Linux ਨਾਲੋਂ ਲਗਭਗ ਸੱਤ ਗੁਣਾ ਵੱਧ ਲਾਗਤ ਲੈਂਦੀ ਹੈ, ਅਤੇ
ਡੀਮਨ ਇਸ ਵੇਲੇ ਇੱਕ ਕੋਰ ਦਾ ਲਗਭਗ 12% ਲਗਾਤਾਰ ਵਰਤਦਾ ਹੈ, ਜੋ ਸਾਡੇ ਆਪਣੇ 5-10% ਬਜਟ ਤੋਂ
ਵੱਧ ਹੈ। ਕੱਚਾ JSON, ਤਰੀਕਾ, ਅਤੇ ਜੋ ਹਾਲੇ ਵੀ ਮਾਪਿਆ ਨਹੀਂ ਗਿਆ, ਉਹ
[docs/OVERHEAD.md](docs/OVERHEAD.md) ਵਿੱਚ ਹੈ।

## ਕੀਮਤ

| ਪਲਾਨ | ਇਹ ਕੀ ਕਵਰ ਕਰਦਾ ਹੈ | ਕੀਮਤ |
|---|---|---|
| **ਮੁਫ਼ਤ** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, ਪੂਰਾ ਡੈਸ਼ਬੋਰਡ, ਸਿਰਫ਼ ਲੋਕਲ | $0 |
| **ਸਟਾਰਟਰ** | ਬਾਕੀ ਹਰ ਰਨਟਾਈਮ, ਫਲੀਟ ਵਿਊ, ਕਲਾਊਡ ਸਿੰਕ | $9 ਪ੍ਰਤੀ ਨੋਡ / ਮਹੀਨਾ |
| **Pro** | ਸਟਾਰਟਰ + ਕੰਟਰੋਲ ਅਤੇ ਮੁਲਾਂਕਣ: ਮਨਜ਼ੂਰੀਆਂ, ਟੂਲ-ਜੋਖਮ ਨੀਤੀਆਂ, ਈਵਲ, ਵਿਗਾੜ ਖੋਜ, ਲਾਗਤ ਓਪਟੀਮਾਈਜ਼ਰ, OTel ਐਕਸਪੋਰਟ, ਟੈਂਪਰ-ਸਬੂਤ ਆਡਿਟ ਲੌਗ | $19 ਪ੍ਰਤੀ ਨੋਡ / ਮਹੀਨਾ |

ਸਾਲਾਨਾ ਪਲਾਨ, Enterprise ਅਤੇ ਮੌਜੂਦਾ ਅੰਕੜੇ
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** 'ਤੇ ਮਿਲਦੇ ਹਨ। ਸਵੈ-ਹੋਸਟਡ ਲਾਈਸੈਂਸ
ਕੁੰਜੀਆਂ ਕਲਾਊਡ ਤੋਂ ਬਿਨਾਂ ਕੰਮ ਕਰਦੀਆਂ ਹਨ (`clawmetry license`)। ਮੁਫ਼ਤ/ਪੇਡ ਦੀ ਸਹੀ ਵੰਡ
[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) ਵਿੱਚ ਹੈ।

## ਤੁਹਾਡਾ ਡੇਟਾ ਤੁਹਾਡੀ ਮਸ਼ੀਨ 'ਤੇ ਰਹਿੰਦਾ ਹੈ

ClawMetry ਸਥਾਨਕ ਸੈਸ਼ਨ ਫ਼ਾਈਲਾਂ ਅਤੇ ਲੌਗ ਪੜ੍ਹਦਾ ਹੈ। **ਕੋਈ ਸੈਸ਼ਨ ਡੇਟਾ ਤੁਹਾਡੇ ਬਾਕਸ ਤੋਂ ਬਾਹਰ ਨਹੀਂ ਜਾਂਦਾ
ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ `clawmetry connect` ਨਹੀਂ ਚਲਾਉਂਦੇ** — ਕੋਈ ਪ੍ਰੌਮਪਟ, ਜਵਾਬ, ਟੂਲ ਆਰਗੂਮੈਂਟ, ਫ਼ਾਈਲ
ਸਮੱਗਰੀ ਜਾਂ ਲੌਗ ਲਾਈਨਾਂ ਨਹੀਂ। ਜਦੋਂ ਤੁਸੀਂ ਜੋੜਦੇ ਹੋ, ਸਨੈਪਸ਼ਾਟ ਇੱਕ ਅਜਿਹੀ
ਕੁੰਜੀ ਨਾਲ ਐਂਡ-ਟੂ-ਐਂਡ ਇਨਕ੍ਰਿਪਟਡ ਹੁੰਦਾ ਹੈ ਜੋ ਤੁਹਾਡੀ ਮਸ਼ੀਨ ਤੋਂ ਕਦੇ ਬਾਹਰ ਨਹੀਂ ਜਾਂਦੀ, ਅਤੇ ਤੁਹਾਡੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਡੀਕ੍ਰਿਪਟ ਹੁੰਦਾ ਹੈ। ਜੇ ਕਿਸੇ
ਨੋਡ ਕੋਲ ਕੋਈ ਕੁੰਜੀ ਨਹੀਂ ਹੈ, ਤਾਂ ਅਪਲੋਡ ਸਾਦੇ ਟੈਕਸਟ ਵਿੱਚ ਭੇਜਣ ਦੀ ਬਜਾਏ ਛੱਡ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਕੋਈ ਵੀ
ਸਰਵਰ ਜਵਾਬ ਇਸਨੂੰ ਬੰਦ ਨਹੀਂ ਕਰ ਸਕਦਾ।

ਜੋੜਨ ਤੋਂ ਪਹਿਲਾਂ ਮੂਲ ਰੂਪ ਵਿੱਚ ਦੋ ਚੀਜ਼ਾਂ ਚੱਲਦੀਆਂ ਹਨ, ਦੋਵੇਂ ਅਪਟ-ਆਊਟ ਅਤੇ ਦੋਵਾਂ ਵਿੱਚ
ਕੋਈ ਸੈਸ਼ਨ ਡੇਟਾ ਨਹੀਂ: ਇੱਕ ਅਗਿਆਤ ਇੰਸਟਾਲ ਪਿੰਗ ਅਤੇ PyPI ਦੇ ਖ਼ਿਲਾਫ਼ ਇੱਕ
ਵਰਜਨ ਚੈੱਕ। ਇੱਕ ਮੂਲ ਇੰਸਟਾਲ ਸ਼ੁਰੂਆਤੀ ਬੈਨਰ ਲਾਈਨ ਲਈ ਤੁਹਾਡਾ ਪਬਲਿਕ IP ਵੀ ਇੱਕ ਵਾਰ
ਵੇਖਦਾ ਹੈ। ਹਰ ਟਿਕਾਣਾ, ਇਹ ਕੀ ਲੈ ਕੇ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇਸਨੂੰ ਕਿਵੇਂ ਬੰਦ ਕਰਨਾ ਹੈ, ਦੀ ਸੂਚੀ
[docs/EGRESS.md](docs/EGRESS.md) ਵਿੱਚ ਹੈ; ਸਵੈ-ਹੋਸਟਡ, ਮੁੜ-ਨਿਰਦੇਸ਼ਿਤ ਅਤੇ ਏਅਰ-ਗੈਪਡ ਇੰਸਟਾਲ
ਕੋਈ ਸਵੈ-ਇੱਛਤ ਬਾਹਰੀ ਕਾਲ ਬਿਲਕੁਲ ਨਹੀਂ ਕਰਦੇ।

ਡੀਕ੍ਰਿਪਸ਼ਨ ਤੁਹਾਡੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਹੁੰਦੀ ਹੈ, ਉਸ ਕੋਡ ਵਿੱਚ ਜੋ ਅਸੀਂ ਤੁਹਾਨੂੰ ਦਿੰਦੇ ਹਾਂ। ਇਹ ਪਹਿਲਾਂ
ਇੱਕ ਵਾਅਦਾ ਹੁੰਦਾ ਸੀ; ਹੁਣ ਇਹ ਕੁਝ ਅਜਿਹਾ ਹੈ ਜਿਸਨੂੰ ਤੁਸੀਂ ਜਾਂਚ ਸਕਦੇ ਹੋ। ਤੁਹਾਡੀ ਕੁੰਜੀ ਨੂੰ ਛੂਹਣ ਵਾਲੀ ਹਰ ਲਾਈਨ
ਇੱਕ ਪੜ੍ਹਨਯੋਗ ਫ਼ਾਈਲ ਵਿੱਚ ਰਹਿੰਦੀ ਹੈ, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
ਜੋ ਵ੍ਹੀਲ ਦੇ ਅੰਦਰ ਭੇਜੀ ਜਾਂਦੀ ਹੈ ਅਤੇ ਹੂ-ਬ-ਹੂ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ, ਇੱਕ Subresource
Integrity ਹੈਸ਼ ਨਾਲ ਪਿੰਨ ਕੀਤੀ ਗਈ। ਇਹ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਕਿ ਬ੍ਰਾਊਜ਼ਰ ਉਹੀ ਚਲਾਉਂਦਾ ਹੈ ਜੋ ਅਸੀਂ ਪ੍ਰਕਾਸ਼ਿਤ ਕੀਤਾ ਹੈ:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

ਇਹ ਕੀ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ: ਅਸੀਂ ਉਹ ਸਫ਼ਾ ਦਿੰਦੇ ਹਾਂ ਜੋ ਫ਼ਾਈਲ ਲੋਡ ਕਰਦਾ ਹੈ, ਇਸ ਲਈ ਅਸੀਂ
ਇੱਕ ਵੱਖਰਾ ਸਫ਼ਾ ਦੇ ਸਕਦੇ ਹਾਂ। Integrity ਹੈਸ਼ ਤੁਹਾਨੂੰ ਇੱਕ ਸਮਝੌਤਾ ਹੋਏ CDN ਤੋਂ ਬਚਾਉਂਦੇ ਹਨ,
ਵੈਂਡਰ ਤੋਂ ਨਹੀਂ। ਤੁਹਾਨੂੰ ਜੋ ਮਿਲਦਾ ਹੈ ਉਹ ਇਹ ਹੈ ਕਿ ਕੋਈ ਵੀ ਬਦਲੀ ਜਾਣਬੁੱਝ ਕੇ, ਸਫ਼ੇ ਦੇ
ਸਰੋਤ ਵਿੱਚ ਦਿਖਾਈ ਦੇਣ ਵਾਲੀ, ਅਤੇ PyPI 'ਤੇ ਮੌਜੂਦ ਕਿਸੇ ਵੀ ਵਿਅਕਤੀ ਦੁਆਰਾ ਲਿਆਂਦੇ ਜਾ ਸਕਣ ਵਾਲੇ
ਆਰਟੀਫ਼ੈਕਟ ਤੋਂ ਵੱਖਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। ਸਵੈ-ਹੋਸਟਿੰਗ ਜਾਂ ਸਿਰਫ਼-ਲੋਕਲ ਰਹਿਣਾ ਇਸ
ਨਿਰਭਰਤਾ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾ ਦਿੰਦਾ ਹੈ।

## ਇੰਸਟਾਲ

```bash
pip install clawmetry     # ਫਿਰ: clawmetry
```

ਜਾਂ ਇੱਕ-ਲਾਈਨਰ: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS, Linux ਜਾਂ Windows 'ਤੇ Python 3.8+ ਅਤੇ ਇੱਕੋ ਮਸ਼ੀਨ 'ਤੇ ਘੱਟੋ-ਘੱਟ ਇੱਕ ਏਜੰਟ ਰਨਟਾਈਮ
ਚਾਹੀਦਾ ਹੈ। Docker ਹਦਾਇਤਾਂ: [docs/DOCKER.md](docs/DOCKER.md)।

ਜਾਂ ਏਜੰਟ ਨੂੰ ਤੁਹਾਡੇ ਲਈ ਇਸਨੂੰ ਸੈੱਟਅੱਪ ਕਰਨ ਦਿਓ। [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
ਸਕਿੱਲ Claude Code, Codex, Cursor, Gemini CLI, Copilot ਜਾਂ OpenCode ਨੂੰ ClawMetry
ਇੰਸਟਾਲ ਕਰਨਾ, ਮਸ਼ੀਨ 'ਤੇ ਏਜੰਟ ਕੀ ਕਰ ਰਹੇ ਹਨ ਅਤੇ ਕਿੰਨਾ ਖਰਚ ਕਰ ਰਹੇ ਹਨ ਦੱਸਣਾ,
ਬੇਨਤੀ 'ਤੇ ਇੱਕ ਸੈਸ਼ਨ ਰੋਕਣਾ, ਅਤੇ ਜੋਖਮ ਭਰੀਆਂ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਮਨਜ਼ੂਰੀ ਲਈ ਰੋਕ ਕੇ ਰੱਖਣਾ
ਸਿਖਾਉਂਦੀ ਹੈ:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## ਦਸਤਾਵੇਜ਼

| | |
|---|---|
| [ਰਨਟਾਈਮ ਅਨੁਕੂਲਤਾ](docs/compatibility.md) | ਹਰ ਅਡੈਪਟਰ ਕੀ ਪੜ੍ਹਦਾ ਹੈ, ਅਤੇ ਇੱਕ ਰਨਟਾਈਮ ਕਿਵੇਂ ਜੋੜਨਾ ਹੈ |
| [ਸੰਦਰਭ ਬਲੋਆਊਟ](docs/CONTEXT_BLOWOUT.md) | ਹਰ ਪ੍ਰੋਵਾਈਡਰ ਦੀ ਵਿੰਡੋ, ਕੰਪੈਕਸ਼ਨ ਬਨਾਮ ਓਵਰਫਲੋ, ਹਰ ਰਨਟਾਈਮ ਲਈ ਕਵਰੇਜ |
| [ਓਵਰਹੈੱਡ](docs/OVERHEAD.md) | ਇੰਸਟਰੂਮੈਂਟੇਸ਼ਨ ਦੀ ਲਾਗਤ ਕੀ ਹੈ, ਮਾਪੀ ਗਈ, ਦੁਹਰਾਉਣ ਲਈ ਹਾਰਨੈੱਸ ਨਾਲ |
| [ਹੱਕਦਾਰੀਆਂ](docs/ENTITLEMENTS.md) | ਮੁਫ਼ਤ ਬਨਾਮ ਪੇਡ, ਟੀਅਰ ਮੈਟ੍ਰਿਕਸ, ਲਾਈਸੈਂਸ CLI |
| [ਮਨਜ਼ੂਰੀਆਂ ਅਤੇ ਨੀਤੀਆਂ](docs/APPROVALS.md) | ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਗੇਟਿੰਗ, ਜੋਖਮ ਸਕੋਰਿੰਗ, ਫ਼ੋਨ ਮਨਜ਼ੂਰੀਆਂ |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | ਕਿਤੇ ਵੀ ਟਰੇਸ ਐਕਸਪੋਰਟ ਕਰੋ, ਕਿਸੇ ਵੀ ਥਾਂ ਤੋਂ OTLP ਇੰਜੈਸਟ ਕਰੋ |
| [ਆਪਣਾ ਏਜੰਟ ਲਿਆਓ](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain ਸ਼ੁਰੂ ਤੋਂ ਅੰਤ ਤੱਕ, ਚਲਾਏ ਜਾ ਸਕਣ ਵਾਲੀਆਂ ਉਦਾਹਰਨਾਂ ਨਾਲ |
| [SDK ਟਰੈਕਿੰਗ](docs/SDK_TRACKING.md) | ਤੁਹਾਡੇ ਖੁਦ ਬਣਾਏ ਏਜੰਟਾਂ ਲਈ ਲਾਗਤ ਵੰਡ |
| [ਚੈਟ ਚੈਨਲ](docs/CHANNELS.md) | ਫ਼ਲੋ ਵਿੱਚ ਦਿਖਾਏ ਗਏ ਚੈਟ ਅਡੈਪਟਰ |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | ਸੈਂਡਬਾਕਸਡ NVIDIA NemoClaw ਸੈੱਟਅੱਪ |
| [Docker](docs/DOCKER.md) | ਇਮੇਜ, ਕੰਪੋਜ਼, ਵਾਲਿਊਮ ਮਾਊਂਟ |
| [ਆਰਕੀਟੈਕਚਰ](ARCHITECTURE.md) · [ਵਿਕਾਸ](docs/DEVELOPMENT.md) | ਅੰਦਰੋਂ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ; ਸੋਰਸ ਤੋਂ ਚਲਾਉਣਾ |
| [ਟੈਲੀਮੈਟਰੀ](docs/TELEMETRY.md) | ਅਗਿਆਤ ਇੰਸਟਾਲ ਅਤੇ ਡੈਸਕਟਾਪ-ਓਪਨ ਪਿੰਗ, ਅਤੇ ਇਹਨਾਂ ਨੂੰ ਬੰਦ ਕਿਵੇਂ ਕਰਨਾ ਹੈ |

## ਸਕਰੀਨਸ਼ਾਟ

ਹੇਠਾਂ ਦਿੱਤਾ ਹਰ ਅੰਕ ਇੱਕ ਅਸਲੀ ਮਸ਼ੀਨ ਤੋਂ ਹੈ, ਸਿਰਫ਼-ਪੜ੍ਹਨ ਲਈ, ਬਿਨਾਂ ਕੁਝ ਵੀ ਪਹਿਲਾਂ ਤੋਂ ਭਰੇ।

**ਇਹ ਤੁਹਾਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ ਕਦੋਂ ਕੁਝ ਗਲਤ ਹੈ, ਸਿਰਫ਼ ਕੀ ਹੋਇਆ ਇਹ ਹੀ ਨਹੀਂ।**
ਉੱਪਰ ਦੋ ਵਿਗਾੜ ਬੈਨਰ: ਖਰਚ ਰੋਜ਼ਾਨਾ ਔਸਤ ਤੋਂ 7 ਗੁਣਾ ਵੱਧ ਚੱਲ ਰਿਹਾ ਹੈ, ਅਤੇ ਇੱਕ
4.2 ਗੁਣਾ ਲਾਗਤ ਵਾਧਾ। ਉਹਨਾਂ ਦੇ ਹੇਠਾਂ, 667 ਹਾਲੀਆ ਸੈਸ਼ਨਾਂ ਵਿੱਚੋਂ 324 ਵਿੱਚ ਇੱਕ
ਬਰਬਾਦੀ ਸੰਕੇਤ ਮਿਲਿਆ, ਕਾਰਨ ਅਨੁਸਾਰ ਸੂਚੀਬੱਧ।

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**ਇਹ ਤੁਹਾਨੂੰ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਪੈਸਾ ਕਿੱਥੇ ਗਿਆ, ਹਰ ਵਿੰਡੋ ਵਿੱਚ।**
ਅੱਜ $252.47, ਇਸ ਹਫ਼ਤੇ $513.15, ਇਸ ਮਹੀਨੇ $1,312.92, ਹਰ ਇੱਕ ਦੇ ਪਿੱਛੇ ਦੇ
ਟੋਕਨਾਂ ਅਤੇ ਤੁਹਾਡੀ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਪਹਿਲਾਂ ਹੀ ਕਿੰਨਾ ਕਵਰ ਕਰਦੀ ਹੈ ਸਮੇਤ। ਉਸਦੇ ਹੇਠਾਂ,
ਲਗਭਗ $1,128/ਮਹੀਨਾ ਵਸੂਲੀਯੋਗ ਵਜੋਂ ਸੂਚੀਬੱਧ ਅਤੇ ਕੈਸ਼ ਦੁਬਾਰਾ ਵਰਤੋਂ ਨਾਲ ਪਹਿਲਾਂ ਹੀ
$17,256/ਮਹੀਨਾ ਬਚਾਏ ਗਏ।

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**ਇਹ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਇੱਕ ਸੁਨੇਹਾ ਜਵਾਬ ਕਿਵੇਂ ਬਣਦਾ ਹੈ।**
ਲਾਈਵ ਫ਼ਲੋ ਡਾਇਗ੍ਰਾਮ: ਤੁਸੀਂ, ਉਹ ਚੈਨਲ ਜਿੱਥੇ ਇਹ ਆਇਆ, ਗੇਟਵੇ, ਹੁਣੇ
ਜਵਾਬ ਦੇ ਰਿਹਾ ਮਾਡਲ, ਅਤੇ ਹਰ ਟੂਲ ਜਿਸ ਤੱਕ ਇਹ ਪਹੁੰਚਿਆ। ਨੋਡ ਰੋਸ਼ਨ ਹੋ ਜਾਂਦੇ ਹਨ ਜਿਵੇਂ-ਜਿਵੇਂ ਕੰਮ
ਉਹਨਾਂ ਵਿੱਚੋਂ ਲੰਘਦਾ ਹੈ।

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**ਮਸ਼ੀਨ 'ਤੇ ਹਰ ਏਜੰਟ, ਇੱਕ ਟੇਬਲ ਵਿੱਚ।**
ਇਹ ਕੀ ਚਲਾਉਂਦਾ ਹੈ, ਪਿਛਲੇ 24 ਘੰਟਿਆਂ ਵਿੱਚ ਅਤੇ ਆਪਣੀ ਪੂਰੀ ਉਮਰ ਵਿੱਚ ਇਸਦੀ ਲਾਗਤ, ਕਦੋਂ
ਆਖਰੀ ਵਾਰ ਦੇਖਿਆ ਗਿਆ, ਇਸਦਾ ਮਾਲਕ ਕੌਣ ਹੈ, ਅਤੇ ਕੀ ਕੋਈ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਬਿੱਲ ਕਵਰ ਕਰ ਰਹੀ ਹੈ।
ਇੱਥੇ 14 ਏਜੰਟ, 3 ਸੈਸ਼ਨ ਕੰਮ ਕਰ ਰਹੇ, 13 ਸ਼ਾਂਤ।

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**ਇਹ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਇੱਕ ਵਾਰੀ ਦਾ ਸਮਾਂ ਅਤੇ ਪੈਸਾ ਕਿੱਥੇ ਗਿਆ, ਟੂਲ-ਦਰ-ਟੂਲ।**
ਇੱਕ ਅਸਲੀ ਸੈਸ਼ਨ ਦੀ ਇੱਕ ਵਾਰੀ: 11.2 ਮਿੰਟਾਂ ਵਿੱਚ $1.16 ਲਈ 11 ਟੂਲ। ਹਰ Bash
ਕਾਲ ਅਤੇ ਮਾਡਲ ਕਾਲ ਨੂੰ ਟਾਈਮਲਾਈਨ 'ਤੇ ਆਪਣੀ ਬਾਰ ਮਿਲਦੀ ਹੈ, ਤਾਂ ਜੋ 4.1 ਮਿੰਟ
ਚੱਲੀ ਕਮਾਂਡ ਅਤੇ 226ms ਚੱਲੀ ਕਮਾਂਡ ਇੱਕ ਨਜ਼ਰ ਵਿੱਚ ਵੱਖਰੀਆਂ ਦਿਖਾਈ ਦੇਣ।

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**ਇਹ ਕੰਮ ਨੂੰ ਗ੍ਰੇਡ ਕਰਦਾ ਹੈ, ਸਿਰਫ਼ ਖਰਚ ਨੂੰ ਨਹੀਂ।**
ਇਸ ਹਫ਼ਤੇ ਇੱਕ A: 54 ਕੰਮ ਸਾਫ਼ ਵਾਪਸ ਆਏ, 2 ਮੁਸ਼ਕਿਲ ਵਾਲਿਆਂ ਦੀ ਲਾਗਤ $48.57 ਸੀ, ਅਤੇ
ਜਿਹੜੇ ਰਨ ਨੂੰ ਗਰੇਡ ਕਰਨ ਲਈ ਬਹੁਤ ਘੱਟ ਗਤੀਵਿਧੀ ਸੀ ਉਹਨਾਂ ਨੂੰ ਜਿੱਤ ਵਜੋਂ ਗਿਣਨ ਦੀ ਬਜਾਏ
ਗ੍ਰੇਡ ਤੋਂ ਬਾਹਰ ਛੱਡ ਦਿੱਤਾ ਗਿਆ। ਹਰ ਮੁਸ਼ਕਿਲ ਰਨ ਆਪਣੇ ਟਰੇਸ ਨਾਲ ਜੁੜਿਆ ਹੋਇਆ ਹੈ।

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**ਇਹ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਸੰਦਰਭ ਵਿੰਡੋ ਕਿਉਂ ਭਰਦੀ ਰਹਿੰਦੀ ਹੈ।**
ਆਖਰੀ ਵਾਰੀ 'ਤੇ 1M-ਟੋਕਨ ਵਿੰਡੋ ਵਿੱਚੋਂ 715K, 83.3% ਦਾ ਸਿਖਰ, 4 ਕੰਪੈਕਸ਼ਨ
ਜੋ ਸਾਰੇ ਓਵਰਫਲੋ ਦੀ ਬਜਾਏ ਪਹਿਲਾਂ ਤੋਂ ਹੀ ਚੱਲੇ, ਅਤੇ ਇਸ ਪਿੱਛੇ ਹਰ ਵਾਰੀ ਦੀ ਵਰਤੋਂ।

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**ਖੋਜ ਤੁਹਾਡੇ ਕੁਝ ਵੀ ਕੌਂਫ਼ਿਗਰ ਕੀਤੇ ਬਿਨਾਂ ਚੱਲਦੀ ਹੈ।**
ਬਿਲਟ-ਇਨ ਡਿਟੈਕਟਰ ਇੰਸਟਾਲ ਤੋਂ ਹੀ ਚਾਲੂ ਹਨ: ਏਜੰਟ ਸ਼ਾਂਤ ਹੋ ਗਿਆ, ਟੈਲੀਮੈਟਰੀ ਫ਼ੀਡ
ਰੁਕ ਗਈ, ਲਾਗਤ ਵਾਧਾ, ਟੋਕਨ ਬਰਸਟ, ਗਲਤੀਆਂ ਵਧ ਰਹੀਆਂ, ਗਲਤੀ ਵਾਧਾ, ਬਜਟ
ਥ੍ਰੈਸ਼ਹੋਲਡ, ਖ਼ਤਰੇ ਦਾ ਦਸਤਖ਼ਤ ਮਿਲਿਆ, ਸੁਰੱਖਿਆ ਟੂਲ ਦੀ ਖੋਜ, ਸੁਰੱਖਿਆ ਸਥਿਤੀ
ਬਦਲੀ। ਤੁਹਾਡੇ ਆਪਣੇ ਨਿਯਮ ਇਸ ਦੇ ਉੱਪਰ ਵਿਕਲਪਿਕ ਹਨ।

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**ਜੋਖਮ ਭਰੀ ਕਾਲ ਰੋਕਣਾ ਅਪਟ-ਇਨ ਹੈ, ਅਤੇ ਬੰਦ ਹਾਲਤ ਵਿੱਚ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ।**
ਰਿਕਰਸਿਵ ਡਿਲੀਟ, ਫ਼ੋਰਸ ਪੁਸ਼, sudo, ਸੀਕ੍ਰੇਟ, ਪੈਕੇਜ ਇੰਸਟਾਲ ਅਤੇ ਬਾਹਰੀ
ਕਾਲਾਂ ਵਿੱਚੋਂ ਹਰ ਇੱਕ ਲਈ ਇੱਕ ਨਿਯਮ ਹੈ ਜੋ ਤੁਸੀਂ ਚਾਲੂ ਕਰ ਸਕਦੇ ਹੋ। ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ ਅਜਿਹਾ ਨਹੀਂ ਕਰਦੇ,
ClawMetry ਵੇਖਦਾ ਹੈ ਅਤੇ ਕੁਝ ਨਹੀਂ ਬਦਲਦਾ। ਇੱਕ ਵਾਰ ਚਾਲੂ ਹੋ ਜਾਵੇ, ਮੇਲ ਖਾਂਦੀਆਂ ਕਾਲਾਂ ਇੱਥੇ
(ਜਾਂ ਤੁਹਾਡੇ ਫ਼ੋਨ 'ਤੇ) ਮਨਜ਼ੂਰੀ ਜਾਂ ਇਨਕਾਰ ਦੀ ਉਡੀਕ ਕਰਦੀਆਂ ਹਨ।

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

ਹੋਰ, ਹਰ ਰਨਟਾਈਮ ਲਈ: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md)।

## ਮਾਨਤਾ

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## ਸਟਾਰ ਹਿਸਟਰੀ

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## ਲਾਈਸੈਂਸ

MIT · [@vivekchand](https://github.com/vivekchand) ਦੁਆਰਾ ਬਣਾਇਆ ਗਿਆ · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
