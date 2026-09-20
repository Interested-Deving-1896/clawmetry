<!-- i18n-src:b22579578775 -->
> עברית translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**סוכן יכול לבצע מאה קריאות כלים בלי להתקדם.** ClawMetry
קוראת את קובצי הסשן שסוכני הקוד שלכם כבר כותבים, ומרכזת את ציר הזמן,
קריאות הכלים וכל נתוני הטוקנים והעלות שהריצה חושפת בתצוגה אחת —
כך שתוכלו להבחין בין ריצה ארוכה שעובדת לבין ריצה שנתקעה.

עובד עם **32 ריצות סוכני AI** — Claude Code, OpenAI Codex, Hermes, OpenClaw ועוד 28. לוח מחוונים אחד לכל צי הסוכנים שלכם. ([הרשימה המלאה](SUPPORTED_RUNTIMES.txt), נוצרת מהקטלוג.)

> 🌐 **קראו את זה ב:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [עוד →](docs/i18n/)

פקודה אחת. אפס הגדרות. מזהה הכול אוטומטית.

```bash
pip install clawmetry && clawmetry
```

נפתח בכתובת **http://localhost:8900**. אפס הגדרות: הכלי מוצא את ריצות הסוכנים
שכבר יש לכם, קורא אותן במצב קריאה בלבד, ולא משנה דבר באופן שבו הן פועלות.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## לפני שמתקינים

| | |
|---|---|
| **מה זה עושה** | קורא את קובצי הסשן והלוגים שהסוכנים שלכם כבר כותבים. בלי SDK, בלי שינוי קוד, בלי אינסטרומנטציה באפליקציה שלכם. |
| **מה אתם רואים** | ציר זמן של הסשן, שחזור כלי אחר כלי, פירוט טוקנים ועלויות, ואיתותי מסלול (לולאות, כשלים חוזרים) — לכל ריצה בנפרד. |
| **מה חינמי** | `pip install clawmetry` קורא את **OpenClaw, NVIDIA NemoClaw, Goose ו-Qwen Code** בלי חשבון, בלי מפתח ובלי קריאת רשת. שאר ה-28 — Claude Code, Codex, Cursor והשאר — נקראים על ידי הרכיב הנלווה סגור-הקוד `clawmetry-pro`, שמגיע עם תקופת הניסיון של 7 ימים או עם תוכנית בתשלום — ראו [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) לפירוט המדויק. |
| **איך מתחילים** | `pip install clawmetry && clawmetry`, ואז פותחים את localhost:8900. אין עדיין סוכנים על המחשב הזה? `clawmetry --sample` נפתח עם שלושה סשנים סינתטיים מתויגים. |
| **מה יוצא מהמחשב שלכם** | שום נתוני סשן, אלא אם תריצו `clawmetry connect`. שני דברים כן רצים כברירת מחדל, שניהם ניתנים לביטול ואף אחד מהם לא נושא תוכן סשן: פינג התקנה אנונימי ובדיקת גרסה מול PyPI. כל יעד מתועד ב-[docs/EGRESS.md](docs/EGRESS.md), שנבנה מחדש מלכידת תעבורת רשת ולא מקריאת הערות בקוד. |

שתי מגבלות שכדאי להכיר לפני שפוסקים על הפלט: ריצות שונות חושפות נתונים שונים
מאוד (חלקן לא מפרסמות עלות בכלל — [הטבלה](docs/compatibility.md) מפרטת אילו,
לפי ריצה), ולצפות בפעולה זה לא כמו היכולת לחסום אותה
([אילו פקדים אמיתיים, לפי ריצה](docs/APPROVALS.md)).


## עובד עם 32 ריצות סוכנים

**חינמי באפליקציית הקוד הפתוח:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**בתוכנית בתשלום:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

כל ריצה מקבלת את אותו לוח מחוונים. הריצו כמה בו-זמנית והבורר בכותרת
ימקד מחדש כל טאב לאחת מהן.

בניתם את הסוכן שלכם על SDK במקום זאת? המיירט עוקב גם אחרי קריאות ה-LLM שלו.
ראו [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## מה מקבלים

- **סשנים ותמלולים**: מה כל סוכן עשה, תור אחר תור, עם שחזור
- **עלות וטוקנים**: לפי ריצה, מודל, סשן ויום, עם דגלי חריגה
- **זרימה**: תרשים חי של הודעות שזזות בין ערוצים, מודלים וכלים
- **מוח (Brain)**: זרם אירועי החשיבה וקריאות הכלים בזמן אמת
- **התפוצצות הקשר (Context blowout)**: ניצול חלון הקשר בגודל לפי ספק, כיווץ (compaction) מול גלישה כפויה, ומיפוי לפי ריצה של מה שאנחנו *לא* יכולים לראות ([איך](docs/CONTEXT_BLOWOUT.md))
- **זיכרון וכישורים (Memory & skills)**: הקבצים והכישורים שכל ריצה בפועל טענה
- **בריאות ולוגים**: דיסק, זיכרון, שיעורי שגיאות, מגבלות קצב, זרם לוגים חי
- **התראות**: תקרות תקציב, קפיצות שגיאות, סוכן לא מגיב, מנותב ל-Slack, Discord, PagerDuty, Telegram, אימייל
- **אישורים**: השהיית קריאות כלים מסוכנות *לפני* שהן רצות ואישור מהטלפון ([איך](docs/APPROVALS.md))

## התפוצצות הקשר, ומה עולה לעקוב אחריה

שתי שאלות ששווה לענות עליהן לפני שסומכים על כל כלי להשוואת סוכנים.

**איך זה מטפל בהתפוצצות חלון הקשר בין ריצות שונות?**

אחוז ניצול הוא כן רק כמו המספר שהוא מחולק בו. ClawMetry
קובעת את גודל החלון לפי ספק מ[טבלה שאפשר לקרוא ולשלוח עליה PR](clawmetry/context_windows.py),
המכסה את Anthropic, OpenAI, Google, xAI, DeepSeek, Kimi, Qwen, Mistral, Llama ו-GLM. היא לא
מודדת את כל 32 הריצות בסרגל של ספק אחד. זה חשוב: תור של 300K טוקנים ב-GPT-5
שנמדד מול 200K של Anthropic נקרא ">100%, התפוצץ" כאשר בפועל הוא ב-75% מ-400K
של GPT-5. אותו סרגל מסתיר תור DeepSeek של 130K שבאמת גלש כ-65% נוח.

כל חלון מגיע עם המקור שלו: `model_table`, `explicit_marker`,
`observed_floor`, או `default` כן כשלא ידוע לנו המודל. מד שבנוי על ניחוש
לעולם לא יוצג עם אותה סמכות כמו כזה שבנוי על חיפוש בטבלה.

ClawMetry יכולה לראות אירועי כיווץ (compaction) רק בחלק מהריצות. לכן
`GET /api/context-coverage` מדווחת, לפי ריצה, האם **אפס פירושו "רץ נקי" או "אנחנו עיוורים"**.
אפס שבאמת פירושו עיוור אומר את זה במפורש.
[פירוט מלא](docs/CONTEXT_BLOWOUT.md)

**מה עולה האינסטרומנטציה?**

| נתיב | נוסף לסוכן שלכם | ברירת מחדל? |
|---|---|---|
| מעקב אחרי קובצי סשן (כל 32 הריצות) | **0**. תהליך נפרד, אין קוד ClawMetry בסוכן שלכם | פועל |
| מיירט HTTP (`CLAWMETRY_INTERCEPT=1`) | **+0.44 מילישניות** לכל קריאת LLM, או 0.009% מקריאה של 5 שניות | כבוי |
| שער hook טרום-כלי (מטמון חם) | **+44 מילישניות** לכל קריאת כלי שנשערת, מעל רצפת מפרש של 36 מילישניות | כבוי |
| פרוקסי אכיפה | **+9.7 מילישניות** לכל קריאת LLM | כבוי |

עלות מארח הדימון: **2,762 אירועים לשנייה** בקליטה, **710 בייטים לאירוע** על הדיסק
(67.7 מגה-בייט לכל 100 אלף אירועים), וכ-**12% מליבה אחת** בממוצע קבוע בהתקנה עמוסה.
המספר האחרון הזה חורג מהתקציב שהצהרנו עליו של 5-10%, ולכן הוא מפורסם כבאג
שצריך לרדוף אחריו ולא נשמט מהדף.

נמדד על Apple M2 Pro עם `benchmarks/overhead.py`. הרתמה מריצה
כל תנאי בתהליך נפרד, מחליפה את סדר הריצה, **ומסרבת להדפיס מספר
כאשר הסבבים חלוקים על הסימן שלו**. הריצו את זה על המחשב שלכם בתוך דקה:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

כל נתיב נמדד, כולל שערי ה-hook ופרוקסי האכיפה,
והרתמה רצה על Linux, macOS ו-Windows ב-CI. שתי תוצאות ששווה להכיר: הפרוקסי
עולה בערך פי שבעה יותר על Windows מאשר על Linux, והדימון כרגע מחזיק בקביעות
כ-12% מליבה אחת, מעל התקציב שלנו עצמנו של 5-10%. ה-JSON הגולמי, השיטה, ומה
שעדיין לא נמדד נמצאים ב-[docs/OVERHEAD.md](docs/OVERHEAD.md).

## תמחור

| תוכנית | מה היא מכסה | מחיר |
|---|---|---|
| **חינם (Free)** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, לוח מחוונים מלא, מקומי בלבד | $0 |
| **Starter** | כל ריצה נוספת מלמעלה, תצוגת צי, סנכרון ענן | $9 לצומת / חודש |
| **Pro** | Starter + בקרה והערכה: אישורים, מדיניות סיכון כלים, evals, זיהוי חריגות, אופטימיזציית עלויות, ייצוא OTel, יומן ביקורת עמיד בפני שיבוש | $19 לצומת / חודש |

תוכניות שנתיות, Enterprise והמספרים העדכניים נמצאים בכתובת
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**. מפתחות רישיון לאירוח עצמי
פועלים בלי הענן (`clawmetry license`). החלוקה המדויקת בין חינם לתשלום נמצאת
ב-[docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md).

## הנתונים שלכם נשארים על המחשב שלכם

ClawMetry קוראת קובצי סשן ולוגים מקומיים. **שום נתון סשן לא יוצא מהמכונה שלכם
אלא אם תריצו `clawmetry connect`** — לא הנחיות (prompts), תשובות, ארגומנטים
של כלים, תוכן קבצים או שורות לוג. כשאתם כן מתחברים, התמונת המצב מוצפנת
מקצה לקצה עם מפתח שלעולם לא יוצא מהמכונה שלכם, ומפוענחת בדפדפן שלכם. אם
לצומת אין מפתח, ההעלאה מדולגת במקום להישלח בגלוי, ואף תגובת שרת לא יכולה
לכבות את זה.

שני דברים כן רצים כברירת מחדל לפני שאתם מתחברים, שניהם ניתנים לביטול ואף אחד
מהם לא נושא נתוני סשן: פינג התקנה אנונימי ובדיקת גרסה מול PyPI. התקנה כברירת
מחדל גם מחפשת פעם אחת את כתובת ה-IP הציבורית שלכם עבור שורת באנר בהפעלה. כל
יעד, מה שהוא נושא, ואיך לכבות אותו מפורטים ב-[docs/EGRESS.md](docs/EGRESS.md);
התקנות המתארחות עצמאית, מנותבות מחדש ומבודדות מרשת לא מבצעות שום קריאה
יוצאת שרירותית כלל.

הפענוח קורה בדפדפן שלכם, בקוד שאנחנו מגישים לכם. זו הייתה הבטחה בעבר;
עכשיו זה משהו שאפשר לבדוק. כל שורה שנוגעת במפתח שלכם נמצאת בקובץ קריא אחד,
[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
שנשלח בתוך ה-wheel ומוגש כלשונו, מקובע עם hash של Subresource Integrity.
כדי לאמת שהדפדפן מריץ את מה שפרסמנו:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

מה שזה לא מוכיח: אנחנו מגישים את הדף שטוען את הקובץ, כך שאנחנו יכולים
להגיש דף אחר. hash-ים של שלמות מגנים עליכם מ-CDN שנפרץ, לא מהספק. מה
שאתם מרוויחים הוא שכל החלפה חייבת להיות מכוונת, גלויה בקוד המקור של הדף,
ושונה מארטיפקט ב-PyPI שכל אחד יכול להוריד. אירוח עצמי או הישארות מקומית
בלבד מסירים את התלות הזאת לחלוטין.

## התקנה

```bash
pip install clawmetry     # ואז: clawmetry
```

או השורה האחת: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

דורש Python 3.8+ ב-macOS, Linux או Windows, ולפחות ריצת סוכן אחת על
אותה מכונה. הוראות Docker: [docs/DOCKER.md](docs/DOCKER.md).

או תנו לסוכן להתקין עבורכם. הכישור [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
מלמד את Claude Code, Codex, Cursor, Gemini CLI, Copilot או OpenCode
להתקין את ClawMetry, לדווח מה הסוכנים על המכונה עושים ומוציאים,
לעצור סשן אחד לפי בקשה, ולעכב קריאות כלים מסוכנות לאישור:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## תיעוד

| | |
|---|---|
| [תאימות ריצות](docs/compatibility.md) | מה כל מתאם קורא, ואיך מוסיפים ריצה |
| [התפוצצות הקשר](docs/CONTEXT_BLOWOUT.md) | חלונות לפי ספק, כיווץ מול גלישה, כיסוי לפי ריצה |
| [תקורה (Overhead)](docs/OVERHEAD.md) | כמה עולה האינסטרומנטציה, נמדד, עם הרתמה לשחזור |
| [זכאויות (Entitlements)](docs/ENTITLEMENTS.md) | חינם מול תשלום, טבלת דרגות, CLI לרישיון |
| [אישורים ומדיניות](docs/APPROVALS.md) | שערור לפני ביצוע, ניקוד סיכון, אישורים מהטלפון |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | ייצוא traces לכל מקום, קליטת OTLP מכל דבר |
| [הביאו את הסוכן שלכם](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain מקצה לקצה, עם דוגמאות שרצות |
| [מעקב SDK](docs/SDK_TRACKING.md) | ייחוס עלויות לסוכנים שבניתם בעצמכם |
| [ערוצי צ'אט](docs/CHANNELS.md) | מתאמי הצ'אט המוצגים ב-Flow |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | הגדרות NVIDIA NemoClaw מבודדות (sandboxed) |
| [Docker](docs/DOCKER.md) | תמונה, compose, הרכבות volume |
| [ארכיטקטורה](ARCHITECTURE.md) · [פיתוח](docs/DEVELOPMENT.md) | איך זה עובד מבפנים; הרצה מהמקור |
| [טלמטריה](docs/TELEMETRY.md) | הפינגים האנונימיים של התקנה ופתיחת דסקטופ, ואיך לכבות אותם |

## צילומי מסך

כל מספר למטה לקוח ממכונה אמיתית אחת, במצב קריאה בלבד, בלי שום דבר מוזרע.

**זה אומר לכם מתי משהו לא בסדר, לא רק מה קרה.**
שני באנרי חריגה למעלה: הוצאה שרצה פי 7 מהממוצע היומי, וקפיצת עלות של פי 4.2.
מתחתם, 324 מתוך 667 סשנים אחרונים נושאים איתות בזבוז, מפורטים לפי סיבה.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**זה מראה לכם לאן הכסף הלך, בכל חלון זמן.**
$252.47 היום, $513.15 השבוע, $1,312.92 החודש, כל אחד עם הטוקנים
שמאחוריו וכמה מזה המנוי שלכם כבר מכסה. מתחת לזה, בערך $1,128 לחודש
מפורטים כניתנים להחזרה ו-$17,256 לחודש כבר נחסכו בזכות שימוש חוזר במטמון (cache).

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**זה מצייר איך הודעה הופכת לתשובה.**
תרשים הזרימה החי: אתם, הערוץ שממנו זה הגיע, השער (gateway), המודל
שעונה כרגע, וכל כלי שהוא פנה אליו. צמתים נדלקים כשעבודה עוברת דרכם.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**כל סוכן על המכונה, בטבלה אחת.**
מה הוא מריץ, כמה הוא עולה ב-24 השעות האחרונות ולאורך כל חייו, מתי
נראה לאחרונה, מי הבעלים שלו, והאם מנוי מכסה את החשבון. 14 סוכנים
כאן, 3 סשנים עובדים, 13 שקטים.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**זה מראה לאן הזמן והכסף של תור הלכו, כלי אחר כלי.**
תור אחד של סשן אמיתי: 11 כלים ב-11.2 דקות תמורת $1.16. לכל קריאת
Bash וקריאת מודל יש פס משלה בציר הזמן, כך שהפקודה שרצה 4.1 דקות
והפקודה שרצה 226 מילישניות נבדלות זו מזו במבט חטוף.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**זה מדרג את העבודה, לא רק את ההוצאה.**
ציון A השבוע: 54 משימות חזרו נקיות, 2 מחוספסות עלו $48.57, וריצות
עם פעילות מועטה מדי לשיפוט מושמטות מהציון במקום להיחשב כזכיות. כל
ריצה מחוספסת מקושרת ל-trace שלה.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**זה מראה למה חלון ההקשר ממשיך להתמלא.**
715K מתוך חלון של 1M טוקנים בתור האחרון, שיא של 83.3%, 4 כיווצים
(compactions) שכולם הופעלו יזומית ולא עקב גלישה, וניצול כל תור מאחורי זה.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**הזיהוי פועל בלי שתגדירו כלום.**
הגלאים המובנים פועלים מרגע ההתקנה: הסוכן השתתק, זרם הטלמטריה
הפסיק, קפיצת עלות, התפרצות טוקנים, שגיאות מטפסות, קפיצת שגיאות, סף
תקציב, זוהתה חתימת איום, ממצא של כלי אבטחה, שינוי בעמדת האבטחה.
הכללים שלכם עצמכם אופציונליים בנוסף.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**עיכוב קריאה מסוכנת הוא אופציונלי, ומגיע כבוי.**
מחיקות רקורסיביות, force push, sudo, סודות, התקנות חבילות וקריאות
יוצאות מקבלים כל אחד כלל שאפשר להפעיל. עד שתעשו זאת, ClawMetry
צופה ולא משנה דבר. ברגע שאחד מופעל, קריאות תואמות ממתינות כאן (או
בטלפון שלכם) לאישור או דחייה.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

עוד, לפי ריצה: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## הכרה

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## היסטוריית כוכבים

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## רישיון

MIT · נבנה על ידי [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
