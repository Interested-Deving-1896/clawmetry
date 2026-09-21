<!-- i18n-src:b22579578775 -->
> Türkçe translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**Bir ajan, ilerleme kaydetmeden yüzlerce araç çağrısı yapabilir.** ClawMetry,
kodlama ajanlarınızın zaten yazdığı oturum dosyalarını okur ve zaman çizelgesini,
araç çağrılarını ve çalışma zamanının sunduğu token ve maliyet verilerini tek bir
görünümde toplar; böylece çalışan uzun bir koşuyu takılıp kalmış olandan
ayırt edebilirsiniz.

**32 AI ajan çalışma zamanıyla** çalışır: Claude Code, OpenAI Codex, Hermes, OpenClaw ve 28 tane daha. Tüm ajan filonuz için tek bir gösterge paneli. ([tam liste](SUPPORTED_RUNTIMES.txt), katalogdan üretilir.)

> 🌐 **Bunu şu dillerde okuyun:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [daha fazlası →](docs/i18n/)

Tek komut. Sıfır yapılandırma. Her şeyi otomatik algılar.

```bash
pip install clawmetry && clawmetry
```

**http://localhost:8900** adresinde açılır. Sıfır yapılandırma: zaten sahip olduğunuz
ajan çalışma zamanlarını bulur, onları salt okunur şekilde okur ve nasıl çalıştıkları
konusunda hiçbir şeyi değiştirmez.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## Kurmadan önce

| | |
|---|---|
| **Ne yapar** | Ajanlarınızın zaten yazdığı oturum dosyalarını ve günlükleri okur. SDK yok, kod değişikliği yok, uygulamanızda enstrümantasyon yok. |
| **Ne görürsünüz** | Oturum zaman çizelgesi, araç araç yeniden oynatma, token ve maliyet dökümü ve yörünge sinyalleri (döngüye girme, tekrarlanan hatalar) — çalışma zamanı başına. |
| **Ücretsiz olan** | `pip install clawmetry`, hesap, anahtar veya ağ çağrısı olmadan **OpenClaw, NVIDIA NemoClaw, Goose ve Qwen Code**'u okur. Diğer 28 tanesi (Claude Code, Codex, Cursor ve geri kalanı), 7 günlük deneme veya bir planla birlikte gelen kapalı kaynaklı `clawmetry-pro` eklentisi tarafından okunur; tam ayrım için bkz. [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md). |
| **Nasıl başlanır** | `pip install clawmetry && clawmetry`, ardından localhost:8900'ü açın. Bu makinede henüz ajan yok mu? `clawmetry --sample`, etiketlenmiş üç sentetik oturumla açılır. |
| **Makinenizden ne çıkar** | `clawmetry connect` çalıştırmadığınız sürece hiçbir oturum verisi çıkmaz. Varsayılan olarak iki şey çalışır, ikisi de devre dışı bırakılabilir ve hiçbiri oturum içeriği taşımaz: anonim bir kurulum pingi ve bir PyPI sürüm kontrolü. Her hedef, yorumları okuyarak değil bir tel yakalamasından yeniden oluşturularak [docs/EGRESS.md](docs/EGRESS.md) içinde envanterlenmiştir. |

Çıktıyı değerlendirmeden önce bilinmesi gereken iki sınır var: çalışma zamanları
çok farklı veriler sunar (bazıları hiç maliyet yayınlamaz — [matris](docs/compatibility.md)
hangisinin, çalışma zamanı bazında, olduğunu söyler) ve bir eylemi gözlemlemek onu
engelleyebilmekle aynı şey değildir ([hangi kontroller gerçek, çalışma zamanı bazında](docs/APPROVALS.md)).


## 32 çalışma zamanıyla çalışır

**Açık kaynak uygulamada ücretsiz:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**Ücretli bir planda:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

Her çalışma zamanı aynı gösterge panelini alır. Aynı anda birkaçını çalıştırın,
üst bilgideki değiştirici her sekmeyi bunlardan birine yeniden odaklar.

Kendi ajanınızı bir SDK üzerine mi inşa ettiniz? Interceptor onun LLM çağrılarını
da izler. Bkz. [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## Neler elde edersiniz

- **Oturumlar ve dökümler**: her ajanın ne yaptığı, tur tur, yeniden oynatmayla
- **Maliyet ve tokenlar**: çalışma zamanı, model, oturum ve gün bazında, anomali işaretleriyle
- **Akış (Flow)**: kanallar, modeller ve araçlar arasında hareket eden mesajların canlı diyagramı
- **Beyin (Brain)**: gerçekleştiği anda muhakeme ve araç çağrısı olay akışı
- **Bağlam taşması**: sağlayıcı bazında boyutlandırılmış pencere kullanımı, sıkıştırma ile zorlanmış taşma karşılaştırması, ayrıca çalışma zamanı bazında *göremediğimiz* şeylerin bir haritası ([nasıl](docs/CONTEXT_BLOWOUT.md))
- **Bellek ve beceriler**: her çalışma zamanının gerçekte yüklediği dosyalar ve beceriler
- **Sağlık ve günlükler**: disk, bellek, hata oranları, hız sınırları, canlı günlük akışı
- **Uyarılar**: bütçe sınırları, hata artışları, ajan çevrimdışı olayları; Slack, Discord, PagerDuty, Telegram, E-posta'ya yönlendirilir
- **Onaylar**: riskli araç çağrılarını çalışmadan *önce* duraklatın ve telefonunuzdan onaylayın ([nasıl](docs/APPROVALS.md))

## Bağlam taşması ve izlemenin maliyeti

Herhangi bir ajan karşılaştırma aracına güvenmeden önce yanıtlanmaya değer iki soru.

**Çalışma zamanları arasında bağlam penceresi taşmasını nasıl ele alıyor?**

Bir kullanım yüzdesi, ancak neye bölündüğü kadar dürüsttür. ClawMetry, pencereyi
[okuyabileceğiniz ve PR gönderebileceğiniz bir tablodan](clawmetry/context_windows.py)
sağlayıcı bazında boyutlandırır; Anthropic, OpenAI, Google, xAI, DeepSeek, Kimi,
Qwen, Mistral, Llama ve GLM'yi kapsar. 32 çalışma zamanının tamamını tek bir
satıcının cetveliyle ölçmez. Bu önemlidir: Anthropic'in 200K'sına karşı
puanlanan 300K'lık bir GPT-5 turu, aslında GPT-5'in 400K'sının %75'indeyken
">%100, taşmış" olarak okunur. Aynı cetvel, gerçekten taşmış 130K'lık bir
DeepSeek turunu rahat bir %65 olarak gizler.

Her pencere, kaynağıyla birlikte gelir: `model_table`, `explicit_marker`,
`observed_floor` veya modeli bilmediğimizde dürüst bir `default`. Bir tahmin
üzerine kurulu bir gösterge, hiçbir zaman bir arama üzerine kurulu olanla aynı
otoriteyle görüntülenmez.

ClawMetry, sıkıştırma olaylarını yalnızca bazı çalışma zamanlarında görebilir.
Bu yüzden `GET /api/context-coverage`, çalışma zamanı bazında, **sıfırın
"temiz çalıştı" mı yoksa "kör durumdayız" mı** anlamına geldiğini raporlar.
Gerçekte kör anlamına gelen bir `0`, bunu belirtir.
[Tam ayrıntı](docs/CONTEXT_BLOWOUT.md)

**Enstrümantasyonun maliyeti nedir?**

| Yol | Ajanınıza eklenen | Varsayılan mı? |
|---|---|---|
| Oturum dosyası izleme (tüm 32 çalışma zamanı) | **0**. Ayrı işlem, ajanınızda ClawMetry kodu yok | açık |
| HTTP interceptor (`CLAWMETRY_INTERCEPT=1`) | LLM çağrısı başına **+0,44 ms**, yani 5 saniyelik bir çağrının %0,009'u | kapalı |
| Ön-araç hook geçidi (ısınmış önbellek) | Geçit uygulanan araç çağrısı başına **+44 ms**, 36 ms'lik yorumlayıcı tabanının üzerinde | kapalı |
| Uygulama proxy'si | LLM çağrısı başına **+9,7 ms** | kapalı |

Daemon ana bilgisayar maliyeti: alım başına **saniyede 2.762 olay**, diskte
**olay başına 710 bayt** (100 bin olay için 67,7 MB) ve yoğun bir kurulumda
sürdürülen **bir çekirdeğin ~%12'si**. Bu son rakam, kendi belirttiğimiz
%5-10 bütçenin üzerinde, bu yüzden sayfadan çıkarılmak yerine peşine
düşülmesi gereken bir hata olarak yayınlanıyor.

Bir Apple M2 Pro üzerinde `benchmarks/overhead.py` ile ölçülmüştür. Kabuk
(harness), her durumu ayrı bir işlemde çalıştırır, sıralarını değiştirir ve
**turlar işaret konusunda anlaşamadığında bir sayı basmayı reddeder**.
Kendi makinenizde bir dakikada çalıştırın:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

Hook geçitleri ve uygulama proxy'si dahil her yol ölçülür ve kabuk, CI'da
Linux, macOS ve Windows üzerinde çalışır. Bilinmeye değer iki sonuç: proxy,
Windows'ta Linux'a göre yaklaşık yedi kat daha maliyetli ve daemon şu anda
bir çekirdeğin yaklaşık %12'sini sürdürüyor, kendi %5-10 bütçemizin üzerinde.
Ham JSON, yöntem ve hâlâ ölçülmemiş olanlar
[docs/OVERHEAD.md](docs/OVERHEAD.md) içindedir.

## Fiyatlandırma

| Plan | Neyi kapsar | Fiyat |
|---|---|---|
| **Ücretsiz** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, tam gösterge paneli, yalnızca yerel | $0 |
| **Starter** | Yukarıdaki diğer tüm çalışma zamanları, filo görünümü, bulut senkronizasyonu | Düğüm başına ayda $9 |
| **Pro** | Starter + kontrol ve değerlendirme: onaylar, araç riski politikaları, değerlendirmeler, anomali tespiti, maliyet optimize edici, OTel dışa aktarımı, kurcalamaya karşı kanıtlı denetim günlüğü | Düğüm başına ayda $19 |

Yıllık planlar, Enterprise ve güncel rakamlar
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** adresinde bulunur.
Kendi barındırılan lisans anahtarları bulut olmadan çalışır (`clawmetry license`).
Tam ücretsiz/ücretli ayrımı [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) içindedir.

## Verileriniz makinenizde kalır

ClawMetry yerel oturum dosyalarını ve günlükleri okur. **`clawmetry connect`
çalıştırmadığınız sürece hiçbir oturum verisi kutunuzdan çıkmaz** — istemler,
yanıtlar, araç bağımsız değişkenleri, dosya içerikleri veya günlük satırları
dahil değil. Bağlandığınızda, anlık görüntü, makinenizden hiç çıkmayan bir
anahtarla uçtan uca şifrelenir ve tarayıcınızda şifresi çözülür. Bir düğümün
anahtarı yoksa yükleme, açık metin olarak gönderilmek yerine atlanır ve
hiçbir sunucu yanıtı bunu kapatamaz.

Bağlanmadan önce varsayılan olarak iki şey çalışır, ikisi de devre dışı
bırakılabilir ve hiçbiri oturum verisi taşımaz: anonim bir kurulum pingi ve
PyPI'ye karşı bir sürüm kontrolü. Varsayılan bir kurulum ayrıca başlangıç
banner satırı için genel IP adresinizi bir kez sorgular. Her hedef, ne
taşıdığı ve nasıl kapatılacağı [docs/EGRESS.md](docs/EGRESS.md) içinde
listelenmiştir; kendi barındırılan, yeniden yönlendirilmiş ve hava boşluklu
kurulumlar hiçbir isteğe bağlı giden çağrı yapmaz.

Şifre çözme, size sunduğumuz kodla tarayıcınızda gerçekleşir. Bu eskiden bir
vaatti; artık kontrol edebileceğiniz bir şey. Anahtarınıza dokunan her satır
okunabilir tek bir dosyada yaşar, [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
bu dosya wheel içinde gönderilir ve olduğu gibi, bir Subresource Integrity
hash'iyle sabitlenmiş şekilde sunulur. Tarayıcının yayınladığımız şeyi
çalıştırdığını doğrulamak için:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

Bunun kanıtlamadığı şey: dosyayı yükleyen sayfayı biz sunuyoruz, dolayısıyla
farklı bir sayfa sunabiliriz. Integrity hash'leri sizi ele geçirilmiş bir
CDN'den korur, satıcıdan değil. Kazandığınız şey, herhangi bir değiştirmenin
kasıtlı, sayfa kaynağında görünür ve herkesin PyPI'den alabileceği bir
yapıttan farklı olması gerektiğidir. Kendi barındırma veya yalnızca yerel
kalma, bu bağımlılığı tamamen ortadan kaldırır.

## Kurulum

```bash
pip install clawmetry     # ardından: clawmetry
```

Ya da tek satırlık kurulum: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

macOS, Linux veya Windows üzerinde Python 3.8+ ve aynı makinede en az bir ajan
çalışma zamanı gerekir. Docker talimatları: [docs/DOCKER.md](docs/DOCKER.md).

Ya da kurulumu sizin için ajana yaptırın. [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
becerisi, Claude Code, Codex, Cursor, Gemini CLI, Copilot veya OpenCode'a
ClawMetry'yi kurmayı, makinedeki ajanların ne yaptığını ve ne harcadığını
raporlamayı, istek üzerine bir oturumu durdurmayı ve riskli araç çağrılarını
onay için bekletmeyi öğretir:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Dokümanlar

| | |
|---|---|
| [Çalışma zamanı uyumluluğu](docs/compatibility.md) | Her adaptörün okuduğu şeyler ve bir çalışma zamanının nasıl eklenir |
| [Bağlam taşması](docs/CONTEXT_BLOWOUT.md) | Sağlayıcı bazında pencereler, sıkıştırma ile taşma karşılaştırması, çalışma zamanı bazında kapsam |
| [Yük (Overhead)](docs/OVERHEAD.md) | Enstrümantasyonun maliyeti, ölçülmüş, yeniden üretmek için kabukla birlikte |
| [Yetkilendirmeler (Entitlements)](docs/ENTITLEMENTS.md) | Ücretsiz ve ücretli, katman matrisi, lisans CLI'si |
| [Onaylar ve politikalar](docs/APPROVALS.md) | Yürütme öncesi geçit, risk puanlama, telefon onayları |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | İzleri (trace) herhangi bir yere dışa aktarın, herhangi bir yerden OTLP alın |
| [Kendi ajanınızı getirin](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, uçtan uca LangChain, çalıştırılabilir örneklerle |
| [SDK izleme](docs/SDK_TRACKING.md) | Kendi oluşturduğunuz ajanlar için maliyet ilişkilendirmesi |
| [Sohbet kanalları](docs/CHANNELS.md) | Flow'da gösterilen sohbet adaptörleri |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | Sanal alan (sandboxed) NVIDIA NemoClaw kurulumları |
| [Docker](docs/DOCKER.md) | İmaj, compose, birim (volume) bağlantıları |
| [Mimari](ARCHITECTURE.md) · [Geliştirme](docs/DEVELOPMENT.md) | İçeride nasıl çalıştığı; kaynaktan çalıştırma |
| [Telemetri](docs/TELEMETRY.md) | Anonim kurulum ve masaüstü-açma pingleri ve bunların nasıl kapatılacağı |

## Ekran görüntüleri

Aşağıdaki her rakam, hiçbir şey tohumlanmadan, salt okunur şekilde, gerçek bir
makineden alınmıştır.

**Sadece ne olduğunu değil, bir şeyin yanlış gittiğini de söyler.**
Üstte iki anomali banner'ı: harcama günlük ortalamanın 7 katı ve 4,2 kat bir
maliyet sıçraması. Altında, son 667 oturumdan 324'ü bir israf sinyali
taşıyor, nedene göre ayrıştırılmış.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**Paranın nereye gittiğini, her pencerede gösterir.**
Bugün $252,47, bu hafta $513,15, bu ay $1.312,92; her biri arkasındaki
tokenlarla ve abonmanınızın zaten ne kadarını karşıladığıyla birlikte.
Altında, geri kazanılabilir olarak ayrıştırılmış yaklaşık $1.128/ay ve
önbellek yeniden kullanımıyla zaten tasarruf edilen $17.256/ay.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**Bir mesajın nasıl bir cevaba dönüştüğünü çizer.**
Canlı akış diyagramı: siz, mesajın geldiği kanal, gateway, şu anda cevap
veren model ve başvurduğu her araç. Düğümler, iş içlerinden geçtikçe
yanıp söner.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**Makinedeki her ajan, tek bir tabloda.**
Ne çalıştırdığı, son 24 saatte ve ömrü boyunca neye mal olduğu, en son ne
zaman görüldüğü, kime ait olduğu ve bir abonmanın faturayı karşılayıp
karşılamadığı. Burada 14 ajan, 3 oturum çalışıyor, 13'ü sessiz.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**Bir turun zamanının ve parasının nereye gittiğini, araç araç gösterir.**
Gerçek bir oturumun bir turu: 11,2 dakikada 11 araç, $1,16 karşılığında.
Her Bash çağrısı ve model çağrısı zaman çizelgesinde kendi çubuğunu alır,
böylece 4,1 dakika süren komutla 226 ms süren komut bir bakışta ayırt
edilebilir.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**Sadece harcamayı değil, işi de notlandırır.**
Bu hafta bir A notu: 54 görev sorunsuz döndü, 2 pürüzlü görev $48,57'ye mal
oldu ve yargılamak için çok az etkinliği olan koşular, kazanç olarak
sayılmak yerine notun dışında bırakıldı. Her pürüzlü koşu kendi izine (trace)
bağlanır.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**Bağlam penceresinin neden sürekli dolduğunu gösterir.**
Son turda 1M token'lık pencerenin 715K'sı, %83,3 zirve, hepsi bir taşma
üzerine değil proaktif olarak tetiklenen 4 sıkıştırma ve arkasındaki her
turun kullanım oranı.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**Tespit, siz hiçbir şey yapılandırmadan çalışır.**
Yerleşik dedektörler kurulumdan itibaren açıktır: ajan sessizleşti, telemetri
akışı durdu, maliyet sıçraması, token patlaması, artan hatalar, hata
sıçraması, bütçe eşiği, tehdit imzası eşleşmesi, güvenlik aracı bulgusu,
değişen güvenlik duruşu. Kendi kurallarınız üstüne isteğe bağlı olarak
eklenebilir.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**Riskli bir çağrıyı bekletmek isteğe bağlıdır ve kapalı olarak gönderilir.**
Özyinelemeli silmeler, zorla push'lar, sudo, sırlar, paket kurulumları ve
giden çağrıların her biri açabileceğiniz bir kurala sahiptir. Siz açana
kadar ClawMetry izler ve hiçbir şeyi değiştirmez. Biri açıldığında,
eşleşen çağrılar burada (veya telefonunuzda) bir onay veya red için bekler.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

Daha fazlası, çalışma zamanı bazında: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## Tanınma

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Yıldız Geçmişi

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## Lisans

MIT · [@vivekchand](https://github.com/vivekchand) tarafından geliştirildi · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
