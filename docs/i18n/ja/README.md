<!-- i18n-src:b22579578775 -->
> 日本語 translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**エージェントは進捗を生まないまま何百回もツール呼び出しを行うことがあります。** ClawMetryは、コーディングエージェントがすでに書き出しているセッションファイルを読み取り、タイムライン、ツール呼び出し、そしてランタイムが公開しているトークン・コストデータを一つのビューにまとめます。これにより、うまく機能している長時間の実行と、行き詰まっている実行を見分けられます。

**32のAIエージェントランタイム**に対応 — Claude Code、OpenAI Codex、Hermes、OpenClaw、その他28種類。エージェント群全体を一つのダッシュボードで。([全リストはこちら](SUPPORTED_RUNTIMES.txt)。カタログから生成されています。)

> 🌐 **他の言語で読む:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [もっと見る →](docs/i18n/)

コマンド一つ。設定ゼロ。すべて自動検出。

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** で開きます。設定は不要です。すでにお使いのエージェントランタイムを自動で見つけ、読み取り専用でアクセスし、動作方法には一切手を加えません。

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## インストール前に

| | |
|---|---|
| **できること** | エージェントがすでに書き出しているセッションファイルとログを読み取ります。SDKも、コード変更も、アプリへの計装も不要です。 |
| **見えるもの** | セッションのタイムライン、ツール単位のリプレイ、トークンとコストの内訳、そして軌跡シグナル(ループ、繰り返す失敗)を、ランタイムごとに確認できます。 |
| **無料の範囲** | `pip install clawmetry` は、アカウント不要・キー不要・ネットワーク通信不要で **OpenClaw、NVIDIA NemoClaw、Goose、Qwen Code** を読み取れます。その他28種類 — Claude Code、Codex、Cursorなど — はクローズドソースの `clawmetry-pro` コンパニオンが読み取ります。これは7日間のトライアルまたはプランに付属します。正確な区分は[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)を参照してください。 |
| **始め方** | `pip install clawmetry && clawmetry` を実行し、localhost:8900を開いてください。このマシンにまだエージェントがない場合は、`clawmetry --sample` を実行するとラベル付きの合成セッション3件で開きます。 |
| **マシン外に出るもの** | `clawmetry connect` を実行しない限り、セッションデータは外部に出ません。デフォルトで動作するものが2つあり、どちらもオプトアウト可能で、セッション内容は含みません:匿名のインストールping、そしてPyPIバージョンチェックです。すべての送信先はコメントを読むのではなく通信キャプチャから再構築され、[docs/EGRESS.md](docs/EGRESS.md)に一覧化されています。 |

判断する前に知っておくべき2つの制限があります。ランタイムごとに公開されるデータは大きく異なり(コストを一切公開しないものもあります — [対応表](docs/compatibility.md)にランタイムごとの詳細があります)、また行動を観測できることとそれを止められることは別問題です([ランタイムごとにどの制御が実際に機能するか](docs/APPROVALS.md))。


## 32のエージェントランタイムに対応

**オープンソースアプリで無料:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**有料プランで:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

どのランタイムも同じダッシュボードで扱えます。複数を同時に実行しても、ヘッダーのスイッチャーが各タブの対象を切り替えます。

SDKを使って独自エージェントを構築した場合も、インターセプターがそのLLM呼び出しを追跡します。詳しくは[docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)を参照してください。

## 得られるもの

- **セッションとトランスクリプト**: 各エージェントがターンごとに何をしたか、リプレイ付きで確認
- **コストとトークン**: ランタイム・モデル・セッション・日単位で、異常検知フラグ付き
- **Flow**: メッセージがチャネル、モデル、ツールを通って移動する様子をリアルタイム図で表示
- **Brain**: 推論とツール呼び出しのイベントストリームをリアルタイムで表示
- **コンテキスト膨張**: プロバイダーごとに正しくサイズ調整されたウィンドウ利用率、compaction対強制オーバーフロー、そして「見えていない」部分をランタイムごとに示すマップ([詳細](docs/CONTEXT_BLOWOUT.md))
- **メモリとスキル**: 各ランタイムが実際に読み込んだファイルとスキル
- **ヘルスとログ**: ディスク、メモリ、エラー率、レート制限、ログのライブストリーム
- **アラート**: 予算上限、エラー急増、エージェントのオフライン検知。Slack、Discord、PagerDuty、Telegram、Emailへの通知に対応
- **承認**: 危険なツール呼び出しを*実行前に*一時停止し、スマートフォンから承認できます([詳細](docs/APPROVALS.md))

## コンテキスト膨張、そして監視のコスト

どんなエージェント比較ツールを信頼する前にも、答えておく価値のある2つの問いがあります。

**ランタイムをまたいだコンテキストウィンドウの膨張をどう扱っているか?**

利用率のパーセンテージは、その分母が正しいかどうかにしか誠実さを持ちません。ClawMetryは[読んでPRできる表](clawmetry/context_windows.py)を使ってプロバイダーごとにウィンドウサイズを決定しており、Anthropic、OpenAI、Google、xAI、DeepSeek、Kimi、Qwen、Mistral、Llama、GLMをカバーしています。32種類すべてのランタイムを一社の物差しで測ることはしません。これは重要な違いです。GPT-5の30万トークンのターンをAnthropicの20万トークンの物差しで評価すると「100%超、破綻」と読めますが、実際はGPT-5の40万トークンの75%に過ぎません。同じ物差しは、本当にオーバーフローした13万トークンのDeepSeekのターンを、快適な65%として隠してしまいます。

すべてのウィンドウにはその出所が付きます: `model_table`、`explicit_marker`、`observed_floor`、あるいはモデルが不明な場合の正直な `default` です。推測で組み立てられたゲージが、ルックアップで組み立てられたものと同じ権威を持って表示されることはありません。

ClawMetryは一部のランタイムでしかcompactionイベントを確認できません。そのため `GET /api/context-coverage` は、ランタイムごとに**ゼロが「問題なく動いた」を意味するのか「見えていない」を意味するのか**を報告します。実際には見えていないことを意味するゼロは、そう明記されます。[詳細](docs/CONTEXT_BLOWOUT.md)

**計装のコストはどれくらいか?**

| パス | エージェントへの追加コスト | デフォルト? |
|---|---|---|
| セッションファイルの追跡(全32ランタイム) | **0**。別プロセスで動作し、エージェント側にClawMetryのコードは一切入りません | オン |
| HTTPインターセプター (`CLAWMETRY_INTERCEPT=1`) | LLM呼び出し1回あたり**+0.44ミリ秒**。5秒の呼び出しの0.009% | オフ |
| ツール実行前フック(ゲート、ウォームキャッシュ時) | ゲート対象のツール呼び出し1回あたり**+44ミリ秒**(インタプリタの下限36ミリ秒を上乗せ) | オフ |
| 実行制御プロキシ | LLM呼び出し1回あたり**+9.7ミリ秒** | オフ |

デーモンのホストコスト: 取り込み**毎秒2,762イベント**、ディスク上**イベントあたり710バイト**(10万イベントあたり67.7MB)、そして稼働中のインストールで持続的に**1コアの約12%**。この最後の数字は、私たち自身が掲げる5〜10%の予算を上回っているため、隠さずに「追いかけるべきバグ」として公開しています。

Apple M2 Proで `benchmarks/overhead.py` を使って計測しました。このハーネスは各条件を別プロセスで実行し、順序を入れ替え、**ラウンド間で符号が一致しない場合は数値を出力しません**。ご自身のマシンでも1分程度で実行できます:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

フックゲートや実行制御プロキシを含め、すべてのパスが計測されており、このハーネスはLinux、macOS、WindowsのCI上でも実行されます。知っておく価値のある2つの結果: プロキシのコストはWindowsではLinuxの約7倍かかること、そしてデーモンは現在1コアの約12%を持続的に消費しており、私たち自身が掲げる5〜10%の予算を上回っています。生のJSON、計測方法、そしてまだ計測できていない部分は[docs/OVERHEAD.md](docs/OVERHEAD.md)にあります。

## 料金

| プラン | 対応範囲 | 価格 |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code、ダッシュボード全機能、ローカルのみ | $0 |
| **Starter** | 上記以外のすべてのランタイム、フリートビュー、クラウド同期 | ノードあたり月額$9 |
| **Pro** | Starter + 制御と評価: 承認、ツールリスクポリシー、評価、異常検知、コスト最適化、OTelエクスポート、改ざん検知監査ログ | ノードあたり月額$19 |

年額プラン、Enterprise、最新の価格は**[clawmetry.com/pricing](https://clawmetry.com/pricing)**にあります。セルフホスト型のライセンスキーはクラウドなしでも機能します(`clawmetry license`)。無料/有料の正確な区分は[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)にあります。

## データはあなたのマシンに留まります

ClawMetryはローカルのセッションファイルとログを読み取ります。**`clawmetry connect` を実行しない限り、セッションデータは一切あなたのマシンから出ません** — プロンプト、返答、ツールの引数、ファイル内容、ログ行もすべて含まれません。接続する際は、あなたのマシンから決して出ない鍵を使ってスナップショットがエンドツーエンドで暗号化され、ブラウザ内で復号されます。ノードに鍵がない場合、アップロードは平文で送信されるのではなくスキップされ、サーバー側の応答でこの挙動を変更することはできません。

接続前にもデフォルトで動作するものが2つあり、どちらもオプトアウト可能で、セッションデータは含みません: 匿名のインストールpingと、PyPIに対するバージョンチェックです。デフォルトのインストールでは、起動時のバナー行のためにパブリックIPを1回だけ照会します。すべての送信先、含まれる内容、無効化方法は[docs/EGRESS.md](docs/EGRESS.md)に一覧化されています。セルフホスト型、送信先変更済み、エアギャップ済みのインストールは、任意の送信通信を一切行いません。

復号はブラウザ内で、私たちが提供するコードによって行われます。これはかつては単なる約束事でしたが、今では確認できるものになっています。鍵に触れるすべての行は1つの読みやすいファイル、[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js)に収められており、これはwheelに同梱されそのまま提供され、Subresource Integrityハッシュで固定されています。ブラウザが公開したものと同じコードを実行していることを確認するには:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

これが証明しないこと: 私たちはこのファイルを読み込むページ自体を提供しているため、そのページを別のものにすり替えることは可能です。Integrityハッシュは、侵害されたCDNからは守ってくれますが、提供元自身からは守ってくれません。得られるのは、いかなる差し替えも意図的なものになり、ページのソース上で可視化され、誰でも取得できるPyPI上の成果物とは異なるものになる、ということです。セルフホストまたはローカルのみで運用すれば、この依存関係自体がなくなります。

## インストール

```bash
pip install clawmetry     # then: clawmetry
```

またはワンライナー: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS、Linux、WindowsでPython 3.8以上が必要で、同じマシン上に少なくとも1つのエージェントランタイムが必要です。Dockerでの手順は[docs/DOCKER.md](docs/DOCKER.md)を参照してください。

エージェントにセットアップさせることもできます。[`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)スキルは、Claude Code、Codex、Cursor、Gemini CLI、Copilot、OpenCodeに対して、ClawMetryのインストール方法、マシン上のエージェントが何をしていて何を消費しているかの報告方法、要求に応じたセッションの停止方法、承認待ちのために危険なツール呼び出しを保留する方法を教えます:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## ドキュメント

| | |
|---|---|
| [ランタイム対応表](docs/compatibility.md) | 各アダプターが何を読み取るか、そしてランタイムを追加する方法 |
| [コンテキスト膨張](docs/CONTEXT_BLOWOUT.md) | プロバイダーごとのウィンドウ、compaction対オーバーフロー、ランタイムごとのカバレッジ |
| [オーバーヘッド](docs/OVERHEAD.md) | 計装にかかる実測コストと、再現用のハーネス |
| [Entitlements](docs/ENTITLEMENTS.md) | 無料と有料の違い、ティア表、ライセンスCLI |
| [承認とポリシー](docs/APPROVALS.md) | 実行前ゲーティング、リスクスコアリング、スマートフォン承認 |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | どこへでもトレースをエクスポート、どこからでもOTLPを取り込み |
| [独自エージェントの持ち込み](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore、Pydantic AI、LangChainをエンドツーエンドで、実行可能な例付き |
| [SDKトラッキング](docs/SDK_TRACKING.md) | 自作エージェントのコスト帰属 |
| [チャットチャネル](docs/CHANNELS.md) | Flowに表示されるチャットアダプター |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | サンドボックス化されたNVIDIA NemoClawのセットアップ |
| [Docker](docs/DOCKER.md) | イメージ、compose、ボリュームマウント |
| [アーキテクチャ](ARCHITECTURE.md) · [開発](docs/DEVELOPMENT.md) | 内部の仕組み、ソースからの実行方法 |
| [テレメトリ](docs/TELEMETRY.md) | 匿名のインストール・デスクトップ起動pingと、その無効化方法 |

## スクリーンショット

以下の数値はすべて、何も種を仕込んでいない実際のマシン1台から、読み取り専用で取得したものです。

**何が起きたかだけでなく、何が問題かを教えてくれます。**
上部に2つの異常バナー: 支出が日次平均の7倍で推移していること、そして4.2倍のコスト急増。その下には、直近667セッション中324セッションが原因別に分類された無駄シグナルを含んでいることが表示されています。

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**お金がどこへ行ったのかを、あらゆる期間で示します。**
今日$252.47、今週$513.15、今月$1,312.92、それぞれの背後にあるトークン数と、すでにサブスクリプションでカバーされている割合とともに表示されます。その下には、月あたり約$1,128分の回収可能な無駄と、キャッシュ再利用によりすでに節約された月あたり$17,256が項目別に表示されます。

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**メッセージがどのように回答になるかを図示します。**
ライブフロー図: あなた、メッセージが届いたチャネル、ゲートウェイ、現在回答しているモデル、そしてそれが使ったすべてのツール。作業が進むにつれてノードが点灯します。

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**マシン上のすべてのエージェントが1つの表に。**
実行しているもの、過去24時間と累計のコスト、最終確認日時、所有者、そしてサブスクリプションで料金がカバーされているかどうか。ここでは14のエージェント、稼働中の3セッション、静止中の13セッションが表示されています。

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**1ターンの時間とお金がツールごとにどこへ行ったかを示します。**
実際のセッションの1ターン: 11.2分で11個のツールを使い$1.16。すべてのBash呼び出しとモデル呼び出しがタイムライン上に自分の棒グラフを持つため、4.1分かかったコマンドと226ミリ秒で終わったコマンドを一目で見分けられます。

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**支出だけでなく、作業の質を評価します。**
今週の評価はA: 54件のタスクがきれいに完了し、2件の粗い実行に$48.57かかりました。判断材料になるほどの活動量がない実行は、勝ちとしてカウントされるのではなく評価から除外されます。各粗い実行はそのトレースにリンクされています。

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**なぜコンテキストウィンドウが埋まり続けるのかを示します。**
直近のターンで100万トークンのウィンドウのうち71.5万トークンを使用、ピーク83.3%、オーバーフローではなくすべてプロアクティブに発火した4回のcompaction、そしてその背後にあるすべてのターンの利用率。

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**設定不要で検知が動作します。**
組み込みの検知器はインストール直後から有効です: エージェントの応答停止、テレメトリフィードの停止、コスト急増、トークンバースト、エラー増加、エラー急増、予算しきい値、脅威シグネチャの一致、セキュリティツールの検出、セキュリティ体制の変化。独自ルールはこの上にオプションで追加できます。

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**危険な呼び出しの保留はオプトインで、初期状態ではオフです。**
再帰的な削除、force push、sudo、シークレット、パッケージインストール、外部への通信呼び出しには、それぞれオンにできるルールがあります。オンにするまでは、ClawMetryは監視するだけで何も変更しません。一度オンにすると、一致する呼び出しはここ(またはスマートフォン)で承認または拒否を待ちます。

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

ランタイムごとの詳細: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md)。

## 評価・受賞

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## スター履歴

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## ライセンス

MIT · Built by [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
