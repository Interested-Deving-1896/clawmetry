<!-- i18n-src:b22579578775 -->
> 繁體中文 translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**一個代理程式可以呼叫一百次工具卻毫無進展。** ClawMetry
讀取你的編碼代理程式已經在寫入的 session 檔案，把時間軸、
工具呼叫，以及執行環境所公開的任何 token 與成本資料整合到同一個
畫面中——讓你能分辨正在正常運作的長時間執行任務，和卡住的任務。

支援 **32 種 AI 代理執行環境**——Claude Code、OpenAI Codex、Hermes、OpenClaw 及其他 28 種。一個儀表板管理你整個代理程式艦隊。([完整清單](SUPPORTED_RUNTIMES.txt)，由目錄自動產生。)

> 🌐 **以其他語言閱讀：** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [更多 →](docs/i18n/)

一行指令。零設定。自動偵測一切。

```bash
pip install clawmetry && clawmetry
```

在 **http://localhost:8900** 開啟。零設定：它會找到你機器上已經
安裝的代理執行環境，以唯讀方式讀取它們,不會改變它們的任何運作方式。

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## 安裝前須知

| | |
|---|---|
| **它做什麼** | 讀取你的代理程式已經在寫入的 session 檔案與日誌。沒有 SDK、不需要修改程式碼、不需要在你的應用程式中植入任何監測代碼。 |
| **你會看到什麼** | Session 時間軸、逐一工具呼叫重播、token 與成本明細，以及軌跡訊號（迴圈、重複失敗）——依執行環境區分。 |
| **免費的部分** | `pip install clawmetry` 可讀取 **OpenClaw、NVIDIA NemoClaw、Goose 與 Qwen Code**，不需要帳號、金鑰或任何網路連線。其餘 28 種——Claude Code、Codex、Cursor 及其他——則由閉源的 `clawmetry-pro` 附加元件讀取，隨 7 天試用或付費方案一併提供——詳見 [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) 了解確切劃分方式。 |
| **如何開始** | `pip install clawmetry && clawmetry`,然後開啟 localhost:8900。這台機器上還沒有任何代理程式？`clawmetry --sample` 會以三個標示清楚的合成 session 開啟。 |
| **哪些資料會離開你的機器** | 除非你執行 `clawmetry connect`,否則不會有任何 session 資料外流。有兩件事預設會執行，兩者皆可選擇退出，且都不帶有 session 內容：匿名安裝回報，以及 PyPI 版本檢查。所有目的地都列在 [docs/EGRESS.md](docs/EGRESS.md) 中，該文件是根據網路封包擷取重建的,而非僅憑程式碼註解。 |

在你評判結果之前，有兩個限制值得先了解：不同執行環境公開的資料
差異很大（有些完全不公開成本——[相容性矩陣](docs/compatibility.md)
說明每種執行環境公開哪些資料），而且能觀察到某個動作,不代表
就能阻止它（[各執行環境哪些控制是真的能生效](docs/APPROVALS.md)）。


## 支援 32 種代理執行環境

**開源應用程式中免費：** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**付費方案：** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

每種執行環境都使用相同的儀表板。同時執行多個時，頂端的切換器
會把每個分頁重新指向其中一個執行環境。

自行以 SDK 打造代理程式？攔截器同樣能追蹤它的 LLM 呼叫。
詳見 [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)。

## 你能獲得什麼

- **Session 與逐字稿**：每個代理程式逐輪做了什麼，並可重播
- **成本與 token**：依執行環境、模型、session 與日期劃分，並附異常標記
- **Flow**：訊息在頻道、模型與工具之間流動的即時圖表
- **Brain**：即時發生的推理與工具呼叫事件串流
- **Context blowout（上下文爆量）**：依各服務商調整大小的視窗使用率、壓縮 vs 強制溢出，以及各執行環境「我們看不到什麼」的對照表 ([如何運作](docs/CONTEXT_BLOWOUT.md))
- **記憶與技能**：每個執行環境實際載入了哪些檔案與技能
- **健康狀態與日誌**：磁碟、記憶體、錯誤率、速率限制、即時日誌串流
- **警示**：預算上限、錯誤激增、代理程式離線，可路由到 Slack、Discord、PagerDuty、Telegram、Email
- **核准**：在高風險工具呼叫執行*之前*先暫停，並可從手機核准 ([如何運作](docs/APPROVALS.md))

## Context blowout，以及觀測要付出的成本

在你信任任何代理程式比較工具之前，有兩個問題值得先問清楚。

**它如何處理各執行環境之間的上下文視窗爆量？**

使用率百分比的可信度，取決於分母算得誠不誠實。ClawMetry
依據[一份你可以閱讀並提交 PR 的資料表](clawmetry/context_windows.py)
為每個服務商調整視窗大小，涵蓋 Anthropic、OpenAI、Google、xAI、
DeepSeek、Kimi、Qwen、Mistral、Llama 與 GLM。它不會用某一家廠商
的尺規去衡量全部 32 種執行環境。這一點很重要：一個 300K 的
GPT-5 回合若拿 Anthropic 的 200K 來對照，會顯示「>100%，爆量」，
但它其實只用了 GPT-5 的 400K 視窗的 75%。同一把尺規也會把一個
確實已溢出的 130K DeepSeek 回合，掩蓋成看似無虞的 65%。

每個視窗都附有其來源說明：`model_table`、`explicit_marker`、
`observed_floor`，或是在我們不知道該模型時如實標示的 `default`。
建立在猜測之上的量表,絕不會與建立在查表之上的量表以同等
權威性呈現。

ClawMetry 只能在部分執行環境上看到壓縮事件。因此
`GET /api/context-coverage` 會針對每個執行環境回報,一個「0」
究竟代表「乾淨執行完畢」還是「我們看不見」。若某個 `0`
實際上代表看不見，它會明確說明。
[完整說明](docs/CONTEXT_BLOWOUT.md)

**這套監測工具本身要付出什麼代價？**

| 路徑 | 加到你的代理程式上的額外開銷 | 預設啟用？ |
|---|---|---|
| Session 檔案追蹤讀取（全部 32 種執行環境） | **0**。獨立程序，你的代理程式中沒有任何 ClawMetry 程式碼 | 開啟 |
| HTTP 攔截器（`CLAWMETRY_INTERCEPT=1`） | 每次 LLM 呼叫 **+0.44 毫秒**，相當於一次 5 秒呼叫的 0.009% | 關閉 |
| 前置工具鉤子閘門（暖快取） | 每次受管控的工具呼叫 **+44 毫秒**，超出 36 毫秒的直譯器基準值 | 關閉 |
| 執行代理程式 | 每次 LLM 呼叫 **+9.7 毫秒** | 關閉 |

守護程式主機成本：擷取速度 **每秒 2,762 個事件**，磁碟上
**每個事件 710 位元組**（每 10 萬個事件 67.7 MB），在繁忙的
安裝環境中持續佔用 **約一個核心的 12%**。最後這個數字超出
我們自訂的 5-10% 預算，因此我們把它當作一個要追蹤的 bug
公開，而不是隱藏不提。

以 Apple M2 Pro 搭配 `benchmarks/overhead.py` 測得。此測試工具
會在獨立程序中執行每個情境、交替執行順序，並且**在各輪結果
正負號不一致時拒絕印出數字**。你可以在自己的機器上一分鐘內
執行它：

```bash
pip install clawmetry && python -m benchmarks.overhead
```

每一條路徑都經過測量，包括鉤子閘門與執行代理程式,而這套
測試工具在 CI 中會於 Linux、macOS 與 Windows 上執行。有兩項
結果值得留意：這個代理程式在 Windows 上的成本大約是 Linux
上的七倍，而守護程式目前持續佔用約一個核心的 12%，超出我們
自訂的 5-10% 預算。原始 JSON 資料、測量方法,以及尚未測量的
部分都列在 [docs/OVERHEAD.md](docs/OVERHEAD.md) 中。

## 定價

| 方案 | 涵蓋內容 | 價格 |
|---|---|---|
| **免費** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code,完整儀表板,僅限本機 | $0 |
| **Starter** | 上述以外的所有執行環境、艦隊檢視、雲端同步 | 每節點每月 $9 |
| **Pro** | Starter + 控制與評估功能：核准、工具風險政策、評估、異常偵測、成本最佳化工具、OTel 匯出、防竄改稽核日誌 | 每節點每月 $19 |

年繳方案、企業方案及最新價格請見
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**。自架授權
金鑰可在不使用雲端的情況下運作（`clawmetry license`）。確切的
免費/付費劃分請見 [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)。

## 你的資料留在你的機器上

ClawMetry 讀取本機的 session 檔案與日誌。**除非你執行
`clawmetry connect`，否則不會有任何 session 資料離開你的機器**——
不包含提示詞、回覆、工具參數、檔案內容或日誌內容。當你確實
連線時，快照會以端對端加密方式傳輸，加密金鑰永遠不會離開你的
機器，並在你的瀏覽器端解密。若某個節點沒有金鑰,上傳會直接
被略過而不會以明文傳送，而且任何伺服器回應都無法關閉這項
保護。

在你連線之前,預設有兩件事會執行，兩者皆可選擇退出，且都不帶
session 資料：匿名安裝回報，以及對 PyPI 的版本檢查。預設安裝
也會查詢一次你的公開 IP，用於啟動橫幅訊息。每個目的地傳輸的
內容,以及如何關閉它，都列在 [docs/EGRESS.md](docs/EGRESS.md)
中；自架、重新指向或氣隙（air-gapped）安裝完全不會有任何自主
對外呼叫。

解密過程發生在你的瀏覽器中,使用我們提供給你的程式碼。這件事
過去只是一個承諾；現在你可以自行驗證。每一行會接觸到你金鑰
的程式碼都在同一個可讀的檔案中，
[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js)，
它會隨 wheel 套件一起發佈,並以原樣提供,並以子資源完整性
（Subresource Integrity）雜湊值固定。若要確認瀏覽器執行的是
我們發佈的版本：

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

這無法證明的是：我們同時提供載入該檔案的頁面,因此我們理論上
可以提供不同的頁面。完整性雜湊值能保護你免受 CDN 遭入侵的
影響，但無法防範供應商本身的行為。你所得到的保障是,任何
替換行為都必須是刻意的、在頁面原始碼中可見的，並且與任何人
都能從 PyPI 取得的成品不同。自架或僅使用本機模式可完全消除
這項依賴。

## 安裝

```bash
pip install clawmetry     # 然後執行：clawmetry
```

或使用一行指令：`curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

需要 macOS、Linux 或 Windows 上的 Python 3.8 以上版本，並且
同一台機器上至少有一個代理執行環境。Docker 安裝說明：
[docs/DOCKER.md](docs/DOCKER.md)。

或讓代理程式幫你設定。[`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
技能可教會 Claude Code、Codex、Cursor、Gemini CLI、Copilot 或
OpenCode 安裝 ClawMetry、回報機器上各代理程式正在做什麼與花費
多少、依要求停止某個 session，並暫留高風險的工具呼叫以等待
核准：

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## 文件

| | |
|---|---|
| [執行環境相容性](docs/compatibility.md) | 每個轉接器能讀取什麼，以及如何新增執行環境 |
| [Context blowout](docs/CONTEXT_BLOWOUT.md) | 各服務商視窗大小、壓縮 vs 溢出、各執行環境涵蓋範圍 |
| [開銷](docs/OVERHEAD.md) | 監測工具的實際成本測量結果,以及可重現的測試工具 |
| [權益（Entitlements）](docs/ENTITLEMENTS.md) | 免費 vs 付費、方案矩陣、授權 CLI |
| [核准與政策](docs/APPROVALS.md) | 執行前把關、風險評分、手機核准 |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | 將追蹤資料匯出到任何地方，從任何來源接收 OTLP |
| [自帶代理程式](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore、Pydantic AI、LangChain 全流程，附可執行範例 |
| [SDK 追蹤](docs/SDK_TRACKING.md) | 為你自行打造的代理程式進行成本歸屬 |
| [聊天頻道](docs/CHANNELS.md) | Flow 中顯示的聊天轉接器 |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | 沙箱化的 NVIDIA NemoClaw 設定 |
| [Docker](docs/DOCKER.md) | 映像檔、compose、掛載磁碟區 |
| [架構](ARCHITECTURE.md) · [開發](docs/DEVELOPMENT.md) | 內部運作原理；如何從原始碼執行 |
| [遙測](docs/TELEMETRY.md) | 匿名安裝與開啟桌面應用程式的回報，以及如何關閉它們 |

## 螢幕截圖

以下每個數字都來自一台真實機器，以唯讀方式讀取，未經任何
特別安排。

**它會告訴你何時出了問題,而不只是發生了什麼事。**
頂端有兩則異常橫幅：花費是每日平均的 7 倍,以及一次 4.2 倍的
成本激增。下方則是最近 667 個 session 中有 324 個帶有浪費訊號，
並依原因逐項列出。

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**它會告訴你錢花到哪裡去了,涵蓋每一個時間範圍。**
今日 $252.47、本週 $513.15、本月 $1,312.92，各自附上背後的
token 用量,以及訂閱方案已經涵蓋了多少。下方則列出約每月
$1,128 被歸類為可回收的浪費，以及快取重用已經節省的每月
$17,256。

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**它會描繪出一則訊息如何變成一個答案。**
即時流程圖：你、訊息抵達的頻道、閘道、目前正在回應的模型，
以及它呼叫過的每一項工具。節點會隨著工作流經而亮起。

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**機器上的每個代理程式,全部整合在一張表格中。**
它在執行什麼、過去 24 小時與整個生命週期的成本、上次出現的
時間、擁有者是誰，以及是否有訂閱方案在支付費用。這裡有 14 個
代理程式，3 個 session 正在工作，13 個閒置中。

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**它會顯示每一輪對話的時間與金錢花在哪裡,逐一工具呈現。**
一個真實 session 的一輪對話：11 項工具、11.2 分鐘、花費
$1.16。每一次 Bash 呼叫與模型呼叫在時間軸上都有自己的長條，
因此一眼就能分辨出跑了 4.1 分鐘的那個指令,和只跑了 226 毫秒
的那個指令。

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**它評的是工作品質,而不只是花費。**
本週的成績是 A：54 個任務乾淨完成，2 個較差的任務花費
$48.57，而活動量太少、不足以評判的執行則被排除在評分之外，
而不是被算作成功。每個較差的執行都連結到它的追蹤紀錄。

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**它會顯示上下文視窗為何不斷被填滿。**
最新一輪對話用掉 1M token 視窗中的 715K，峰值達 83.3%，
4 次壓縮全都是主動觸發、而非因溢出而觸發，並附上背後每一輪
對話的使用率。

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**偵測功能無需任何設定即可運作。**
內建偵測器從安裝時就已啟用：代理程式無回應、遙測資料饋送
中斷、成本激增、token 用量暴增、錯誤攀升、錯誤激增、預算
門檻、符合威脅特徵、安全工具發現、安全態勢變化。你也可以
另外選擇加上自訂規則。

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**攔截高風險呼叫是選擇加入的功能,且預設關閉。**
遞迴刪除、強制推送、sudo、密鑰存取、套件安裝與對外呼叫,
每一項都有可個別開啟的規則。在你開啟之前，ClawMetry 只會
觀察，不會改變任何事情。一旦開啟某項規則，符合條件的呼叫
就會在此處（或你的手機上）等待核准或拒絕。

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

更多依執行環境分類的截圖：[docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md)。

## 榮譽紀錄

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Star 成長歷史

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## 授權條款

MIT · 由 [@vivekchand](https://github.com/vivekchand) 開發 · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
