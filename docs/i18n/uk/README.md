<!-- i18n-src:b22579578775 -->
> Українська translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**Агент може зробити сотню викликів інструментів, так і не досягнувши прогресу.** ClawMetry
читає файли сесій, які ваші кодуючі агенти вже пишуть, і зводить хронологію,
виклики інструментів та будь-які дані про токени й вартість, які надає середовище виконання, в один
вигляд — щоб ви могли відрізнити довгий прогін, що працює, від того, що застряг.

Працює з **32 середовищами виконання ШІ-агентів** — Claude Code, OpenAI Codex, Hermes, OpenClaw та ще 28. Одна панель на весь ваш парк агентів. ([повний список](SUPPORTED_RUNTIMES.txt), згенерований з каталогу.)

> 🌐 **Читати цією мовою:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [ще →](docs/i18n/)

Одна команда. Без налаштувань. Все визначається автоматично.

```bash
pip install clawmetry && clawmetry
```

Відкривається за адресою **http://localhost:8900**. Без налаштувань: система знаходить середовища виконання агентів,
які у вас уже є, читає їх у режимі лише для читання й нічого не змінює в їхній роботі.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## Перед встановленням

| | |
|---|---|
| **Що це робить** | Читає файли сесій і журнали, які ваші агенти вже пишуть. Жодного SDK, жодних змін коду, жодної інструментації у вашому застосунку. |
| **Що ви бачите** | Хронологію сесії, покроковий відтворений виклик кожного інструменту, розподіл токенів і вартості та сигнали траєкторії (зациклення, повторювані збої) — для кожного середовища виконання. |
| **Що безкоштовно** | `pip install clawmetry` читає **OpenClaw, NVIDIA NemoClaw, Goose і Qwen Code** без облікового запису, ключа чи мережевого виклику. Решту 28 — Claude Code, Codex, Cursor та інші — читає закритий супутній модуль `clawmetry-pro`, який надається разом із 7-денною пробною версією або тарифним планом — точний розподіл у [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md). |
| **Як почати** | `pip install clawmetry && clawmetry`, потім відкрийте localhost:8900. Ще немає агентів на цій машині? `clawmetry --sample` відкриється з трьома позначеними синтетичними сесіями. |
| **Що залишає вашу машину** | Жодні дані сесій, якщо ви не запустите `clawmetry connect`. Дві речі виконуються за замовчуванням, обидві можна вимкнути, і жодна не несе вмісту сесій: анонімний пінг про встановлення та перевірка версії на PyPI. Кожен пункт призначення перелічено в [docs/EGRESS.md](docs/EGRESS.md), відновлено на основі перехоплення трафіку, а не з коментарів у коді. |

Варто знати два обмеження, перш ніж оцінювати результат: середовища виконання надають дуже
різні дані (деякі взагалі не публікують вартість — [матриця](docs/compatibility.md)
показує, які саме, для кожного середовища), а спостереження за дією не те саме, що можливість
її заблокувати ([які засоби контролю реальні, для кожного середовища](docs/APPROVALS.md)).


## Працює з 32 середовищами виконання агентів

**Безкоштовно у застосунку з відкритим кодом:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**На платному тарифі:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

Кожне середовище виконання отримує однакову панель. Запустіть кілька одночасно, і перемикач у
шапці переналаштує кожну вкладку на одне з них.

Створили власного агента на основі SDK? Перехоплювач відстежує й його виклики LLM.
Дивіться [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## Що ви отримуєте

- **Сесії та транскрипти**: що робив кожен агент, хід за ходом, з відтворенням
- **Вартість і токени**: по кожному середовищу виконання, моделі, сесії й дню, з позначками аномалій
- **Потік**: діаграма руху повідомлень через канали, моделі й інструменти в реальному часі
- **Brain**: потік подій міркувань і викликів інструментів у реальному часі
- **Перевищення контексту**: використання вікна, розраховане для кожного провайдера, стиснення проти примусового переповнення, а також мапа того, що ми *не бачимо* для кожного середовища виконання ([як](docs/CONTEXT_BLOWOUT.md))
- **Пам'ять і навички**: файли та навички, які фактично завантажило кожне середовище виконання
- **Стан і журнали**: диск, пам'ять, частота помилок, ліміти швидкості, потік журналів у реальному часі
- **Сповіщення**: ліміти бюджету, сплески помилок, агент офлайн, маршрутизуються в Slack, Discord, PagerDuty, Telegram, Email
- **Підтвердження**: призупиняйте ризиковані виклики інструментів *до* їх виконання та підтверджуйте з телефону ([як](docs/APPROVALS.md))

## Перевищення контексту та вартість спостереження

Два запитання, на які варто відповісти перш ніж довіряти будь-якому інструменту порівняння агентів.

**Як воно обробляє перевищення контекстного вікна в різних середовищах виконання?**

Відсоток використання настільки чесний, наскільки чесним є знаменник. ClawMetry
визначає розмір вікна для кожного провайдера з [таблиці, яку можна прочитати й
запропонувати PR](clawmetry/context_windows.py), що охоплює Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama і GLM. Вона не вимірює всі 32
середовища виконання однією лінійкою одного постачальника. Це важливо: хід на 300 тис. токенів GPT-5,
оцінений за міркою Anthropic у 200 тис., читається як ">100%, перевищено", тоді як насправді він на рівні 75% від
400 тис. GPT-5. Та сама лінійка приховує справді переповнений хід DeepSeek на 130 тис.
як комфортні 65%.

Кожне вікно постачається з походженням значення: `model_table`, `explicit_marker`,
`observed_floor` або чесне `default`, коли ми не знаємо модель. Індикатор, побудований на
здогадці, ніколи не відображається з тим самим авторитетом, що й побудований на
довіднику.

ClawMetry може бачити події стиснення лише в деяких середовищах виконання. Тому
`GET /api/context-coverage` повідомляє, для кожного середовища виконання, чи означає **нуль
"пройшло чисто" чи "ми не бачимо"**. `0`, що насправді означає сліпу зону, так і повідомляє.
[Повні деталі](docs/CONTEXT_BLOWOUT.md)

**Скільки коштує інструментація?**

| Шлях | Додано до вашого агента | За замовчуванням? |
|---|---|---|
| Читання файлів сесій (усі 32 середовища виконання) | **0**. Окремий процес, жодного коду ClawMetry у вашому агенті | увімкнено |
| HTTP-перехоплювач (`CLAWMETRY_INTERCEPT=1`) | **+0,44 мс** на виклик LLM, або 0,009% від 5-секундного виклику | вимкнено |
| Перед-інструментальний хук-шлюз (теплий кеш) | **+44 мс** на кожен контрольований виклик інструменту, понад базові 36 мс інтерпретатора | вимкнено |
| Проксі примусового виконання | **+9,7 мс** на виклик LLM | вимкнено |

Вартість хосту демона: приймання **2762 подій/с**, **710 байт/подію** на диску
(67,7 МБ на 100 тис. подій), і **приблизно 12% одного ядра** стабільно на активній
установці. Це останнє число перевищує наш власний заявлений бюджет 5-10%, тож воно
опубліковане як помилка, яку варто виправити, а не приховане зі сторінки.

Виміряно на Apple M2 Pro за допомогою `benchmarks/overhead.py`. Тестовий набір запускає
кожну умову в окремому процесі, чергує їх порядок і **відмовляється друкувати число,
якщо раунди розходяться в його знаку**. Запустіть його на власній машині за хвилину:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

Виміряно кожен шлях, включно з хук-шлюзами та проксі примусового виконання,
а тестовий набір працює на Linux, macOS і Windows у CI. Два результати варто
знати: проксі коштує приблизно в сім разів більше на Windows, ніж на Linux, а
демон наразі стабільно споживає близько 12% одного ядра, понад наш власний бюджет 5-10%.
Необроблений JSON, методика та те, що досі не виміряно, — у
[docs/OVERHEAD.md](docs/OVERHEAD.md).

## Ціноутворення

| Тариф | Що включено | Ціна |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, повна панель, лише локально | $0 |
| **Starter** | Усі інші середовища виконання вище, огляд парку, синхронізація з хмарою | $9 за вузол / місяць |
| **Pro** | Starter + контроль та оцінювання: підтвердження, політики ризику інструментів, оцінки, виявлення аномалій, оптимізатор вартості, експорт OTel, журнал аудиту, захищений від підробки | $19 за вузол / місяць |

Річні тарифи, Enterprise і актуальні ціни на
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**. Самостійно розміщені ліцензійні
ключі працюють без хмари (`clawmetry license`). Точний розподіл безкоштовного й платного —
у [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md).

## Ваші дані залишаються на вашій машині

ClawMetry читає локальні файли сесій і журнали. **Жодні дані сесій не залишають вашу машину,
якщо ви не запустите `clawmetry connect`** — жодних підказок, відповідей, аргументів інструментів, вмісту
файлів чи рядків журналів. Коли ви все ж підключаєтесь, знімок шифрується наскрізно
ключем, який ніколи не залишає вашу машину, і розшифровується у вашому браузері. Якщо у
вузла немає ключа, завантаження пропускається, а не надсилається у відкритому вигляді, і жодна
відповідь сервера не може це вимкнути.

Дві речі виконуються за замовчуванням до підключення, обидві можна вимкнути, і жодна не
несе даних сесій: анонімний пінг про встановлення та перевірка версії відносно
PyPI. Стандартна установка також один раз перевіряє вашу публічну IP-адресу для рядка
банера при запуску. Кожен пункт призначення, що він містить і як його вимкнути, перелічено в
[docs/EGRESS.md](docs/EGRESS.md); самостійно розміщені, перенаправлені та ізольовані від мережі
установки не роблять жодних довільних вихідних викликів взагалі.

Розшифрування відбувається у вашому браузері, у коді, який ми вам надсилаємо. Раніше це було
обіцянкою; тепер це те, що можна перевірити. Кожен рядок, що торкається вашого ключа,
міститься в одному читабельному файлі, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
який постачається всередині wheel-пакета й надається дослівно, закріплений хешем Subresource
Integrity. Щоб підтвердити, що браузер виконує саме те, що ми опублікували:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

Чого це не доводить: ми надаємо сторінку, яка завантажує цей файл, тож ми могли б
надати іншу сторінку. Хеші цілісності захищають вас від скомпрометованої CDN,
а не від постачальника. Ви отримуєте те, що будь-яка підміна має бути
навмисною, видимою в коді сторінки й відрізнятися від артефакту на PyPI,
який будь-хто може завантажити. Самостійне розміщення або робота лише локально повністю
усуває цю залежність.

## Встановлення

```bash
pip install clawmetry     # потім: clawmetry
```

Або однорядковий варіант: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

Потрібен Python 3.8+ на macOS, Linux або Windows, і хоча б одне середовище виконання агента на
тій самій машині. Інструкції для Docker: [docs/DOCKER.md](docs/DOCKER.md).

Або дозвольте агенту налаштувати це за вас. Навичка [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
навчає Claude Code, Codex, Cursor, Gemini CLI, Copilot або OpenCode
встановлювати ClawMetry, повідомляти, що роблять і скільки витрачають агенти на машині,
зупиняти одну сесію на вимогу та утримувати ризиковані виклики інструментів для підтвердження:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Документація

| | |
|---|---|
| [Сумісність середовищ виконання](docs/compatibility.md) | Що читає кожен адаптер і як додати середовище виконання |
| [Перевищення контексту](docs/CONTEXT_BLOWOUT.md) | Вікна для кожного провайдера, стиснення проти переповнення, покриття для кожного середовища виконання |
| [Накладні витрати](docs/OVERHEAD.md) | Скільки коштує інструментація, виміряно, з набором для відтворення |
| [Права доступу](docs/ENTITLEMENTS.md) | Безкоштовне проти платного, матриця тарифів, CLI ліцензії |
| [Підтвердження та політики](docs/APPROVALS.md) | Контроль перед виконанням, оцінка ризику, підтвердження з телефону |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | Експортуйте трейси куди завгодно, приймайте OTLP звідки завгодно |
| [Принесіть власного агента](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain від початку до кінця, з робочими прикладами |
| [Відстеження SDK](docs/SDK_TRACKING.md) | Атрибуція вартості для агентів, які ви створили самостійно |
| [Чат-канали](docs/CHANNELS.md) | Чат-адаптери, показані в Потоці |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | Ізольовані середовища NVIDIA NemoClaw |
| [Docker](docs/DOCKER.md) | Образ, compose, монтування томів |
| [Архітектура](ARCHITECTURE.md) · [Розробка](docs/DEVELOPMENT.md) | Як це працює всередині; запуск з коду |
| [Телеметрія](docs/TELEMETRY.md) | Анонімні пінги при встановленні та відкритті на робочому столі, і як їх вимкнути |

## Знімки екрана

Кожне число нижче — з однієї реальної машини, у режимі лише для читання, без жодних початкових даних.

**Повідомляє, коли щось не так, а не просто що сталося.**
Два банери аномалій зверху: витрати вдвічі перевищують середньоденні у 7 разів, і
сплеск вартості у 4,2 рази. Нижче — 324 з 667 останніх сесій із сигналом
марнотратства, розбитим за причинами.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**Показує, куди пішли гроші, у кожному вікні.**
$252,47 сьогодні, $513,15 цього тижня, $1312,92 цього місяця, кожне з токенами
за цим і тим, скільки з цього вже покриває ваша підписка. Нижче —
близько $1128/міс, позначено як таке, що можна повернути, і $17 256/міс уже заощаджено
завдяки повторному використанню кешу.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**Малює, як повідомлення стає відповіддю.**
Діаграма потоку в реальному часі: ви, канал, яким воно надійшло, шлюз, модель,
що відповідає прямо зараз, і кожен інструмент, до якого вона зверталася. Вузли підсвічуються
в міру проходження роботи через них.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**Кожен агент на машині, в одній таблиці.**
Що він виконує, скільки коштує за останні 24 години й за весь час, коли
його востаннє бачили, хто ним володіє, і чи покриває підписка рахунок. 14 агентів тут,
3 сесії працюють, 13 у спокої.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**Показує, куди пішов час і гроші ходу, інструмент за інструментом.**
Один хід реальної сесії: 11 інструментів за 11,2 хвилини за $1,16. Кожен виклик Bash
і виклик моделі отримує власний стовпець на хронології, тож команду, що виконувалась
4,1 хвилини, і ту, що виконувалась 226 мс, легко відрізнити з першого погляду.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**Оцінює роботу, а не лише витрати.**
Оцінка A цього тижня: 54 завдання виконані чисто, 2 складні коштували $48,57, а
прогони з надто малою активністю для оцінки виключені з оцінки, а не зараховані
як успіхи. Кожен складний прогін посилається на свій трейс.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**Показує, чому контекстне вікно продовжує заповнюватись.**
715 тис. з 1 млн токенів вікна на останньому ході, пік 83,3%, 4 стиснення,
всі спрацювали проактивно, а не через переповнення, і використання
кожного ходу за цим.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**Виявлення працює без будь-яких налаштувань з вашого боку.**
Вбудовані детектори увімкнені з моменту встановлення: агент замовк, потік телеметрії
зупинився, сплеск вартості, сплеск токенів, зростання помилок, сплеск помилок, поріг
бюджету, збіг сигнатури загрози, знахідка інструменту безпеки, зміна стану безпеки.
Власні правила — опційне доповнення.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**Утримання ризикованого виклику — опційне, і постачається вимкненим.**
Рекурсивні видалення, примусові push, sudo, секрети, встановлення пакетів і вихідні
виклики — кожен отримує правило, яке можна увімкнути. Доки ви цього не зробите, ClawMetry спостерігає й
нічого не змінює. Щойно правило увімкнено, відповідні виклики чекають тут (або на вашому телефоні)
на підтвердження чи відмову.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

Більше, для кожного середовища виконання: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## Визнання

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Історія зірок

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## Ліцензія

MIT · Створено [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
