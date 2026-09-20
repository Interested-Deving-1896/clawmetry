<!-- i18n-src:b22579578775 -->
> 简体中文 translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**一个智能体可以进行一百次工具调用却毫无进展。** ClawMetry
读取你的编码智能体已经写入的会话文件，并将时间线、
工具调用以及运行时所暴露的任何 token 与成本数据整合到一个
视图中——这样你就能分辨出哪些长时间运行是在正常工作，哪些其实卡住了。

支持 **32 种 AI 智能体运行时**——Claude Code、OpenAI Codex、Hermes、OpenClaw，以及另外 28 种。一个仪表盘管理你整个智能体舰队。（[完整列表](SUPPORTED_RUNTIMES.txt)，由目录自动生成。）

> 🌐 **切换语言：** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [更多 →](docs/i18n/)

一条命令。零配置。自动检测一切。

```bash
pip install clawmetry && clawmetry
```

在 **http://localhost:8900** 打开。零配置：它会找到你机器上已有的
智能体运行时，以只读方式读取它们，不会改变它们的任何运行方式。

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## 安装前须知

| | |
|---|---|
| **它做什么** | 读取你的智能体已经写入的会话文件和日志。无需 SDK，无需修改代码，不在你的应用中植入任何插桩。 |
| **你能看到什么** | 会话时间线、逐工具回放、token 与成本明细，以及轨迹信号（循环、重复失败）——按运行时区分。 |
| **哪些是免费的** | `pip install clawmetry` 可以读取 **OpenClaw、NVIDIA NemoClaw、Goose 和 Qwen Code**，无需账号、无需密钥、也不产生任何网络调用。其余 28 种——Claude Code、Codex、Cursor 等——由闭源的 `clawmetry-pro` 配套组件读取，该组件随 7 天试用或付费计划提供——确切的划分见 [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)。 |
| **如何开始** | `pip install clawmetry && clawmetry`，然后打开 localhost:8900。这台机器上还没有智能体？`clawmetry --sample` 会打开三个已标注的合成会话。 |
| **哪些数据会离开你的机器** | 除非你运行 `clawmetry connect`，否则没有任何会话数据会离开。默认情况下确实会运行两件事，两者都可选择关闭，且都不携带会话内容：一次匿名安装 ping 和一次 PyPI 版本检查。所有目的地都记录在 [docs/EGRESS.md](docs/EGRESS.md) 中，该清单是通过抓包重建的，而不是靠阅读代码注释得出的。 |

在你评判输出结果之前，有两点局限值得了解：不同运行时暴露的数据差异很大
（有些运行时根本不发布成本数据——具体哪些运行时见[对照表](docs/compatibility.md)），
而能观察到某个操作并不等于能够阻止它
（[各运行时哪些控制能力是真实可用的](docs/APPROVALS.md)）。


## 支持 32 种智能体运行时

**在开源应用中免费：** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**付费计划：** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

每种运行时都拥有相同的仪表盘。同时运行多个时，顶部的切换器
会将每个标签页重新限定到其中一个运行时。

用 SDK 自己搭建了智能体？拦截器同样会追踪它的 LLM 调用。
详见 [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)。

## 你能获得什么

- **会话与记录**：每个智能体做了什么，逐轮呈现，可回放
- **成本与 token**：按运行时、模型、会话和天数统计，并带有异常标记
- **Flow**：消息在渠道、模型和工具之间流动的实时图示
- **Brain**：推理与工具调用事件流的实时呈现
- **上下文爆量（Context blowout）**：按各家服务商实际窗口大小计算的利用率、压缩（compaction）与被迫溢出的区分，以及每种运行时“我们看不到什么”的地图（[原理说明](docs/CONTEXT_BLOWOUT.md)）
- **Memory 与 Skills**：每个运行时实际加载了哪些文件和技能
- **健康状况与日志**：磁盘、内存、错误率、速率限制、实时日志流
- **告警**：预算上限、错误突增、智能体离线，可路由到 Slack、Discord、PagerDuty、Telegram、Email
- **审批**：在高风险工具调用*执行前*暂停，并可在手机上完成审批（[原理说明](docs/APPROVALS.md)）

## 上下文爆量，以及监控要付出的代价

在你信任任何智能体对比工具之前，有两个问题值得先弄清楚。

**它如何处理跨运行时的上下文窗口爆量？**

利用率百分比的可信度，取决于它的分母是否诚实。ClawMetry
根据[一张你可以阅读并提交 PR 的表格](clawmetry/context_windows.py)按服务商设定窗口大小，
覆盖 Anthropic、OpenAI、Google、xAI、
DeepSeek、Kimi、Qwen、Mistral、Llama 和 GLM。它不会用某一家厂商的标尺去衡量全部
32 种运行时。这一点很重要：一次 300K 的 GPT-5 对话轮，如果套用 Anthropic 的
200K 标尺，会被读成“>100%，已爆量”，但实际上它只用了 GPT-5 自身 400K 窗口的
75%。同样的标尺，也会把一次真正溢出的 130K DeepSeek 对话轮，掩盖成看似
舒适的 65%。

每个窗口都附带其来源标注：`model_table`、`explicit_marker`、
`observed_floor`，或者在我们不知道模型是什么时诚实标注为 `default`。
建立在猜测之上的量表，永远不该以和建立在查表之上的量表相同的权威性呈现。

ClawMetry 只能在部分运行时上看到压缩（compaction）事件。因此
`GET /api/context-coverage` 会针对每种运行时报告，**数值为零究竟代表
“运行正常”还是“我们看不见”**。真正代表“看不见”的零值会明确说明这一点。
[详情](docs/CONTEXT_BLOWOUT.md)

**这套插桩的开销是多少？**

| 路径 | 给你的智能体带来的开销 | 是否默认开启？ |
|---|---|---|
| 会话文件尾随读取（全部 32 种运行时） | **0**。独立进程，你的智能体中没有任何 ClawMetry 代码 | 开启 |
| HTTP 拦截器（`CLAWMETRY_INTERCEPT=1`） | 每次 LLM 调用 **+0.44 毫秒**，相当于一次 5 秒调用的 0.009% | 关闭 |
| 工具执行前的钩子门（预热缓存） | 每次受管控的工具调用 **+44 毫秒**，高于 36 毫秒的解释器基线 | 关闭 |
| 强制执行代理 | 每次 LLM 调用 **+9.7 毫秒** | 关闭 |

守护进程主机开销：摄取速率 **2,762 事件/秒**，磁盘占用**每事件 710 字节**
（每 10 万事件 67.7 MB），在繁忙的安装环境下持续占用 **约 12% 的一个核心**。
最后这个数字超出了我们自己设定的 5%-10% 预算，因此我们把它作为一个
需要追踪的 bug 公开出来，而不是从页面上删掉。

在 Apple M2 Pro 上使用 `benchmarks/overhead.py` 测得。该测试工具在
独立进程中运行每种条件，交替它们的运行顺序，并且**当多轮结果的正负号
不一致时，拒绝给出任何数字**。你可以在自己的机器上一分钟内运行一次：

```bash
pip install clawmetry && python -m benchmarks.overhead
```

每条路径都经过测量，包括钩子门和强制执行代理，测试工具在 CI 中
分别于 Linux、macOS 和 Windows 上运行。有两个结果值得注意：该代理在
Windows 上的开销约为 Linux 上的七倍，且守护进程目前持续占用约 12%
的一个核心，超出了我们自己设定的 5%-10% 预算。原始 JSON 数据、
测量方法，以及尚未测量的部分，都在
[docs/OVERHEAD.md](docs/OVERHEAD.md) 中。

## 价格

| 计划 | 覆盖范围 | 价格 |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code，完整仪表盘，仅限本地 | $0 |
| **Starter** | 以上之外的全部其他运行时、舰队视图、云同步 | 每节点每月 $9 |
| **Pro** | Starter + 管控与评估：审批、工具风险策略、评估（evals）、异常检测、成本优化器、OTel 导出、防篡改审计日志 | 每节点每月 $19 |

年付计划、企业版以及最新价格详见
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**。自托管许可证
密钥无需云端即可使用（`clawmetry license`）。免费与付费的确切划分见
[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)。

## 你的数据留在你的机器上

ClawMetry 读取本地会话文件和日志。**除非你运行 `clawmetry connect`，
否则不会有任何会话数据离开你的设备**——不包括提示词、回复、工具参数、文件
内容或日志行。当你确实连接时，快照会以端到端加密方式传输，密钥永远不会
离开你的机器，解密在你的浏览器中完成。如果某个节点没有密钥，上传会被
跳过，而不是以明文发送，并且没有任何服务器响应能够关闭这一限制。

在你连接之前，默认情况下确实会运行两件事，两者都可以选择关闭，且都不
携带会话数据：一次匿名安装 ping 和一次针对 PyPI 的版本检查。默认安装
还会查询一次你的公网 IP，用于启动横幅信息。每个目的地、它携带什么数据、
以及如何关闭它，都列在
[docs/EGRESS.md](docs/EGRESS.md) 中；自托管、重新指向或air-gapped（完全隔离网络）的安装
不会产生任何可自主决定的出站调用。

解密发生在你的浏览器中，运行的是我们提供给你的代码。这曾经只是一个
承诺，现在则是可以核实的。每一行接触你密钥的代码都在同一个可读文件中，
[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js)，
它随 wheel 包一起发布，原样提供，并以子资源完整性（Subresource
Integrity）哈希固定。要确认浏览器运行的正是我们发布的版本：

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

这个方法无法证明的是：我们负责提供加载该文件的页面，所以我们理论上
可以提供一个不同的页面。完整性哈希能保护你免受 CDN 被攻破的影响，
却无法防范厂商本身作恶。你能获得的保障是，任何替换都必须是刻意的、
在页面源码中可见的，并且与任何人都能从 PyPI 获取到的产物不同。
自托管或仅使用本地模式可以完全消除这种依赖。

## 安装

```bash
pip install clawmetry     # 然后运行：clawmetry
```

或者使用一行命令：`curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

需要 macOS、Linux 或 Windows 上的 Python 3.8+，以及同一台机器上至少
一个智能体运行时。Docker 安装说明见 [docs/DOCKER.md](docs/DOCKER.md)。

或者让智能体帮你完成设置。[`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
技能会教会 Claude Code、Codex、Cursor、Gemini CLI、Copilot 或 OpenCode
安装 ClawMetry、报告机器上各智能体正在做什么以及花费情况、
按需停止某个会话，并对高风险工具调用进行拦截以等待审批：

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## 文档

| | |
|---|---|
| [运行时兼容性](docs/compatibility.md) | 每个适配器读取哪些内容，以及如何新增一个运行时 |
| [上下文爆量](docs/CONTEXT_BLOWOUT.md) | 按服务商划分的窗口大小、压缩与溢出的区别、各运行时的覆盖情况 |
| [开销](docs/OVERHEAD.md) | 插桩的实测开销，以及可复现该测试的工具 |
| [权益（Entitlements）](docs/ENTITLEMENTS.md) | 免费与付费的划分、层级对照表、license CLI |
| [审批与策略](docs/APPROVALS.md) | 执行前拦截、风险评分、手机端审批 |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | 将追踪数据导出到任意位置，从任意来源摄取 OTLP |
| [接入你自己的智能体](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore、Pydantic AI、LangChain 全流程示例，附可运行代码 |
| [SDK 追踪](docs/SDK_TRACKING.md) | 为你自己搭建的智能体做成本归因 |
| [聊天渠道](docs/CHANNELS.md) | Flow 中展示的各聊天适配器 |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | 沙箱化的 NVIDIA NemoClaw 配置 |
| [Docker](docs/DOCKER.md) | 镜像、compose、卷挂载 |
| [架构](ARCHITECTURE.md) · [开发](docs/DEVELOPMENT.md) | 内部工作原理；如何从源码运行 |
| [遥测](docs/TELEMETRY.md) | 匿名安装与桌面打开 ping，以及如何关闭它们 |

## 截图

以下所有数据均来自同一台真实机器，只读获取，未做任何预置。

**它会在出问题时告诉你，而不仅仅是告诉你发生了什么。**
顶部两个异常横幅：支出达到日均的 7 倍，以及一次 4.2 倍的成本突增。
下方是 667 个近期会话中有 324 个带有浪费信号，并按原因逐项列出。

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**它会告诉你钱花在了哪里，覆盖每个时间窗口。**
今天 $252.47，本周 $513.15，本月 $1,312.92，每一项都附带背后的 token 数
以及你的订阅已经覆盖了其中多少。下方是约每月 $1,128 的可回收开支明细，
以及缓存复用已经节省的每月约 $17,256。

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**它绘制出一条消息是如何变成一个答案的。**
实时流程图：你、消息到达的渠道、网关、当前正在回答的模型，以及它
调用的每一个工具。随着工作在其中流转，节点会依次点亮。

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**机器上的每一个智能体，汇总在一张表里。**
它在运行什么、过去 24 小时和整个生命周期的花费、最后一次活跃时间、
归属者，以及是否有订阅正在覆盖这笔费用。这里有 14 个智能体，3 个
会话正在工作，13 个空闲。

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**它会展示一个对话轮的时间和金钱花在了哪个工具上。**
一个真实会话中的一轮：11.2 分钟内调用了 11 个工具，花费 $1.16。每次
Bash 调用和每次模型调用都在时间线上拥有自己的条形图，因此那个运行了
4.1 分钟的命令和那个只运行了 226 毫秒的命令一眼就能区分开来。

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**它评估的是工作质量，而不仅仅是花费。**
本周评级为 A：54 个任务干净利落地完成，2 个不太顺利的任务花费了
$48.57，而那些活动量太少、无法判断的运行会被排除在评级之外，
而不是被算作成功。每个不太顺利的运行都链接到其追踪记录。

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**它展示了上下文窗口为什么会一直被填满。**
最近一个对话轮用掉了 100 万 token 窗口中的 71.5 万，峰值利用率
83.3%，4 次压缩全部是主动触发而非因溢出触发，并展示了此前每一轮
的利用率。

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**检测功能无需任何配置即可运行。**
内置检测器从安装起就已开启：智能体沉默、遥测数据流中断、成本突增、
token 突增、错误率攀升、错误突增、预算阈值、威胁特征匹配、安全工具
发现、安全态势变化。你自己的规则是在此基础上的可选补充。

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**拦截高风险调用是可选启用的，默认关闭出厂。**
递归删除、强制推送、sudo、密钥泄露、包安装和出站调用，每一项都有
对应的规则供你开启。在你开启之前，ClawMetry 只会观察，不会改变任何
东西。一旦某项开启，匹配的调用就会在这里（或在你的手机上）等待
批准或拒绝。

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

更多按运行时区分的截图：[docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md)。

## 荣誉

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Star 历史

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## 许可证

MIT · 由 [@vivekchand](https://github.com/vivekchand) 构建 · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
