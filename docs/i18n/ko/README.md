<!-- i18n-src:b22579578775 -->
> 한국어 translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**에이전트는 진전 없이도 수백 번의 도구 호출을 할 수 있습니다.** ClawMetry는
코딩 에이전트가 이미 작성하고 있는 세션 파일을 읽어서, 타임라인과
도구 호출, 그리고 런타임이 제공하는 토큰 및 비용 데이터를 하나의
화면에 모아줍니다. 그래서 잘 진행되고 있는 긴 실행과 멈춰버린 실행을
구분할 수 있습니다.

**32개의 AI 에이전트 런타임**과 함께 작동합니다 — Claude Code, OpenAI Codex, Hermes, OpenClaw 외 28개. 여러분의 전체 에이전트 플릿을 위한 하나의 대시보드. ([전체 목록](SUPPORTED_RUNTIMES.txt)은 카탈로그에서 생성됩니다.)

> 🌐 **다른 언어로 읽기:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [더 보기 →](docs/i18n/)

명령어 하나. 설정은 필요 없습니다. 모든 것을 자동으로 감지합니다.

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** 에서 열립니다. 설정 불필요: 여러분이 이미 가지고 있는
에이전트 런타임을 찾아서, 읽기 전용으로 읽고, 그것들이 실행되는 방식은
전혀 바꾸지 않습니다.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## 설치하기 전에

| | |
|---|---|
| **하는 일** | 여러분의 에이전트가 이미 작성하고 있는 세션 파일과 로그를 읽습니다. SDK도, 코드 변경도, 앱에 계측 코드를 넣을 필요도 없습니다. |
| **볼 수 있는 것** | 세션 타임라인, 도구별 리플레이, 토큰 및 비용 분석, 그리고 궤적 신호(반복, 반복되는 실패) — 런타임별로 제공됩니다. |
| **무료 범위** | `pip install clawmetry`는 **OpenClaw, NVIDIA NemoClaw, Goose, Qwen Code**를 계정, 키, 네트워크 호출 없이 읽습니다. 나머지 28개 — Claude Code, Codex, Cursor 등 — 는 클로즈드소스 `clawmetry-pro` 컴패니언이 읽으며, 이는 7일 체험판 또는 요금제와 함께 제공됩니다 — 정확한 구분은 [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)를 참고하세요. |
| **시작하는 법** | `pip install clawmetry && clawmetry`를 실행한 뒤 localhost:8900을 엽니다. 이 머신에 아직 에이전트가 없나요? `clawmetry --sample`은 라벨이 붙은 세 개의 합성 세션으로 열립니다. |
| **머신 밖으로 나가는 것** | `clawmetry connect`를 실행하지 않는 한 세션 데이터는 나가지 않습니다. 기본적으로 실행되는 것은 두 가지뿐이며, 둘 다 옵트아웃 가능하고 세션 내용을 담지 않습니다: 익명 설치 핑과 PyPI 버전 확인입니다. 모든 목적지는 주석이 아니라 실제 와이어 캡처로 재구성되어 [docs/EGRESS.md](docs/EGRESS.md)에 정리되어 있습니다. |

결과를 판단하기 전에 알아둘 만한 두 가지 한계가 있습니다: 런타임마다
노출하는 데이터가 매우 다르고(일부는 비용을 전혀 게시하지 않습니다 —
[매트릭스](docs/compatibility.md)가 런타임별로 어떤지 알려줍니다),
동작을 관찰하는 것과 그것을 차단할 수 있는 것은 서로 다른 문제입니다
([런타임별로 어떤 컨트롤이 실제로 동작하는지](docs/APPROVALS.md)).


## 32개 에이전트 런타임과 함께 작동합니다

**오픈소스 앱에서 무료:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**유료 요금제에서:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

모든 런타임은 동일한 대시보드를 제공받습니다. 여러 개를 동시에
실행하면 헤더의 전환기가 모든 탭의 범위를 그중 하나로 다시 맞춰줍니다.

SDK로 자체 에이전트를 만드셨나요? 인터셉터가 그 LLM 호출도 함께
추적합니다. [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)를 참고하세요.

## 제공되는 기능

- **세션 및 트랜스크립트**: 각 에이전트가 턴별로 무엇을 했는지, 리플레이와 함께
- **비용 및 토큰**: 런타임, 모델, 세션, 일자별로, 이상 징후 표시와 함께
- **Flow**: 채널, 모델, 도구를 오가는 메시지의 실시간 다이어그램
- **Brain**: 추론과 도구 호출 이벤트 스트림을 실시간으로
- **컨텍스트 블로우아웃**: 프로바이더별로 산정된 윈도우 활용률, 압축 대 강제 오버플로, 그리고 우리가 *볼 수 없는* 부분에 대한 런타임별 지도 ([방법](docs/CONTEXT_BLOWOUT.md))
- **메모리 및 스킬**: 각 런타임이 실제로 로드한 파일과 스킬
- **상태 및 로그**: 디스크, 메모리, 에러율, 레이트 리밋, 실시간 로그 스트림
- **알림**: 예산 한도, 에러 급증, 에이전트 오프라인, Slack, Discord, PagerDuty, Telegram, 이메일로 라우팅
- **승인**: 위험한 도구 호출을 실행 *전에* 일시 정지하고 휴대폰으로 승인 ([방법](docs/APPROVALS.md))

## 컨텍스트 블로우아웃, 그리고 관찰 비용

어떤 에이전트 비교 도구든 신뢰하기 전에 답해볼 만한 두 가지 질문이 있습니다.

**런타임 간 컨텍스트 윈도우 블로우아웃을 어떻게 처리하나요?**

활용률 백분율은 그 분모가 정직한 만큼만 정직합니다. ClawMetry는
[읽고 PR할 수 있는 테이블](clawmetry/context_windows.py)을 기반으로
프로바이더별로 윈도우 크기를 산정하며, Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama, GLM을 포괄합니다. 32개 런타임 전부를
한 벤더의 자로 측정하지 않습니다. 이는 중요한 차이를 만듭니다: 300K
토큰짜리 GPT-5 턴을 Anthropic의 200K 기준으로 채점하면 "100% 초과, 터짐"으로
읽히지만, 실제로는 GPT-5의 400K 중 75%에 불과합니다. 같은 자로는 실제로
오버플로된 130K DeepSeek 턴이 편안한 65%로 숨겨집니다.

모든 윈도우는 `model_table`, `explicit_marker`, `observed_floor`, 또는
모델을 모를 때의 정직한 `default`라는 출처 정보와 함께 제공됩니다.
추측으로 만든 게이지는 조회로 만든 게이지와 같은 신뢰도로 표시되지
않습니다.

ClawMetry는 일부 런타임에서만 압축 이벤트를 볼 수 있습니다. 그래서
`GET /api/context-coverage`는 런타임별로 **0이 "정상적으로 실행됨"을
의미하는지 "우리가 볼 수 없음"을 의미하는지**를 보고합니다. 실제로
보이지 않는 것을 의미하는 `0`은 그렇다고 표시됩니다.
[자세히 보기](docs/CONTEXT_BLOWOUT.md)

**계측 비용은 얼마인가요?**

| 경로 | 에이전트에 추가되는 것 | 기본값? |
|---|---|---|
| 세션 파일 테일링 (32개 런타임 전부) | **0**. 별도 프로세스이며 에이전트 안에는 ClawMetry 코드가 없음 | 켜짐 |
| HTTP 인터셉터 (`CLAWMETRY_INTERCEPT=1`) | LLM 호출당 **+0.44ms**, 5초 호출의 0.009% | 꺼짐 |
| 사전 도구 훅 게이트 (웜 캐시) | 게이트된 도구 호출당 **+44ms**, 36ms 인터프리터 기준선 위 | 꺼짐 |
| 강제 프록시 | LLM 호출당 **+9.7ms** | 꺼짐 |

데몬 호스트 비용: 수집 **초당 2,762건**의 이벤트, 이벤트당 **710바이트**
디스크 사용(10만 건당 67.7MB), 그리고 바쁜 설치 환경에서 지속적으로
**코어 1개의 약 12%**. 마지막 수치는 우리가 스스로 정한 5~10% 예산을
초과하므로, 숨기지 않고 계속 추적해야 할 버그로 공개되어 있습니다.

Apple M2 Pro에서 `benchmarks/overhead.py`로 측정했습니다. 이 하네스는
각 조건을 별도 프로세스에서 실행하고, 순서를 번갈아가며 실행하며,
**라운드끼리 부호가 일치하지 않으면 수치를 출력하지 않습니다**.
여러분의 머신에서 1분 안에 직접 실행해볼 수 있습니다:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

훅 게이트와 강제 프록시를 포함한 모든 경로가 측정되며, 이 하네스는
CI에서 Linux, macOS, Windows에서 실행됩니다. 알아둘 만한 두 가지 결과:
프록시는 Linux보다 Windows에서 약 7배 더 비용이 들고, 데몬은 현재
코어 1개의 약 12%를 지속적으로 사용하며 이는 우리 자체 5~10% 예산을
초과합니다. 원본 JSON, 방법론, 그리고 아직 측정되지 않은 부분은
[docs/OVERHEAD.md](docs/OVERHEAD.md)에 있습니다.

## 가격

| 요금제 | 포함 범위 | 가격 |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, 전체 대시보드, 로컬 전용 | $0 |
| **Starter** | 위의 다른 모든 런타임, 플릿 뷰, 클라우드 동기화 | 노드당 월 $9 |
| **Pro** | Starter + 제어 및 평가: 승인, 도구 위험 정책, 평가, 이상 탐지, 비용 최적화, OTel 내보내기, 변조 방지 감사 로그 | 노드당 월 $19 |

연간 요금제, Enterprise, 현재 가격은
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** 에서 확인할 수 있습니다.
셀프 호스팅 라이선스 키는 클라우드 없이도 작동합니다 (`clawmetry license`).
정확한 무료/유료 구분은 [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)에 있습니다.

## 여러분의 데이터는 여러분의 머신에 머무릅니다

ClawMetry는 로컬 세션 파일과 로그를 읽습니다. **`clawmetry connect`를
실행하지 않는 한 어떤 세션 데이터도 여러분의 박스를 벗어나지 않습니다**
— 프롬프트, 응답, 도구 인자, 파일 내용, 로그 라인 그 무엇도요. 연결할 경우
스냅샷은 여러분의 머신을 벗어나지 않는 키로 종단 간 암호화되며, 브라우저에서
복호화됩니다. 노드에 키가 없으면 업로드는 평문으로 전송되는 대신 건너뛰어지며,
어떤 서버 응답도 이를 끌 수 없습니다.

연결하기 전에도 기본적으로 실행되는 것이 두 가지 있으며, 둘 다 옵트아웃
가능하고 세션 데이터를 담지 않습니다: 익명 설치 핑과 PyPI 대비 버전 확인입니다.
기본 설치는 또한 시작 배너 한 줄을 위해 여러분의 공인 IP를 한 번 조회합니다.
각 목적지와 그것이 담는 내용, 끄는 방법은 모두
[docs/EGRESS.md](docs/EGRESS.md)에 정리되어 있으며, 셀프 호스팅 및
재지정, 에어갭 설치는 재량적인 아웃바운드 호출을 전혀 하지 않습니다.

복호화는 우리가 제공하는 코드로 여러분의 브라우저에서 이루어집니다.
과거에는 이것이 하나의 약속이었지만, 이제는 직접 확인할 수 있는 것이
되었습니다. 여러분의 키를 다루는 모든 줄은 읽을 수 있는 파일 하나,
[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js)에
들어 있으며, 이는 휠 안에 포함되어 그대로 제공되고 Subresource
Integrity 해시로 고정됩니다. 브라우저가 우리가 배포한 것과 동일한
코드를 실행하는지 확인하려면:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

이것이 증명하지 못하는 것: 이 파일을 불러오는 페이지 자체는 우리가
제공하므로, 우리가 다른 페이지를 제공할 수도 있습니다. 무결성 해시는
손상된 CDN으로부터 여러분을 보호하지만, 벤더 자체로부터는 보호하지
않습니다. 여러분이 얻는 것은, 어떤 대체든 의도적이어야 하고 페이지
소스에서 보여야 하며 누구나 가져올 수 있는 PyPI상의 아티팩트와
달라야 한다는 점입니다. 셀프 호스팅이나 로컬 전용 사용은 이 의존성
자체를 완전히 제거합니다.

## 설치

```bash
pip install clawmetry     # 이후: clawmetry
```

또는 한 줄 설치: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS, Linux, Windows에서 Python 3.8 이상이 필요하며, 같은 머신에
에이전트 런타임이 최소 하나 있어야 합니다. Docker 안내:
[docs/DOCKER.md](docs/DOCKER.md).

또는 에이전트가 대신 설정하게 할 수도 있습니다. [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
스킬은 Claude Code, Codex, Cursor, Gemini CLI, Copilot 또는 OpenCode에게
ClawMetry를 설치하고, 머신에 있는 에이전트들이 무엇을 하고 얼마를 쓰고
있는지 보고하고, 요청 시 세션 하나를 중지하고, 위험한 도구 호출을
승인을 위해 보류하도록 가르칩니다:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## 문서

| | |
|---|---|
| [런타임 호환성](docs/compatibility.md) | 각 어댑터가 무엇을 읽는지, 런타임을 추가하는 방법 |
| [컨텍스트 블로우아웃](docs/CONTEXT_BLOWOUT.md) | 프로바이더별 윈도우, 압축 대 오버플로, 런타임별 커버리지 |
| [오버헤드](docs/OVERHEAD.md) | 계측 비용이 실측으로 얼마인지, 재현 가능한 하네스와 함께 |
| [Entitlements](docs/ENTITLEMENTS.md) | 무료 대 유료, 티어 매트릭스, 라이선스 CLI |
| [승인 및 정책](docs/APPROVALS.md) | 실행 전 게이팅, 위험도 산정, 휴대폰 승인 |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | 트레이스를 어디로든 내보내고, 무엇에서든 OTLP를 수집 |
| [여러분의 에이전트 가져오기](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain 전 과정, 실행 가능한 예제와 함께 |
| [SDK 추적](docs/SDK_TRACKING.md) | 직접 만든 에이전트의 비용 귀속 |
| [채팅 채널](docs/CHANNELS.md) | Flow에 표시되는 채팅 어댑터 |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | 샌드박스화된 NVIDIA NemoClaw 설정 |
| [Docker](docs/DOCKER.md) | 이미지, compose, 볼륨 마운트 |
| [아키텍처](ARCHITECTURE.md) · [개발](docs/DEVELOPMENT.md) | 내부 동작 방식; 소스에서 실행하기 |
| [텔레메트리](docs/TELEMETRY.md) | 익명 설치 및 데스크톱 오픈 핑, 그리고 끄는 방법 |

## 스크린샷

아래의 모든 수치는 실제 머신 한 대에서, 읽기 전용으로, 아무것도
심지 않은 상태에서 나온 것입니다.

**단순히 무슨 일이 일어났는지가 아니라, 무언가 잘못됐을 때 알려줍니다.**
상단에 두 개의 이상 징후 배너: 일평균의 7배로 치솟은 지출, 그리고
4.2배의 비용 급증. 그 아래에는 최근 세션 667개 중 324개가 낭비 신호를
보이고 있으며, 원인별로 항목화되어 있습니다.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**돈이 어디로 갔는지, 모든 기간에 대해 보여줍니다.**
오늘 $252.47, 이번 주 $513.15, 이번 달 $1,312.92, 각각 그 뒤에 있는
토큰 수와 구독으로 이미 커버되는 비율과 함께. 그 아래에는 회수 가능한
것으로 항목화된 월 약 $1,128와 캐시 재사용으로 이미 절약된 월 $17,256가
있습니다.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**메시지가 어떻게 답변이 되는지 그려줍니다.**
실시간 플로우 다이어그램: 여러분, 메시지가 도착한 채널, 게이트웨이,
지금 답변하고 있는 모델, 그리고 그것이 사용한 모든 도구. 작업이
흐르면서 노드가 켜집니다.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**머신 위의 모든 에이전트를 하나의 테이블로.**
무엇을 실행하는지, 지난 24시간과 전체 기간 동안 비용이 얼마인지,
마지막으로 목격된 시점, 소유자, 구독으로 요금이 커버되는지 여부.
여기 14개의 에이전트, 3개 세션이 작업 중, 13개는 조용합니다.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**한 턴의 시간과 비용이 도구별로 어디로 갔는지 보여줍니다.**
실제 세션의 한 턴: 11.2분 동안 11개 도구, $1.16. 모든 Bash 호출과
모델 호출은 타임라인에서 자체 막대를 가지므로, 4.1분 동안 실행된
명령과 226ms 동안 실행된 명령을 한눈에 구분할 수 있습니다.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**지출뿐 아니라 작업의 품질도 평가합니다.**
이번 주 A등급: 54개의 작업이 깔끔하게 완료됐고, 거친 작업 2개가
$48.57의 비용이 들었으며, 판단하기에 활동이 너무 적은 실행은 승리로
카운트되는 대신 등급에서 제외됩니다. 각 거친 실행은 자신의 트레이스로
연결됩니다.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**컨텍스트 윈도우가 왜 계속 차오르는지 보여줍니다.**
최근 턴에서 1M 토큰 윈도우 중 715K, 83.3%의 최고치, 오버플로가 아니라
모두 선제적으로 발동된 압축 4회, 그리고 그 뒤에 있는 모든 턴의 사용률.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**아무 설정 없이도 탐지가 작동합니다.**
내장 탐지기는 설치 시점부터 켜져 있습니다: 에이전트가 조용해짐,
텔레메트리 피드 중단, 비용 급증, 토큰 버스트, 에러 증가, 에러 급증,
예산 임계값, 위협 시그니처 매칭, 보안 도구 발견, 보안 태세 변화. 여러분
자신의 규칙은 그 위에 선택적으로 추가할 수 있습니다.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**위험한 호출을 보류하는 것은 선택 사항이며, 꺼진 채로 출시됩니다.**
재귀적 삭제, 강제 푸시, sudo, 시크릿, 패키지 설치, 아웃바운드 호출은
각각 켤 수 있는 규칙을 가지고 있습니다. 켜기 전까지 ClawMetry는 지켜볼
뿐 아무것도 바꾸지 않습니다. 하나를 켜면, 일치하는 호출은 여기서(또는
여러분의 휴대폰에서) 승인 또는 거부를 기다립니다.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

런타임별로 더 많은 스크린샷: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## 수상 내역

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Star History

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## 라이선스

MIT · [@vivekchand](https://github.com/vivekchand)가 만듦 · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
