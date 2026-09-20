<!-- i18n-src:b22579578775 -->
> Bahasa Indonesia translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**Sebuah agent bisa melakukan ratusan panggilan tool tanpa membuat kemajuan apa pun.** ClawMetry
membaca file sesi yang sudah ditulis oleh coding agent Anda, lalu menyatukan linimasa,
panggilan tool, serta data token dan biaya apa pun yang diekspos oleh runtime ke dalam satu
tampilan — sehingga Anda bisa membedakan proses panjang yang sedang berjalan baik dari yang sedang macet.

Bekerja dengan **32 AI agent runtime** — Claude Code, OpenAI Codex, Hermes, OpenClaw & 28 lainnya. Satu dashboard untuk seluruh armada agent Anda. ([daftar lengkap](SUPPORTED_RUNTIMES.txt), dihasilkan dari katalog.)

> 🌐 **Baca ini dalam:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [lainnya →](docs/i18n/)

Satu perintah. Tanpa konfigurasi. Mendeteksi semuanya secara otomatis.

```bash
pip install clawmetry && clawmetry
```

Terbuka di **http://localhost:8900**. Tanpa konfigurasi: aplikasi ini menemukan agent runtime
yang sudah Anda miliki, membacanya secara read-only, dan tidak mengubah apa pun tentang cara kerjanya.

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## Sebelum Anda menginstal

| | |
|---|---|
| **Apa yang dilakukannya** | Membaca file sesi dan log yang sudah ditulis oleh agent Anda. Tidak ada SDK, tidak ada perubahan kode, tidak ada instrumentasi di aplikasi Anda. |
| **Apa yang Anda lihat** | Linimasa sesi, replay tool demi tool, rincian token dan biaya, serta sinyal trajektori (looping, kegagalan berulang) — per runtime. |
| **Apa yang gratis** | `pip install clawmetry` membaca **OpenClaw, NVIDIA NemoClaw, Goose dan Qwen Code** tanpa akun, tanpa kunci, dan tanpa panggilan jaringan. 28 lainnya — Claude Code, Codex, Cursor dan sisanya — dibaca oleh pendamping closed-source `clawmetry-pro`, yang tersedia melalui uji coba 7 hari atau paket berbayar — lihat [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) untuk rincian pastinya. |
| **Cara memulai** | `pip install clawmetry && clawmetry`, lalu buka localhost:8900. Belum ada agent di mesin ini? `clawmetry --sample` akan terbuka dengan tiga sesi sintetis berlabel. |
| **Apa yang keluar dari mesin Anda** | Tidak ada data sesi, kecuali Anda menjalankan `clawmetry connect`. Dua hal berjalan secara default, keduanya opt-out dan tidak membawa konten sesi: ping instalasi anonim dan pemeriksaan versi PyPI. Setiap tujuan didaftarkan di [docs/EGRESS.md](docs/EGRESS.md), dibangun ulang dari tangkapan lalu lintas jaringan, bukan dari membaca komentar. |

Dua batasan yang perlu diketahui sebelum Anda menilai hasilnya: runtime mengekspos data yang
sangat berbeda-beda (beberapa tidak mempublikasikan biaya sama sekali — [matriksnya](docs/compatibility.md)
menunjukkan yang mana, per runtime), dan mengamati sebuah tindakan tidak sama dengan mampu
memblokirnya ([kontrol mana yang nyata, per runtime](docs/APPROVALS.md)).


## Bekerja dengan 32 agent runtime

**Gratis di aplikasi open source:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**Pada paket berbayar:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

Setiap runtime mendapat dashboard yang sama. Jalankan beberapa sekaligus dan pengalih header
akan menata ulang setiap tab ke salah satu di antaranya.

Membangun agent Anda sendiri di atas sebuah SDK? Interceptor juga melacak panggilan LLM-nya.
Lihat [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md).

## Apa yang Anda dapatkan

- **Sesi & transkrip**: apa yang dilakukan setiap agent, giliran demi giliran, dengan replay
- **Biaya & token**: per runtime, model, sesi dan hari, dengan penanda anomali
- **Flow**: diagram langsung pesan yang bergerak melalui channel, model dan tool
- **Brain**: aliran peristiwa penalaran dan panggilan tool saat terjadi
- **Context blowout**: pemanfaatan window yang diukur per provider, compaction vs overflow paksa, plus peta per runtime tentang apa yang *tidak bisa* kita lihat ([caranya](docs/CONTEXT_BLOWOUT.md))
- **Memory & skills**: file dan skill yang benar-benar dimuat oleh setiap runtime
- **Health & logs**: disk, memori, tingkat error, rate limit, aliran log langsung
- **Alerts**: batas anggaran, lonjakan error, agent-offline, dirutekan ke Slack, Discord, PagerDuty, Telegram, Email
- **Approvals**: menjeda panggilan tool yang berisiko *sebelum* dijalankan dan menyetujuinya dari ponsel Anda ([caranya](docs/APPROVALS.md))

## Context blowout, dan biaya pengamatannya

Dua pertanyaan yang layak dijawab sebelum Anda mempercayai alat pembanding agent apa pun.

**Bagaimana ia menangani context-window blowout di berbagai runtime?**

Persentase pemanfaatan hanya sejujur apa yang menjadi pembaginya. ClawMetry
mengukur window per provider dari [tabel yang bisa Anda baca dan
PR](clawmetry/context_windows.py), mencakup Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama dan GLM. Ia tidak mengukur ke-32
runtime dengan penggaris satu vendor saja. Itu penting: giliran GPT-5 300K yang
dinilai terhadap 200K milik Anthropic terbaca ">100%, blown" padahal sebenarnya
berada di 75% dari 400K milik GPT-5. Penggaris yang sama menyembunyikan
giliran DeepSeek 130K yang benar-benar overflow sebagai 65% yang nyaman.

Setiap window dikirim dengan asal-usulnya: `model_table`, `explicit_marker`,
`observed_floor`, atau `default` yang jujur saat kita tidak tahu modelnya. Gauge
yang dibangun dari tebakan tidak pernah dirender dengan otoritas yang sama
seperti yang dibangun dari lookup.

ClawMetry hanya bisa melihat peristiwa compaction pada beberapa runtime. Jadi
`GET /api/context-coverage` melaporkan, per runtime, apakah **nol berarti
"berjalan bersih" atau "kami buta"**. Sebuah `0` yang sebenarnya berarti buta
akan mengatakannya. [Detail lengkap](docs/CONTEXT_BLOWOUT.md)

**Berapa biaya instrumentasinya?**

| Jalur | Ditambahkan ke agent Anda | Default? |
|---|---|---|
| Session-file tailing (semua 32 runtime) | **0**. Proses terpisah, tanpa kode ClawMetry di agent Anda | aktif |
| HTTP interceptor (`CLAWMETRY_INTERCEPT=1`) | **+0.44 ms** per panggilan LLM, atau 0.009% dari panggilan 5 detik | nonaktif |
| Pre-tool hook gate (warm cache) | **+44 ms** per panggilan tool yang di-gate, di atas floor interpreter 36 ms | nonaktif |
| Enforcement proxy | **+9.7 ms** per panggilan LLM | nonaktif |

Biaya host daemon: **2.762 event/detik** ingest, **710 byte/event** di disk
(67.7 MB per 100 ribu event), dan **~12% dari satu core** berkelanjutan pada
instalasi yang sibuk. Angka terakhir itu melebihi anggaran 5-10% yang kami
tetapkan sendiri, jadi dipublikasikan sebagai bug yang perlu dikejar, bukan
disembunyikan dari halaman ini.

Diukur pada Apple M2 Pro dengan `benchmarks/overhead.py`. Harness ini menjalankan
setiap kondisi dalam proses terpisah, mengganti-ganti urutannya, dan **menolak
mencetak angka ketika putaran-putaran tersebut tidak sepakat soal tandanya**.
Jalankan di mesin Anda sendiri dalam waktu semenit:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

Setiap jalur diukur, termasuk hook gate dan enforcement proxy, dan harness ini
berjalan di Linux, macOS dan Windows dalam CI. Dua hasil yang perlu diketahui:
proxy berbiaya sekitar tujuh kali lebih mahal di Windows dibanding Linux, dan
daemon saat ini bertahan pada sekitar 12% dari satu core, melebihi anggaran
5-10% kami sendiri. JSON mentah, metodenya, dan apa yang belum diukur ada di
[docs/OVERHEAD.md](docs/OVERHEAD.md).

## Harga

| Paket | Cakupan | Harga |
|---|---|---|
| **Free** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, dashboard lengkap, hanya lokal | $0 |
| **Starter** | Semua runtime lain di atas, tampilan armada, sinkronisasi cloud | $9 per node / bulan |
| **Pro** | Starter + kontrol dan evaluasi: approval, kebijakan risiko tool, eval, deteksi anomali, cost optimizer, ekspor OTel, log audit tamper-evident | $19 per node / bulan |

Paket tahunan, Enterprise dan angka terkini ada di
**[clawmetry.com/pricing](https://clawmetry.com/pricing)**. Kunci lisensi self-hosted
berfungsi tanpa cloud (`clawmetry license`). Pembagian pasti gratis/berbayar ada
di [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md).

## Data Anda tetap di mesin Anda

ClawMetry membaca file sesi dan log lokal. **Tidak ada data sesi yang keluar dari
mesin Anda kecuali Anda menjalankan `clawmetry connect`** — tanpa prompt, balasan,
argumen tool, isi file atau baris log. Saat Anda memang terhubung, snapshot
dienkripsi end-to-end dengan kunci yang tidak pernah meninggalkan mesin Anda, dan
didekripsi di browser Anda. Jika sebuah node tidak punya kunci, unggahan dilewati
alih-alih dikirim dalam bentuk tidak terenkripsi, dan tidak ada respons server yang
bisa mematikan hal itu.

Dua hal berjalan secara default sebelum Anda terhubung, keduanya opt-out dan tidak
membawa data sesi: ping instalasi anonim dan pemeriksaan versi terhadap PyPI.
Instalasi default juga mencari IP publik Anda sekali untuk baris banner saat startup.
Setiap tujuan, apa yang dibawanya dan cara mematikannya terdaftar di
[docs/EGRESS.md](docs/EGRESS.md); instalasi self-hosted, yang dialihkan, dan yang
air-gapped tidak membuat panggilan keluar diskresioner sama sekali.

Dekripsi terjadi di browser Anda, dalam kode yang kami sajikan kepada Anda. Itu dulunya
sebuah janji; sekarang menjadi sesuatu yang bisa Anda periksa. Setiap baris yang
menyentuh kunci Anda berada dalam satu file yang bisa dibaca,
[`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js),
yang dikirim di dalam wheel dan disajikan apa adanya, dipatok dengan hash
Subresource Integrity. Untuk memastikan browser menjalankan apa yang kami publikasikan:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

Apa yang tidak dibuktikan oleh ini: kami menyajikan halaman yang memuat file
tersebut, jadi kami bisa saja menyajikan halaman yang berbeda. Hash integritas
melindungi Anda dari CDN yang disusupi, bukan dari vendor. Yang Anda peroleh
adalah bahwa penggantian apa pun harus disengaja, terlihat di sumber halaman,
dan berbeda dari artefak di PyPI yang bisa diambil siapa saja. Melakukan
self-hosting atau tetap lokal saja menghilangkan ketergantungan ini sepenuhnya.

## Instalasi

```bash
pip install clawmetry     # lalu: clawmetry
```

Atau one-liner-nya: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

Membutuhkan Python 3.8+ di macOS, Linux atau Windows, dan setidaknya satu
agent runtime pada mesin yang sama. Petunjuk Docker: [docs/DOCKER.md](docs/DOCKER.md).

Atau biarkan agent yang mengaturnya untuk Anda. Skill [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
mengajarkan Claude Code, Codex, Cursor, Gemini CLI, Copilot atau OpenCode untuk
menginstal ClawMetry, melaporkan apa yang sedang dilakukan dan dibelanjakan oleh
agent-agent di mesin tersebut, menghentikan satu sesi atas permintaan, dan menahan
panggilan tool yang berisiko untuk persetujuan:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## Dokumentasi

| | |
|---|---|
| [Kompatibilitas runtime](docs/compatibility.md) | Apa yang dibaca setiap adapter, dan cara menambahkan runtime |
| [Context blowout](docs/CONTEXT_BLOWOUT.md) | Window per provider, compaction vs overflow, cakupan per runtime |
| [Overhead](docs/OVERHEAD.md) | Biaya instrumentasi, terukur, dengan harness untuk mereproduksinya |
| [Entitlements](docs/ENTITLEMENTS.md) | Gratis vs berbayar, matriks tier, CLI lisensi |
| [Approvals & policies](docs/APPROVALS.md) | Gating pra-eksekusi, penilaian risiko, persetujuan lewat ponsel |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | Ekspor trace ke mana saja, ingest OTLP dari mana saja |
| [Bring your own agent](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain dari ujung ke ujung, dengan contoh yang bisa dijalankan |
| [SDK tracking](docs/SDK_TRACKING.md) | Atribusi biaya untuk agent yang Anda bangun sendiri |
| [Chat channels](docs/CHANNELS.md) | Adapter chat yang ditampilkan di Flow |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | Pengaturan NVIDIA NemoClaw yang disandbox |
| [Docker](docs/DOCKER.md) | Image, compose, volume mount |
| [Architecture](ARCHITECTURE.md) · [Development](docs/DEVELOPMENT.md) | Cara kerjanya di dalam; menjalankan dari source |
| [Telemetry](docs/TELEMETRY.md) | Ping instalasi anonim dan desktop-open, dan cara mematikannya |

## Tangkapan layar

Setiap angka di bawah ini berasal dari satu mesin nyata, read-only, tanpa apa pun yang disemai.

**Ia memberi tahu Anda saat ada yang salah, bukan hanya apa yang terjadi.**
Dua banner anomali di bagian atas: pengeluaran berjalan 7x rata-rata harian, dan
lonjakan biaya 4.2x. Di bawahnya, 324 dari 667 sesi terbaru membawa sinyal
pemborosan, dirinci berdasarkan penyebabnya.

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**Ia menunjukkan ke mana uang itu pergi, di setiap window.**
$252.47 hari ini, $513.15 minggu ini, $1,312.92 bulan ini, masing-masing dengan
token di baliknya dan seberapa banyak yang sudah dicakup langganan Anda. Di
bawahnya, sekitar $1,128/bulan dirinci sebagai bisa dipulihkan dan $17,256/bulan
sudah dihemat lewat penggunaan ulang cache.

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**Ia menggambarkan bagaimana sebuah pesan menjadi jawaban.**
Diagram flow langsung: Anda, channel tempat pesan itu tiba, gateway, model yang
sedang menjawab saat ini, dan setiap tool yang dijangkaunya. Node menyala saat
pekerjaan bergerak melaluinya.

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**Setiap agent di mesin, dalam satu tabel.**
Apa yang dijalankannya, berapa biayanya dalam 24 jam terakhir dan sepanjang
masa pakainya, kapan terakhir terlihat, siapa pemiliknya, dan apakah langganan
menanggung tagihannya. 14 agent di sini, 3 sesi sedang bekerja, 13 diam.

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**Ia menunjukkan ke mana waktu dan uang sebuah giliran pergi, tool demi tool.**
Satu giliran dari sesi nyata: 11 tool dalam 11.2 menit seharga $1.16. Setiap
panggilan Bash dan panggilan model mendapat batangnya sendiri di linimasa,
sehingga perintah yang berjalan 4.1 menit dan yang berjalan 226ms bisa
dibedakan sekilas.

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**Ia menilai hasil kerjanya, bukan sekadar pengeluarannya.**
Nilai A minggu ini: 54 tugas selesai dengan bersih, 2 yang bermasalah menghabiskan
$48.57, dan proses yang aktivitasnya terlalu sedikit untuk dinilai dikeluarkan
dari penilaian, bukan dihitung sebagai kemenangan. Setiap proses bermasalah
tertaut ke trace-nya.

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**Ia menunjukkan mengapa context window terus terisi penuh.**
715K dari window 1M token pada giliran terbaru, puncak 83.3%, 4 compaction
yang semuanya terjadi secara proaktif alih-alih akibat overflow, dan
pemanfaatan setiap giliran di baliknya.

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**Deteksi berjalan tanpa Anda perlu mengonfigurasi apa pun.**
Detektor bawaan aktif sejak instalasi: agent diam, feed telemetri berhenti,
lonjakan biaya, lonjakan token, error meningkat, lonjakan error, ambang
anggaran, signature ancaman cocok, temuan tool keamanan, postur keamanan
berubah. Aturan Anda sendiri bersifat opsional sebagai tambahan.

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**Menahan panggilan berisiko bersifat opt-in, dan dikirim dalam kondisi nonaktif.**
Recursive delete, force push, sudo, secrets, instalasi paket dan panggilan
keluar masing-masing mendapat aturan yang bisa Anda aktifkan. Sampai Anda
melakukannya, ClawMetry hanya mengamati dan tidak mengubah apa pun. Setelah
salah satu diaktifkan, panggilan yang cocok akan menunggu di sini (atau di
ponsel Anda) untuk disetujui atau ditolak.

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

Lebih lanjut, per runtime: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md).

## Pengakuan

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## Riwayat Star

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## Lisensi

MIT · Dibuat oleh [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
