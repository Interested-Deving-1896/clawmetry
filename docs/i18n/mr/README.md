<!-- i18n-src:b22579578775 -->
> मराठी translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**एखादा एजंट प्रगती न करता शेकडो टूल कॉल्स करू शकतो.** ClawMetry तुमचे कोडिंग एजंट्स आधीच लिहित असलेल्या सेशन फाइल्स वाचते आणि टाइमलाइन, टूल कॉल्स आणि रनटाइम जे काही टोकन व कॉस्ट डेटा उघड करते ते सर्व एका दृश्यात मांडते — जेणेकरून काम करत असलेली दीर्घ रन आणि अडकलेली रन यातला फरक तुम्हाला सहज कळेल.

**32 AI एजंट रनटाइम्ससोबत** काम करते — Claude Code, OpenAI Codex, Hermes, OpenClaw आणि आणखी 28. तुमच्या संपूर्ण एजंट फ्लीटसाठी एकच डॅशबोर्ड. ([संपूर्ण यादी](SUPPORTED_RUNTIMES.txt), कॅटलॉगमधून जनरेट केलेली.)

> 🌐 **हे यामध्ये वाचा:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [अधिक →](docs/i18n/)

एक कमांड. शून्य कॉन्फिगरेशन. सर्वकाही आपोआप शोधते.

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** वर उघडते. शून्य कॉन्फिगरेशन: तुमच्याकडे आधीपासून असलेले एजंट रनटाइम्स ते शोधते, त्यांना केवळ-वाचनासाठी (read-only) वाचते, आणि ते कसे चालतात यात काहीही बदल करत नाही.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## इन्स्टॉल करण्यापूर्वी

| | |
|---|---|
| **हे काय करते** | तुमचे एजंट्स आधीच लिहित असलेल्या सेशन फाइल्स आणि लॉग्ज वाचते. कोणताही SDK नाही, कोड बदल नाही, तुमच्या ॲपमध्ये कोणतीही इन्स्ट्रुमेंटेशन नाही. |
| **तुम्हाला काय दिसते** | सेशन टाइमलाइन, टूल-बाय-टूल रिप्ले, टोकन आणि कॉस्ट ब्रेकडाउन, आणि ट्रॅजेक्टरी सिग्नल्स (लूपिंग, वारंवार होणारे अपयश) — प्रत्येक रनटाइमनुसार. |
| **मोफत काय आहे** | `pip install clawmetry` कोणत्याही खात्याशिवाय, की (key) शिवाय आणि नेटवर्क कॉलशिवाय **OpenClaw, NVIDIA NemoClaw, Goose आणि Qwen Code** वाचते. इतर 28 — Claude Code, Codex, Cursor आणि उर्वरित — क्लोज्ड-सोर्स `clawmetry-pro` कम्पॅनियनद्वारे वाचले जातात, जे 7-दिवसांच्या ट्रायलसह किंवा प्लॅनसोबत मिळते — नेमकी विभागणी पाहण्यासाठी [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) पहा. |
| **कसे सुरू करावे** | `pip install clawmetry && clawmetry`, त्यानंतर localhost:8900 उघडा. या मशीनवर अजून कोणतेही एजंट नाहीत? `clawmetry --sample` तीन लेबल केलेल्या सिंथेटिक सेशन्ससह उघडते. |
| **तुमच्या मशीनमधून काय बाहेर जाते** | तुम्ही `clawmetry connect` चालवत नाही तोपर्यंत कोणताही सेशन डेटा नाही. डिफॉल्टने दोन गोष्टी चालतात, दोन्ही ऑप्ट-आउट करण्यायोग्य आणि दोन्हीमध्ये सेशन कंटेंट नसतो: एक अनामिक इन्स्टॉल पिंग आणि एक PyPI व्हर्जन चेक. प्रत्येक डेस्टिनेशनची यादी [docs/EGRESS.md](docs/EGRESS.md) मध्ये आहे, जी टिप्पण्या वाचण्याऐवजी वायर कॅप्चरमधून पुन्हा तयार केली गेली आहे. |

आउटपुटचा निर्णय घेण्यापूर्वी जाणून घेण्यासारख्या दोन मर्यादा आहेत: रनटाइम्स खूप वेगवेगळा डेटा उघड करतात (काही कोणतीही कॉस्ट प्रकाशित करत नाहीत — कोणत्या रनटाइमबद्दल हे [मॅट्रिक्स](docs/compatibility.md) सांगतो), आणि एखादी क्रिया पाहणे म्हणजे ती थांबवण्याची क्षमता असणे असे नाही ([कोणते नियंत्रण खरे आहेत, प्रत्येक रनटाइमनुसार](docs/APPROVALS.md)).


## 32 एजंट रनटाइम्ससोबत काम करते

**ओपन सोर्स ॲपमध्ये मोफत:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**पेड प्लॅनवर:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

प्रत्येक रनटाइमला तोच डॅशबोर्ड मिळतो. एकाच वेळी अनेक चालवा आणि हेडर स्विचर प्रत्येक टॅबला त्यापैकी एकावर पुन्हा स्कोप करेल.

तुम्ही SDK वर तुमचा स्वतःचा एजंट तयार केला आहे का? इंटरसेप्टर त्याच्या LLM कॉल्सचाही मागोवा घेतो. पहा [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## तुम्हाला काय मिळते

- **सेशन्स आणि ट्रान्सक्रिप्ट्स**: प्रत्येक एजंटने काय केले, टप्प्याटप्प्याने, रिप्लेसह
- **कॉस्ट आणि टोकन्स**: रनटाइम, मॉडेल, सेशन आणि दिवसानुसार, अनोमली फ्लॅग्जसह
- **फ्लो**: चॅनल्स, मॉडेल्स आणि टूल्समधून जाणाऱ्या मेसेजेसचा लाइव्ह डायग्राम
- **ब्रेन**: रिझनिंग आणि टूल-कॉल इव्हेंट स्ट्रीम, जसे ते घडते
- **कॉन्टेक्स्ट ब्लोआउट**: प्रोव्हायडरनुसार साइज केलेला विंडो युटिलायझेशन, कॉम्पॅक्शन विरुद्ध फोर्स्ड ओव्हरफ्लो, तसेच आपल्याला *काय दिसू शकत नाही* याचा प्रत्येक रनटाइमनुसार नकाशा ([कसे](docs/CONTEXT_BLOWOUT.md))
- **मेमरी आणि स्किल्स**: प्रत्येक रनटाइमने प्रत्यक्षात लोड केलेल्या फाइल्स आणि स्किल्स
- **हेल्थ आणि लॉग्ज**: डिस्क, मेमरी, एरर रेट्स, रेट लिमिट्स, लाइव्ह लॉग स्ट्रीम
- **अलर्ट्स**: बजेट कॅप्स, एरर स्पाइक्स, एजंट-ऑफलाइन, Slack, Discord, PagerDuty, Telegram, Email कडे रूट केलेले
- **अप्रूव्हल्स**: जोखमीचे टूल कॉल्स *चालण्यापूर्वी* थांबवा आणि तुमच्या फोनवरून मंजूर करा ([कसे](docs/APPROVALS.md))

## कॉन्टेक्स्ट ब्लोआउट, आणि निरीक्षणाची किंमत

कोणत्याही एजंट-तुलना टूलवर विश्वास ठेवण्यापूर्वी उत्तर द्यायला हव्या अशा दोन गोष्टी.

**हे विविध रनटाइम्समधील कॉन्टेक्स्ट-विंडो ब्लोआउट कसे हाताळते?**

युटिलायझेशन टक्केवारी ती ज्याने भागली जाते तितकीच प्रामाणिक असते. ClawMetry [एका सारणीतून](clawmetry/context_windows.py) प्रत्येक प्रोव्हायडरनुसार विंडो साइज करते, जी तुम्ही वाचू शकता आणि PR करू शकता — Anthropic, OpenAI, Google, xAI, DeepSeek, Kimi, Qwen, Mistral, Llama आणि GLM समाविष्ट. ते सर्व 32 रनटाइम्सना एका वेंडरच्या मोजपट्टीने मोजत नाही. हे महत्त्वाचे आहे: Anthropic च्या 200K विरुद्ध मोजलेली 300K GPT-5 टर्न ">100%, blown" दाखवते, जेव्हा प्रत्यक्षात ती GPT-5 च्या 400K पैकी 75% असते. तीच मोजपट्टी खऱ्या अर्थाने ओव्हरफ्लो झालेल्या 130K DeepSeek टर्नला एका आरामदायक 65% प्रमाणे लपवते.

प्रत्येक विंडो तिच्या मूळ स्त्रोतासह येते: `model_table`, `explicit_marker`, `observed_floor`, किंवा जेव्हा आम्हाला मॉडेल माहीत नसते तेव्हा एक प्रामाणिक `default`. अंदाजावर आधारित गेज कधीच लुकअपवर आधारित गेजसारखा सत्ताधिकार घेऊन रेंडर होत नाही.

ClawMetry काही रनटाइम्सवरच कॉम्पॅक्शन इव्हेंट्स पाहू शकते. त्यामुळे `GET /api/context-coverage` प्रत्येक रनटाइमनुसार अहवाल देते की एक शून्य म्हणजे **"स्वच्छ चालले" की "आम्हाला दिसत नाही"**. ज्या शून्याचा खरा अर्थ आंधळेपणा आहे, ते तसे सांगते. [संपूर्ण तपशील](docs/CONTEXT_BLOWOUT.md)

**इन्स्ट्रुमेंटेशनची किंमत काय आहे?**

| पथ | तुमच्या एजंटमध्ये जोडले जाणारे | डिफॉल्ट? |
|---|---|---|
| सेशन-फाइल टेलिंग (सर्व 32 रनटाइम्स) | **0**. वेगळी प्रक्रिया, तुमच्या एजंटमध्ये ClawMetry कोड नाही | चालू |
| HTTP इंटरसेप्टर (`CLAWMETRY_INTERCEPT=1`) | प्रति LLM कॉल **+0.44 ms**, किंवा 5 सेकंदांच्या कॉलचे 0.009% | बंद |
| प्री-टूल हुक गेट (वॉर्म कॅशे) | 36 ms इंटरप्रीटर फ्लोअरवर, प्रति गेटेड टूल कॉल **+44 ms** | बंद |
| एन्फोर्समेंट प्रॉक्सी | प्रति LLM कॉल **+9.7 ms** | बंद |

डिमन होस्ट कॉस्ट: **2,762 इव्हेंट्स/सेकंद** इनजेस्ट, डिस्कवर **710 बाइट्स/इव्हेंट** (100k इव्हेंट्ससाठी 67.7 MB), आणि व्यस्त इन्स्टॉलवर सतत **एका कोरच्या ~12%**. तो शेवटचा आकडा आमच्या स्वतःच्या 5-10% बजेटपेक्षा जास्त आहे, त्यामुळे तो पानावरून वगळण्याऐवजी पाठलाग करायचा बग म्हणून प्रकाशित केला आहे.

Apple M2 Pro वर `benchmarks/overhead.py` सह मोजले. हार्नेस प्रत्येक स्थिती वेगळ्या प्रक्रियेत चालवतो, त्यांचा क्रम बदलतो, आणि **जेव्हा फेऱ्यांमध्ये चिन्हावर मतभेद असतो तेव्हा आकडा छापण्यास नकार देतो**. तुमच्या स्वतःच्या मशीनवर एका मिनिटात चालवा:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

हुक गेट्स आणि एन्फोर्समेंट प्रॉक्सीसह प्रत्येक पथ मोजला जातो, आणि हार्नेस CI मध्ये Linux, macOS आणि Windows वर चालतो. जाणून घेण्यासारखे दोन निकाल: Windows वर प्रॉक्सीची किंमत Linux पेक्षा सुमारे सात पट जास्त आहे, आणि डिमन सध्या एका कोरच्या सुमारे 12% सतत वापरतो, जे आमच्या स्वतःच्या 5-10% बजेटपेक्षा जास्त आहे. रॉ JSON, पद्धत, आणि अजूनही न मोजलेले काय आहे ते [docs/OVERHEAD.md](docs/OVERHEAD.md) मध्ये आहे.

## किंमत

| प्लॅन | यात काय समाविष्ट आहे | किंमत |
|---|---|---|
| **मोफत** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, संपूर्ण डॅशबोर्ड, फक्त स्थानिक | $0 |
| **स्टार्टर** | वरील इतर सर्व रनटाइम्स, फ्लीट व्ह्यू, क्लाउड सिंक | $9 प्रति नोड / महिना |
| **Pro** | स्टार्टर + नियंत्रण आणि मूल्यांकन: अप्रूव्हल्स, टूल-रिस्क पॉलिसीज, इव्हल्स, अनोमली डिटेक्शन, कॉस्ट ऑप्टिमायझर, OTel एक्सपोर्ट, टँपर-एव्हिडंट ऑडिट लॉग | $19 प्रति नोड / महिना |

वार्षिक प्लॅन्स, एंटरप्राइझ आणि सध्याचे आकडे **[clawmetry.com/pricing](https://clawmetry.com/pricing)** येथे आहेत. सेल्फ-होस्टेड लायसन्स की क्लाउडशिवाय काम करतात (`clawmetry license`). नेमकी मोफत/पेड विभागणी [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) मध्ये आहे.

## तुमचा डेटा तुमच्या मशीनवरच राहतो

ClawMetry स्थानिक सेशन फाइल्स आणि लॉग्ज वाचते. **तुम्ही `clawmetry connect` चालवत नाही तोपर्यंत तुमच्या बॉक्समधून कोणताही सेशन डेटा बाहेर जात नाही** — कोणतेही प्रॉम्प्ट्स, रिप्लाय, टूल आर्ग्युमेंट्स, फाइल कंटेंट किंवा लॉग लाइन्स नाहीत. जेव्हा तुम्ही कनेक्ट करता, तेव्हा स्नॅपशॉट अशा कीने एंड-टू-एंड एन्क्रिप्ट केला जातो जी तुमच्या मशीनमधून कधीही बाहेर जात नाही, आणि तुमच्या ब्राउझरमध्ये डिक्रिप्ट केला जातो. जर एखाद्या नोडकडे की नसेल, तर अपलोड स्पष्ट स्वरूपात पाठवण्याऐवजी वगळला जातो, आणि कोणताही सर्व्हर रिस्पॉन्स ते बंद करू शकत नाही.

तुम्ही कनेक्ट करण्यापूर्वी डिफॉल्टने दोन गोष्टी चालतात, दोन्ही ऑप्ट-आउट करण्यायोग्य आणि दोन्हीमध्ये सेशन डेटा नसतो: एक अनामिक इन्स्टॉल पिंग आणि PyPI विरुद्ध व्हर्जन चेक. डिफॉल्ट इन्स्टॉल स्टार्टअप बॅनर लाइनसाठी एकदा तुमचा पब्लिक IP देखील लुकअप करते. प्रत्येक डेस्टिनेशन, त्यात काय असते आणि ते कसे बंद करावे याची यादी [docs/EGRESS.md](docs/EGRESS.md) मध्ये आहे; सेल्फ-होस्टेड, रीपॉइंटेड आणि एअर-गॅप्ड इन्स्टॉल्स अजिबात स्वेच्छेचे आउटबाउंड कॉल्स करत नाहीत.

डिक्रिप्शन तुमच्या ब्राउझरमध्ये होते, आम्ही तुम्हाला दिलेल्या कोडमध्ये. हे पूर्वी एक वचन होते; आता ती अशी गोष्ट आहे जी तुम्ही तपासू शकता. तुमच्या कीला स्पर्श करणारी प्रत्येक ओळ एका वाचण्यायोग्य फाइलमध्ये आहे, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js), जी व्हीलमध्ये समाविष्ट होते आणि जशीच्या तशी सर्व्ह केली जाते, Subresource Integrity हॅशसह पिन केलेली. ब्राउझर आम्ही प्रकाशित केलेलेच चालवतो याची खात्री करण्यासाठी:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

हे काय सिद्ध करत नाही: आम्ही ती पेज सर्व्ह करतो जी फाइल लोड करते, त्यामुळे आम्ही वेगळी पेज सर्व्ह करू शकतो. इंटिग्रिटी हॅशेस तुम्हाला तडजोड झालेल्या CDN पासून संरक्षण देतात, वेंडरपासून नाही. तुम्हाला जे मिळते ते म्हणजे कोणतीही बदली मुद्दाम, पेज सोर्समध्ये दृश्यमान आणि कोणीही मिळवू शकेल अशा PyPI वरील आर्टिफॅक्टपेक्षा वेगळी असावी लागते. सेल्फ-होस्टिंग किंवा फक्त-स्थानिक राहिल्याने ही अवलंबित्व पूर्णपणे नाहीशी होते.

## इन्स्टॉल करा

```bash
pip install clawmetry     # नंतर: clawmetry
```

किंवा एक-लाइनर: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS, Linux किंवा Windows वर Python 3.8+ आणि त्याच मशीनवर किमान एक एजंट रनटाइम आवश्यक. Docker सूचना: [docs/DOCKER.md](docs/DOCKER.md).

किंवा एजंटला तुमच्यासाठी सेटअप करू द्या. [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md) स्किल Claude Code, Codex, Cursor, Gemini CLI, Copilot किंवा OpenCode ला ClawMetry इन्स्टॉल करणे, मशीनवरील एजंट्स काय करत आहेत आणि किती खर्च करत आहेत याचा अहवाल देणे, विनंतीनुसार एखादे सेशन थांबवणे, आणि जोखमीचे टूल कॉल्स मंजुरीसाठी थांबवणे शिकवते:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## डॉक्स

| | |
|---|---|
| [रनटाइम सुसंगतता](docs/compatibility.md) | प्रत्येक अडॅप्टर काय वाचतो, आणि नवीन रनटाइम कसा जोडावा |
| [कॉन्टेक्स्ट ब्लोआउट](docs/CONTEXT_BLOWOUT.md) | प्रोव्हायडरनुसार विंडो, कॉम्पॅक्शन विरुद्ध ओव्हरफ्लो, प्रति-रनटाइम कव्हरेज |
| [ओव्हरहेड](docs/OVERHEAD.md) | इन्स्ट्रुमेंटेशनची मोजलेली किंमत, ती पुन्हा तयार करण्यासाठीच्या हार्नेससह |
| [एंटायटलमेंट्स](docs/ENTITLEMENTS.md) | मोफत विरुद्ध पेड, टियर मॅट्रिक्स, लायसन्स CLI |
| [अप्रूव्हल्स आणि पॉलिसीज](docs/APPROVALS.md) | प्री-एक्झिक्युशन गेटिंग, रिस्क स्कोरिंग, फोन अप्रूव्हल्स |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | कुठेही ट्रेसेस एक्सपोर्ट करा, कुठूनही OTLP इनजेस्ट करा |
| [तुमचा स्वतःचा एजंट आणा](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain शेवटपासून शेवटपर्यंत, चालवण्यायोग्य उदाहरणांसह |
| [SDK ट्रॅकिंग](docs/SDK_TRACKING.md) | तुम्ही स्वतः तयार केलेल्या एजंट्ससाठी कॉस्ट अट्रिब्यूशन |
| [चॅट चॅनल्स](docs/CHANNELS.md) | फ्लोमध्ये दाखवलेले चॅट अडॅप्टर्स |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | सँडबॉक्स्ड NVIDIA NemoClaw सेटअप्स |
| [Docker](docs/DOCKER.md) | इमेज, कंपोझ, व्हॉल्यूम माउंट्स |
| [आर्किटेक्चर](ARCHITECTURE.md) · [डेव्हलपमेंट](docs/DEVELOPMENT.md) | आतमध्ये हे कसे कार्य करते; सोर्सवरून चालवणे |
| [टेलिमेट्री](docs/TELEMETRY.md) | अनामिक इन्स्टॉल आणि डेस्कटॉप-ओपन पिंग्ज, आणि त्या कशा बंद कराव्यात |

## स्क्रीनशॉट्स

खालील प्रत्येक आकडा एका खऱ्या मशीनवरून, केवळ-वाचनासाठी, काहीही सीड न करता घेतलेला आहे.

**काय झाले हेच नाही, तर काहीतरी चुकीचे असल्यास ते तुम्हाला सांगते.**
वर दोन अनोमली बॅनर्स: दैनंदिन सरासरीच्या 7 पट खर्च चालू आहे, आणि 4.2x कॉस्ट स्पाइक. त्याखाली, अलीकडील 667 पैकी 324 सेशन्समध्ये वेस्ट सिग्नल आहे, कारणानुसार वर्गीकृत.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**पैसे कुठे गेले हे प्रत्येक विंडोमध्ये दाखवते.**
आज $252.47, या आठवड्यात $513.15, या महिन्यात $1,312.92, प्रत्येकामागील टोकन्स आणि तुमचे सबस्क्रिप्शन आधीच किती कव्हर करते यासह. त्याखाली, सुमारे $1,128/महिना रिकव्हर करण्यायोग्य म्हणून वर्गीकृत आणि कॅशे रीयूजमुळे आधीच $17,256/महिना वाचवले गेलेले.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**मेसेज उत्तरात कसा बदलतो हे ते रेखाटते.**
लाइव्ह फ्लो डायग्राम: तुम्ही, तो ज्या चॅनलवर आला तो चॅनल, गेटवे, सध्या उत्तर देणारा मॉडेल, आणि त्याने वापरलेले प्रत्येक टूल. काम त्यांच्यामधून जाताना नोड्स उजळतात.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**मशीनवरील प्रत्येक एजंट, एका टेबलमध्ये.**
तो काय चालवतो, गेल्या 24 तासांत आणि आयुष्यभर त्याची किंमत काय आहे, तो शेवटचा कधी दिसला, त्याचा मालक कोण आहे, आणि सबस्क्रिप्शन बिल कव्हर करत आहे का. इथे 14 एजंट्स, 3 सेशन्स काम करत आहेत, 13 शांत आहेत.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**एका टर्नचा वेळ आणि पैसा टूल-बाय-टूल कुठे गेला हे ते दाखवते.**
खऱ्या सेशनची एक टर्न: 11.2 मिनिटांत 11 टूल्स $1.16 साठी. प्रत्येक Bash कॉल आणि मॉडेल कॉलला टाइमलाइनवर स्वतःचा बार मिळतो, त्यामुळे 4.1 मिनिटे चाललेली कमांड आणि 226ms चाललेली कमांड एका नजरेत ओळखता येतात.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**केवळ खर्चच नाही, तर कामाला गुण देते.**
या आठवड्यात A: 54 कामे व्यवस्थित पूर्ण झाली, 2 खडबडीत कामांची किंमत $48.57 होती, आणि निर्णय घेण्याइतकी पुरेशी क्रिया नसलेल्या रन्स गुणांमध्ये मोजण्याऐवजी वगळल्या गेल्या. प्रत्येक खडबडीत रन तिच्या ट्रेसकडे लिंक करते.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**कॉन्टेक्स्ट विंडो का भरत राहते हे ते दाखवते.**
शेवटच्या टर्नमध्ये 1M-टोकन विंडोपैकी 715K, 83.3% पीक, ओव्हरफ्लोऐवजी सक्रियपणे झालेली 4 कॉम्पॅक्शन्स, आणि त्यामागील प्रत्येक टर्नचा युटिलायझेशन.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**तुम्ही काहीही कॉन्फिगर न करता डिटेक्शन चालते.**
इन्स्टॉलपासूनच बिल्ट-इन डिटेक्टर्स चालू आहेत: एजंट शांत झाला, टेलिमेट्री फीड थांबला, कॉस्ट स्पाइक, टोकन बर्स्ट, वाढणाऱ्या एरर्स, एरर स्पाइक, बजेट थ्रेशोल्ड, थ्रेट सिग्नेचर जुळला, सिक्युरिटी टूल फाइंडिंग, सिक्युरिटी पोश्चर बदल. तुमचे स्वतःचे नियम त्यावर पर्यायी आहेत.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**जोखमीचा कॉल थांबवणे ऑप्ट-इन आहे, आणि बंद अवस्थेत शिप होते.**
रिकर्सिव्ह डिलीट्स, फोर्स पुशेस, sudo, सिक्रेट्स, पॅकेज इन्स्टॉल्स आणि आउटबाउंड कॉल्स — प्रत्येकाला तुम्ही चालू करू शकाल असा नियम मिळतो. तुम्ही तसे करेपर्यंत, ClawMetry फक्त बघते आणि काहीही बदलत नाही. एकदा एक चालू केला की, जुळणारे कॉल्स इथे (किंवा तुमच्या फोनवर) मंजुरी किंवा नकारासाठी थांबतात.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

अधिक, प्रत्येक रनटाइमनुसार: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## ओळख

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Star History

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## लायसन्स

MIT · [@vivekchand](https://github.com/vivekchand) द्वारे तयार केले · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
