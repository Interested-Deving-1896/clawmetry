<!-- i18n-src:b22579578775 -->
> Filipino translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**Kayang gumawa ng isang ahente ng isandaang tool call nang walang anumang pag-unlad.** Binabasa ng ClawMetry
ang mga session file na isinusulat na ng iyong mga coding agent, at inilalagay ang timeline,
ang mga tool call, at anumang datos ng token at gastos na inilalantad ng runtime sa iisang
view — para makilala mo ang isang mahabang run na gumagana laban sa isang natigil na.

Gumagana sa **32 AI agent runtime** — Claude Code, OpenAI Codex, Hermes, OpenClaw at 28 pa. Isang dashboard para sa buong fleet ng iyong ahente. ([ang buong listahan](SUPPORTED_RUNTIMES.txt), na nabubuo mula sa katalogo.)

> 🌐 **Basahin ito sa:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [higit pa →](docs/i18n/)

Isang command. Walang configuration. Awtomatikong nadedetect ang lahat.

```bash
pip install clawmetry && clawmetry
```

Nagbubukas sa **http://localhost:8900**. Walang configuration: hinahanap nito ang mga agent runtime na
mayroon ka na, binabasa ang mga ito nang read-only, at walang binabago sa kung paano sila tumatakbo.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## Bago ka mag-install

| | |
|---|---|
| **Ano ang ginagawa nito** | Binabasa ang mga session file at log na isinusulat na ng iyong mga ahente. Walang SDK, walang pagbabago sa code, walang instrumentation sa iyong app. |
| **Ano ang makikita mo** | Session timeline, tool-by-tool na replay, breakdown ng token at gastos, at mga trajectory signal (looping, paulit-ulit na kabiguan) — bawat runtime. |
| **Ano ang libre** | Binabasa ng `pip install clawmetry` ang **OpenClaw, NVIDIA NemoClaw, Goose at Qwen Code** nang walang account, walang key, at walang network call. Ang iba pang 28 — Claude Code, Codex, Cursor at ang mga natitira — ay binabasa ng closed-source na kasamang `clawmetry-pro`, na dumarating kasama ang 7-araw na trial o isang plano — tingnan ang [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) para sa eksaktong hatian. |
| **Paano magsimula** | `pip install clawmetry && clawmetry`, pagkatapos buksan ang localhost:8900. Wala pang ahente sa makinang ito? Ang `clawmetry --sample` ay nagbubukas sa tatlong may-etiketang synthetic na session. |
| **Ano ang umaalis sa iyong makina** | Walang datos ng session, maliban kung patakbuhin mo ang `clawmetry connect`. May dalawang bagay na tumatakbo bilang default, kapwa opt-out at wala sa mga ito ang may laman ng session: isang anonymous na install ping at isang PyPI version check. Bawat destinasyon ay nakalista sa [docs/EGRESS.md](docs/EGRESS.md), na muling itinayo mula sa isang wire capture sa halip na mula sa pagbabasa ng mga komento. |

May dalawang limitasyong dapat malaman bago mo husgahan ang resulta: naglalantad ang mga runtime ng
ibang-ibang datos (may ilan na walang inilalantad na gastos — [ang matrix](docs/compatibility.md)
ang nagsasabi kung alin, bawat runtime), at ang pagmamasid sa isang aksyon ay hindi pareho sa kakayahang
harangin ito ([alin sa mga kontrol ang totoo, bawat runtime](docs/APPROVALS.md)).


## Gumagana sa 32 agent runtime

**Libre sa open source app:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**Sa bayad na plano:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

Bawat runtime ay nakakakuha ng parehong dashboard. Magpatakbo ng ilan nang sabay-sabay at ang
header switcher ay muling nagsi-scope ng bawat tab sa isa sa kanila.

Gumawa ka ba ng sarili mong ahente gamit ang isang SDK sa halip? Tina-track din ng interceptor ang
mga LLM call nito. Tingnan ang [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## Ano ang makukuha mo

- **Mga Session at transcript**: kung ano ang ginawa ng bawat ahente, turno kada turno, na may replay
- **Gastos at Token**: bawat runtime, modelo, session at araw, na may mga anomaly flag
- **Flow**: live na diagram ng mga mensaheng gumagalaw sa mga channel, modelo, at tool
- **Brain**: ang reasoning at tool-call event stream habang ito ay nangyayari
- **Context blowout**: window utilization na sinusukat bawat provider, compaction laban sa pinilit na overflow, kasama ang per-runtime na mapa kung ano ang *hindi* namin makita ([paano](docs/CONTEXT_BLOWOUT.md))
- **Memory at skills**: ang mga file at skill na aktwal na na-load ng bawat runtime
- **Kalusugan at Logs**: disk, memory, error rate, rate limit, live log stream
- **Alerts**: mga limitasyon ng budget, pagtaas ng error, agent-offline, na iruruta sa Slack, Discord, PagerDuty, Telegram, Email
- **Approvals**: i-pause ang mapanganib na tool call *bago* ito tumakbo at aprubahan mula sa iyong telepono ([paano](docs/APPROVALS.md))

## Context blowout, at ang gastos ng pagmamasid

Dalawang tanong na sulit sasagutin bago ka magtiwala sa anumang tool na naghahambing ng ahente.

**Paano nito hinahawakan ang context-window blowout sa iba't ibang runtime?**

Ang isang utilization percentage ay kasing-tapat lamang ng hinahatian nito. Sinusukat ng ClawMetry
ang window bawat provider mula sa [isang table na mababasa at
maaaring i-PR](clawmetry/context_windows.py), na sumasaklaw sa Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama at GLM. Hindi nito sinusukat ang lahat ng 32
runtime gamit ang panukat ng isang vendor. Mahalaga iyon: isang 300K GPT-5 turn na sinukat
laban sa 200K ng Anthropic ay nababasa bilang ">100%, blown" gayong ito ay talagang nasa 75% ng
400K ng GPT-5. Ang parehong panukat ang nagtatago ng isang tunay na na-overflow na 130K DeepSeek turn
bilang isang komportableng 65%.

Bawat window ay dala ang pinagmulan nito: `model_table`, `explicit_marker`,
`observed_floor`, o isang tapat na `default` kapag hindi namin alam ang modelo. Ang isang gauge na
binuo sa isang hula ay hindi kailanman iri-render na may parehong awtoridad ng isang binuo sa
isang lookup.

Makikita lamang ng ClawMetry ang mga compaction event sa ilang runtime. Kaya iniuulat ng
`GET /api/context-coverage`, bawat runtime, kung ang **zero ay nangangahulugang "tumakbong malinis"
o "bulag kami."** Ang isang `0` na aktwal na nangangahulugang bulag ay sinasabi iyon.
[Buong detalye](docs/CONTEXT_BLOWOUT.md)

**Magkano ang gastos ng instrumentation?**

| Landas | Idinagdag sa iyong ahente | Default? |
|---|---|---|
| Session-file tailing (lahat ng 32 runtime) | **0**. Hiwalay na proseso, walang code ng ClawMetry sa iyong ahente | on |
| HTTP interceptor (`CLAWMETRY_INTERCEPT=1`) | **+0.44 ms** bawat LLM call, o 0.009% ng 5s na call | off |
| Pre-tool hook gate (warm cache) | **+44 ms** bawat gated tool call, higit sa 36 ms na interpreter floor | off |
| Enforcement proxy | **+9.7 ms** bawat LLM call | off |

Gastos sa host ng daemon: **2,762 event/sec** na ingest, **710 byte/event** sa disk
(67.7 MB bawat 100k na event), at **~12% ng isang core** na sustenido sa isang abalang
install. Ang huling bilang na iyon ay lampas sa aming sariling nakasaad na 5-10% na badyet, kaya ito ay
inilathala bilang isang bug na hahabulin sa halip na iwan sa labas ng pahina.

Sinukat sa isang Apple M2 Pro gamit ang `benchmarks/overhead.py`. Pinapatakbo ng harness
ang bawat kondisyon sa hiwalay na proseso, pinagpapalit-palit ang pagkakasunod-sunod ng mga ito, at
**tumatanggi na mag-print ng bilang kapag hindi nagkakasundo ang mga round sa sign nito**. Patakbuhin ito sa iyong
sariling makina sa loob ng isang minuto:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

Bawat landas ay sinusukat, kasama na ang mga hook gate at ang enforcement proxy,
at ang harness ay tumatakbo sa Linux, macOS at Windows sa CI. May dalawang resultang sulit
malaman: mas mahal ang proxy ng humigit-kumulang pitong ulit sa Windows kaysa sa Linux, at
ang daemon sa kasalukuyan ay sustenido ang humigit-kumulang 12% ng isang core, higit sa aming sariling
5-10% na badyet. Ang hilaw na JSON, ang metodo, at kung ano pa ang hindi pa nasusukat ay nasa
[docs/OVERHEAD.md](docs/OVERHEAD.md).

## Pagpepresyo

| Plano | Ano ang saklaw nito | Presyo |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, buong dashboard, lokal lamang | $0 |
| **Starter** | Bawat ibang runtime sa itaas, fleet view, cloud sync | $9 bawat node / buwan |
| **Pro** | Starter + kontrol at ebalwasyon: approvals, mga patakaran sa panganib ng tool, evals, anomaly detection, cost optimizer, OTel export, tamper-evident audit log | $19 bawat node / buwan |

Ang mga taunang plano, Enterprise at ang kasalukuyang mga numero ay matatagpuan sa
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**. Gumagana ang mga self-hosted license
key nang walang cloud (`clawmetry license`). Ang eksaktong hatian ng free/bayad ay nasa
[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md).

## Nananatili sa iyong makina ang iyong datos

Binabasa ng ClawMetry ang mga lokal na session file at log. **Walang datos ng session na umaalis sa iyong
makina maliban kung patakbuhin mo ang `clawmetry connect`** — walang prompt, tugon, tool argument, laman ng
file, o linya ng log. Kapag kumonekta ka, ang snapshot ay end-to-end na naka-encrypt
gamit ang isang key na hindi kailanman umaalis sa iyong makina, at naka-decrypt sa iyong browser. Kung
walang key ang isang node, nilalaktawan ang upload sa halip na ipadala nang bukas, at walang
tugon ng server ang makakapagpatay niyan.

May dalawang bagay na tumatakbo bilang default bago ka kumonekta, kapwa opt-out at wala sa mga ito ang may
laman ng datos ng session: isang anonymous na install ping at isang version check laban sa
PyPI. Ang isang default na install ay minsan ding tumitingin sa iyong pampublikong IP para sa isang startup banner
line. Bawat destinasyon, ang laman nito at kung paano ito papatayin ay nakalista sa
[docs/EGRESS.md](docs/EGRESS.md); ang mga self-hosted, repointed at air-gapped na install
ay walang ginagawang discretionary na outbound call.

Ang decryption ay nangyayari sa iyong browser, sa code na ipinapadala namin sa iyo. Dati itong isang
pangako; ngayon ay isang bagay na mave-verify mo. Bawat linyang humipo sa iyong key ay
nasa isang mababasang file, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
na sinasama sa loob ng wheel at ipinapadala nang buo, na naka-pin gamit ang isang Subresource
Integrity hash. Para kumpirmahin na pinapatakbo ng browser kung ano ang aming inilathala:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

Ang hindi napapatunayan nito: kami ang nagpapadala ng pahinang naglo-load ng file, kaya maaari kaming
magpadala ng ibang pahina. Ang mga integrity hash ay nagpoprotekta sa iyo mula sa isang nakompromisong
CDN, hindi mula sa vendor. Ang nakukuha mo ay ang anumang pagpapalit ay dapat sadya,
nakikita sa page source, at iba sa isang artifact sa PyPI na kahit sino ay maaaring kunin.
Ang pag-self-host o pananatiling lokal lamang ang siyang ganap na nag-aalis sa dependency.

## Pag-install

```bash
pip install clawmetry     # pagkatapos: clawmetry
```

O ang one-liner: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

Kailangan ng Python 3.8+ sa macOS, Linux o Windows, at kahit isang agent runtime sa
parehong makina. Mga tagubilin sa Docker: [docs/DOCKER.md](docs/DOCKER.md).

O hayaan ang ahente na i-set up ito para sa iyo. Ang [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
skill ay tinuturuan ang Claude Code, Codex, Cursor, Gemini CLI, Copilot o OpenCode na
i-install ang ClawMetry, iulat kung ano ang ginagawa at ginagastos ng mga ahente sa makina,
ihinto ang isang session kapag hiniling, at pigilan ang mapanganib na tool call para sa pag-apruba:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Dokumentasyon

| | |
|---|---|
| [Runtime compatibility](docs/compatibility.md) | Kung ano ang binabasa ng bawat adapter, at kung paano magdagdag ng runtime |
| [Context blowout](docs/CONTEXT_BLOWOUT.md) | Mga window bawat provider, compaction laban sa overflow, per-runtime na coverage |
| [Overhead](docs/OVERHEAD.md) | Ano ang gastos ng instrumentation, sinukat, kasama ang harness para i-reproduce ito |
| [Entitlements](docs/ENTITLEMENTS.md) | Libre laban sa bayad, tier matrix, license CLI |
| [Approvals & policies](docs/APPROVALS.md) | Pre-execution gating, risk scoring, mga approval sa telepono |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | I-export ang mga trace kahit saan, i-ingest ang OTLP mula sa kahit ano |
| [Bring your own agent](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain simula hanggang katapusan, na may mga tatakbong halimbawa |
| [SDK tracking](docs/SDK_TRACKING.md) | Attribution ng gastos para sa mga ahenteng sarili mong ginawa |
| [Chat channels](docs/CHANNELS.md) | Ang mga chat adapter na ipinapakita sa Flow |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | Mga sandboxed na setup ng NVIDIA NemoClaw |
| [Docker](docs/DOCKER.md) | Image, compose, volume mount |
| [Architecture](ARCHITECTURE.md) · [Development](docs/DEVELOPMENT.md) | Paano ito gumagana sa loob; pagpapatakbo mula sa source |
| [Telemetry](docs/TELEMETRY.md) | Ang anonymous na install at desktop-open na ping, at kung paano papatayin ang mga ito |

## Mga Screenshot

Bawat numero sa ibaba ay mula sa isang tunay na makina, read-only, na walang anumang seeded.

**Sinasabihan ka nito kapag may mali, hindi lang kung ano ang nangyari.**
Dalawang anomaly banner sa itaas: gastos na tumatakbo nang 7x ang araw-araw na average, at isang
4.2x na cost spike. Sa ibaba nila, 324 sa 667 na kamakailang session ang may dalang waste
signal, na inisa-isa ayon sa dahilan.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**Ipinapakita nito kung saan napunta ang pera, sa bawat window.**
$252.47 ngayon, $513.15 ngayong linggo, $1,312.92 ngayong buwan, bawat isa ay may kasamang
mga token sa likod nito at kung gaano na ito nasasaklaw ng iyong subscription. Sa ibaba niyan, mga
$1,128/buwan na na-itemize bilang mababawi at $17,256/buwan na naligtas na ng
cache reuse.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**Iginuhit nito kung paano nagiging sagot ang isang mensahe.**
Ang live na flow diagram: ikaw, ang channel kung saan ito dumating, ang gateway, ang modelong
sumasagot sa ngayon, at bawat tool na ginamit nito. Nagliliwanag ang mga node habang gumagalaw
ang trabaho sa kanila.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**Bawat ahente sa makina, sa isang table.**
Ano ang tumatakbo nito, magkano ang gastos nito sa nakaraang 24 oras at sa buong buhay nito, kailan
ito huling nakita, sino ang may-ari, at kung may sumasaklaw na subscription sa bill. 14 na
ahente dito, 3 session na gumagana, 13 tahimik.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**Ipinapakita nito kung saan napunta ang oras at pera ng isang turn, tool bawat tool.**
Isang turn ng isang tunay na session: 11 tool sa loob ng 11.2 minuto para sa $1.16. Bawat Bash
call at model call ay may sariling bar sa timeline, kaya ang command na tumakbo nang 4.1 minuto
at ang isang tumakbo nang 226ms ay nakikilala sa isang tingin.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**Ginagrado nito ang trabaho, hindi lang ang gastos.**
Isang A ngayong linggo: 54 na gawain ang bumalik na malinis, 2 magaspang na gumastos ng $48.57, at
ang mga run na may masyadong kakaunting aktibidad para husgahan ay hindi isinama sa grado sa halip
na bilangin bilang panalo. Bawat magaspang na run ay naka-link sa sarili nitong trace.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**Ipinapakita nito kung bakit patuloy na napupuno ang context window.**
715K sa 1M-token na window sa pinakahuling turn, isang 83.3% na peak, 4 na compaction na
lahat ay nag-trigger nang proactive sa halip na sa overflow, at ang utilization ng
bawat turn sa likod nito.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**Tumatakbo ang detection nang walang anumang i-configure mo.**
Naka-on mula sa install ang mga built-in na detector: tumahimik ang ahente, huminto ang telemetry
feed, cost spike, token burst, pataas na error, error spike, threshold ng budget, tugmang
threat signature, natuklasang security tool, nagbagong security posture. Opsyonal ang
sarili mong mga patakaran sa ibabaw nito.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**Opt-in ang pagpigil sa isang mapanganib na call, at ship-off.**
Ang mga recursive delete, force push, sudo, secrets, pag-install ng package at outbound
call ay bawat isa ay may patakarang pwede mong i-on. Hanggang gawin mo iyon, pinagmamasdan
lang ng ClawMetry at walang binabago. Kapag naka-on na ang isa, naghihintay dito ang mga
tugmang call (o sa iyong telepono) para sa isang apruba o tanggihan.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

Higit pa, bawat runtime: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## Pagkilala

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Kasaysayan ng Star

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## Lisensya

MIT · Ginawa ni [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
