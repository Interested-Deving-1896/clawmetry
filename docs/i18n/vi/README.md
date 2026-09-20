<!-- i18n-src:b22579578775 -->
> Tiếng Việt translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**Một agent có thể thực hiện hàng trăm lệnh gọi công cụ mà không đạt được tiến triển nào.** ClawMetry
đọc các tệp phiên làm việc mà các agent lập trình của bạn đã ghi sẵn, và đưa dòng thời gian,
các lệnh gọi công cụ, cùng bất kỳ dữ liệu token và chi phí nào mà runtime cung cấp vào một
giao diện duy nhất — để bạn có thể phân biệt một tiến trình dài đang hoạt động tốt với một tiến trình đang bị kẹt.

Hoạt động với **32 runtime agent AI** — Claude Code, OpenAI Codex, Hermes, OpenClaw & 28 runtime khác. Một bảng điều khiển cho toàn bộ đội ngũ agent của bạn. ([danh sách đầy đủ](SUPPORTED_RUNTIMES.txt), được tạo tự động từ danh mục.)

> 🌐 **Đọc bằng ngôn ngữ khác:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [thêm →](docs/i18n/)

Một lệnh duy nhất. Không cần cấu hình. Tự động phát hiện mọi thứ.

```bash
pip install clawmetry && clawmetry
```

Mở tại **http://localhost:8900**. Không cần cấu hình: nó tìm ra các runtime agent
bạn đã có sẵn, đọc chúng ở chế độ chỉ đọc, và không thay đổi bất cứ điều gì về cách chúng chạy.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## Trước khi cài đặt

| | |
|---|---|
| **Nó làm gì** | Đọc các tệp phiên làm việc và log mà các agent của bạn đã ghi sẵn. Không cần SDK, không cần thay đổi code, không cần instrumentation trong ứng dụng của bạn. |
| **Bạn thấy gì** | Dòng thời gian phiên làm việc, phát lại từng công cụ, phân tích token và chi phí, và các tín hiệu quỹ đạo (lặp vòng, lặp lại lỗi) — theo từng runtime. |
| **Miễn phí gồm những gì** | `pip install clawmetry` đọc được **OpenClaw, NVIDIA NemoClaw, Goose và Qwen Code** mà không cần tài khoản, không cần key và không cần gọi mạng. 28 runtime còn lại — Claude Code, Codex, Cursor và các runtime khác — được đọc bởi companion mã nguồn đóng `clawmetry-pro`, đi kèm với bản dùng thử 7 ngày hoặc một gói trả phí — xem [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) để biết chi tiết phân chia chính xác. |
| **Cách bắt đầu** | `pip install clawmetry && clawmetry`, sau đó mở localhost:8900. Chưa có agent nào trên máy này? `clawmetry --sample` sẽ mở với ba phiên tổng hợp được gắn nhãn sẵn. |
| **Điều gì rời khỏi máy của bạn** | Không có dữ liệu phiên làm việc nào, trừ khi bạn chạy `clawmetry connect`. Có hai thứ chạy mặc định, cả hai đều có thể tắt và không mang theo nội dung phiên làm việc: một ping cài đặt ẩn danh và một lần kiểm tra phiên bản PyPI. Mọi điểm đến đều được liệt kê trong [docs/EGRESS.md](docs/EGRESS.md), được xây dựng lại từ việc bắt gói tin thay vì từ việc đọc comment trong code. |

Có hai giới hạn đáng biết trước khi bạn đánh giá kết quả: các runtime cung cấp
dữ liệu rất khác nhau (một số không công bố chi phí nào cả — [bảng ma trận](docs/compatibility.md)
cho biết runtime nào, theo từng runtime), và việc quan sát một hành động không giống với việc có thể
chặn nó ([những điều khiển nào là thật, theo từng runtime](docs/APPROVALS.md)).


## Hoạt động với 32 runtime agent

**Miễn phí trong ứng dụng mã nguồn mở:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**Trong gói trả phí:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

Mọi runtime đều nhận được cùng một bảng điều khiển. Chạy nhiều runtime cùng lúc và
bộ chuyển ở phần đầu sẽ định phạm vi lại mọi tab về một trong số chúng.

Đã tự xây agent của riêng bạn trên một SDK thay vì runtime có sẵn? Bộ chặn (interceptor) cũng theo dõi
các lệnh gọi LLM của agent đó. Xem [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## Bạn nhận được gì

- **Phiên làm việc & bản ghi**: từng agent đã làm gì, theo từng lượt, có thể phát lại
- **Chi phí & token**: theo từng runtime, mô hình, phiên làm việc và ngày, kèm cờ báo bất thường
- **Flow**: sơ đồ trực tiếp về luồng tin nhắn di chuyển qua các kênh, mô hình và công cụ
- **Brain**: luồng sự kiện suy luận và gọi công cụ ngay khi nó xảy ra
- **Bùng nổ ngữ cảnh (Context blowout)**: mức sử dụng cửa sổ ngữ cảnh được tính theo từng nhà cung cấp, so sánh nén ngữ cảnh (compaction) với tràn bộ nhớ cưỡng bức, cùng bản đồ theo từng runtime về những gì chúng ta *không thể* thấy ([cách thức](docs/CONTEXT_BLOWOUT.md))
- **Bộ nhớ & kỹ năng**: các tệp và kỹ năng mà mỗi runtime thực sự đã tải
- **Sức khỏe & log**: ổ đĩa, bộ nhớ, tỷ lệ lỗi, giới hạn tốc độ, luồng log trực tiếp
- **Cảnh báo**: giới hạn ngân sách, tăng vọt lỗi, agent ngoại tuyến, định tuyến đến Slack, Discord, PagerDuty, Telegram, Email
- **Phê duyệt**: tạm dừng các lệnh gọi công cụ rủi ro *trước khi* chúng chạy và phê duyệt từ điện thoại của bạn ([cách thức](docs/APPROVALS.md))

## Bùng nổ ngữ cảnh, và cái giá của việc theo dõi nó

Có hai câu hỏi đáng trả lời trước khi bạn tin tưởng bất kỳ công cụ so sánh agent nào.

**Nó xử lý việc bùng nổ cửa sổ ngữ cảnh (context-window blowout) trên các runtime khác nhau như thế nào?**

Tỷ lệ sử dụng chỉ trung thực khi mẫu số của nó đúng. ClawMetry
tính kích thước cửa sổ theo từng nhà cung cấp từ [một bảng bạn có thể đọc và
gửi PR](clawmetry/context_windows.py), bao gồm Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama và GLM. Nó không đo cả 32
runtime bằng thước đo của một nhà cung cấp duy nhất. Điều này quan trọng: một lượt GPT-5 300K token
được chấm điểm theo tiêu chuẩn 200K của Anthropic sẽ đọc là ">100%, đã bùng nổ" trong khi thực tế nó chỉ đạt 75% của
mức 400K của GPT-5. Cùng một thước đo đó lại che giấu một lượt DeepSeek 130K thực sự đã tràn
như một mức 65% thoải mái.

Mỗi cửa sổ đều đi kèm nguồn gốc của nó: `model_table`, `explicit_marker`,
`observed_floor`, hoặc một mức `default` trung thực khi chúng ta không biết mô hình đó. Một
đồng hồ đo được xây dựng dựa trên phỏng đoán sẽ không bao giờ hiển thị với cùng độ tin cậy như một
đồng hồ được xây dựng dựa trên tra cứu.

ClawMetry chỉ có thể thấy các sự kiện nén ngữ cảnh (compaction) trên một số runtime nhất định. Vì vậy
`GET /api/context-coverage` báo cáo, theo từng runtime, liệu **giá trị 0 có nghĩa là "chạy sạch" hay
"chúng ta bị mù"**. Một giá trị `0` thực sự có nghĩa là bị mù thì sẽ nói rõ như vậy.
[Chi tiết đầy đủ](docs/CONTEXT_BLOWOUT.md)

**Việc instrumentation tốn kém bao nhiêu?**

| Đường dẫn | Thêm vào agent của bạn | Mặc định? |
|---|---|---|
| Theo dõi tệp phiên làm việc (cả 32 runtime) | **0**. Tiến trình riêng biệt, không có code ClawMetry nào trong agent của bạn | bật |
| Bộ chặn HTTP (`CLAWMETRY_INTERCEPT=1`) | **+0.44 ms** cho mỗi lệnh gọi LLM, hay 0.009% của một lệnh gọi 5 giây | tắt |
| Cổng hook trước-công-cụ (bộ nhớ đệm ấm) | **+44 ms** cho mỗi lệnh gọi công cụ được gác cổng, trên nền 36 ms của trình thông dịch | tắt |
| Proxy thực thi | **+9.7 ms** cho mỗi lệnh gọi LLM | tắt |

Chi phí máy chủ daemon: **2.762 sự kiện/giây** khi thu nạp, **710 byte/sự kiện** trên đĩa
(67.7 MB cho mỗi 100k sự kiện), và **~12% của một lõi CPU** duy trì trên một
cài đặt bận rộn. Con số cuối cùng đó vượt quá ngân sách 5-10% mà chúng tôi tự đặt ra, nên nó
được công bố như một lỗi cần khắc phục thay vì bị giấu đi.

Được đo trên một Apple M2 Pro bằng `benchmarks/overhead.py`. Bộ đo chạy
mỗi điều kiện trong một tiến trình riêng biệt, luân phiên thứ tự của chúng, và **từ chối
in ra một con số khi các vòng đo không thống nhất về dấu của nó**. Chạy thử ngay trên
máy của bạn trong một phút:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

Mọi đường dẫn đều được đo, bao gồm cả các cổng hook và proxy thực thi,
và bộ đo chạy trên Linux, macOS và Windows trong CI. Có hai kết quả đáng biết:
proxy tốn kém gấp khoảng bảy lần trên Windows so với trên Linux, và
daemon hiện đang duy trì khoảng 12% của một lõi CPU, vượt quá ngân sách 5-10% mà chúng tôi tự đặt ra.
Dữ liệu JSON gốc, phương pháp đo, và những gì vẫn chưa được đo có trong
[docs/OVERHEAD.md](docs/OVERHEAD.md).

## Giá cả

| Gói | Bao gồm những gì | Giá |
|---|---|---|
| **Miễn phí** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, bảng điều khiển đầy đủ, chỉ chạy cục bộ | $0 |
| **Starter** | Tất cả các runtime khác ở trên, chế độ xem đội ngũ (fleet view), đồng bộ hóa đám mây | $9 mỗi node / tháng |
| **Pro** | Starter + điều khiển và đánh giá: phê duyệt, chính sách rủi ro công cụ, đánh giá (evals), phát hiện bất thường, tối ưu chi phí, xuất OTel, nhật ký kiểm toán chống giả mạo | $19 mỗi node / tháng |

Các gói hàng năm, gói Enterprise và giá hiện tại có tại
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**. Các key giấy phép tự lưu trữ
hoạt động mà không cần đám mây (`clawmetry license`). Phân chia chính xác giữa miễn phí/trả phí
có trong [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md).

## Dữ liệu của bạn ở lại trên máy của bạn

ClawMetry đọc các tệp phiên làm việc và log cục bộ. **Không có dữ liệu phiên làm việc nào rời khỏi máy của bạn
trừ khi bạn chạy `clawmetry connect`** — không có prompt, phản hồi, tham số công cụ, nội dung tệp
hay dòng log nào cả. Khi bạn kết nối, ảnh chụp nhanh (snapshot) được mã hóa đầu-cuối
với một key không bao giờ rời khỏi máy của bạn, và được giải mã ngay trong trình duyệt của bạn. Nếu một
node không có key, việc tải lên sẽ bị bỏ qua thay vì gửi ở dạng không mã hóa, và không có
phản hồi máy chủ nào có thể tắt điều đó.

Có hai thứ chạy mặc định trước khi bạn kết nối, cả hai đều có thể tắt và không
mang theo dữ liệu phiên làm việc: một ping cài đặt ẩn danh và một lần kiểm tra phiên bản so với
PyPI. Một lần cài đặt mặc định cũng tra cứu địa chỉ IP công khai của bạn một lần cho dòng banner khởi động.
Mọi điểm đến, những gì nó mang theo và cách tắt nó được liệt kê trong
[docs/EGRESS.md](docs/EGRESS.md); các bản cài đặt tự lưu trữ, định tuyến lại và cách ly mạng
không thực hiện bất kỳ lệnh gọi ra ngoài tùy ý nào cả.

Việc giải mã diễn ra ngay trong trình duyệt của bạn, bằng code chúng tôi cung cấp cho bạn. Điều này từng
chỉ là một lời hứa; giờ đây nó là điều bạn có thể kiểm chứng. Mọi dòng code chạm vào key của bạn
đều nằm trong một tệp dễ đọc duy nhất, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
được đóng gói bên trong wheel và phục vụ nguyên văn, được ghim với một hash Subresource
Integrity. Để xác nhận trình duyệt chạy đúng những gì chúng tôi đã công bố:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

Điều đó không chứng minh được: chúng tôi phục vụ trang tải tệp đó, vì vậy chúng tôi có thể
phục vụ một trang khác. Các hash integrity bảo vệ bạn khỏi một CDN bị xâm nhập,
chứ không phải khỏi nhà cung cấp. Điều bạn đạt được là bất kỳ sự thay thế nào cũng phải
cố ý, hiển thị rõ trong mã nguồn trang, và khác với artifact trên PyPI
mà bất kỳ ai cũng có thể tải về. Việc tự lưu trữ hoặc chỉ dùng cục bộ sẽ loại bỏ hoàn toàn
sự phụ thuộc này.

## Cài đặt

```bash
pip install clawmetry     # sau đó: clawmetry
```

Hoặc lệnh một dòng: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

Cần Python 3.8+ trên macOS, Linux hoặc Windows, và ít nhất một runtime agent trên
cùng máy đó. Hướng dẫn Docker: [docs/DOCKER.md](docs/DOCKER.md).

Hoặc để agent tự cài đặt cho bạn. Kỹ năng [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
dạy Claude Code, Codex, Cursor, Gemini CLI, Copilot hoặc OpenCode cách
cài đặt ClawMetry, báo cáo những gì các agent trên máy đang làm và chi tiêu,
dừng một phiên làm việc theo yêu cầu, và giữ lại các lệnh gọi công cụ rủi ro để chờ phê duyệt:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Tài liệu

| | |
|---|---|
| [Khả năng tương thích runtime](docs/compatibility.md) | Mỗi adapter đọc được gì, và cách thêm một runtime |
| [Bùng nổ ngữ cảnh](docs/CONTEXT_BLOWOUT.md) | Cửa sổ theo từng nhà cung cấp, nén ngữ cảnh so với tràn bộ nhớ, mức độ bao phủ theo từng runtime |
| [Chi phí phát sinh](docs/OVERHEAD.md) | Chi phí của instrumentation, đã được đo, kèm bộ công cụ để tái tạo lại |
| [Quyền hạn (Entitlements)](docs/ENTITLEMENTS.md) | Miễn phí so với trả phí, ma trận các gói, CLI giấy phép |
| [Phê duyệt & chính sách](docs/APPROVALS.md) | Gác cổng trước khi thực thi, chấm điểm rủi ro, phê duyệt qua điện thoại |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | Xuất trace đến bất cứ đâu, thu nạp OTLP từ bất cứ nguồn nào |
| [Mang theo agent của riêng bạn](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain từ đầu đến cuối, kèm ví dụ chạy được |
| [Theo dõi SDK](docs/SDK_TRACKING.md) | Quy trách nhiệm chi phí cho các agent bạn tự xây dựng |
| [Kênh chat](docs/CHANNELS.md) | Các adapter chat được hiển thị trong Flow |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | Các thiết lập NVIDIA NemoClaw trong sandbox |
| [Docker](docs/DOCKER.md) | Image, compose, gắn volume |
| [Kiến trúc](ARCHITECTURE.md) · [Phát triển](docs/DEVELOPMENT.md) | Cách nó hoạt động bên trong; chạy từ mã nguồn |
| [Telemetry](docs/TELEMETRY.md) | Các ping cài đặt ẩn danh và mở desktop, và cách tắt chúng |

## Ảnh chụp màn hình

Mỗi con số dưới đây đến từ một máy thật, chỉ đọc, không có dữ liệu giả nào được gieo sẵn.

**Nó cho bạn biết khi có gì đó không ổn, không chỉ những gì đã xảy ra.**
Hai banner cảnh báo bất thường ở trên cùng: chi tiêu đang chạy gấp 7 lần mức trung bình hàng ngày, và một
đợt tăng vọt chi phí 4.2 lần. Bên dưới đó, 324 trong số 667 phiên làm việc gần đây mang
tín hiệu lãng phí, được phân loại theo nguyên nhân.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**Nó cho bạn thấy tiền đã đi đâu, trong mọi khung thời gian.**
$252.47 hôm nay, $513.15 tuần này, $1,312.92 tháng này, mỗi khoản đều kèm số token đứng sau nó
và gói đăng ký của bạn đã bao trả bao nhiêu trong số đó. Bên dưới, khoảng $1,128/tháng
được liệt kê là có thể thu hồi và $17,256/tháng đã được tiết kiệm nhờ tái sử dụng cache.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**Nó vẽ ra cách một tin nhắn trở thành một câu trả lời.**
Sơ đồ luồng trực tiếp: bạn, kênh mà tin nhắn đến, gateway, mô hình
đang trả lời ngay lúc này, và mọi công cụ nó đã sử dụng. Các nút sáng lên khi công việc
di chuyển qua chúng.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**Mọi agent trên máy, trong một bảng duy nhất.**
Nó chạy gì, chi phí bao nhiêu trong 24 giờ qua và trong toàn bộ vòng đời, khi nào
nó được thấy lần cuối, ai sở hữu nó, và liệu một gói đăng ký có đang chi trả cho
hóa đơn hay không. 14 agent ở đây, 3 phiên đang hoạt động, 13 phiên yên lặng.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**Nó cho thấy thời gian và tiền bạc của một lượt làm việc đã đi đâu, theo từng công cụ.**
Một lượt của một phiên làm việc thực tế: 11 công cụ trong 11.2 phút với giá $1.16. Mỗi lệnh gọi
Bash và lệnh gọi mô hình đều có thanh riêng trên dòng thời gian, để lệnh chạy
trong 4.1 phút và lệnh chạy trong 226ms được phân biệt chỉ bằng một cái nhìn.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**Nó chấm điểm công việc, không chỉ chi tiêu.**
Điểm A trong tuần này: 54 tác vụ hoàn thành sạch sẽ, 2 lượt gập ghềnh tốn $48.57, và các
lượt có quá ít hoạt động để đánh giá được loại ra khỏi điểm số thay vì được tính là thành công.
Mỗi lượt gập ghềnh liên kết đến trace của nó.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**Nó cho thấy tại sao cửa sổ ngữ cảnh cứ tiếp tục đầy lên.**
715K trong cửa sổ 1M token ở lượt gần nhất, đỉnh 83.3%, 4 lần nén ngữ cảnh
đều được kích hoạt chủ động thay vì do tràn bộ nhớ, cùng mức sử dụng của
mọi lượt đứng sau nó.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**Việc phát hiện chạy mà không cần bạn cấu hình gì cả.**
Các bộ phát hiện tích hợp sẵn được bật ngay từ khi cài đặt: agent im lặng, luồng telemetry
dừng lại, chi phí tăng vọt, bùng nổ token, lỗi tăng dần, tăng vọt lỗi, ngưỡng
ngân sách, khớp chữ ký mối đe dọa, phát hiện từ công cụ bảo mật, thay đổi tư thế bảo mật.
Các quy tắc của riêng bạn là tùy chọn bổ sung thêm vào.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**Việc giữ lại một lệnh gọi rủi ro là tùy chọn, và mặc định tắt.**
Xóa đệ quy, force push, sudo, secret, cài đặt gói và các lệnh gọi ra ngoài
mỗi loại đều có một quy tắc bạn có thể bật. Cho đến khi bạn bật, ClawMetry chỉ quan sát và
không thay đổi gì cả. Một khi được bật, các lệnh gọi khớp sẽ chờ ở đây (hoặc trên điện thoại của bạn)
để được phê duyệt hoặc từ chối.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

Thêm nữa, theo từng runtime: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## Ghi nhận

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Lịch sử Star

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## Giấy phép

MIT · Xây dựng bởi [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
