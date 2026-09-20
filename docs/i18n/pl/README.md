<!-- i18n-src:b22579578775 -->
> Polski translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**Agent może wykonać sto wywołań narzędzi, nie robiąc żadnego postępu.** ClawMetry
odczytuje pliki sesji, które twoje agenty kodujące już zapisują, i zestawia oś czasu,
wywołania narzędzi oraz wszelkie dane o tokenach i kosztach udostępniane przez środowisko
uruchomieniowe w jednym widoku — dzięki czemu potrafisz odróżnić długi przebieg, który
działa poprawnie, od takiego, który utknął.

Działa z **32 środowiskami uruchomieniowymi agentów AI** — Claude Code, OpenAI Codex, Hermes, OpenClaw i 28 innych. Jeden dashboard dla całej floty twoich agentów. ([pełna lista](SUPPORTED_RUNTIMES.txt), generowana z katalogu.)

> 🌐 **Przeczytaj to w:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [więcej →](docs/i18n/)

Jedno polecenie. Zero konfiguracji. Wykrywa wszystko automatycznie.

```bash
pip install clawmetry && clawmetry
```

Otwiera się pod adresem **http://localhost:8900**. Zero konfiguracji: znajduje
środowiska uruchomieniowe agentów, które już masz, odczytuje je w trybie tylko do odczytu
i niczego nie zmienia w sposobie ich działania.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## Zanim zainstalujesz

| | |
|---|---|
| **Co to robi** | Odczytuje pliki sesji i logi, które twoje agenty już zapisują. Bez SDK, bez zmian w kodzie, bez instrumentacji w twojej aplikacji. |
| **Co widzisz** | Oś czasu sesji, odtwarzanie krok po kroku wywołań narzędzi, podział tokenów i kosztów oraz sygnały trajektorii (pętle, powtarzające się błędy) — dla każdego środowiska uruchomieniowego. |
| **Co jest darmowe** | `pip install clawmetry` odczytuje **OpenClaw, NVIDIA NemoClaw, Goose i Qwen Code** bez konta, bez klucza i bez połączenia sieciowego. Pozostałe 28 — Claude Code, Codex, Cursor i reszta — jest odczytywanych przez zamknięty komponent `clawmetry-pro`, który dostępny jest w ramach 7-dniowego okresu próbnego lub planu płatnego — dokładny podział znajdziesz w [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md). |
| **Jak zacząć** | `pip install clawmetry && clawmetry`, następnie otwórz localhost:8900. Nie masz jeszcze agentów na tej maszynie? `clawmetry --sample` otwiera się z trzema oznaczonymi, syntetycznymi sesjami. |
| **Co opuszcza twoją maszynę** | Żadne dane sesji, chyba że uruchomisz `clawmetry connect`. Domyślnie działają dwie rzeczy, obie opcjonalne (opt-out) i żadna nie przenosi treści sesji: anonimowy ping instalacyjny i sprawdzenie wersji w PyPI. Każdy cel jest spisany w [docs/EGRESS.md](docs/EGRESS.md), odtworzony na podstawie przechwytu ruchu sieciowego, a nie na podstawie komentarzy w kodzie. |

Dwa ograniczenia warto znać, zanim ocenisz wyniki: środowiska uruchomieniowe udostępniają
bardzo różne dane (niektóre w ogóle nie publikują kosztów — [macierz](docs/compatibility.md)
mówi, które konkretnie), a obserwowanie działania to nie to samo, co możliwość jego
zablokowania ([które kontrolki są realne, dla każdego środowiska](docs/APPROVALS.md)).


## Działa z 32 środowiskami uruchomieniowymi agentów

**Darmowe w aplikacji open source:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**W planie płatnym:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

Każde środowisko uruchomieniowe otrzymuje ten sam dashboard. Uruchom kilka naraz,
a przełącznik w nagłówku przeskaluje każdą zakładkę do jednego z nich.

Zbudowałeś własnego agenta na SDK zamiast tego? Interceptor śledzi także jego
wywołania LLM. Zobacz [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## Co otrzymujesz

- **Sesje i transkrypty**: co zrobił każdy agent, tura po turze, z odtwarzaniem
- **Koszty i tokeny**: dla każdego środowiska uruchomieniowego, modelu, sesji i dnia, z oznaczeniami anomalii
- **Flow**: diagram na żywo przedstawiający wiadomości przepływające przez kanały, modele i narzędzia
- **Brain**: strumień zdarzeń rozumowania i wywołań narzędzi na żywo
- **Przepełnienie kontekstu**: wykorzystanie okna liczone osobno dla każdego dostawcy, kompaktowanie kontra wymuszone przepełnienie, a także mapa tego, czego *nie widzimy* dla każdego środowiska uruchomieniowego ([jak](docs/CONTEXT_BLOWOUT.md))
- **Pamięć i umiejętności**: pliki i umiejętności, które faktycznie załadowało każde środowisko uruchomieniowe
- **Zdrowie i logi**: dysk, pamięć, wskaźniki błędów, limity zapytań, strumień logów na żywo
- **Alerty**: limity budżetu, skoki błędów, agent offline, kierowane do Slack, Discord, PagerDuty, Telegram, Email
- **Zatwierdzenia**: wstrzymuj ryzykowne wywołania narzędzi *przed* ich wykonaniem i zatwierdzaj je z telefonu ([jak](docs/APPROVALS.md))

## Przepełnienie kontekstu i koszt obserwacji

Dwa pytania warte odpowiedzi, zanim zaufasz jakiemukolwiek narzędziu do porównywania agentów.

**Jak radzi sobie z przepełnieniem okna kontekstu w różnych środowiskach uruchomieniowych?**

Procent wykorzystania jest tak wiarygodny, jak wartość, przez którą jest dzielony.
ClawMetry ustala rozmiar okna dla każdego dostawcy na podstawie
[tabeli, którą możesz przeczytać i zgłosić PR](clawmetry/context_windows.py),
obejmującej Anthropic, OpenAI, Google, xAI, DeepSeek, Kimi, Qwen, Mistral, Llama
i GLM. Nie mierzy wszystkich 32 środowisk uruchomieniowych jedną miarką jednego
dostawcy. To ma znaczenie: tura na 300K tokenów w GPT-5, oceniana wg 200K
Anthropic, pokazuje ">100%, przepełnione", podczas gdy w rzeczywistości to 75%
z 400K GPT-5. Ta sama miarka ukrywa faktycznie przepełnioną turę DeepSeek na
130K jako komfortowe 65%.

Każde okno ma swoją proweniencję: `model_table`, `explicit_marker`,
`observed_floor` albo uczciwe `default`, gdy nie znamy modelu. Wskaźnik
zbudowany na domysłach nigdy nie wyświetla się z taką samą pewnością, jak ten
zbudowany na podstawie tabeli.

ClawMetry może zobaczyć zdarzenia kompaktowania tylko w niektórych środowiskach
uruchomieniowych. Dlatego `GET /api/context-coverage` raportuje, dla każdego
środowiska uruchomieniowego, czy **zero oznacza „przebiegło czysto” czy „jesteśmy
ślepi”**. `0`, które w rzeczywistości oznacza ślepotę, mówi o tym wprost.
[Pełne informacje](docs/CONTEXT_BLOWOUT.md)

**Ile kosztuje instrumentacja?**

| Ścieżka | Dodane do twojego agenta | Domyślnie? |
|---|---|---|
| Śledzenie plików sesji (wszystkie 32 środowiska uruchomieniowe) | **0**. Osobny proces, żadnego kodu ClawMetry w twoim agencie | włączone |
| Interceptor HTTP (`CLAWMETRY_INTERCEPT=1`) | **+0,44 ms** na wywołanie LLM, czyli 0,009% wywołania trwającego 5s | wyłączone |
| Bramka pre-tool hook (ciepły cache) | **+44 ms** na bramkowane wywołanie narzędzia, ponad podłogę interpretera wynoszącą 36 ms | wyłączone |
| Proxy egzekwujące | **+9,7 ms** na wywołanie LLM | wyłączone |

Koszt hosta demona: **2762 zdarzenia/s** przy pozyskiwaniu, **710 bajtów/zdarzenie**
na dysku (67,7 MB na 100 tys. zdarzeń) oraz **~12% jednego rdzenia** w trybie ciągłym
przy obciążonej instalacji. Ta ostatnia liczba przekracza nasz własny deklarowany
budżet 5-10%, więc jest publikowana jako błąd do naprawienia, a nie pominięta na stronie.

Mierzone na Apple M2 Pro za pomocą `benchmarks/overhead.py`. Harness uruchamia
każdy warunek w osobnym procesie, zmienia ich kolejność i **odmawia wypisania
liczby, gdy rundy nie zgadzają się co do jej znaku**. Uruchom go na własnej maszynie
w minutę:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

Każda ścieżka jest mierzona, w tym bramki hooków i proxy egzekwujące, a harness
działa w CI na Linuksie, macOS i Windows. Dwa wyniki warto znać: proxy kosztuje
około siedmiokrotnie więcej na Windows niż na Linuksie, a demon obecnie utrzymuje
około 12% jednego rdzenia, powyżej naszego własnego budżetu 5-10%. Surowy JSON,
metodologia i to, co wciąż nie jest zmierzone, znajdują się w
[docs/OVERHEAD.md](docs/OVERHEAD.md).

## Cennik

| Plan | Co obejmuje | Cena |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, pełny dashboard, tylko lokalnie | 0 $ |
| **Starter** | Każde inne środowisko uruchomieniowe powyżej, widok floty, synchronizacja w chmurze | 9 $ za węzeł / miesiąc |
| **Pro** | Starter + kontrola i ewaluacja: zatwierdzenia, polityki ryzyka narzędzi, ewaluacje, wykrywanie anomalii, optymalizator kosztów, eksport OTel, dziennik audytu odporny na manipulacje | 19 $ za węzeł / miesiąc |

Plany roczne, Enterprise i aktualne ceny znajdują się na stronie
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**. Klucze licencji
self-hosted działają bez chmury (`clawmetry license`). Dokładny podział na
funkcje darmowe i płatne znajduje się w [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md).

## Twoje dane pozostają na twojej maszynie

ClawMetry odczytuje lokalne pliki sesji i logi. **Żadne dane sesji nie opuszczają
twojej maszyny, chyba że uruchomisz `clawmetry connect`** — żadnych promptów,
odpowiedzi, argumentów narzędzi, zawartości plików ani wierszy logów. Gdy już
się połączysz, migawka jest szyfrowana end-to-end kluczem, który nigdy nie
opuszcza twojej maszyny, i odszyfrowywana w twojej przeglądarce. Jeśli węzeł
nie ma klucza, przesyłanie jest pomijane zamiast wysyłania w formie jawnej, i
żadna odpowiedź serwera nie może tego wyłączyć.

Dwie rzeczy działają domyślnie, zanim się połączysz, obie opcjonalne (opt-out)
i żadna nie przenosi danych sesji: anonimowy ping instalacyjny i sprawdzenie
wersji względem PyPI. Domyślna instalacja sprawdza też raz twój publiczny adres
IP na potrzeby linii banera startowego. Każdy cel, to co przenosi i jak to
wyłączyć, jest wymienione w [docs/EGRESS.md](docs/EGRESS.md); instalacje
self-hosted, przekierowane i odizolowane od sieci (air-gapped) nie wykonują
żadnych opcjonalnych połączeń wychodzących.

Odszyfrowanie odbywa się w twojej przeglądarce, w kodzie, który ci dostarczamy.
Kiedyś była to obietnica; teraz jest to coś, co możesz sprawdzić. Każda linia
mająca dostęp do twojego klucza znajduje się w jednym czytelnym pliku,
[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
który jest dołączony do wheel i serwowany dosłownie, przypięty skrótem
Subresource Integrity. Aby potwierdzić, że przeglądarka uruchamia to, co
opublikowaliśmy:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

Czego to nie dowodzi: serwujemy stronę, która ładuje ten plik, więc moglibyśmy
serwować inną stronę. Skróty integralności chronią cię przed skompromitowanym
CDN-em, nie przed dostawcą. To, co zyskujesz, to fakt, że każda podmiana musi
być celowa, widoczna w źródle strony i inna od artefaktu w PyPI, który każdy
może pobrać. Self-hosting lub pozostanie wyłącznie lokalnym całkowicie usuwa
tę zależność.

## Instalacja

```bash
pip install clawmetry     # następnie: clawmetry
```

Albo jedna linijka: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

Wymaga Pythona 3.8+ na macOS, Linuksie lub Windows oraz co najmniej jednego
środowiska uruchomieniowego agenta na tej samej maszynie. Instrukcje Docker:
[docs/DOCKER.md](docs/DOCKER.md).

Albo pozwól agentowi skonfigurować to za ciebie. Umiejętność
[`agent-kill-switch`](skills/agent-kill-switch/SKILL.md) uczy Claude Code,
Codex, Cursor, Gemini CLI, Copilot lub OpenCode, jak zainstalować ClawMetry,
raportować, co robią i ile wydają agenty na maszynie, zatrzymać jedną sesję
na żądanie oraz wstrzymywać ryzykowne wywołania narzędzi do zatwierdzenia:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Dokumentacja

| | |
|---|---|
| [Zgodność środowisk uruchomieniowych](docs/compatibility.md) | Co odczytuje każdy adapter i jak dodać środowisko uruchomieniowe |
| [Przepełnienie kontekstu](docs/CONTEXT_BLOWOUT.md) | Okna dla każdego dostawcy, kompaktowanie kontra przepełnienie, pokrycie dla każdego środowiska uruchomieniowego |
| [Narzut](docs/OVERHEAD.md) | Ile kosztuje instrumentacja, zmierzone, wraz z harnessem do odtworzenia |
| [Uprawnienia](docs/ENTITLEMENTS.md) | Darmowe kontra płatne, macierz poziomów, CLI licencji |
| [Zatwierdzenia i polityki](docs/APPROVALS.md) | Bramkowanie przed wykonaniem, ocena ryzyka, zatwierdzenia z telefonu |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | Eksportuj ślady gdziekolwiek, pozyskuj OTLP z czegokolwiek |
| [Podłącz własnego agenta](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain od początku do końca, z przykładami do uruchomienia |
| [Śledzenie SDK](docs/SDK_TRACKING.md) | Przypisywanie kosztów dla agentów, które sam zbudowałeś |
| [Kanały czatu](docs/CHANNELS.md) | Adaptery czatu pokazane w Flow |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | Odizolowane konfiguracje NVIDIA NemoClaw |
| [Docker](docs/DOCKER.md) | Obraz, compose, montowanie wolumenów |
| [Architektura](ARCHITECTURE.md) · [Rozwój](docs/DEVELOPMENT.md) | Jak to działa od środka; uruchamianie ze źródeł |
| [Telemetria](docs/TELEMETRY.md) | Anonimowe pingi instalacji i otwarcia aplikacji desktopowej oraz jak je wyłączyć |

## Zrzuty ekranu

Każda liczba poniżej pochodzi z jednej prawdziwej maszyny, w trybie tylko do odczytu, bez żadnych danych podstawionych na potrzeby demonstracji.

**Informuje, kiedy coś jest nie tak, a nie tylko co się wydarzyło.**
Dwa banery anomalii na górze: wydatki na poziomie 7-krotności dziennej średniej
oraz 4,2-krotny skok kosztów. Poniżej, 324 z 667 ostatnich sesji niosących sygnał
marnotrawstwa, z podziałem na przyczyny.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**Pokazuje, gdzie poszły pieniądze, w każdym oknie czasowym.**
252,47 $ dzisiaj, 513,15 $ w tym tygodniu, 1312,92 $ w tym miesiącu, każda kwota
wraz z tokenami, które ją wygenerowały, i informacją, ile z tego pokrywa już twoja
subskrypcja. Poniżej, około 1128 $/mies. oznaczone jako możliwe do odzyskania
i już 17 256 $/mies. zaoszczędzone dzięki ponownemu wykorzystaniu cache.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**Rysuje, jak wiadomość staje się odpowiedzią.**
Diagram przepływu na żywo: ty, kanał, przez który dotarła wiadomość, gateway,
model odpowiadający w danej chwili oraz każde narzędzie, po które sięgnął.
Węzły podświetlają się w miarę przepływu pracy.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**Każdy agent na maszynie, w jednej tabeli.**
Co uruchamia, ile kosztuje w ciągu ostatnich 24 godzin i przez cały czas
istnienia, kiedy był ostatnio widziany, kto jest jego właścicielem oraz czy
subskrypcja pokrywa rachunek. 14 agentów tutaj, 3 sesje w trakcie pracy, 13
w spoczynku.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**Pokazuje, gdzie poszedł czas i pieniądze danej tury, narzędzie po narzędziu.**
Jedna tura prawdziwej sesji: 11 narzędzi w 11,2 minuty za 1,16 $. Każde
wywołanie Bash i wywołanie modelu ma swój własny pasek na osi czasu, dzięki
czemu polecenie trwające 4,1 minuty i to trwające 226 ms od razu daje się
odróżnić na pierwszy rzut oka.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**Ocenia jakość pracy, a nie tylko wydatki.**
Ocena A w tym tygodniu: 54 zadania wróciły czyste, 2 problematyczne kosztowały
48,57 $, a przebiegi z za małą ilością aktywności, by je ocenić, są pomijane
w ocenie zamiast liczyć się jako sukcesy. Każdy problematyczny przebieg
odsyła do swojego śladu (trace).

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**Pokazuje, dlaczego okno kontekstu wciąż się zapełnia.**
715K z okna 1M tokenów w ostatniej turze, szczyt 83,3%, 4 kompaktowania,
z których wszystkie uruchomiły się proaktywnie, a nie z powodu przepełnienia,
oraz wykorzystanie każdej tury, która do tego doprowadziła.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**Wykrywanie działa bez żadnej konfiguracji z twojej strony.**
Wbudowane detektory są włączone od instalacji: agent zamilkł, strumień
telemetrii się zatrzymał, skok kosztów, wybuch liczby tokenów, rosnąca liczba
błędów, skok błędów, próg budżetu, wykryta sygnatura zagrożenia, wynik
narzędzia bezpieczeństwa, zmiana postawy bezpieczeństwa. Twoje własne reguły
są opcjonalnym dodatkiem.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**Wstrzymywanie ryzykownych wywołań jest opcjonalne (opt-in) i wysyłane od razu.**
Rekurencyjne usuwanie, wymuszone push'e, sudo, sekrety, instalacje pakietów
i wywołania wychodzące — każde z nich ma regułę, którą możesz włączyć. Dopóki
tego nie zrobisz, ClawMetry obserwuje i niczego nie zmienia. Gdy jedna z nich
jest włączona, pasujące wywołania czekają tutaj (lub na twoim telefonie) na
zatwierdzenie albo odrzucenie.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

Więcej, dla każdego środowiska uruchomieniowego: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## Uznanie

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Historia gwiazdek

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## Licencja

MIT · Stworzone przez [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
