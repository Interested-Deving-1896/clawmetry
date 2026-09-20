<!-- i18n-src:b22579578775 -->
> Русский translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**Агент может сделать сотню вызовов инструментов, так и не продвинувшись вперёд.** ClawMetry
читает файлы сессий, которые ваши кодинг-агенты уже пишут, и собирает временную шкалу,
вызовы инструментов и данные о токенах и стоимости, которые предоставляет среда выполнения, в едином
представлении — чтобы вы могли отличить долгий, но работающий прогон от застрявшего.

Работает с **32 средами выполнения ИИ-агентов** — Claude Code, OpenAI Codex, Hermes, OpenClaw и ещё 28. Одна панель для всего вашего флота агентов. ([полный список](SUPPORTED_RUNTIMES.txt), сгенерированный из каталога.)

> 🌐 **Читать на других языках:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [ещё →](docs/i18n/)

Одна команда. Никакой настройки. Всё определяется автоматически.

```bash
pip install clawmetry && clawmetry
```

Открывается по адресу **http://localhost:8900**. Никакой настройки: приложение находит уже
установленные у вас среды выполнения агентов, читает их только для чтения и ничего не меняет в их работе.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## Прежде чем устанавливать

| | |
|---|---|
| **Что делает** | Читает файлы сессий и логи, которые ваши агенты уже пишут. Никакого SDK, никаких изменений кода, никакой инструментации в вашем приложении. |
| **Что вы видите** | Временную шкалу сессии, пошаговое воспроизведение вызовов инструментов, разбивку по токенам и стоимости, а также сигналы траектории (зацикливание, повторяющиеся сбои) — для каждой среды выполнения. |
| **Что бесплатно** | `pip install clawmetry` читает **OpenClaw, NVIDIA NemoClaw, Goose и Qwen Code** без аккаунта, ключа и сетевых вызовов. Остальные 28 — Claude Code, Codex, Cursor и другие — читаются закрытым дополнением `clawmetry-pro`, которое доступно с 7-дневным пробным периодом или по подписке — точное разделение см. в [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md). |
| **Как начать** | `pip install clawmetry && clawmetry`, затем откройте localhost:8900. Ещё нет агентов на этой машине? `clawmetry --sample` откроет панель с тремя размеченными синтетическими сессиями. |
| **Что покидает вашу машину** | Никакие данные сессий, если вы не запустите `clawmetry connect`. По умолчанию выполняются две вещи, обе можно отключить, и ни одна не содержит содержимого сессий: анонимный пинг об установке и проверка версии на PyPI. Каждый пункт назначения перечислен в [docs/EGRESS.md](docs/EGRESS.md), восстановлен из перехвата трафика, а не из комментариев в коде. |

Стоит знать два ограничения, прежде чем судить о результатах: среды выполнения предоставляют очень
разные данные (некоторые вообще не публикуют стоимость — [таблица совместимости](docs/compatibility.md)
показывает, какие именно, по каждой среде выполнения), а наблюдение за действием — не то же самое, что
возможность его заблокировать ([какие элементы управления реальны, по каждой среде выполнения](docs/APPROVALS.md)).


## Работает с 32 средами выполнения агентов

**Бесплатно в приложении с открытым исходным кодом:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**По платной подписке:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

Каждая среда выполнения получает одну и ту же панель. Запускайте несколько одновременно, и переключатель
в шапке будет перенастраивать каждую вкладку на выбранную из них.

Собрали своего агента на базе SDK? Перехватчик отслеживает и его вызовы LLM
тоже. См. [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## Что вы получаете

- **Сессии и транскрипты**: что делал каждый агент, ход за ходом, с воспроизведением
- **Стоимость и токены**: по средам выполнения, моделям, сессиям и дням, с флагами аномалий
- **Flow**: живая диаграмма движения сообщений через каналы, модели и инструменты
- **Brain**: поток событий рассуждений и вызовов инструментов в реальном времени
- **Переполнение контекста**: утилизация окна с учётом провайдера, сжатие против принудительного переполнения, плюс карта того, что мы *не можем* увидеть по каждой среде выполнения ([как это работает](docs/CONTEXT_BLOWOUT.md))
- **Память и навыки**: файлы и навыки, которые действительно загрузила каждая среда выполнения
- **Здоровье и логи**: диск, память, частота ошибок, лимиты скорости, поток логов в реальном времени
- **Оповещения**: лимиты бюджета, всплески ошибок, офлайн-агент, отправка в Slack, Discord, PagerDuty, Telegram, Email
- **Подтверждения**: приостановка рискованных вызовов инструментов *до* их выполнения и подтверждение с телефона ([как это работает](docs/APPROVALS.md))

## Переполнение контекста и стоимость наблюдения

Два вопроса, на которые стоит ответить, прежде чем доверять любому инструменту сравнения агентов.

**Как это обрабатывает переполнение контекстного окна между разными средами выполнения?**

Процент утилизации честен ровно настолько, насколько честен знаменатель. ClawMetry
определяет размер окна для каждого провайдера по [таблице, которую можно прочитать и
предложить PR](clawmetry/context_windows.py), охватывающей Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama и GLM. Это не измерение всех 32
сред выполнения одной линейкой одного вендора. Это важно: ход на 300K токенов в GPT-5, оценённый
по линейке Anthropic в 200K, читается как ">100%, переполнено", хотя на самом деле это 75% от
400K у GPT-5. Та же линейка скрывает действительно переполненный ход DeepSeek на 130K,
показывая его как комфортные 65%.

Каждое окно поставляется с указанием происхождения: `model_table`, `explicit_marker`,
`observed_floor` или честный `default`, когда модель нам неизвестна. Индикатор, построенный на
догадке, никогда не отображается с той же достоверностью, что и построенный на
таблице соответствий.

ClawMetry может видеть события сжатия только на некоторых средах выполнения. Поэтому
`GET /api/context-coverage` сообщает по каждой среде выполнения, означает ли **ноль
"прошло чисто" или "мы не видим"**. `0`, который на самом деле означает "не видим", так и указывается.
[Подробности](docs/CONTEXT_BLOWOUT.md)

**Сколько стоит инструментация?**

| Путь | Добавлено к вашему агенту | По умолчанию? |
|---|---|---|
| Чтение файлов сессий (все 32 среды выполнения) | **0**. Отдельный процесс, никакого кода ClawMetry в вашем агенте | включено |
| HTTP-перехватчик (`CLAWMETRY_INTERCEPT=1`) | **+0.44 мс** на вызов LLM, или 0.009% от 5-секундного вызова | выключено |
| Хук перед вызовом инструмента (тёплый кэш) | **+44 мс** на каждый проверяемый вызов инструмента, сверх базового порога интерпретатора в 36 мс | выключено |
| Прокси принуждения | **+9.7 мс** на вызов LLM | выключено |

Стоимость для хоста демона: приём **2762 события/сек**, **710 байт/событие** на диске
(67.7 МБ на 100 тыс. событий), и **~12% одного ядра** в устойчивом режиме на загруженной
установке. Последнее число превышает наш собственный заявленный бюджет в 5-10%, поэтому оно
опубликовано как баг, который нужно исправить, а не скрыто со страницы.

Измерено на Apple M2 Pro с помощью `benchmarks/overhead.py`. Тестовый стенд запускает
каждое условие в отдельном процессе, чередует их порядок и **отказывается печатать
число, если раунды расходятся в его знаке**. Запустите его на своей
машине за минуту:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

Измерен каждый путь, включая хуки-проверки и прокси принуждения,
и тестовый стенд запускается на Linux, macOS и Windows в CI. Стоит знать два результата:
прокси стоит примерно в семь раз дороже на Windows, чем на Linux, а
демон в настоящее время стабильно использует около 12% одного ядра, что превышает наш собственный бюджет в 5-10%.
Необработанные данные JSON, методика и то, что пока не измерено, находятся в
[docs/OVERHEAD.md](docs/OVERHEAD.md).

## Цены

| План | Что включает | Цена |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, полная панель, только локально | $0 |
| **Starter** | Все остальные среды выполнения из списка выше, представление флота, облачная синхронизация | $9 за узел / месяц |
| **Pro** | Starter + управление и оценка: подтверждения, политики риска инструментов, оценки (evals), обнаружение аномалий, оптимизатор стоимости, экспорт OTel, защищённый от подделки журнал аудита | $19 за узел / месяц |

Годовые планы, Enterprise и актуальные цены находятся на
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**. Ключи для самостоятельного размещения
работают без облака (`clawmetry license`). Точное разделение бесплатного и платного —
в [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md).

## Ваши данные остаются на вашей машине

ClawMetry читает локальные файлы сессий и логи. **Никакие данные сессий не покидают вашу машину,
если вы не запустите `clawmetry connect`** — ни запросы, ни ответы, ни аргументы инструментов, ни содержимое файлов
или строк логов. Когда вы всё же подключаетесь, снимок шифруется сквозным шифрованием
с ключом, который никогда не покидает вашу машину, и расшифровывается в вашем браузере. Если у
узла нет ключа, загрузка пропускается, а не отправляется в открытом виде, и никакой
ответ сервера не может это отключить.

По умолчанию до подключения выполняются две вещи, обе отключаемые и ни одна не
содержит данных сессий: анонимный пинг об установке и проверка версии на
PyPI. Установка по умолчанию также один раз запрашивает ваш публичный IP для строки в
баннере при запуске. Каждый пункт назначения, что он содержит и как его отключить, перечислены в
[docs/EGRESS.md](docs/EGRESS.md); установки с самостоятельным размещением, с переопределённым адресом и изолированные от сети
вообще не делают никаких необязательных исходящих вызовов.

Расшифровка происходит в вашем браузере, в коде, который мы вам предоставляем. Раньше это было
обещанием; теперь это можно проверить. Каждая строка, которая обращается к вашему ключу,
находится в одном читаемом файле, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
который поставляется внутри wheel-пакета и отдаётся без изменений, закреплённый хешем Subresource
Integrity. Чтобы убедиться, что браузер выполняет именно то, что мы опубликовали:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

Чего это не доказывает: мы сами отдаём страницу, которая загружает этот файл, поэтому теоретически
могли бы отдать другую страницу. Хеши целостности защищают вас от скомпрометированного CDN,
но не от самого вендора. Что вы получаете — это то, что любая подмена должна быть
намеренной, видимой в исходном коде страницы и отличаться от артефакта на PyPI,
который может получить кто угодно. Самостоятельное размещение или работа только локально полностью
устраняет эту зависимость.

## Установка

```bash
pip install clawmetry     # затем: clawmetry
```

Или однострочник: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

Требуется Python 3.8+ на macOS, Linux или Windows, и хотя бы одна среда выполнения агента на
той же машине. Инструкции по Docker: [docs/DOCKER.md](docs/DOCKER.md).

Или позвольте агенту настроить всё за вас. Навык [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
учит Claude Code, Codex, Cursor, Gemini CLI, Copilot или OpenCode
устанавливать ClawMetry, сообщать, что делают и сколько тратят агенты на машине,
останавливать сессию по запросу и удерживать рискованные вызовы инструментов для подтверждения:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Документация

| | |
|---|---|
| [Совместимость сред выполнения](docs/compatibility.md) | Что читает каждый адаптер и как добавить среду выполнения |
| [Переполнение контекста](docs/CONTEXT_BLOWOUT.md) | Окна по провайдерам, сжатие против переполнения, покрытие по каждой среде выполнения |
| [Накладные расходы](docs/OVERHEAD.md) | Что стоит инструментация, измерено, со стендом для воспроизведения |
| [Права доступа](docs/ENTITLEMENTS.md) | Бесплатно против платно, матрица тарифов, license CLI |
| [Подтверждения и политики](docs/APPROVALS.md) | Проверка перед выполнением, оценка риска, подтверждения с телефона |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | Экспорт трасс куда угодно, приём OTLP откуда угодно |
| [Подключите своего агента](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain от начала до конца, с рабочими примерами |
| [Отслеживание через SDK](docs/SDK_TRACKING.md) | Учёт стоимости для агентов, которых вы создали сами |
| [Чат-каналы](docs/CHANNELS.md) | Адаптеры чатов, отображаемые во Flow |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | Изолированные (sandboxed) настройки NVIDIA NemoClaw |
| [Docker](docs/DOCKER.md) | Образ, compose, монтирование томов |
| [Архитектура](ARCHITECTURE.md) · [Разработка](docs/DEVELOPMENT.md) | Как это устроено внутри; запуск из исходников |
| [Телеметрия](docs/TELEMETRY.md) | Анонимные пинги об установке и открытии десктопного приложения, и как их отключить |

## Скриншоты

Каждая цифра ниже — с одной реальной машины, только для чтения, без каких-либо подготовленных данных.

**Приложение сообщает, когда что-то не так, а не просто что произошло.**
Два баннера аномалий сверху: расход, работающий в 7 раз выше среднедневного, и
всплеск стоимости в 4.2 раза. Ниже — 324 из 667 последних сессий, несущих сигнал
потерь, с разбивкой по причинам.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**Приложение показывает, куда ушли деньги, в любом окне времени.**
$252.47 сегодня, $513.15 за эту неделю, $1312.92 за этот месяц, с указанием
токенов за каждой цифрой и того, сколько из этого уже покрывает ваша подписка. Ниже —
около $1128/мес, размеченных как возможные к возврату, и уже $17 256/мес,
сэкономленных за счёт повторного использования кэша.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**Приложение рисует, как сообщение превращается в ответ.**
Живая диаграмма потока: вы, канал, по которому пришло сообщение, шлюз, модель,
отвечающая прямо сейчас, и каждый инструмент, к которому она обращалась. Узлы загораются по мере того,
как через них проходит работа.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**Каждый агент на машине — в одной таблице.**
Что он выполняет, сколько стоит за последние 24 часа и за всё время, когда
был замечен в последний раз, кому принадлежит и покрывается ли счёт подпиской.
Здесь 14 агентов, 3 сессии в работе, 13 в покое.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**Приложение показывает, куда ушло время и деньги хода, инструмент за инструментом.**
Один ход реальной сессии: 11 инструментов за 11.2 минуты за $1.16. Каждый вызов
Bash и каждый вызов модели получает свою полосу на временной шкале, поэтому команда, которая
выполнялась 4.1 минуты, и та, что выполнилась за 226 мс, различимы с первого взгляда.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**Приложение оценивает работу, а не только расходы.**
Оценка A за эту неделю: 54 задачи выполнены чисто, 2 неудачные обошлись в $48.57, а
прогоны со слишком малой активностью для оценки исключены из итоговой оценки, а не
засчитаны как успехи. Каждый неудачный прогон ссылается на свою трассировку.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**Приложение показывает, почему контекстное окно продолжает заполняться.**
715K из 1M-токенного окна на последнем ходу, пик 83.3%, 4 сжатия,
все сработавшие проактивно, а не из-за переполнения, и утилизация
каждого хода за этим.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**Обнаружение работает без какой-либо настройки с вашей стороны.**
Встроенные детекторы включены сразу после установки: агент замолчал, поток телеметрии
остановился, всплеск стоимости, всплеск токенов, растущее число ошибок, всплеск ошибок, порог
бюджета, обнаружена сигнатура угрозы, находка инструмента безопасности, изменение
состояния безопасности. Ваши собственные правила — опциональное дополнение.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**Удержание рискованного вызова — опция, отключённая по умолчанию.**
Рекурсивные удаления, принудительные пуши (force push), sudo, секреты, установка пакетов и исходящие
вызовы — для каждого можно включить своё правило. Пока вы этого не сделаете, ClawMetry наблюдает и
ничего не меняет. Как только правило включено, подходящие под него вызовы ждут здесь (или на вашем телефоне)
подтверждения или отклонения.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

Больше скриншотов по каждой среде выполнения: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## Признание

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## История звёзд

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## Лицензия

MIT · Создано [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
