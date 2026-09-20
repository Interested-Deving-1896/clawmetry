<!-- i18n-src:b22579578775 -->
> اردو translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**ایک ایجنٹ بغیر کسی پیش رفت کے سو ٹول کالز کر سکتا ہے۔** ClawMetry آپ کے کوڈنگ ایجنٹس کی پہلے سے لکھی ہوئی سیشن فائلوں کو پڑھتا ہے، اور ٹائم لائن، ٹول کالز اور رن ٹائم کی جانب سے ظاہر کیے جانے والے ٹوکن اور لاگت کے ڈیٹا کو ایک ہی منظر میں جمع کرتا ہے، تاکہ آپ ایک کامیابی سے چلنے والی طویل رن کو ایک اٹکی ہوئی رن سے پہچان سکیں۔

**32 AI ایجنٹ رن ٹائمز** کے ساتھ کام کرتا ہے، Claude Code، OpenAI Codex، Hermes، OpenClaw اور 28 مزید۔ آپ کے پورے ایجنٹ فلیٹ کے لیے ایک ہی ڈیش بورڈ۔ ([مکمل فہرست](SUPPORTED_RUNTIMES.txt)، کیٹلاگ سے خودکار طور پر تیار کردہ۔)

> 🌐 **اسے اس زبان میں پڑھیں:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [مزید →](docs/i18n/)

ایک کمانڈ۔ کوئی کنفیگریشن نہیں۔ سب کچھ خودکار طور پر پہچان لیتا ہے۔

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** پر کھلتا ہے۔ کوئی کنفیگریشن درکار نہیں: یہ آپ کے پہلے سے موجود ایجنٹ رن ٹائمز کو ڈھونڈتا ہے، انہیں صرف پڑھنے کے موڈ میں پڑھتا ہے، اور ان کے چلنے کے طریقے میں کچھ بھی تبدیل نہیں کرتا۔

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## انسٹال کرنے سے پہلے

| | |
|---|---|
| **یہ کیا کرتا ہے** | آپ کے ایجنٹس کی پہلے سے لکھی ہوئی سیشن فائلوں اور لاگز کو پڑھتا ہے۔ کوئی SDK نہیں، کوڈ میں کوئی تبدیلی نہیں، آپ کی ایپ میں کوئی انسٹرومینٹیشن نہیں۔ |
| **آپ کیا دیکھتے ہیں** | سیشن ٹائم لائن، ٹول بہ ٹول ری پلے، ٹوکن اور لاگت کی تفصیل، اور رجحان کے اشارے (لوپنگ، بار بار ناکامیاں)، ہر رن ٹائم کے لیے۔ |
| **کیا مفت ہے** | `pip install clawmetry` بغیر کسی اکاؤنٹ، کسی کلید یا کسی نیٹ ورک کال کے **OpenClaw، NVIDIA NemoClaw، Goose اور Qwen Code** کو پڑھتا ہے۔ باقی 28، یعنی Claude Code، Codex، Cursor اور دیگر، کو کلوز سورس `clawmetry-pro` ساتھی ذریعے پڑھا جاتا ہے، جو 7 دن کے ٹرائل یا کسی پلان کے ساتھ آتا ہے۔ درست تقسیم کے لیے دیکھیں [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)۔ |
| **شروع کیسے کریں** | `pip install clawmetry && clawmetry`، پھر localhost:8900 کھولیں۔ اس مشین پر ابھی کوئی ایجنٹ نہیں؟ `clawmetry --sample` تین لیبل شدہ مصنوعی سیشنز کے ساتھ کھلتا ہے۔ |
| **آپ کی مشین سے کیا باہر جاتا ہے** | کوئی سیشن ڈیٹا نہیں، جب تک آپ `clawmetry connect` نہ چلائیں۔ دو چیزیں بطور ڈیفالٹ چلتی ہیں، دونوں آپٹ آؤٹ کرنے کے قابل اور کوئی بھی سیشن مواد نہیں لے جاتیں: ایک گمنام انسٹال پنگ اور ایک PyPI ورژن چیک۔ ہر منزل [docs/EGRESS.md](docs/EGRESS.md) میں درج ہے، جو تبصروں کو پڑھنے کے بجائے ایک وائر کیپچر سے دوبارہ تیار کی گئی ہے۔ |

فیصلہ کرنے سے پہلے دو حدود جاننا ضروری ہیں: رن ٹائمز بہت مختلف ڈیٹا ظاہر کرتے ہیں (کچھ کوئی لاگت بالکل شائع نہیں کرتے، [میٹرکس](docs/compatibility.md) بتاتا ہے کہ کون سا رن ٹائم کیا دکھاتا ہے)، اور کسی عمل کا مشاہدہ کرنا اسے روکنے کی صلاحیت رکھنے کے برابر نہیں ہے ([فی رن ٹائم کون سے کنٹرولز حقیقی ہیں](docs/APPROVALS.md))۔


## 32 ایجنٹ رن ٹائمز کے ساتھ کام کرتا ہے

**اوپن سورس ایپ میں مفت:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**ایک ادا شدہ پلان پر:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

ہر رن ٹائم کو ایک ہی ڈیش بورڈ ملتا ہے۔ ایک ساتھ کئی چلائیں اور ہیڈر سوئچر ہر ٹیب کو ان میں سے کسی ایک کے دائرے میں دوبارہ ترتیب دے گا۔

کیا آپ نے کسی SDK پر اپنا ایجنٹ خود بنایا ہے؟ انٹرسیپٹر اس کی LLM کالز بھی ٹریک کرتا ہے۔ دیکھیں [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)۔

## آپ کو کیا ملتا ہے

- **سیشنز اور ٹرانسکرپٹس**: ہر ایجنٹ نے کیا کیا، باری بہ باری، ری پلے کے ساتھ
- **لاگت اور ٹوکنز**: رن ٹائم، ماڈل، سیشن اور دن کے حساب سے، اسامانیتا کے نشانات کے ساتھ
- **فلو**: چینلز، ماڈلز اور ٹولز کے درمیان حرکت کرتے پیغامات کا لائیو ڈایاگرام
- **برین**: استدلال اور ٹول کال کے واقعات کا سلسلہ جیسے ہی وہ ہوتا ہے
- **کانٹیکسٹ بلو آؤٹ**: ہر فراہم کنندہ کے لحاظ سے ونڈو کا استعمال، کمپیکشن بمقابلہ زبردستی اوورفلو، ساتھ ہی یہ نقشہ کہ ہر رن ٹائم میں ہم کیا *نہیں* دیکھ سکتے ([کیسے](docs/CONTEXT_BLOWOUT.md))
- **میموری اور مہارتیں**: وہ فائلیں اور مہارتیں جو ہر رن ٹائم نے واقعی لوڈ کیں
- **صحت اور لاگز**: ڈسک، میموری، خرابی کی شرح، ریٹ لمٹس، لائیو لاگ سلسلہ
- **الرٹس**: بجٹ کی حدیں، خرابی میں اضافہ، ایجنٹ آف لائن، جو Slack، Discord، PagerDuty، Telegram، Email پر بھیجے جاتے ہیں
- **منظوریاں**: خطرناک ٹول کالز کو چلنے *سے پہلے* روکیں اور اپنے فون سے منظور کریں ([کیسے](docs/APPROVALS.md))

## کانٹیکسٹ بلو آؤٹ، اور نگرانی کی قیمت

دو سوالات جو کسی بھی ایجنٹ موازنہ کرنے والے ٹول پر بھروسہ کرنے سے پہلے جاننا ضروری ہیں۔

**یہ رن ٹائمز کے درمیان کانٹیکسٹ ونڈو بلو آؤٹ کو کیسے سنبھالتا ہے؟**

استعمال کا فیصد اتنا ہی درست ہوتا ہے جتنا کہ وہ عدد جس سے اسے تقسیم کیا جاتا ہے۔ ClawMetry ہر فراہم کنندہ کے لیے ونڈو کا سائز ایک ایسی [ٹیبل](clawmetry/context_windows.py) سے لیتا ہے جسے آپ پڑھ سکتے اور ترمیم کے لیے PR بھیج سکتے ہیں، جس میں Anthropic، OpenAI، Google، xAI، DeepSeek، Kimi، Qwen، Mistral، Llama اور GLM شامل ہیں۔ یہ تمام 32 رن ٹائمز کو ایک ہی فراہم کنندہ کے پیمانے سے نہیں ناپتا۔ یہ اہم ہے: Anthropic کے 200K کے مقابلے میں ماپی گئی 300K GPT-5 باری ">100%، بلو آؤٹ" پڑھتی ہے جبکہ درحقیقت وہ GPT-5 کے 400K کا 75% ہے۔ وہی پیمانہ ایک حقیقتاً اوورفلو ہو چکی 130K DeepSeek باری کو ایک آرام دہ 65% کے طور پر چھپاتا ہے۔

ہر ونڈو اپنی اصلیت کے ساتھ آتی ہے: `model_table`، `explicit_marker`، `observed_floor`، یا جب ہمیں ماڈل معلوم نہ ہو تو ایک ایماندار `default`۔ اندازے پر بنایا گیا گیج کبھی بھی اس اتھارٹی کے ساتھ رینڈر نہیں ہوتا جو ایک لُک اپ پر بنائے گئے گیج کو حاصل ہوتی ہے۔

ClawMetry صرف کچھ رن ٹائمز پر کمپیکشن واقعات دیکھ سکتا ہے۔ اس لیے `GET /api/context-coverage` ہر رن ٹائم کے لیے یہ رپورٹ کرتا ہے کہ آیا **صفر کا مطلب ہے "صاف چلا" یا "ہم اندھے ہیں"**۔ ایک `0` جس کا اصل مطلب اندھا ہونا ہے، وہ ایسا ہی بتاتا ہے۔
[مکمل تفصیل](docs/CONTEXT_BLOWOUT.md)

**انسٹرومینٹیشن کی قیمت کیا ہے؟**

| راستہ | آپ کے ایجنٹ میں شامل ہوا | ڈیفالٹ؟ |
|---|---|---|
| سیشن فائل ٹیلنگ (تمام 32 رن ٹائمز) | **0**۔ الگ پراسیس، آپ کے ایجنٹ میں کوئی ClawMetry کوڈ نہیں | آن |
| HTTP انٹرسیپٹر (`CLAWMETRY_INTERCEPT=1`) | فی LLM کال **+0.44 ms**، یا 5 سیکنڈ کی کال کا 0.009% | آف |
| پری ٹول ہک گیٹ (گرم کیش) | 36 ms کے انٹرپریٹر فرش کے اوپر، فی گیٹڈ ٹول کال **+44 ms** | آف |
| انفورسمنٹ پراکسی | فی LLM کال **+9.7 ms** | آف |

ڈیمن ہوسٹ کی قیمت: **2,762 واقعات فی سیکنڈ** انجیسٹ، ڈسک پر **710 بائٹس فی واقعہ** (100 ہزار واقعات کے لیے 67.7 MB)، اور مصروف انسٹال پر مستقل طور پر **ایک کور کا تقریباً 12%**۔ وہ آخری عدد ہمارے اپنے بتائے گئے 5-10% بجٹ سے زیادہ ہے، اس لیے اسے صفحے سے ہٹانے کے بجائے ایک ایسے بگ کے طور پر شائع کیا گیا ہے جسے حل کرنا ہے۔

Apple M2 Pro پر `benchmarks/overhead.py` کے ذریعے ناپا گیا۔ ہارنس ہر حالت کو الگ پراسیس میں چلاتا ہے، ان کی ترتیب کو بدلتا رہتا ہے، اور **جب راؤنڈز کسی عدد کی علامت پر متفق نہ ہوں تو اسے چھاپنے سے انکار کر دیتا ہے**۔ اسے اپنی ہی مشین پر ایک منٹ میں چلائیں:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

ہر راستہ ناپا گیا ہے، بشمول ہک گیٹس اور انفورسمنٹ پراکسی، اور ہارنس CI میں Linux، macOS اور Windows پر چلتا ہے۔ جاننے کے قابل دو نتائج: پراکسی کی قیمت Windows پر Linux کے مقابلے میں تقریباً سات گنا زیادہ ہے، اور ڈیمن اس وقت ایک کور کے تقریباً 12% کو مستقل طور پر برداشت کرتا ہے، جو ہمارے اپنے 5-10% بجٹ سے زیادہ ہے۔ خام JSON، طریقہ کار، اور جو ابھی تک ناپا نہیں گیا وہ [docs/OVERHEAD.md](docs/OVERHEAD.md) میں ہے۔

## قیمتیں

| پلان | یہ کیا شامل کرتا ہے | قیمت |
|---|---|---|
| **مفت** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code، مکمل ڈیش بورڈ، صرف لوکل | $0 |
| **Starter** | اوپر دیے گئے باقی تمام رن ٹائمز، فلیٹ ویو، کلاؤڈ سنک | $9 فی نوڈ / ماہ |
| **Pro** | Starter + کنٹرول اور جانچ: منظوریاں، ٹول رسک پالیسیاں، ایویلز، اسامانیتا کی شناخت، لاگت کا بہتر کنندہ، OTel ایکسپورٹ، ٹیمپر ایویڈنٹ آڈٹ لاگ | $19 فی نوڈ / ماہ |

سالانہ پلانز، Enterprise اور موجودہ اعداد و شمار
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** پر موجود ہیں۔ سیلف ہوسٹڈ لائسنس
کلیدیں کلاؤڈ کے بغیر کام کرتی ہیں (`clawmetry license`)۔ مفت/ادا شدہ کی درست تقسیم
[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) میں ہے۔

## آپ کا ڈیٹا آپ کی مشین پر ہی رہتا ہے

ClawMetry مقامی سیشن فائلوں اور لاگز کو پڑھتا ہے۔ **کوئی سیشن ڈیٹا آپ کے باکس سے باہر نہیں جاتا
جب تک آپ `clawmetry connect` نہ چلائیں**، یعنی کوئی پرامپٹس، جوابات، ٹول کے دلائل، فائل
کا مواد یا لاگ لائنیں نہیں۔ جب آپ کنیکٹ کرتے ہیں، تو اسنیپ شاٹ ایک ایسی کلید سے
اینڈ ٹو اینڈ خفیہ کیا جاتا ہے جو کبھی آپ کی مشین سے باہر نہیں جاتی، اور آپ کے براؤزر میں ڈی کرپٹ ہوتا ہے۔ اگر کسی
نوڈ کے پاس کوئی کلید نہ ہو، تو اپ لوڈ کو صاف متن میں بھیجنے کے بجائے چھوڑ دیا جاتا ہے، اور کوئی
سرور ردعمل اسے بند نہیں کر سکتا۔

کنیکٹ کرنے سے پہلے دو چیزیں بطور ڈیفالٹ چلتی ہیں، دونوں آپٹ آؤٹ کرنے کے قابل اور کوئی
سیشن ڈیٹا نہیں لے جاتیں: ایک گمنام انسٹال پنگ اور PyPI کے خلاف ایک ورژن چیک۔ ایک ڈیفالٹ انسٹال
اسٹارٹ اپ بینر لائن کے لیے آپ کا عوامی IP بھی ایک بار تلاش کرتا ہے۔ ہر منزل، وہ کیا لے جاتی ہے اور اسے کیسے بند کیا جائے، سب
[docs/EGRESS.md](docs/EGRESS.md) میں درج ہے؛ سیلف ہوسٹڈ، دوبارہ منسلک اور ایئر گیپڈ انسٹالز
کوئی بھی اختیاری بیرونی کالز بالکل نہیں کرتیں۔

ڈی کرپشن آپ کے براؤزر میں، اس کوڈ میں ہوتی ہے جو ہم آپ کو فراہم کرتے ہیں۔ یہ پہلے
ایک وعدہ تھا؛ اب یہ ایک ایسی چیز ہے جسے آپ خود جانچ سکتے ہیں۔ ہر لائن جو آپ کی کلید کو چھوتی ہے
ایک قابل مطالعہ فائل، [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js) میں موجود ہے،
جو وہیل کے اندر شپ ہوتی ہے اور جوں کی توں فراہم کی جاتی ہے، ایک سب ریسورس
انٹیگریٹی ہیش کے ساتھ پن کی گئی۔ یہ تصدیق کرنے کے لیے کہ براؤزر وہی چلاتا ہے جو ہم نے شائع کیا:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

یہ کیا ثابت نہیں کرتا: ہم وہ صفحہ فراہم کرتے ہیں جو فائل کو لوڈ کرتا ہے، لہذا ہم ایک
مختلف صفحہ بھی فراہم کر سکتے تھے۔ انٹیگریٹی ہیشز آپ کو ایک سمجھوتہ شدہ CDN سے
تحفظ دیتی ہیں، فراہم کنندہ سے نہیں۔ آپ کو جو حاصل ہوتا ہے وہ یہ ہے کہ کسی بھی تبدیلی کو
جان بوجھ کر ہونا پڑے گا، صفحے کے ماخذ میں نظر آنا پڑے گا، اور PyPI پر موجود کسی چیز سے مختلف ہونا پڑے گا
جسے کوئی بھی حاصل کر سکتا ہے۔ سیلف ہوسٹنگ یا صرف لوکل رہنا اس انحصار کو مکمل طور پر ختم کر دیتا ہے۔

## انسٹال

```bash
pip install clawmetry     # پھر: clawmetry
```

یا ون لائنر: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS، Linux یا Windows پر Python 3.8+ درکار ہے، اور اسی مشین پر کم از کم ایک ایجنٹ رن ٹائم۔
Docker کی ہدایات: [docs/DOCKER.md](docs/DOCKER.md)۔

یا ایجنٹ کو خود آپ کے لیے سیٹ اپ کرنے دیں۔ [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
مہارت Claude Code، Codex، Cursor، Gemini CLI، Copilot یا OpenCode کو
ClawMetry انسٹال کرنا، مشین پر موجود ایجنٹس کیا کر رہے ہیں اور خرچ کر رہے ہیں اس کی رپورٹ دینا،
درخواست پر ایک سیشن روکنا، اور خطرناک ٹول کالز کو منظوری کے لیے روک کر رکھنا سکھاتی ہے:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## دستاویزات

| | |
|---|---|
| [رن ٹائم مطابقت](docs/compatibility.md) | ہر ایڈاپٹر کیا پڑھتا ہے، اور ایک رن ٹائم کیسے شامل کریں |
| [کانٹیکسٹ بلو آؤٹ](docs/CONTEXT_BLOWOUT.md) | فی فراہم کنندہ ونڈوز، کمپیکشن بمقابلہ اوورفلو، فی رن ٹائم کوریج |
| [اووَرہیڈ](docs/OVERHEAD.md) | انسٹرومینٹیشن کی قیمت کیا ہے، ناپی گئی، اسے دوبارہ پیدا کرنے والے ہارنس کے ساتھ |
| [Entitlements](docs/ENTITLEMENTS.md) | مفت بمقابلہ ادا شدہ، ٹئیر میٹرکس، لائسنس CLI |
| [منظوریاں اور پالیسیاں](docs/APPROVALS.md) | عمل سے پہلے کی جانچ، رسک اسکورنگ، فون سے منظوریاں |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | ٹریسز کہیں بھی ایکسپورٹ کریں، کسی بھی چیز سے OTLP انجیسٹ کریں |
| [اپنا ایجنٹ لائیں](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore، Pydantic AI، LangChain سرے سے آخر تک، چلائے جانے کے قابل مثالوں کے ساتھ |
| [SDK ٹریکنگ](docs/SDK_TRACKING.md) | آپ کے خود بنائے گئے ایجنٹس کے لیے لاگت کی نسبت |
| [چیٹ چینلز](docs/CHANNELS.md) | وہ چیٹ ایڈاپٹرز جو فلو میں دکھائے جاتے ہیں |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | سینڈ باکسڈ NVIDIA NemoClaw سیٹ اپس |
| [Docker](docs/DOCKER.md) | امیج، کمپوز، والیوم ماؤنٹس |
| [آرکیٹیکچر](ARCHITECTURE.md) · [ڈیویلپمنٹ](docs/DEVELOPMENT.md) | یہ اندر سے کیسے کام کرتا ہے؛ ماخذ سے چلانا |
| [ٹیلی میٹری](docs/TELEMETRY.md) | گمنام انسٹال اور ڈیسک ٹاپ اوپن پنگز، اور انہیں کیسے بند کریں |

## اسکرین شاٹس

نیچے دیا گیا ہر عدد ایک حقیقی مشین سے ہے، صرف پڑھنے کے موڈ میں، بغیر کسی بیج ڈیٹا کے۔

**یہ آپ کو بتاتا ہے کہ کب کچھ غلط ہے، صرف یہ نہیں کہ کیا ہوا۔**
اوپر دو اسامانیتا بینرز: روزانہ اوسط کے 7 گنا خرچ، اور لاگت میں 4.2 گنا اضافہ۔
ان کے نیچے، حالیہ 667 سیشنز میں سے 324 ایک ضیاع کا اشارہ لے کر، وجہ کے لحاظ سے تقسیم شدہ۔

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**یہ آپ کو دکھاتا ہے کہ پیسہ کہاں گیا، ہر ونڈو میں۔**
آج $252.47، اس ہفتے $513.15، اس مہینے $1,312.92، ہر ایک کے پیچھے موجود ٹوکنز اور
آپ کا سبسکرپشن پہلے ہی کتنا احاطہ کرتا ہے کے ساتھ۔ اس کے نیچے، تقریباً $1,128/ماہ کو قابل بازیابی کے طور پر تفصیل سے
اور کیش کے دوبارہ استعمال سے پہلے ہی بچائے گئے تقریباً $17,256/ماہ۔

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**یہ دکھاتا ہے کہ ایک پیغام کیسے جواب بنتا ہے۔**
لائیو فلو ڈایاگرام: آپ، وہ چینل جس پر یہ پہنچا، گیٹ وے، ابھی جواب دینے والا ماڈل،
اور ہر وہ ٹول جسے اس نے استعمال کیا۔ جیسے جیسے کام ان سے گزرتا ہے، نوڈز روشن ہوتے ہیں۔

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**مشین پر موجود ہر ایجنٹ، ایک ہی ٹیبل میں۔**
یہ کیا چلاتا ہے، پچھلے 24 گھنٹوں میں اور اپنی پوری زندگی میں اس کی لاگت کیا ہے، آخری بار
کب دیکھا گیا، مالک کون ہے، اور آیا کوئی سبسکرپشن بل کا احاطہ کر رہا ہے۔ یہاں 14 ایجنٹس، 3 سیشنز
کام کر رہے ہیں، 13 خاموش۔

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**یہ دکھاتا ہے کہ ایک باری کا وقت اور پیسہ کہاں گیا، ٹول بہ ٹول۔**
ایک حقیقی سیشن کی ایک باری: 11.2 منٹ میں 11 ٹولز کی قیمت $1.16۔ ہر Bash
کال اور ماڈل کال کو ٹائم لائن پر اپنی الگ پٹی ملتی ہے، تاکہ 4.1 منٹ تک چلنے والی کمانڈ اور
226ms تک چلنے والی کمانڈ کو ایک نظر میں الگ پہچانا جا سکے۔

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**یہ کام کو گریڈ دیتا ہے، صرف خرچ کو نہیں۔**
اس ہفتے ایک A: 54 کام صاف ستھرے واپس آئے، 2 مشکل کاموں کی قیمت $48.57 رہی، اور
جن رنز میں فیصلہ کرنے کے لیے کافی سرگرمی نہیں تھی انہیں گریڈ میں شمار کیے جانے کے بجائے چھوڑ دیا گیا۔
ہر مشکل رن اپنے ٹریس سے منسلک ہے۔

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**یہ دکھاتا ہے کہ کانٹیکسٹ ونڈو کیوں بھرتی رہتی ہے۔**
آخری باری میں 1M ٹوکن ونڈو میں سے 715K، 83.3% کی چوٹی، 4 کمپیکشنز جو سب
اوورفلو کے بجائے پیشگی طور پر فائر ہوئیں، اور ان کے پیچھے ہر باری کا استعمال۔

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**آپ کے کچھ بھی کنفیگر کیے بغیر شناخت کا عمل چلتا ہے۔**
بلٹ ان ڈیٹیکٹرز انسٹال سے ہی آن ہوتے ہیں: ایجنٹ خاموش ہو گیا، ٹیلی میٹری فیڈ
رک گئی، لاگت میں اضافہ، ٹوکن کا اچانک اضافہ، خرابیوں میں اضافہ، خرابی کا اچانک اضافہ، بجٹ کی
حد، خطرے کے دستخط سے مماثلت، سیکیورٹی ٹول کی تلاش، سیکیورٹی کی حالت میں تبدیلی۔ آپ کے اپنے
قواعد اوپر سے اختیاری ہیں۔

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**خطرناک کال کو روکنا اختیاری ہے، اور بند حالت میں شپ ہوتا ہے۔**
ریکرسیو ڈیلیٹس، فورس پُش، sudo، سیکرٹس، پیکج انسٹالز اور بیرونی کالز میں سے ہر ایک کے
لیے ایک قاعدہ ہے جسے آپ آن کر سکتے ہیں۔ جب تک آپ ایسا نہ کریں، ClawMetry دیکھتا رہتا ہے اور
کچھ بھی تبدیل نہیں کرتا۔ ایک بار کوئی قاعدہ آن ہو جائے، تو مماثل کالز یہاں (یا آپ کے فون پر) منظوری یا
انکار کے لیے انتظار کرتی ہیں۔

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

مزید، فی رن ٹائم: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md)۔

## پہچان

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## اسٹار ہسٹری

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## لائسنس

MIT · [@vivekchand](https://github.com/vivekchand) کی جانب سے بنایا گیا · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
