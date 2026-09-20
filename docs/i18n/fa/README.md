<!-- i18n-src:b22579578775 -->
> فارسی translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**یک عامل هوشمند می‌تواند صدها فراخوانی ابزار انجام دهد بدون اینکه پیشرفتی حاصل شود.** ClawMetry
فایل‌های نشستی را که عامل‌های کدنویسی شما از قبل می‌نویسند می‌خواند، و جدول زمانی،
فراخوانی‌های ابزار و هر داده توکن و هزینه‌ای که هسته اجرایی افشا می‌کند را در یک
نما قرار می‌دهد — تا بتوانید یک اجرای طولانی که در حال کار کردن است را از اجرایی که گیر کرده تشخیص دهید.

با **۳۲ هسته اجرایی عامل هوش مصنوعی** کار می‌کند — Claude Code، OpenAI Codex، Hermes، OpenClaw و ۲۸ مورد دیگر. یک داشبورد برای کل ناوگان عامل‌های شما. ([فهرست کامل](SUPPORTED_RUNTIMES.txt)، تولید شده از کاتالوگ.)

> 🌐 **این متن را به این زبان‌ها بخوانید:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [بیشتر ←](docs/i18n/)

یک دستور. بدون پیکربندی. همه‌چیز را به‌طور خودکار شناسایی می‌کند.

```bash
pip install clawmetry && clawmetry
```

در **http://localhost:8900** باز می‌شود. بدون پیکربندی: هسته‌های اجرایی عاملی را که از قبل دارید پیدا می‌کند، آن‌ها را فقط به‌صورت خواندنی می‌خواند، و چیزی را در نحوه اجرای آن‌ها تغییر نمی‌دهد.

![داشبورد ClawMetry: هر هسته اجرایی عامل هوش مصنوعی روی یک ماشین به همراه هزینه ۲۴ ساعته و کل عمر به ازای هر عامل](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## قبل از نصب

| | |
|---|---|
| **این ابزار چه کاری انجام می‌دهد** | فایل‌های نشست و لاگ‌هایی را که عامل‌های شما از قبل می‌نویسند می‌خواند. بدون SDK، بدون تغییر کد، بدون ابزارسازی درون برنامه شما. |
| **چه چیزی می‌بینید** | جدول زمانی نشست، بازپخش ابزار به ابزار، تفکیک توکن و هزینه، و سیگنال‌های مسیر حرکت (حلقه زدن، شکست‌های تکراری) — به ازای هر هسته اجرایی. |
| **چه چیزی رایگان است** | `pip install clawmetry` قابلیت خواندن **OpenClaw، NVIDIA NemoClaw، Goose و Qwen Code** را بدون نیاز به حساب کاربری، کلید یا فراخوانی شبکه فراهم می‌کند. ۲۸ مورد دیگر — Claude Code، Codex، Cursor و بقیه — توسط همراه بسته‌منبع `clawmetry-pro` خوانده می‌شوند، که همراه با دوره آزمایشی ۷ روزه یا یک پلن ارائه می‌شود — برای تفکیک دقیق به [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) مراجعه کنید. |
| **چگونه شروع کنیم** | `pip install clawmetry && clawmetry`، سپس localhost:8900 را باز کنید. هنوز هیچ عاملی روی این ماشین ندارید؟ `clawmetry --sample` با سه نشست مصنوعی برچسب‌گذاری‌شده باز می‌شود. |
| **چه چیزی از ماشین شما خارج می‌شود** | هیچ داده نشستی، مگر اینکه `clawmetry connect` را اجرا کنید. دو چیز به‌طور پیش‌فرض اجرا می‌شوند، هر دو قابل غیرفعال‌سازی و هیچ‌کدام حامل محتوای نشست نیستند: یک پینگ نصب ناشناس و یک بررسی نسخه در PyPI. هر مقصد در [docs/EGRESS.md](docs/EGRESS.md) فهرست شده، که از یک ضبط ترافیک شبکه بازسازی شده نه از خواندن کامنت‌ها. |

دو محدودیت که ارزش دانستن قبل از قضاوت درباره خروجی را دارند: هسته‌های اجرایی داده‌های بسیار
متفاوتی را افشا می‌کنند (برخی اصلاً هیچ هزینه‌ای منتشر نمی‌کنند — [جدول تطبیق](docs/compatibility.md)
می‌گوید کدام‌یک، به ازای هر هسته اجرایی)، و رصد کردن یک اقدام به معنای توانایی مسدود کردن
آن نیست ([کدام کنترل‌ها واقعی هستند، به ازای هر هسته اجرایی](docs/APPROVALS.md)).


## با ۳۲ هسته اجرایی عامل کار می‌کند

**رایگان در برنامه متن‌باز:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**در یک پلن پولی:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

همه هسته‌های اجرایی همان داشبورد را دریافت می‌کنند. چندین مورد را همزمان اجرا کنید و
سوییچر بالای صفحه هر تب را دوباره به یکی از آن‌ها محدود می‌کند.

عامل خودتان را با استفاده از یک SDK ساخته‌اید؟ رهگیر (interceptor) فراخوانی‌های LLM آن را
نیز ردیابی می‌کند. به [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md) مراجعه کنید.

## چه چیزی به دست می‌آورید

- **نشست‌ها و رونوشت‌ها**: هر عامل چه کاری انجام داد، نوبت به نوبت، همراه با بازپخش
- **هزینه و توکن‌ها**: به ازای هر هسته اجرایی، مدل، نشست و روز، همراه با پرچم‌های ناهنجاری
- **جریان**: نمودار زنده پیام‌هایی که از کانال‌ها، مدل‌ها و ابزارها عبور می‌کنند
- **مغز (Brain)**: جریان رویداد استدلال و فراخوانی ابزار همان‌طور که رخ می‌دهد
- **انفجار زمینه (Context blowout)**: استفاده از پنجره اندازه‌گیری‌شده به ازای هر ارائه‌دهنده، فشرده‌سازی در مقابل سرریز اجباری، به‌علاوه نقشه‌ای به ازای هر هسته اجرایی از آنچه *نمی‌توانیم* ببینیم ([چگونه](docs/CONTEXT_BLOWOUT.md))
- **حافظه و مهارت‌ها**: فایل‌ها و مهارت‌هایی که هر هسته اجرایی واقعاً بارگذاری کرده است
- **سلامت و لاگ‌ها**: دیسک، حافظه، نرخ خطا، محدودیت‌های نرخ، جریان زنده لاگ
- **هشدارها**: سقف بودجه، افزایش خطا، آفلاین شدن عامل، ارسال شده به Slack، Discord، PagerDuty، Telegram، ایمیل
- **تأییدها**: توقف فراخوانی‌های ابزار پرریسک *قبل* از اجرا و تأیید از گوشی خود ([چگونه](docs/APPROVALS.md))

## انفجار زمینه، و هزینه رصد کردن آن

دو سؤال که ارزش پاسخ دادن قبل از اعتماد به هر ابزار مقایسه عامل را دارند.

**چگونه انفجار پنجره زمینه را در بین هسته‌های اجرایی مدیریت می‌کند؟**

درصد استفاده تنها به اندازه صداقت مخرجی که بر آن تقسیم می‌شود، صادق است. ClawMetry
اندازه پنجره را به ازای هر ارائه‌دهنده از [جدولی که می‌توانید بخوانید و
درخواست ادغام (PR) بدهید](clawmetry/context_windows.py) تعیین می‌کند،
که Anthropic، OpenAI، Google، xAI،
DeepSeek، Kimi، Qwen، Mistral، Llama و GLM را پوشش می‌دهد. تمام ۳۲
هسته اجرایی را با خط‌کش یک فروشنده اندازه‌گیری نمی‌کند. این مهم است: یک نوبت ۳۰۰ هزار توکنی GPT-5 که
در برابر ۲۰۰ هزار توکن Anthropic سنجیده شود ">۱۰۰٪، منفجر شده" خوانده می‌شود در حالی که در واقع در ۷۵٪ از
۴۰۰ هزار توکن GPT-5 است. همین خط‌کش یک نوبت DeepSeek واقعاً سرریزشده با ۱۳۰ هزار توکن را
به‌عنوان یک ۶۵٪ راحت پنهان می‌کند.

هر پنجره با منشأ خود ارسال می‌شود: `model_table`، `explicit_marker`،
`observed_floor`، یا یک `default` صادقانه زمانی که مدل را نمی‌شناسیم. یک
سنجه ساخته‌شده بر یک حدس هرگز با همان اعتباری که یک سنجه ساخته‌شده بر
یک جست‌وجو رندر می‌شود، نمایش داده نمی‌شود.

ClawMetry فقط می‌تواند رویدادهای فشرده‌سازی را روی برخی هسته‌های اجرایی ببیند. بنابراین
`GET /api/context-coverage` به ازای هر هسته اجرایی گزارش می‌دهد که آیا **صفر به معنای
"تمیز اجرا شد" است یا "ما کور هستیم"**. صفری که واقعاً به معنای کور بودن است، این را اعلام می‌کند.
[جزئیات کامل](docs/CONTEXT_BLOWOUT.md)

**ابزارسازی چقدر هزینه دارد؟**

| مسیر | افزوده شده به عامل شما | پیش‌فرض؟ |
|---|---|---|
| دنبال کردن فایل نشست (هر ۳۲ هسته اجرایی) | **۰**. فرایند جداگانه، بدون کد ClawMetry در عامل شما | روشن |
| رهگیر HTTP (`CLAWMETRY_INTERCEPT=1`) | **+۰.۴۴ میلی‌ثانیه** به ازای هر فراخوانی LLM، یا ۰.۰۰۹٪ از یک فراخوانی ۵ ثانیه‌ای | خاموش |
| دروازه هوک پیش از ابزار (حافظه پنهان گرم) | **+۴۴ میلی‌ثانیه** به ازای هر فراخوانی ابزار دروازه‌بانی‌شده، فراتر از کف ۳۶ میلی‌ثانیه‌ای مفسر | خاموش |
| پروکسی اجرایی | **+۹.۷ میلی‌ثانیه** به ازای هر فراخوانی LLM | خاموش |

هزینه میزبان دیمن: **۲٬۷۶۲ رویداد/ثانیه** دریافت، **۷۱۰ بایت/رویداد** روی دیسک
(۶۷.۷ مگابایت به ازای هر ۱۰۰ هزار رویداد)، و **حدود ۱۲٪ از یک هسته** به‌صورت پایدار روی
یک نصب شلوغ. آن عدد آخر فراتر از بودجه اعلام‌شده خودمان یعنی ۵ تا ۱۰٪ است، بنابراین
به‌عنوان یک باگ برای پیگیری منتشر می‌شود، نه اینکه از صفحه حذف شود.

اندازه‌گیری‌شده روی یک Apple M2 Pro با `benchmarks/overhead.py`. این ابزار هر
شرایط را در یک فرایند جداگانه اجرا می‌کند، ترتیب آن‌ها را جابه‌جا می‌کند، و **از چاپ یک
عدد خودداری می‌کند وقتی دورها روی علامت آن توافق نداشته باشند**. آن را روی ماشین خودتان
در یک دقیقه اجرا کنید:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

هر مسیر اندازه‌گیری شده، از جمله دروازه‌های هوک و پروکسی اجرایی،
و این ابزار روی Linux، macOS و Windows در CI اجرا می‌شود. دو نتیجه ارزش
دانستن دارند: پروکسی روی Windows حدود هفت برابر بیشتر از Linux هزینه دارد، و
دیمن در حال حاضر حدود ۱۲٪ از یک هسته را پایدار نگه می‌دارد، فراتر از بودجه
۵ تا ۱۰٪ خودمان. JSON خام، روش، و آنچه هنوز اندازه‌گیری نشده در
[docs/OVERHEAD.md](docs/OVERHEAD.md) است.

## قیمت‌گذاری

| پلن | چه چیزی را پوشش می‌دهد | قیمت |
|---|---|---|
| **رایگان** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code، داشبورد کامل، فقط محلی | ۰ دلار |
| **Starter** | هر هسته اجرایی دیگری که در بالا ذکر شد، نمای ناوگان، همگام‌سازی ابری | ۹ دلار به ازای هر گره / ماه |
| **Pro** | Starter + کنترل و ارزیابی: تأییدها، سیاست‌های ریسک ابزار، ارزیابی‌ها، تشخیص ناهنجاری، بهینه‌ساز هزینه، صادرات OTel، لاگ حسابرسی ضدتغییر | ۱۹ دلار به ازای هر گره / ماه |

پلن‌های سالانه، Enterprise و اعداد فعلی در
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** موجود است. کلیدهای مجوز خودمیزبانی‌شده
بدون نیاز به ابر کار می‌کنند (`clawmetry license`). تفکیک دقیق رایگان/پولی
در [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) است.

## داده‌های شما روی ماشین خودتان باقی می‌ماند

ClawMetry فایل‌های نشست و لاگ‌های محلی را می‌خواند. **هیچ داده نشستی از جعبه شما خارج نمی‌شود
مگر اینکه `clawmetry connect` را اجرا کنید** — بدون درخواست‌ها، پاسخ‌ها، آرگومان‌های ابزار، محتوای
فایل یا خطوط لاگ. زمانی که متصل می‌شوید، عکس فوری با رمزنگاری سرتاسر
با کلیدی که هرگز از ماشین شما خارج نمی‌شود رمزگذاری می‌شود، و در مرورگر شما رمزگشایی می‌شود. اگر یک
گره کلیدی نداشته باشد، بارگذاری به جای ارسال به‌صورت رمزگشایی‌نشده، رد می‌شود، و هیچ
پاسخ سروری نمی‌تواند این را خاموش کند.

دو چیز به‌طور پیش‌فرض قبل از اتصال شما اجرا می‌شوند، هر دو قابل غیرفعال‌سازی و هیچ‌کدام
حامل داده نشست نیستند: یک پینگ نصب ناشناس و یک بررسی نسخه در برابر
PyPI. یک نصب پیش‌فرض همچنین یک‌بار IP عمومی شما را برای یک خط بنر شروع
جست‌وجو می‌کند. هر مقصد، چه چیزی حمل می‌کند و چگونه آن را خاموش کنیم در
[docs/EGRESS.md](docs/EGRESS.md) فهرست شده است؛ نصب‌های خودمیزبانی‌شده، تغییرمسیریافته و ایزوله از شبکه
هیچ فراخوانی خروجی اختیاری انجام نمی‌دهند.

رمزگشایی در مرورگر شما، در کدی که به شما ارائه می‌دهیم، انجام می‌شود. این قبلاً
یک وعده بود؛ اکنون چیزی است که می‌توانید بررسی کنید. هر خطی که کلید شما را لمس می‌کند
در یک فایل قابل‌خواندن زندگی می‌کند، [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js)،
که درون wheel ارسال می‌شود و کلمه به کلمه ارائه می‌شود، پین‌شده با یک هش Subresource
Integrity. برای تأیید اینکه مرورگر چیزی را اجرا می‌کند که ما منتشر کرده‌ایم:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

آنچه این ثابت نمی‌کند: ما صفحه‌ای را ارائه می‌دهیم که فایل را بارگذاری می‌کند، بنابراین می‌توانیم
صفحه متفاوتی را ارائه دهیم. هش‌های Integrity از شما در برابر یک CDN به‌خطرافتاده محافظت می‌کنند،
نه در برابر فروشنده. آنچه به دست می‌آورید این است که هر جایگزینی باید
عمدی، قابل مشاهده در سورس صفحه، و متفاوت از یک artifact در PyPI باشد
که هر کسی می‌تواند آن را واکشی کند. خودمیزبانی یا ماندن فقط-محلی این
وابستگی را کاملاً حذف می‌کند.

## نصب

```bash
pip install clawmetry     # سپس: clawmetry
```

یا دستور تک‌خطی: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

نیاز به Python 3.8+ روی macOS، Linux یا Windows، و حداقل یک هسته اجرایی عامل روی
همان ماشین دارد. دستورالعمل‌های Docker: [docs/DOCKER.md](docs/DOCKER.md).

یا بگذارید عامل آن را برای شما راه‌اندازی کند. مهارت [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
به Claude Code، Codex، Cursor، Gemini CLI، Copilot یا OpenCode یاد می‌دهد که
ClawMetry را نصب کند، گزارش دهد عامل‌های روی ماشین چه کاری انجام می‌دهند و چقدر خرج می‌کنند،
یک نشست را با درخواست متوقف کند، و فراخوانی‌های ابزار پرریسک را برای تأیید نگه دارد:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## مستندات

| | |
|---|---|
| [سازگاری هسته اجرایی](docs/compatibility.md) | هر آداپتور چه چیزی را می‌خواند، و چگونه یک هسته اجرایی اضافه کنیم |
| [انفجار زمینه](docs/CONTEXT_BLOWOUT.md) | پنجره‌ها به ازای هر ارائه‌دهنده، فشرده‌سازی در مقابل سرریز، پوشش به ازای هر هسته اجرایی |
| [سربار](docs/OVERHEAD.md) | ابزارسازی چقدر هزینه دارد، اندازه‌گیری‌شده، همراه با ابزار برای بازتولید آن |
| [مجوزها](docs/ENTITLEMENTS.md) | رایگان در مقابل پولی، ماتریس سطح، CLI مجوز |
| [تأییدها و سیاست‌ها](docs/APPROVALS.md) | دروازه‌بانی پیش از اجرا، امتیازدهی ریسک، تأییدهای تلفنی |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | صادرات ترِیس‌ها به هر جا، دریافت OTLP از هر چیزی |
| [عامل خودتان را بیاورید](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore، Pydantic AI، LangChain سرتاسر، همراه با نمونه‌های قابل اجرا |
| [ردیابی SDK](docs/SDK_TRACKING.md) | انتساب هزینه برای عامل‌هایی که خودتان ساخته‌اید |
| [کانال‌های چت](docs/CHANNELS.md) | آداپتورهای چت نمایش داده شده در Flow |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | راه‌اندازی‌های ایزوله NVIDIA NemoClaw |
| [Docker](docs/DOCKER.md) | تصویر، compose، مانت‌های حجم |
| [معماری](ARCHITECTURE.md) · [توسعه](docs/DEVELOPMENT.md) | چگونگی کارکرد درونی آن؛ اجرا از سورس |
| [تله‌متری](docs/TELEMETRY.md) | پینگ‌های ناشناس نصب و باز شدن دسکتاپ، و چگونگی خاموش کردن آن‌ها |

## اسکرین‌شات‌ها

هر عدد در زیر از یک ماشین واقعی است، فقط-خواندنی، بدون هیچ داده اولیه‌ای.

**زمانی که چیزی اشتباه است به شما می‌گوید، نه فقط آنچه رخ داده.**
دو بنر ناهنجاری در بالا: هزینه‌ای که ۷ برابر میانگین روزانه در حال اجراست، و یک
جهش هزینه ۴.۲ برابری. زیر آن‌ها، ۳۲۴ نشست از ۶۶۷ نشست اخیر که سیگنال
اتلاف حمل می‌کنند، جزئیات به تفکیک علت.

![نمای کلی: بنرهای ناهنجاری هزینه و جهش هزینه روی کار زنده عامل](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**به شما نشان می‌دهد پول کجا رفته، در هر بازه زمانی.**
۲۵۲.۴۷ دلار امروز، ۵۱۳.۱۵ دلار این هفته، ۱٬۳۱۲.۹۲ دلار این ماه، هرکدام همراه با توکن‌های
پشت آن و اینکه اشتراک شما در حال حاضر چقدر از آن را پوشش می‌دهد. زیر آن، حدود
۱٬۱۲۸ دلار/ماه به‌عنوان قابل‌بازیابی جزئیات داده شده و ۱۷٬۲۵۶ دلار/ماه که قبلاً با استفاده مجدد از
حافظه پنهان صرفه‌جویی شده است.

![هزینه: امروز، این هفته و این ماه، همراه با یک نمره کارایی و ایده‌های صرفه‌جویی جزئیات‌دار](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**نشان می‌دهد چگونه یک پیام به یک پاسخ تبدیل می‌شود.**
نمودار جریان زنده: شما، کانالی که پیام روی آن رسیده، دروازه، مدلی که
همین الان پاسخ می‌دهد، و هر ابزاری که به آن دست یافته است. گره‌ها با حرکت کار
از میان آن‌ها روشن می‌شوند.

![جریان: نمودار زنده از شما از میان دروازه به مدل و ابزارهای آن](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**هر عامل روی ماشین، در یک جدول.**
چه اجرا می‌کند، چقدر در ۲۴ ساعت گذشته و در طول عمر خود هزینه دارد، چه زمانی
آخرین بار دیده شده، چه کسی مالک آن است، و آیا یک اشتراک هزینه آن را پوشش می‌دهد.
۱۴ عامل اینجا، ۳ نشست در حال کار، ۱۳ ساکت.

![عامل‌ها: هر هسته اجرایی روی ماشین همراه با هزینه، مالک، آخرین دیده شدن و کار فعلی](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**نشان می‌دهد زمان و پول یک نوبت به کجا رفته، ابزار به ابزار.**
یک نوبت از یک نشست واقعی: ۱۱ ابزار در ۱۱.۲ دقیقه به قیمت ۱.۱۶ دلار. هر فراخوانی Bash
و فراخوانی مدل نوار خودش را روی جدول زمانی دریافت می‌کند، بنابراین دستوری که ۴.۱ دقیقه
اجرا شده و دستوری که ۲۲۶ میلی‌ثانیه اجرا شده در یک نگاه از هم تشخیص داده می‌شوند.

![نشست‌ها: یک نوبت عامل روی جدول زمانی، هر فراخوانی ابزار همراه با مدت زمان خودش و هزینه نوبت](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**کار را نمره می‌دهد، نه فقط هزینه را.**
یک A این هفته: ۵۴ وظیفه بدون مشکل بازگشتند، ۲ اجرای ناهموار ۴۸.۵۷ دلار هزینه داشتند، و
اجراهایی که فعالیت خیلی کمی برای قضاوت داشتند به جای شمرده شدن به‌عنوان برد، از نمره
کنار گذاشته شده‌اند. هر اجرای ناهموار به ردیابی خودش لینک می‌شود.

![کیفیت: کارنامه این هفته همراه با اجراهای ناهموار و هزینه آن‌ها](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**نشان می‌دهد چرا پنجره زمینه همچنان در حال پر شدن است.**
۷۱۵ هزار توکن از یک پنجره ۱ میلیون توکنی در آخرین نوبت، یک اوج ۸۳.۳٪، ۴ فشرده‌سازی
که همگی به‌طور پیشگیرانه به جای سرریز فعال شدند، و استفاده هر نوبت
پشت آن.

![استفاده از زمینه: استفاده از پنجره به ازای هر نوبت، رویدادهای فشرده‌سازی و توکن‌های بازپس‌گرفته‌شده](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**تشخیص بدون پیکربندی توسط شما اجرا می‌شود.**
آشکارسازهای داخلی از نصب روشن هستند: عامل ساکت شده، فید تله‌متری
متوقف شده، جهش هزینه، انفجار توکن، افزایش خطاها، جهش خطا، آستانه
بودجه، امضای تهدید مطابقت‌یافته، یافته ابزار امنیتی، وضعیت امنیتی
تغییر یافته. قوانین خودتان به‌صورت اختیاری روی این‌ها اضافه می‌شوند.

![هشدارها: آشکارسازهای داخلی به‌علاوه قوانین سفارشی اختیاری](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**نگه داشتن یک فراخوانی پرریسک اختیاری است، و به‌صورت خاموش ارسال می‌شود.**
حذف‌های بازگشتی، push اجباری، sudo، اسرار، نصب بسته‌ها و فراخوانی‌های
خروجی هرکدام یک قانون دریافت می‌کنند که می‌توانید روشن کنید. تا زمانی که این کار را نکنید،
ClawMetry نظارت می‌کند و چیزی را تغییر نمی‌دهد. زمانی که یکی روشن شود، فراخوانی‌های
مطابق اینجا (یا روی گوشی شما) منتظر تأیید یا رد می‌مانند.

![تأییدها: قوانین حفاظتی برای فراخوانی‌های ابزار پرریسک، همه خاموش تا زمانی که آن‌ها را فعال کنید](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

بیشتر، به ازای هر هسته اجرایی: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## قدردانی‌ها

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## تاریخچه ستاره‌ها

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## مجوز

MIT · ساخته شده توسط [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
