<!-- i18n-src:b22579578775 -->
> മലയാളം translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**ഒരു ഏജന്റിന് പുരോഗതി ഒന്നും കൈവരിക്കാതെ തന്നെ നൂറു ടൂൾ കോളുകൾ നടത്താൻ കഴിയും.** നിങ്ങളുടെ കോഡിംഗ് ഏജന്റുകൾ ഇതിനകം എഴുതുന്ന സെഷൻ ഫയലുകൾ ClawMetry വായിക്കുകയും, ടൈംലൈൻ, ടൂൾ കോളുകൾ, റൺടൈം വെളിപ്പെടുത്തുന്ന ടോക്കൺ, ചെലവ് വിവരങ്ങൾ എന്നിവ ഒരൊറ്റ വ്യൂവിൽ ഒരുക്കുകയും ചെയ്യുന്നു — അതിനാൽ ജോലി ചെയ്യുന്ന ഒരു ദീർഘ റണ്ണിനെയും കുടുങ്ങിക്കിടക്കുന്ന ഒന്നിനെയും വേർതിരിച്ചറിയാൻ നിങ്ങൾക്ക് കഴിയും.

**32 AI ഏജന്റ് റൺടൈമുകളുമായി** പ്രവർത്തിക്കുന്നു — Claude Code, OpenAI Codex, Hermes, OpenClaw കൂടാതെ 28 എണ്ണം കൂടി. നിങ്ങളുടെ മുഴുവൻ ഏജന്റ് ഫ്ലീറ്റിനും ഒരു ഡാഷ്ബോർഡ്. ([പൂർണ്ണ പട്ടിക](SUPPORTED_RUNTIMES.txt), കാറ്റലോഗിൽ നിന്ന് ജനറേറ്റ് ചെയ്തത്.)

> 🌐 **ഇത് ഈ ഭാഷകളിൽ വായിക്കുക:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [more →](docs/i18n/)

ഒരൊറ്റ കമാൻഡ്. കോൺഫിഗ് ഒന്നും വേണ്ട. എല്ലാം സ്വയം കണ്ടെത്തുന്നു.

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** ൽ തുറക്കും. കോൺഫിഗ് ഇല്ല: നിങ്ങളുടെ പക്കൽ ഇതിനകം ഉള്ള ഏജന്റ് റൺടൈമുകൾ ഇത് കണ്ടെത്തുന്നു, അവയെ റീഡ്-ഒൺലി ആയി വായിക്കുന്നു, അവ എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്നതിൽ ഒന്നും മാറ്റുന്നില്ല.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## ഇൻസ്റ്റാൾ ചെയ്യുന്നതിന് മുൻപ്

| | |
|---|---|
| **ഇത് എന്ത് ചെയ്യുന്നു** | നിങ്ങളുടെ ഏജന്റുകൾ ഇതിനകം എഴുതുന്ന സെഷൻ ഫയലുകളും ലോഗുകളും വായിക്കുന്നു. SDK ഇല്ല, കോഡ് മാറ്റം ഇല്ല, നിങ്ങളുടെ ആപ്പിൽ ഇൻസ്ട്രുമെന്റേഷൻ ഇല്ല. |
| **നിങ്ങൾ കാണുന്നത്** | സെഷൻ ടൈംലൈൻ, ടൂൾ-ബൈ-ടൂൾ റീപ്ലേ, ടോക്കൺ, ചെലവ് വിഭജനം, ട്രജക്ടറി സിഗ്നലുകൾ (ലൂപ്പിംഗ്, ആവർത്തിച്ചുള്ള പരാജയങ്ങൾ) — ഓരോ റൺടൈമിനും. |
| **സൗജന്യമായത്** | `pip install clawmetry` എന്നത് അക്കൗണ്ടോ കീയോ നെറ്റ്‌വർക്ക് കോളോ ഇല്ലാതെ **OpenClaw, NVIDIA NemoClaw, Goose, Qwen Code** എന്നിവ വായിക്കുന്നു. മറ്റ് 28 എണ്ണം — Claude Code, Codex, Cursor എന്നിവയും ബാക്കിയുള്ളവയും — ക്ലോസ്ഡ്-സോഴ്സ് `clawmetry-pro` കമ്പാനിയൻ വഴി വായിക്കുന്നു, ഇത് 7 ദിവസത്തെ ട്രയലിനൊപ്പമോ ഒരു പ്ലാനിനൊപ്പമോ ലഭിക്കും — കൃത്യമായ വിഭജനത്തിന് [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) കാണുക. |
| **എങ്ങനെ തുടങ്ങാം** | `pip install clawmetry && clawmetry`, പിന്നെ localhost:8900 തുറക്കുക. ഈ മെഷീനിൽ ഏജന്റുകൾ ഒന്നും ഇല്ലേ? `clawmetry --sample` ലേബൽ ചെയ്ത മൂന്ന് സിന്തറ്റിക് സെഷനുകളിൽ തുറക്കും. |
| **നിങ്ങളുടെ മെഷീനിൽ നിന്ന് പുറത്തുപോകുന്നത്** | `clawmetry connect` പ്രവർത്തിപ്പിക്കുന്നില്ലെങ്കിൽ സെഷൻ ഡാറ്റ ഒന്നും പുറത്തുപോകില്ല. ഡിഫോൾട്ടായി രണ്ട് കാര്യങ്ങൾ പ്രവർത്തിക്കുന്നു, രണ്ടും ഓപ്റ്റ്-ഔട്ട് ചെയ്യാവുന്നതും, സെഷൻ ഉള്ളടക്കം വഹിക്കാത്തതും: അജ്ഞാതമായ ഇൻസ്റ്റാൾ പിംഗും PyPI വേർഷൻ ചെക്കും. ഓരോ ഡെസ്റ്റിനേഷനും [docs/EGRESS.md](docs/EGRESS.md) ൽ പട്ടികപ്പെടുത്തിയിട്ടുണ്ട്, കമന്റുകൾ വായിക്കുന്നതിന് പകരം വയർ ക്യാപ്ചറിൽ നിന്ന് പുനർനിർമ്മിച്ചത്. |

ഫലങ്ങൾ വിലയിരുത്തുന്നതിന് മുൻപ് അറിഞ്ഞിരിക്കേണ്ട രണ്ട് പരിധികൾ: റൺടൈമുകൾ വളരെ വ്യത്യസ്തമായ ഡാറ്റ വെളിപ്പെടുത്തുന്നു (ചിലത് ചെലവ് ഒട്ടും പ്രസിദ്ധീകരിക്കുന്നില്ല — ഏതൊക്കെ, ഓരോ റൺടൈമിനും എന്ന് [മാട്രിക്സ്](docs/compatibility.md) പറയുന്നു), കൂടാതെ ഒരു പ്രവർത്തനം നിരീക്ഷിക്കുന്നത് അത് തടയാൻ കഴിയുന്നതിന് തുല്യമല്ല ([ഏതൊക്കെ നിയന്ത്രണങ്ങൾ യഥാർത്ഥമാണ്, ഓരോ റൺടൈമിനും](docs/APPROVALS.md)).


## 32 ഏജന്റ് റൺടൈമുകളുമായി പ്രവർത്തിക്കുന്നു

**ഓപ്പൺ സോഴ്സ് ആപ്പിൽ സൗജന്യം:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**ഒരു പണമടച്ചുള്ള പ്ലാനിൽ:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

എല്ലാ റൺടൈമിനും ഒരേ ഡാഷ്ബോർഡ് തന്നെ ലഭിക്കുന്നു. ഒന്നിലധികം ഒരേസമയം പ്രവർത്തിപ്പിക്കുക, ഹെഡർ സ്വിച്ചർ ഓരോ ടാബിനെയും ഇവയിലൊന്നിലേക്ക് വീണ്ടും സ്കോപ്പ് ചെയ്യും.

SDK ഉപയോഗിച്ച് സ്വന്തമായി ഏജന്റ് നിർമ്മിച്ചോ? ഇന്റർസെപ്റ്റർ അതിന്റെ LLM കോളുകളും ട്രാക്ക് ചെയ്യുന്നു. [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md) കാണുക.

## നിങ്ങൾക്ക് ലഭിക്കുന്നത്

- **സെഷനുകളും ട്രാൻസ്ക്രിപ്റ്റുകളും**: ഓരോ ഏജന്റും എന്ത് ചെയ്തു, ടേൺ ബൈ ടേൺ, റീപ്ലേയോടൊപ്പം
- **ചെലവും ടോക്കണുകളും**: ഓരോ റൺടൈം, മോഡൽ, സെഷൻ, ദിവസം എന്നിവ പ്രകാരം, അസാധാരണത്വ ഫ്ലാഗുകളോടൊപ്പം
- **ഫ്ലോ**: ചാനലുകൾ, മോഡലുകൾ, ടൂളുകൾ വഴി നീങ്ങുന്ന സന്ദേശങ്ങളുടെ ലൈവ് ഡയഗ്രം
- **ബ്രെയിൻ**: റീസണിംഗും ടൂൾ-കോൾ ഇവന്റ് സ്ട്രീമും അത് സംഭവിക്കുന്ന സമയത്ത് തന്നെ
- **കോൺടെക്സ്റ്റ് ബ്ലോഔട്ട്**: ഓരോ പ്രൊവൈഡറിനും അനുസൃതമായ വിൻഡോ വലുപ്പം, കോംപാക്ഷൻ vs നിർബന്ധിത ഓവർഫ്ലോ, ഒപ്പം ഞങ്ങൾക്ക് *കാണാൻ കഴിയാത്തതിന്റെ* ഓരോ റൺടൈം മാപ്പും ([എങ്ങനെ](docs/CONTEXT_BLOWOUT.md))
- **മെമ്മറിയും സ്കില്ലുകളും**: ഓരോ റൺടൈമും യഥാർത്ഥത്തിൽ ലോഡ് ചെയ്ത ഫയലുകളും സ്കില്ലുകളും
- **ആരോഗ്യവും ലോഗുകളും**: ഡിസ്ക്, മെമ്മറി, പിഴവ് നിരക്കുകൾ, റേറ്റ് ലിമിറ്റുകൾ, ലൈവ് ലോഗ് സ്ട്രീം
- **അലേർട്ടുകൾ**: ബജറ്റ് പരിധികൾ, പിഴവ് കുതിപ്പുകൾ, ഏജന്റ്-ഓഫ്‌ലൈൻ, Slack, Discord, PagerDuty, Telegram, Email എന്നിവയിലേക്ക് റൂട്ട് ചെയ്യപ്പെടും
- **അപ്രൂവലുകൾ**: അപകടസാധ്യതയുള്ള ടൂൾ കോളുകൾ പ്രവർത്തിക്കുന്നതിന് *മുൻപ്* താൽക്കാലികമായി നിർത്തി നിങ്ങളുടെ ഫോണിൽ നിന്ന് അംഗീകരിക്കുക ([എങ്ങനെ](docs/APPROVALS.md))

## കോൺടെക്സ്റ്റ് ബ്ലോഔട്ടും, നിരീക്ഷണത്തിന്റെ ചെലവും

ഏതെങ്കിലും ഏജന്റ്-താരതമ്യ ടൂളിനെ വിശ്വസിക്കുന്നതിന് മുൻപ് ഉത്തരം കണ്ടെത്തേണ്ട രണ്ട് ചോദ്യങ്ങൾ.

**റൺടൈമുകൾക്കിടയിൽ കോൺടെക്സ്റ്റ്-വിൻഡോ ബ്ലോഔട്ട് ഇത് എങ്ങനെ കൈകാര്യം ചെയ്യുന്നു?**

ഒരു യൂട്ടിലൈസേഷൻ ശതമാനം അത് എന്തിനെയാണ് ഹരിക്കുന്നത് എന്നതിനെ ആശ്രയിച്ച് മാത്രമേ സത്യസന്ധമാകൂ. Anthropic, OpenAI, Google, xAI, DeepSeek, Kimi, Qwen, Mistral, Llama, GLM എന്നിവ ഉൾപ്പെടുന്ന നിങ്ങൾക്ക് വായിക്കാനും PR ചെയ്യാനും കഴിയുന്ന ഒരു [ടേബിളിൽ](clawmetry/context_windows.py) നിന്ന് ClawMetry ഓരോ പ്രൊവൈഡറിനും അനുസൃതമായി വിൻഡോയുടെ വലുപ്പം നിശ്ചയിക്കുന്നു. ഒരു വെണ്ടറുടെ അളവുകോൽ കൊണ്ട് 32 റൺടൈമുകളും അളക്കുന്നില്ല. ഇത് പ്രധാനമാണ്: 300K GPT-5 ടേൺ Anthropic ന്റെ 200K ക്കെതിരെ സ്കോർ ചെയ്യുമ്പോൾ ">100%, blown" എന്ന് വായിക്കുന്നു, യഥാർത്ഥത്തിൽ അത് GPT-5 ന്റെ 400K യുടെ 75% മാത്രമാണ്. അതേ അളവുകോൽ യഥാർത്ഥത്തിൽ ഓവർഫ്ലോ ആയ ഒരു 130K DeepSeek ടേണിനെ ആശ്വാസകരമായ 65% ആയി മറച്ചുവെക്കുന്നു.

ഓരോ വിൻഡോയും അതിന്റെ പ്രോവിനൻസോടൊപ്പം വരുന്നു: `model_table`, `explicit_marker`, `observed_floor`, അല്ലെങ്കിൽ മോഡൽ ഏതെന്ന് അറിയാത്തപ്പോൾ സത്യസന്ധമായ `default`. ഒരു ഊഹത്തിൽ നിർമ്മിച്ച ഗേജ് ഒരു ലുക്കപ്പിൽ നിർമ്മിച്ച ഒന്നിന് തുല്യമായ ആധികാരികതയോടെ ഒരിക്കലും റെൻഡർ ചെയ്യില്ല.

ചില റൺടൈമുകളിൽ മാത്രമേ ClawMetry ന് കോംപാക്ഷൻ ഇവന്റുകൾ കാണാൻ കഴിയൂ. അതിനാൽ `GET /api/context-coverage` ഓരോ റൺടൈമിനും, **പൂജ്യം എന്നാൽ "വൃത്തിയായി ഓടി" എന്നാണോ "ഞങ്ങൾക്ക് കാണാൻ കഴിയുന്നില്ല" എന്നാണോ** എന്ന് റിപ്പോർട്ട് ചെയ്യുന്നു. യഥാർത്ഥത്തിൽ കാണാൻ കഴിയാത്തതിനെ അർത്ഥമാക്കുന്ന ഒരു `0` അങ്ങനെ പറയുന്നു.
[പൂർണ്ണ വിശദാംശം](docs/CONTEXT_BLOWOUT.md)

**ഇൻസ്ട്രുമെന്റേഷന്റെ ചെലവ് എന്താണ്?**

| പാത | നിങ്ങളുടെ ഏജന്റിലേക്ക് ചേർത്തത് | ഡിഫോൾട്ടോ? |
|---|---|---|
| സെഷൻ-ഫയൽ ടെയ്‌ലിംഗ് (എല്ലാ 32 റൺടൈമുകളും) | **0**. പ്രത്യേക പ്രോസസ്സ്, നിങ്ങളുടെ ഏജന്റിൽ ClawMetry കോഡ് ഇല്ല | ഓൺ |
| HTTP ഇന്റർസെപ്റ്റർ (`CLAWMETRY_INTERCEPT=1`) | ഓരോ LLM കോളിനും **+0.44 ms**, അല്ലെങ്കിൽ 5s കോളിന്റെ 0.009% | ഓഫ് |
| പ്രീ-ടൂൾ ഹുക്ക് ഗേറ്റ് (വാം ക്യാഷ്) | 36 ms ഇന്റർപ്രെറ്റർ ഫ്ലോറിനുമേൽ, ഗേറ്റ് ചെയ്ത ഓരോ ടൂൾ കോളിനും **+44 ms** | ഓഫ് |
| എൻഫോഴ്സ്മെന്റ് പ്രോക്സി | ഓരോ LLM കോളിനും **+9.7 ms** | ഓഫ് |

ഡെമൺ ഹോസ്റ്റ് ചെലവ്: **2,762 events/sec** ഇൻജസ്റ്റ്, ഡിസ്കിൽ **710 bytes/event** (100k ഇവന്റുകൾക്ക് 67.7 MB), തിരക്കുള്ള ഒരു ഇൻസ്റ്റാളിൽ സ്ഥിരമായി **ഒരു കോറിന്റെ ~12%**. ഞങ്ങളുടെ സ്വന്തം പ്രഖ്യാപിത 5-10% ബജറ്റിനും മുകളിലാണ് ആ അവസാന സംഖ്യ, അതിനാൽ പേജിൽ നിന്ന് ഒഴിവാക്കുന്നതിന് പകരം പിന്തുടരേണ്ട ഒരു ബഗ് ആയി ഇത് പ്രസിദ്ധീകരിച്ചിരിക്കുന്നു.

`benchmarks/overhead.py` ഉപയോഗിച്ച് Apple M2 Pro യിൽ അളന്നത്. ഹാർനെസ്സ് ഓരോ കണ്ടീഷനും വേറൊരു പ്രോസസ്സിൽ പ്രവർത്തിപ്പിക്കുന്നു, അവയുടെ ക്രമം മാറ്റിമറിക്കുന്നു, കൂടാതെ **റൗണ്ടുകൾ അതിന്റെ ചിഹ്നത്തിൽ വിയോജിക്കുമ്പോൾ ഒരു സംഖ്യ പ്രിന്റ് ചെയ്യാൻ വിസമ്മതിക്കുന്നു**. ഒരു മിനിറ്റിനുള്ളിൽ നിങ്ങളുടെ സ്വന്തം മെഷീനിൽ ഇത് പ്രവർത്തിപ്പിക്കുക:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

ഹുക്ക് ഗേറ്റുകളും എൻഫോഴ്സ്മെന്റ് പ്രോക്സിയും ഉൾപ്പെടെ ഓരോ പാതയും അളക്കപ്പെടുന്നു, ഹാർനെസ്സ് CI യിൽ Linux, macOS, Windows എന്നിവയിൽ പ്രവർത്തിക്കുന്നു. അറിഞ്ഞിരിക്കേണ്ട രണ്ട് ഫലങ്ങൾ: Linux നെ അപേക്ഷിച്ച് Windows ൽ പ്രോക്സിക്ക് ഏകദേശം ഏഴ് മടങ്ങ് കൂടുതൽ ചെലവാകും, കൂടാതെ ഡെമൺ നിലവിൽ ഒരു കോറിന്റെ ഏകദേശം 12% സ്ഥിരമായി ഉപയോഗിക്കുന്നു, ഞങ്ങളുടെ സ്വന്തം 5-10% ബജറ്റിനും മുകളിൽ. റോ JSON, രീതി, ഇനിയും അളക്കാത്തത് എന്നിവ [docs/OVERHEAD.md](docs/OVERHEAD.md) ൽ ഉണ്ട്.

## വിലനിർണ്ണയം

| പ്ലാൻ | ഇത് എന്താണ് ഉൾക്കൊള്ളുന്നത് | വില |
|---|---|---|
| **സൗജന്യം** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, പൂർണ്ണ ഡാഷ്ബോർഡ്, ലോക്കൽ മാത്രം | $0 |
| **സ്റ്റാർട്ടർ** | മേൽപ്പറഞ്ഞ മറ്റെല്ലാ റൺടൈമുകളും, ഫ്ലീറ്റ് വ്യൂ, ക്ലൗഡ് സിങ്ക് | $9 ഒരു നോഡിന് / മാസം |
| **Pro** | സ്റ്റാർട്ടർ + നിയന്ത്രണവും മൂല്യനിർണ്ണയവും: അപ്രൂവലുകൾ, ടൂൾ-റിസ്ക് പോളിസികൾ, evals, അസാധാരണത്വ കണ്ടെത്തൽ, ചെലവ് ഒപ്റ്റിമൈസർ, OTel export, ടാമ്പർ-എവിഡന്റ് ഓഡിറ്റ് ലോഗ് | $19 ഒരു നോഡിന് / മാസം |

വാർഷിക പ്ലാനുകൾ, Enterprise, നിലവിലെ സംഖ്യകൾ എന്നിവ
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** ൽ ലഭ്യമാണ്. സ്വയം-ഹോസ്റ്റ് ചെയ്ത ലൈസൻസ്
കീകൾ ക്ലൗഡ് ഇല്ലാതെ പ്രവർത്തിക്കുന്നു (`clawmetry license`). കൃത്യമായ free/paid വിഭജനം
[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) ൽ ഉണ്ട്.

## നിങ്ങളുടെ ഡാറ്റ നിങ്ങളുടെ മെഷീനിൽ തന്നെ തുടരുന്നു

ClawMetry ലോക്കൽ സെഷൻ ഫയലുകളും ലോഗുകളും വായിക്കുന്നു. **നിങ്ങൾ `clawmetry connect` പ്രവർത്തിപ്പിക്കുന്നില്ലെങ്കിൽ സെഷൻ ഡാറ്റ ഒന്നും നിങ്ങളുടെ ബോക്സിൽ നിന്ന് പുറത്തുപോകില്ല** — പ്രോംപ്റ്റുകളോ, മറുപടികളോ, ടൂൾ ആർഗ്യുമെന്റുകളോ, ഫയൽ
ഉള്ളടക്കമോ, ലോഗ് ലൈനുകളോ ഇല്ല. നിങ്ങൾ കണക്റ്റ് ചെയ്യുമ്പോൾ, സ്നാപ്‌ഷോട്ട് ഒരിക്കലും നിങ്ങളുടെ മെഷീൻ വിട്ടുപോകാത്ത ഒരു കീ ഉപയോഗിച്ച് എൻഡ്-ടു-എൻഡ് എൻക്രിപ്റ്റ് ചെയ്യപ്പെടുന്നു, കൂടാതെ നിങ്ങളുടെ ബ്രൗസറിൽ ഡിക്രിപ്റ്റ് ചെയ്യപ്പെടുന്നു. ഒരു നോഡിന് കീ ഇല്ലെങ്കിൽ, അപ്‌ലോഡ് വ്യക്തമായ ടെക്സ്റ്റിൽ അയക്കുന്നതിന് പകരം ഒഴിവാക്കപ്പെടുന്നു, ഒരു സെർവർ പ്രതികരണത്തിനും അത് ഓഫ് ചെയ്യാൻ കഴിയില്ല.

നിങ്ങൾ കണക്റ്റ് ചെയ്യുന്നതിന് മുൻപ് ഡിഫോൾട്ടായി രണ്ട് കാര്യങ്ങൾ പ്രവർത്തിക്കുന്നു, രണ്ടും ഓപ്റ്റ്-ഔട്ട് ചെയ്യാവുന്നതും സെഷൻ ഡാറ്റ വഹിക്കാത്തതും: അജ്ഞാതമായ ഇൻസ്റ്റാൾ പിംഗും PyPI ക്കെതിരായ ഒരു വേർഷൻ ചെക്കും. ഒരു ഡിഫോൾട്ട് ഇൻസ്റ്റാൾ ഒരു സ്റ്റാർട്ടപ്പ് ബാനർ ലൈനിനായി നിങ്ങളുടെ പബ്ലിക് IP ഒരു തവണ നോക്കുകയും ചെയ്യുന്നു. ഓരോ ഡെസ്റ്റിനേഷനും, അത് എന്താണ് വഹിക്കുന്നത്, അത് എങ്ങനെ ഓഫ് ചെയ്യാം എന്നത് [docs/EGRESS.md](docs/EGRESS.md) ൽ പട്ടികപ്പെടുത്തിയിട്ടുണ്ട്; സ്വയം-ഹോസ്റ്റ് ചെയ്തതും, റീപോയിന്റ് ചെയ്തതും, എയർ-ഗ്യാപ്പ് ചെയ്തതുമായ ഇൻസ്റ്റാളുകൾ ഓപ്ഷണലായ ഔട്ട്ബൗണ്ട് കോളുകൾ ഒന്നും തന്നെ നടത്തുന്നില്ല.

ഡിക്രിപ്ഷൻ നടക്കുന്നത് നിങ്ങളുടെ ബ്രൗസറിൽ, ഞങ്ങൾ നിങ്ങൾക്ക് നൽകുന്ന കോഡിലാണ്. അത് മുൻപ്
ഒരു വാഗ്ദാനം ആയിരുന്നു; ഇപ്പോൾ അത് നിങ്ങൾക്ക് പരിശോധിക്കാവുന്ന ഒന്നാണ്. നിങ്ങളുടെ കീ സ്പർശിക്കുന്ന ഓരോ വരിയും
ഒരു വായിക്കാവുന്ന ഫയലിലാണ് ഉള്ളത്, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
ഇത് wheel ന് അകത്ത് ഷിപ്പ് ചെയ്യുകയും, അതേപടി സെർവ് ചെയ്യപ്പെടുകയും, ഒരു Subresource
Integrity ഹാഷ് ഉപയോഗിച്ച് പിൻ ചെയ്യപ്പെടുകയും ചെയ്യുന്നു. ബ്രൗസർ ഞങ്ങൾ പ്രസിദ്ധീകരിച്ചത് തന്നെ പ്രവർത്തിപ്പിക്കുന്നു എന്ന് സ്ഥിരീകരിക്കാൻ:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

അത് തെളിയിക്കാത്തത്: ഫയൽ ലോഡ് ചെയ്യുന്ന പേജ് ഞങ്ങൾ സെർവ് ചെയ്യുന്നു, അതിനാൽ ഞങ്ങൾക്ക് വേറൊരു പേജ്
സെർവ് ചെയ്യാൻ കഴിയും. Integrity ഹാഷുകൾ ഒരു കോംപ്രമൈസ് ചെയ്ത CDN ൽ നിന്ന് നിങ്ങളെ സംരക്ഷിക്കുന്നു,
വെണ്ടറിൽ നിന്നല്ല. നിങ്ങൾക്ക് ലഭിക്കുന്നത് ഏതൊരു പകരംവയ്ക്കലും ബോധപൂർവമായതും, പേജ് സോഴ്സിൽ ദൃശ്യമായതും,
ആർക്കും ഫെച്ച് ചെയ്യാൻ കഴിയുന്ന PyPI യിലെ ഒരു ആർട്ടിഫാക്ടിൽ നിന്ന് വ്യത്യസ്തവുമായിരിക്കണം എന്നതാണ്. സ്വയം-ഹോസ്റ്റ് ചെയ്യുന്നതോ ലോക്കൽ മാത്രം ആയി തുടരുന്നതോ ഈ ആശ്രയത്വം പൂർണ്ണമായും നീക്കം ചെയ്യുന്നു.

## ഇൻസ്റ്റാൾ

```bash
pip install clawmetry     # then: clawmetry
```

അല്ലെങ്കിൽ ഒറ്റ-ലൈൻ: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS, Linux അല്ലെങ്കിൽ Windows ൽ Python 3.8+ ഉം, അതേ മെഷീനിൽ കുറഞ്ഞത് ഒരു ഏജന്റ്
റൺടൈമും ആവശ്യമാണ്. Docker നിർദ്ദേശങ്ങൾ: [docs/DOCKER.md](docs/DOCKER.md).

അല്ലെങ്കിൽ ഇത് നിങ്ങൾക്കുവേണ്ടി സെറ്റപ്പ് ചെയ്യാൻ ഏജന്റിനെ അനുവദിക്കുക. [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
സ്കിൽ Claude Code, Codex, Cursor, Gemini CLI, Copilot അല്ലെങ്കിൽ OpenCode എന്നിവയെ
ClawMetry ഇൻസ്റ്റാൾ ചെയ്യാനും, മെഷീനിലെ ഏജന്റുകൾ എന്ത് ചെയ്യുന്നു, എന്ത് ചെലവാക്കുന്നു എന്ന് റിപ്പോർട്ട് ചെയ്യാനും,
ആവശ്യപ്പെട്ടാൽ ഒരു സെഷൻ നിർത്താനും, അപകടസാധ്യതയുള്ള ടൂൾ കോളുകൾ അംഗീകാരത്തിനായി പിടിച്ചുവയ്ക്കാനും പഠിപ്പിക്കുന്നു:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## ഡോക്യുമെന്റേഷൻ

| | |
|---|---|
| [റൺടൈം കോമ്പാറ്റിബിലിറ്റി](docs/compatibility.md) | ഓരോ അഡാപ്റ്ററും എന്ത് വായിക്കുന്നു, ഒരു റൺടൈം എങ്ങനെ ചേർക്കാം |
| [കോൺടെക്സ്റ്റ് ബ്ലോഔട്ട്](docs/CONTEXT_BLOWOUT.md) | ഓരോ പ്രൊവൈഡറിനുമുള്ള വിൻഡോകൾ, കോംപാക്ഷൻ vs ഓവർഫ്ലോ, ഓരോ റൺടൈം കവറേജും |
| [ഓവർഹെഡ്](docs/OVERHEAD.md) | ഇൻസ്ട്രുമെന്റേഷന്റെ ചെലവ്, അളന്നത്, പുനർനിർമ്മിക്കാനുള്ള ഹാർനെസ്സോടൊപ്പം |
| [Entitlements](docs/ENTITLEMENTS.md) | Free vs paid, ടയർ മാട്രിക്സ്, ലൈസൻസ് CLI |
| [അപ്രൂവലുകളും പോളിസികളും](docs/APPROVALS.md) | പ്രീ-എക്സിക്യൂഷൻ ഗേറ്റിംഗ്, റിസ്ക് സ്കോറിംഗ്, ഫോൺ അപ്രൂവലുകൾ |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | ട്രെയ്സുകൾ എവിടെയും export ചെയ്യുക, എന്തിൽ നിന്നും OTLP ingest ചെയ്യുക |
| [നിങ്ങളുടെ സ്വന്തം ഏജന്റ് കൊണ്ടുവരൂ](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain എൻഡ് ടു എൻഡ്, പ്രവർത്തിപ്പിക്കാവുന്ന ഉദാഹരണങ്ങളോടൊപ്പം |
| [SDK ട്രാക്കിംഗ്](docs/SDK_TRACKING.md) | നിങ്ങൾ സ്വയം നിർമ്മിച്ച ഏജന്റുകൾക്കുള്ള ചെലവ് ആട്രിബ്യൂഷൻ |
| [ചാറ്റ് ചാനലുകൾ](docs/CHANNELS.md) | ഫ്ലോയിൽ കാണിക്കുന്ന ചാറ്റ് അഡാപ്റ്ററുകൾ |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | സാൻഡ്ബോക്സ് ചെയ്ത NVIDIA NemoClaw സെറ്റപ്പുകൾ |
| [Docker](docs/DOCKER.md) | ഇമേജ്, കമ്പോസ്, വോളിയം മൗണ്ടുകൾ |
| [ആർക്കിടെക്ചർ](ARCHITECTURE.md) · [ഡെവലപ്മെന്റ്](docs/DEVELOPMENT.md) | ഇത് ഉള്ളിൽ എങ്ങനെ പ്രവർത്തിക്കുന്നു; സോഴ്സിൽ നിന്ന് പ്രവർത്തിപ്പിക്കൽ |
| [ടെലിമെട്രി](docs/TELEMETRY.md) | അജ്ഞാതമായ ഇൻസ്റ്റാളും ഡെസ്ക്ടോപ്പ്-ഓപ്പൺ പിംഗുകളും, അവ എങ്ങനെ ഓഫ് ചെയ്യാം |

## സ്ക്രീൻഷോട്ടുകൾ

താഴെയുള്ള ഓരോ സംഖ്യയും ഒരു യഥാർത്ഥ മെഷീനിൽ നിന്നുള്ളതാണ്, റീഡ്-ഒൺലി, ഒന്നും സീഡ് ചെയ്യാതെ.

**എന്തെങ്കിലും തെറ്റ് സംഭവിക്കുമ്പോൾ ഇത് നിങ്ങളോട് പറയുന്നു, എന്താണ് സംഭവിച്ചത് എന്ന് മാത്രമല്ല.**
മുകളിൽ രണ്ട് അസാധാരണത്വ ബാനറുകൾ: ചെലവ് ദൈനംദിന ശരാശരിയുടെ 7 മടങ്ങ് ഓടുന്നു, കൂടാതെ
4.2 മടങ്ങ് ചെലവ് കുതിപ്പ്. അവയ്ക്ക് താഴെ, ഏറ്റവും അടുത്ത 667 സെഷനുകളിൽ 324 എണ്ണം
ഒരു പാഴ് സിഗ്നൽ വഹിക്കുന്നു, കാരണം അനുസരിച്ച് ഇനംതിരിച്ച്.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**പണം എവിടെ പോയി എന്ന് ഇത് നിങ്ങൾക്ക് കാണിക്കുന്നു, ഓരോ വിൻഡോയിലും.**
ഇന്ന് $252.47, ഈ ആഴ്ച $513.15, ഈ മാസം $1,312.92, ഓരോന്നിനും പിന്നിലെ ടോക്കണുകളോടും
നിങ്ങളുടെ സബ്സ്ക്രിപ്ഷൻ ഇതിനകം എത്ര കവർ ചെയ്യുന്നു എന്നതോടും കൂടി. അതിന് താഴെ, ഏകദേശം
$1,128/മാസം വീണ്ടെടുക്കാവുന്നതായി ഇനംതിരിച്ചതും, ക്യാഷ് പുനരുപയോഗം വഴി $17,256/മാസം
ഇതിനകം ലാഭിച്ചതും.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**ഒരു സന്ദേശം എങ്ങനെ ഒരു ഉത്തരമായി മാറുന്നു എന്ന് ഇത് വരയ്ക്കുന്നു.**
ലൈവ് ഫ്ലോ ഡയഗ്രം: നിങ്ങൾ, അത് വന്ന ചാനൽ, ഗേറ്റ്‌വേ, ഇപ്പോൾ ഉത്തരം നൽകുന്ന മോഡൽ, അത്
ഉപയോഗിച്ച ഓരോ ടൂളും. ജോലി അവയിലൂടെ നീങ്ങുമ്പോൾ നോഡുകൾ പ്രകാശിക്കുന്നു.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**മെഷീനിലെ ഓരോ ഏജന്റും, ഒരൊറ്റ ടേബിളിൽ.**
അത് എന്ത് പ്രവർത്തിപ്പിക്കുന്നു, കഴിഞ്ഞ 24 മണിക്കൂറിലും അതിന്റെ ജീവിതകാലത്തും അതിന് എന്ത് ചെലവാകുന്നു,
ഒടുവിൽ എപ്പോൾ കണ്ടു, ആരാണ് ഉടമ, ഒരു സബ്സ്ക്രിപ്ഷൻ ബില്ല് കവർ ചെയ്യുന്നുണ്ടോ. ഇവിടെ 14 ഏജന്റുകൾ,
3 സെഷനുകൾ പ്രവർത്തിക്കുന്നു, 13 നിശബ്ദം.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**ഒരു ടേണിന്റെ സമയവും പണവും എവിടെ പോയി എന്ന്, ടൂൾ ബൈ ടൂൾ, ഇത് കാണിക്കുന്നു.**
ഒരു യഥാർത്ഥ സെഷന്റെ ഒരു ടേൺ: 11.2 മിനിറ്റിൽ 11 ടൂളുകൾ $1.16 ന്. ഓരോ Bash
കോളിനും മോഡൽ കോളിനും ടൈംലൈനിൽ അതിന്റേതായ ബാർ ലഭിക്കുന്നു, അതിനാൽ 4.1 മിനിറ്റ്
പ്രവർത്തിച്ച കമാൻഡും 226ms പ്രവർത്തിച്ചതും ഒറ്റ നോട്ടത്തിൽ വേർതിരിച്ചറിയാം.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**ഇത് ജോലിയെ ഗ്രേഡ് ചെയ്യുന്നു, ചെലവ് മാത്രമല്ല.**
ഈ ആഴ്ച ഒരു A: 54 ടാസ്കുകൾ വൃത്തിയായി തിരികെ വന്നു, 2 പരുക്കൻ ഇവ $48.57 ചെലവായി,
വിലയിരുത്താൻ പര്യാപ്തമല്ലാത്ത പ്രവർത്തനം ഉള്ള റണ്ണുകൾ വിജയങ്ങളായി കണക്കാക്കുന്നതിന് പകരം
ഗ്രേഡിൽ നിന്ന് ഒഴിവാക്കിയിരിക്കുന്നു. ഓരോ പരുക്കൻ റണ്ണും അതിന്റെ ട്രെയ്സിലേക്ക് ലിങ്ക് ചെയ്യുന്നു.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**കോൺടെക്സ്റ്റ് വിൻഡോ എന്തുകൊണ്ട് നിറഞ്ഞുകൊണ്ടിരിക്കുന്നു എന്ന് ഇത് കാണിക്കുന്നു.**
ഏറ്റവും പുതിയ ടേണിൽ 1M-ടോക്കൺ വിൻഡോയിൽ 715K, 83.3% പീക്ക്, ഓവർഫ്ലോയിൽ അല്ല, മുൻകൂട്ടി
തന്നെ ട്രിഗർ ചെയ്ത 4 കോംപാക്ഷനുകൾ, കൂടാതെ അതിന് പിന്നിലെ ഓരോ ടേണിന്റെയും യൂട്ടിലൈസേഷൻ.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**നിങ്ങൾ ഒന്നും കോൺഫിഗർ ചെയ്യാതെ തന്നെ കണ്ടെത്തൽ പ്രവർത്തിക്കുന്നു.**
ഇൻസ്റ്റാൾ ചെയ്ത ഉടൻ ബിൽറ്റ്-ഇൻ ഡിറ്റക്ടറുകൾ ഓണാണ്: ഏജന്റ് നിശബ്ദമായി, ടെലിമെട്രി ഫീഡ്
നിലച്ചു, ചെലവ് കുതിപ്പ്, ടോക്കൺ കുതിപ്പ്, പിഴവുകൾ കയറുന്നു, പിഴവ് കുതിപ്പ്, ബജറ്റ്
ത്രെഷോൾഡ്, ഭീഷണി സിഗ്നേച്ചർ പൊരുത്തപ്പെട്ടു, സുരക്ഷാ ടൂൾ കണ്ടെത്തൽ, സുരക്ഷാ പൊസ്ചർ
മാറി. നിങ്ങളുടെ സ്വന്തം നിയമങ്ങൾ ഇതിന് മുകളിൽ ഓപ്ഷണലാണ്.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**അപകടസാധ്യതയുള്ള ഒരു കോൾ പിടിച്ചുനിർത്തുന്നത് ഓപ്റ്റ്-ഇൻ ആണ്, ഓഫായി തന്നെ ഷിപ്പ് ചെയ്യുന്നു.**
റിക്കേഴ്സീവ് ഡിലീറ്റുകൾ, ഫോഴ്സ് പുഷുകൾ, sudo, രഹസ്യങ്ങൾ, പാക്കേജ് ഇൻസ്റ്റാളുകൾ, ഔട്ട്ബൗണ്ട്
കോളുകൾ എന്നിവയ്ക്ക് ഓരോന്നിനും നിങ്ങൾക്ക് ഓൺ ചെയ്യാവുന്ന ഒരു നിയമം ലഭിക്കുന്നു. നിങ്ങൾ അത് ചെയ്യുന്നത് വരെ,
ClawMetry നിരീക്ഷിക്കുകയും ഒന്നും മാറ്റാതിരിക്കുകയും ചെയ്യുന്നു. ഒന്ന് ഓൺ ആയാൽ, പൊരുത്തപ്പെടുന്ന കോളുകൾ
ഇവിടെ (അല്ലെങ്കിൽ നിങ്ങളുടെ ഫോണിൽ) അംഗീകാരത്തിനോ നിരസിക്കലിനോ കാത്തിരിക്കുന്നു.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

കൂടുതൽ, ഓരോ റൺടൈമിനും: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## അംഗീകാരം

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Star History

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## ലൈസൻസ്

MIT · നിർമ്മിച്ചത് [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
