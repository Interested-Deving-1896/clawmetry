<!-- i18n-src:b22579578775 -->
> বাংলা translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**একটি এজেন্ট অগ্রগতি ছাড়াই শতাধিক টুল কল করতে পারে।** ClawMetry
আপনার কোডিং এজেন্টগুলো যে সেশন ফাইল আগে থেকেই লিখে রাখে, সেগুলো পড়ে এবং টাইমলাইন,
টুল কল ও রানটাইম যে টোকেন ও খরচের তথ্য প্রকাশ করে তা একটি একক
ভিউতে নিয়ে আসে — যাতে আপনি বুঝতে পারেন কোন দীর্ঘ রান কাজ করছে আর কোনটা আটকে গেছে।

**৩২টি AI এজেন্ট রানটাইমের সাথে কাজ করে** — Claude Code, OpenAI Codex, Hermes, OpenClaw এবং আরও ২৮টি। আপনার পুরো এজেন্ট ফ্লিটের জন্য একটি ড্যাশবোর্ড। ([সম্পূর্ণ তালিকা](SUPPORTED_RUNTIMES.txt), ক্যাটালগ থেকে জেনারেট করা।)

> 🌐 **এটি পড়ুন:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [আরও →](docs/i18n/)

একটি কমান্ড। কোনো কনফিগারেশন নেই। সবকিছু স্বয়ংক্রিয়ভাবে সনাক্ত করে।

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** এ খোলে। কোনো কনফিগারেশন নেই: এটি আপনার কাছে আগে থেকেই থাকা এজেন্ট রানটাইমগুলো খুঁজে বের করে, সেগুলোকে শুধুমাত্র রিড-অনলি মোডে পড়ে, এবং সেগুলো কীভাবে চলে তার কিছুই পরিবর্তন করে না।

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## ইনস্টল করার আগে

| | |
|---|---|
| **এটি কী করে** | আপনার এজেন্টগুলো আগে থেকেই যে সেশন ফাইল ও লগ লেখে সেগুলো পড়ে। কোনো SDK নেই, কোড পরিবর্তন নেই, আপনার অ্যাপে কোনো ইনস্ট্রুমেন্টেশন নেই। |
| **আপনি কী দেখবেন** | সেশন টাইমলাইন, টুল-বাই-টুল রিপ্লে, টোকেন ও খরচের বিভাজন, এবং ট্র্যাজেক্টরি সিগন্যাল (লুপিং, বারবার ব্যর্থতা) — প্রতিটি রানটাইম অনুযায়ী। |
| **কী ফ্রি** | `pip install clawmetry` কোনো অ্যাকাউন্ট, কী বা নেটওয়ার্ক কল ছাড়াই **OpenClaw, NVIDIA NemoClaw, Goose এবং Qwen Code** পড়ে। বাকি ২৮টি — Claude Code, Codex, Cursor এবং বাকিগুলো — ক্লোজড-সোর্স `clawmetry-pro` কম্প্যানিয়ন দিয়ে পড়া হয়, যা ৭-দিনের ট্রায়াল বা একটি প্ল্যানের সাথে আসে — সঠিক বিভাজনের জন্য দেখুন [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)। |
| **কীভাবে শুরু করবেন** | `pip install clawmetry && clawmetry`, তারপর localhost:8900 খুলুন। এই মেশিনে এখনো কোনো এজেন্ট নেই? `clawmetry --sample` তিনটি লেবেলযুক্ত সিন্থেটিক সেশনে খুলবে। |
| **আপনার মেশিন থেকে কী বের হয়** | কোনো সেশন ডেটা বের হয় না, যদি না আপনি `clawmetry connect` চালান। ডিফল্টভাবে দুটি জিনিস চলে, উভয়ই অপ্ট-আউট করা যায় এবং কোনোটিই সেশন কনটেন্ট বহন করে না: একটি অ্যানোনিমাস ইনস্টল পিং এবং একটি PyPI ভার্সন চেক। প্রতিটি গন্তব্যের তালিকা [docs/EGRESS.md](docs/EGRESS.md)-এ আছে, যা মন্তব্য পড়ার বদলে ওয়্যার ক্যাপচার থেকে পুনর্নির্মিত। |

আপনি আউটপুট বিচার করার আগে জানা দরকার এমন দুটি সীমাবদ্ধতা: রানটাইমগুলো খুবই
ভিন্ন ডেটা প্রকাশ করে (কিছু কোনো খরচই প্রকাশ করে না — [ম্যাট্রিক্স](docs/compatibility.md)
দেখায় কোনটি, প্রতিটি রানটাইম অনুযায়ী), এবং একটি অ্যাকশন পর্যবেক্ষণ করা মানে সেটি
ব্লক করতে পারা নয় ([কোন কন্ট্রোলগুলো আসল, প্রতিটি রানটাইম অনুযায়ী](docs/APPROVALS.md))।


## ৩২টি এজেন্ট রানটাইমের সাথে কাজ করে

**ওপেন সোর্স অ্যাপে ফ্রি:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**পেইড প্ল্যানে:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

প্রতিটি রানটাইম একই ড্যাশবোর্ড পায়। একসাথে একাধিক চালান এবং হেডার
সুইচার প্রতিটি ট্যাবকে সেগুলোর একটিতে রি-স্কোপ করবে।

SDK দিয়ে নিজের এজেন্ট বানিয়েছেন? ইন্টারসেপ্টর সেটার LLM কলও
ট্র্যাক করে। দেখুন [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)।

## আপনি যা পাবেন

- **সেশন ও ট্রান্সক্রিপ্ট**: প্রতিটি এজেন্ট কী করেছে, টার্ন বাই টার্ন, রিপ্লে সহ
- **খরচ ও টোকেন**: প্রতিটি রানটাইম, মডেল, সেশন ও দিন অনুযায়ী, অ্যানোমালি ফ্ল্যাগ সহ
- **ফ্লো**: চ্যানেল, মডেল ও টুলের মধ্য দিয়ে চলমান মেসেজের লাইভ ডায়াগ্রাম
- **ব্রেইন**: রিজনিং এবং টুল-কল ইভেন্ট স্ট্রিম, ঘটার সাথে সাথে
- **কনটেক্সট ব্লোআউট**: প্রোভাইডার অনুযায়ী সাইজ করা উইন্ডো ইউটিলাইজেশন, কমপ্যাকশন বনাম জোরপূর্বক ওভারফ্লো, প্লাস আমরা *কী দেখতে পাই না* তার একটি প্রতি-রানটাইম মানচিত্র ([কীভাবে](docs/CONTEXT_BLOWOUT.md))
- **মেমরি ও স্কিল**: প্রতিটি রানটাইম আসলে কী ফাইল ও স্কিল লোড করেছে
- **স্বাস্থ্য ও লগ**: ডিস্ক, মেমরি, এরর রেট, রেট লিমিট, লাইভ লগ স্ট্রিম
- **অ্যালার্ট**: বাজেট ক্যাপ, এরর স্পাইক, এজেন্ট-অফলাইন, Slack, Discord, PagerDuty, Telegram, Email-এ রুট করা
- **অ্যাপ্রুভাল**: ঝুঁকিপূর্ণ টুল কল *চলার আগে* পজ করুন এবং আপনার ফোন থেকে অনুমোদন করুন ([কীভাবে](docs/APPROVALS.md))

## কনটেক্সট ব্লোআউট, এবং পর্যবেক্ষণের খরচ

যেকোনো এজেন্ট-তুলনা টুলকে বিশ্বাস করার আগে জানা দরকার এমন দুটি প্রশ্ন।

**এটি বিভিন্ন রানটাইম জুড়ে কনটেক্সট-উইন্ডো ব্লোআউট কীভাবে সামলায়?**

একটি ইউটিলাইজেশন পার্সেন্টেজ ততটাই সৎ যতটা তার হর সৎ। ClawMetry
প্রতিটি প্রোভাইডারের জন্য উইন্ডো সাইজ করে [একটি টেবিল থেকে যা আপনি পড়তে এবং
PR করতে পারেন](clawmetry/context_windows.py), যা Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama এবং GLM কভার করে। এটি একটি ভেন্ডরের স্কেল
দিয়ে সব ৩২টি রানটাইম মাপে না। এটি গুরুত্বপূর্ণ: একটি ৩০০K GPT-5 টার্ন
Anthropic-এর ২০০K এর বিপরীতে স্কোর করা হলে ">100%, blown" পড়া যায় যখন এটি আসলে
GPT-5-এর ৪০০K-এর ৭৫% এ আছে। একই স্কেল একটি প্রকৃত ওভারফ্লো হওয়া ১৩০K DeepSeek
টার্নকে একটি আরামদায়ক ৬৫% হিসেবে লুকিয়ে রাখে।

প্রতিটি উইন্ডো তার উৎস সহ আসে: `model_table`, `explicit_marker`,
`observed_floor`, অথবা আমরা মডেল না জানলে একটি সৎ `default`। একটি অনুমানের
উপর নির্মিত গেজ কখনো একটি লুকআপের উপর নির্মিত গেজের মতো একই কর্তৃত্ব নিয়ে
রেন্ডার হয় না।

ClawMetry শুধুমাত্র কিছু রানটাইমে কমপ্যাকশন ইভেন্ট দেখতে পারে। তাই
`GET /api/context-coverage` প্রতিটি রানটাইম অনুযায়ী রিপোর্ট করে যে একটি
**শূন্য মানে "পরিষ্কার চলেছে" নাকি "আমরা অন্ধ"**। একটি `0` যা আসলে অন্ধত্ব
বোঝায় তা সেটাই বলে। [পূর্ণ বিবরণ](docs/CONTEXT_BLOWOUT.md)

**ইন্সট্রুমেন্টেশনের খরচ কত?**

| পথ | আপনার এজেন্টে যোগ হয় | ডিফল্ট? |
|---|---|---|
| সেশন-ফাইল টেইলিং (সব ৩২টি রানটাইম) | **0**। আলাদা প্রসেস, আপনার এজেন্টে কোনো ClawMetry কোড নেই | চালু |
| HTTP ইন্টারসেপ্টর (`CLAWMETRY_INTERCEPT=1`) | প্রতি LLM কলে **+0.44 ms**, অথবা একটি 5s কলের 0.009% | বন্ধ |
| প্রি-টুল হুক গেট (ওয়ার্ম ক্যাশে) | প্রতি গেটেড টুল কলে **+44 ms**, একটি 36 ms ইন্টারপ্রেটার ফ্লোরের উপর | বন্ধ |
| এনফোর্সমেন্ট প্রক্সি | প্রতি LLM কলে **+9.7 ms** | বন্ধ |

ডেমন হোস্ট খরচ: **প্রতি সেকেন্ডে ২,৭৬২টি ইভেন্ট** ইনজেস্ট, ডিস্কে
**প্রতি ইভেন্টে ৭১০ বাইট** (প্রতি ১ লক্ষ ইভেন্টে ৬৭.৭ MB), এবং একটি ব্যস্ত
ইনস্টলে টেকসইভাবে **এক কোরের প্রায় ১২%**। শেষ সংখ্যাটি আমাদের নিজেদের
বলা ৫-১০% বাজেটের চেয়ে বেশি, তাই এটি পাতা থেকে বাদ দেওয়ার বদলে
তাড়া করার মতো একটি বাগ হিসেবে প্রকাশ করা হয়েছে।

Apple M2 Pro-তে `benchmarks/overhead.py` দিয়ে পরিমাপ করা। হার্নেস
প্রতিটি কন্ডিশন আলাদা প্রসেসে চালায়, তাদের ক্রম পরিবর্তন করে, এবং **রাউন্ডগুলো
এর চিহ্নে একমত না হলে একটি সংখ্যা প্রিন্ট করতে অস্বীকার করে**। এক মিনিটে
নিজের মেশিনে এটি চালান:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

হুক গেট এবং এনফোর্সমেন্ট প্রক্সি সহ প্রতিটি পথ পরিমাপ করা হয়েছে,
এবং হার্নেসটি CI-তে Linux, macOS এবং Windows-এ চলে। জানা দরকার এমন দুটি ফলাফল:
Linux-এর তুলনায় Windows-এ প্রক্সির খরচ প্রায় সাত গুণ বেশি, এবং ডেমন
বর্তমানে এক কোরের প্রায় ১২% টেকসই করে, যা আমাদের নিজেদের ৫-১০% বাজেটের
চেয়ে বেশি। কাঁচা JSON, পদ্ধতি, এবং এখনো কী পরিমাপ করা হয়নি তা
[docs/OVERHEAD.md](docs/OVERHEAD.md)-এ আছে।

## প্রাইসিং

| প্ল্যান | এটি কী কভার করে | দাম |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, পূর্ণ ড্যাশবোর্ড, শুধু লোকাল | $0 |
| **Starter** | উপরের বাকি সব রানটাইম, ফ্লিট ভিউ, ক্লাউড সিঙ্ক | নোড প্রতি $9 / মাস |
| **Pro** | Starter + কন্ট্রোল এবং ইভালুয়েশন: অ্যাপ্রুভাল, টুল-রিস্ক পলিসি, ইভাল, অ্যানোমালি ডিটেকশন, কস্ট অপ্টিমাইজার, OTel এক্সপোর্ট, ট্যাম্পার-এভিডেন্ট অডিট লগ | নোড প্রতি $19 / মাস |

বার্ষিক প্ল্যান, Enterprise এবং বর্তমান সংখ্যাগুলো আছে
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**-এ। সেল্ফ-হোস্টেড লাইসেন্স
কী ক্লাউড ছাড়াই কাজ করে (`clawmetry license`)। সঠিক ফ্রি/পেইড বিভাজন
[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)-এ আছে।

## আপনার ডেটা আপনার মেশিনেই থাকে

ClawMetry লোকাল সেশন ফাইল ও লগ পড়ে। **আপনি `clawmetry connect` না চালালে
আপনার বক্স থেকে কোনো সেশন ডেটা বের হয় না** — কোনো প্রম্পট, রিপ্লাই, টুল আর্গুমেন্ট,
ফাইল কনটেন্ট বা লগ লাইন নয়। আপনি কানেক্ট করলে, স্ন্যাপশটটি এমন একটি কী দিয়ে
এন্ড-টু-এন্ড এনক্রিপ্ট করা হয় যা কখনো আপনার মেশিন ছেড়ে যায় না, এবং আপনার
ব্রাউজারে ডিক্রিপ্ট হয়। কোনো নোডে যদি কী না থাকে, আপলোডটি প্লেইন টেক্সটে
পাঠানোর বদলে স্কিপ করা হয়, এবং কোনো সার্ভার রেসপন্স তা বন্ধ করতে পারে না।

কানেক্ট করার আগে ডিফল্টভাবে দুটি জিনিস চলে, উভয়ই অপ্ট-আউট করা যায় এবং কোনোটিই
সেশন ডেটা বহন করে না: একটি অ্যানোনিমাস ইনস্টল পিং এবং PyPI-এর বিপরীতে একটি
ভার্সন চেক। একটি ডিফল্ট ইনস্টল স্টার্টআপ ব্যানার লাইনের জন্য একবার আপনার
পাবলিক IP-ও লুকআপ করে। প্রতিটি গন্তব্য, এটি কী বহন করে এবং কীভাবে বন্ধ করতে হয়
তা তালিকাভুক্ত আছে [docs/EGRESS.md](docs/EGRESS.md)-এ; সেল্ফ-হোস্টেড, রিপয়েন্টেড
এবং এয়ার-গ্যাপড ইনস্টলগুলো একেবারেই কোনো ঐচ্ছিক আউটবাউন্ড কল করে না।

ডিক্রিপশনটি আপনার ব্রাউজারে হয়, আমরা আপনাকে যে কোড দিই তাতে। এটি একসময়
একটি প্রতিশ্রুতি ছিল; এখন এটি এমন কিছু যা আপনি যাচাই করতে পারেন। আপনার কী
স্পর্শ করে এমন প্রতিটি লাইন একটি পঠনযোগ্য ফাইলে থাকে,
[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
যা wheel-এর ভেতরে শিপ হয় এবং হুবহু সার্ভ করা হয়, একটি Subresource
Integrity হ্যাশ দিয়ে পিন করা। ব্রাউজার আমরা যা প্রকাশ করেছি তাই চালাচ্ছে
কিনা নিশ্চিত করতে:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

এটি যা প্রমাণ করে না: আমরা সেই পেজটি সার্ভ করি যা ফাইলটি লোড করে, তাই আমরা
একটি ভিন্ন পেজ সার্ভ করতে পারতাম। ইন্টেগ্রিটি হ্যাশ আপনাকে একটি কম্প্রোমাইজড
CDN থেকে রক্ষা করে, ভেন্ডর থেকে নয়। আপনি যা পান তা হলো যেকোনো প্রতিস্থাপন
ইচ্ছাকৃত, পেজ সোর্সে দৃশ্যমান, এবং যে কেউ ফেচ করতে পারে এমন PyPI-এর একটি
আর্টিফ্যাক্ট থেকে ভিন্ন হতে হবে। সেল্ফ-হোস্টিং বা শুধু-লোকাল থাকা এই
নির্ভরতা সম্পূর্ণভাবে সরিয়ে দেয়।

## ইনস্টল

```bash
pip install clawmetry     # তারপর: clawmetry
```

অথবা এক-লাইনার: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS, Linux বা Windows-এ Python 3.8+ দরকার, এবং একই মেশিনে অন্তত একটি
এজেন্ট রানটাইম। Docker নির্দেশাবলী: [docs/DOCKER.md](docs/DOCKER.md)।

অথবা এজেন্টকেই এটি সেটআপ করতে দিন। [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
স্কিলটি Claude Code, Codex, Cursor, Gemini CLI, Copilot বা OpenCode-কে শেখায়
কীভাবে ClawMetry ইনস্টল করতে হয়, মেশিনের এজেন্টগুলো কী করছে ও খরচ করছে তা
রিপোর্ট করতে হয়, অনুরোধে একটি সেশন থামাতে হয়, এবং ঝুঁকিপূর্ণ টুল কল
অনুমোদনের জন্য ধরে রাখতে হয়:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## ডকুমেন্টেশন

| | |
|---|---|
| [Runtime compatibility](docs/compatibility.md) | প্রতিটি অ্যাডাপ্টার কী পড়ে, এবং কীভাবে একটি রানটাইম যোগ করতে হয় |
| [Context blowout](docs/CONTEXT_BLOWOUT.md) | প্রতি-প্রোভাইডার উইন্ডো, কমপ্যাকশন বনাম ওভারফ্লো, প্রতি-রানটাইম কভারেজ |
| [Overhead](docs/OVERHEAD.md) | ইন্সট্রুমেন্টেশনের খরচ কত, পরিমাপ করা, এবং তা পুনরুৎপাদন করার হার্নেস সহ |
| [Entitlements](docs/ENTITLEMENTS.md) | ফ্রি বনাম পেইড, টায়ার ম্যাট্রিক্স, লাইসেন্স CLI |
| [Approvals & policies](docs/APPROVALS.md) | প্রি-এক্সিকিউশন গেটিং, রিস্ক স্কোরিং, ফোন অ্যাপ্রুভাল |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | যেকোনো জায়গায় ট্রেস এক্সপোর্ট করুন, যেকোনো কিছু থেকে OTLP ইনজেস্ট করুন |
| [Bring your own agent](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain এন্ড টু এন্ড, চালানোর মতো উদাহরণ সহ |
| [SDK tracking](docs/SDK_TRACKING.md) | আপনি নিজে যে এজেন্ট বানিয়েছেন তার খরচ অ্যাট্রিবিউশন |
| [Chat channels](docs/CHANNELS.md) | Flow-এ দেখানো চ্যাট অ্যাডাপ্টারগুলো |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | স্যান্ডবক্সড NVIDIA NemoClaw সেটআপ |
| [Docker](docs/DOCKER.md) | ইমেজ, কম্পোজ, ভলিউম মাউন্ট |
| [Architecture](ARCHITECTURE.md) · [Development](docs/DEVELOPMENT.md) | ভেতরে এটি কীভাবে কাজ করে; সোর্স থেকে চালানো |
| [Telemetry](docs/TELEMETRY.md) | অ্যানোনিমাস ইনস্টল ও ডেস্কটপ-ওপেন পিং, এবং কীভাবে সেগুলো বন্ধ করতে হয় |

## স্ক্রিনশট

নিচের প্রতিটি সংখ্যা একটি বাস্তব মেশিন থেকে, শুধুমাত্র-পঠনযোগ্য, কিছুই বীজ না বুনে।

**এটি আপনাকে বলে কখন কিছু ভুল হচ্ছে, শুধু কী ঘটেছে তা নয়।**
উপরে দুটি অ্যানোমালি ব্যানার: দৈনিক গড়ের ৭ গুণ খরচ চলছে, এবং একটি
৪.২ গুণ কস্ট স্পাইক। তার নিচে, সাম্প্রতিক ৬৬৭টি সেশনের মধ্যে ৩২৪টি একটি
অপচয় সিগন্যাল বহন করছে, কারণ অনুযায়ী তালিকাভুক্ত।

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**এটি আপনাকে দেখায় টাকা কোথায় গেছে, প্রতিটি উইন্ডোতে।**
আজ $252.47, এই সপ্তাহে $513.15, এই মাসে $1,312.92, এর পেছনের টোকেন ও
আপনার সাবস্ক্রিপশন এর কতটা ইতিমধ্যে কভার করে তা সহ। তার নিচে, প্রায়
$1,128/মাস পুনরুদ্ধারযোগ্য হিসেবে আইটেমাইজ করা এবং ক্যাশ রিইউজ দিয়ে
ইতিমধ্যে সেভ হওয়া প্রায় $17,256/মাস।

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**এটি আঁকে কীভাবে একটি মেসেজ একটি উত্তরে পরিণত হয়।**
লাইভ ফ্লো ডায়াগ্রাম: আপনি, যে চ্যানেলে এটি এসেছে, গেটওয়ে, এই মুহূর্তে
উত্তর দিচ্ছে এমন মডেল, এবং এটি যে প্রতিটি টুল ব্যবহার করেছে। কাজ তাদের
মধ্য দিয়ে চলার সাথে সাথে নোডগুলো জ্বলে ওঠে।

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**মেশিনের প্রতিটি এজেন্ট, একটি টেবিলে।**
এটি কী চালায়, গত ২৪ ঘণ্টায় এবং তার সারাজীবনে এটির খরচ কত, এটি সর্বশেষ
কখন দেখা গিয়েছিল, এটির মালিক কে, এবং একটি সাবস্ক্রিপশন বিলটি কভার করছে
কিনা। এখানে ১৪টি এজেন্ট, ৩টি সেশন কাজ করছে, ১৩টি নিরব।

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**এটি দেখায় একটি টার্নের সময় ও টাকা কোথায় গেছে, টুল বাই টুল।**
একটি বাস্তব সেশনের একটি টার্ন: ১১.২ মিনিটে ১১টি টুল, $1.16 খরচে।
প্রতিটি Bash কল এবং মডেল কল টাইমলাইনে নিজস্ব বার পায়, তাই ৪.১ মিনিট
ধরে চলা কমান্ড এবং ২২৬ms ধরে চলা কমান্ড এক নজরেই আলাদা করা যায়।

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**এটি শুধু খরচ নয়, কাজেরও গ্রেড দেয়।**
এই সপ্তাহে একটি A: ৫৪টি কাজ পরিষ্কারভাবে ফিরে এসেছে, ২টি খারাপ কাজের
খরচ হয়েছে $48.57, এবং বিচার করার মতো যথেষ্ট কার্যকলাপ না থাকা রানগুলো
জয় হিসেবে গণনা না করে গ্রেড থেকে বাদ দেওয়া হয়েছে। প্রতিটি খারাপ রান তার
ট্রেসের সাথে লিঙ্ক করা।

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**এটি দেখায় কেন কনটেক্সট উইন্ডো ক্রমাগত ভরে যাচ্ছে।**
সর্বশেষ টার্নে ১M-টোকেন উইন্ডোর ৭১৫K, একটি ৮৩.৩% পিক, ৪টি কমপ্যাকশন
যা সবগুলোই একটি ওভারফ্লোর বদলে সক্রিয়ভাবে ফায়ার হয়েছে, প্লাস এর পেছনের
প্রতিটি টার্নের ইউটিলাইজেশন।

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**আপনার কিছু কনফিগার করা ছাড়াই ডিটেকশন চলে।**
ইনস্টল থেকেই বিল্ট-ইন ডিটেক্টরগুলো চালু: এজেন্ট চুপ হয়ে গেছে, টেলিমেট্রি
ফিড থেমে গেছে, কস্ট স্পাইক, টোকেন বার্স্ট, এরর বাড়ছে, এরর স্পাইক, বাজেট
থ্রেশহোল্ড, থ্রেট সিগনেচার মিলেছে, সিকিউরিটি টুল ফাইন্ডিং, সিকিউরিটি
পসচার পরিবর্তিত হয়েছে। এর উপরে আপনার নিজের রুল ঐচ্ছিক।

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**একটি ঝুঁকিপূর্ণ কল ধরে রাখা অপ্ট-ইন, এবং বন্ধ অবস্থায় শিপ হয়।**
রিকার্সিভ ডিলিট, ফোর্স পুশ, sudo, সিক্রেট, প্যাকেজ ইনস্টল এবং আউটবাউন্ড
কল প্রতিটি একটি রুল পায় যা আপনি চালু করতে পারেন। আপনি না করা পর্যন্ত,
ClawMetry শুধু পর্যবেক্ষণ করে এবং কিছুই পরিবর্তন করে না। একটি চালু করলে,
মিলে যাওয়া কলগুলো এখানে (বা আপনার ফোনে) একটি অনুমোদন বা অস্বীকৃতির জন্য
অপেক্ষা করে।

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

আরও, প্রতি-রানটাইম: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md)।

## স্বীকৃতি

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Star History

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## লাইসেন্স

MIT · তৈরি করেছেন [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
