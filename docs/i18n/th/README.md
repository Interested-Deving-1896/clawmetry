<!-- i18n-src:b22579578775 -->
> ไทย translation of [README](../../../README.md), auto-generated from the English source. English is canonical; open a PR against `README.md` for content changes.

# ClawMetry

[![PyPI version](https://img.shields.io/pypi/v/clawmetry?color=E5443A&label=version)](https://pypi.org/project/clawmetry/)
[![PyPI Downloads](https://static.pepy.tech/badge/clawmetry)](https://clickpy.clickhouse.com/dashboard/clawmetry)
[![GitHub stars](https://img.shields.io/github/stars/vivekchand/clawmetry?style=flat&color=E5443A)](https://github.com/vivekchand/clawmetry/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/vivekchand/clawmetry/badge)](https://scorecard.dev/viewer/?uri=github.com/vivekchand/clawmetry)
[![Security policy](https://img.shields.io/badge/security-policy-informational)](SECURITY.md)
[![Egress: documented](https://img.shields.io/badge/egress-documented-informational)](docs/EGRESS.md)

**เอเจนต์สามารถเรียกใช้เครื่องมือได้นับร้อยครั้งโดยไม่มีความคืบหน้า** ClawMetry
อ่านไฟล์เซสชันที่เอเจนต์โค้ดของคุณเขียนอยู่แล้ว และนำไทม์ไลน์
การเรียกใช้เครื่องมือ และข้อมูลโทเคนกับต้นทุนเท่าที่รันไทม์เปิดเผยมารวมไว้ในมุมมองเดียว
เพื่อให้คุณแยกแยะได้ว่าการรันที่ยาวนานนั้นกำลังทำงานได้ผลหรือติดขัดอยู่

ใช้งานได้กับ **รันไทม์เอเจนต์ AI 32 ตัว** — Claude Code, OpenAI Codex, Hermes, OpenClaw และอีก 28 ตัว แดชบอร์ดเดียวสำหรับกองเอเจนต์ทั้งหมดของคุณ ([ดูรายการทั้งหมด](SUPPORTED_RUNTIMES.txt) ซึ่งสร้างขึ้นจากแคตตาล็อก)

> 🌐 **อ่านภาษานี้:** [English](README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [Español](docs/i18n/es/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [العربية](docs/i18n/ar/README.md) · [Русский](docs/i18n/ru/README.md) · [เพิ่มเติม →](docs/i18n/)

คำสั่งเดียว ไม่ต้องตั้งค่า ตรวจจับทุกอย่างโดยอัตโนมัติ

```bash
pip install clawmetry && clawmetry
```

เปิดที่ **http://localhost:8900** ไม่ต้องตั้งค่าใดๆ: มันจะค้นหารันไทม์เอเจนต์
ที่คุณมีอยู่แล้ว อ่านแบบอ่านอย่างเดียว และไม่เปลี่ยนแปลงวิธีการทำงานของมันเลย

![ClawMetry dashboard: every AI agent runtime on one machine with 24h and lifetime cost per agent](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/hero.png)

## ก่อนที่คุณจะติดตั้ง

| | |
|---|---|
| **มันทำอะไร** | อ่านไฟล์เซสชันและล็อกที่เอเจนต์ของคุณเขียนอยู่แล้ว ไม่มี SDK ไม่ต้องแก้โค้ด ไม่มีการฝังเครื่องมือวัดผลในแอปของคุณ |
| **สิ่งที่คุณจะเห็น** | ไทม์ไลน์เซสชัน การเล่นซ้ำทีละเครื่องมือ รายละเอียดโทเคนและต้นทุน และสัญญาณของการวนลูปหรือความล้มเหลวซ้ำๆ ต่อรันไทม์ |
| **สิ่งที่ใช้ฟรี** | `pip install clawmetry` อ่านข้อมูลจาก **OpenClaw, NVIDIA NemoClaw, Goose และ Qwen Code** โดยไม่ต้องมีบัญชี ไม่ต้องใช้คีย์ และไม่มีการเรียกเครือข่ายใดๆ ส่วนอีก 28 ตัว — Claude Code, Codex, Cursor และที่เหลือ — จะถูกอ่านโดยส่วนเสริม `clawmetry-pro` แบบปิดซอร์ส ซึ่งมาพร้อมกับช่วงทดลองใช้ 7 วันหรือแพลน — ดูรายละเอียดที่ [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md) |
| **วิธีเริ่มต้น** | `pip install clawmetry && clawmetry` จากนั้นเปิด localhost:8900 ยังไม่มีเอเจนต์บนเครื่องนี้ใช่ไหม? `clawmetry --sample` จะเปิดพร้อมเซสชันสังเคราะห์สามชุดที่มีป้ายกำกับไว้ |
| **สิ่งที่ออกจากเครื่องของคุณ** | ไม่มีข้อมูลเซสชันใดๆ เว้นแต่คุณจะรัน `clawmetry connect` มีสองอย่างที่ทำงานเป็นค่าเริ่มต้น ซึ่งทั้งคู่สามารถปิดได้และไม่มีเนื้อหาเซสชันติดไปด้วย: การ ping การติดตั้งแบบไม่ระบุตัวตน และการตรวจสอบเวอร์ชันบน PyPI ปลายทางทั้งหมดถูกรวบรวมไว้ใน [docs/EGRESS.md](docs/EGRESS.md) ซึ่งสร้างขึ้นจากการดักจับข้อมูลบนสายจริง ไม่ใช่จากการอ่านคอมเมนต์ในโค้ด |

มีข้อจำกัดสองข้อที่ควรรู้ก่อนตัดสินผลลัพธ์: รันไทม์แต่ละตัวเปิดเผยข้อมูล
ที่แตกต่างกันมาก (บางตัวไม่เปิดเผยต้นทุนเลย — [ตารางเปรียบเทียบ](docs/compatibility.md)
บอกว่าตัวไหนเป็นอย่างไร) และการสังเกตการกระทำก็ไม่เหมือนกับการสามารถ
บล็อกมันได้ ([การควบคุมใดที่ใช้งานได้จริง ต่อรันไทม์](docs/APPROVALS.md))


## ใช้งานได้กับรันไทม์เอเจนต์ 32 ตัว

**ฟรีในแอปโอเพนซอร์ส:** 🦞 **[OpenClaw](https://clawmetry.com/runtimes/openclaw)** · 🟩 **[NVIDIA NemoClaw](https://clawmetry.com/nemoclaw)** · 🪿 **[Goose](https://clawmetry.com/runtimes/goose)** · ◈ **[Qwen Code](https://clawmetry.com/runtimes/qwen-code)**

**บนแพลนแบบเสียเงิน:** ◆ **[Claude Code](https://clawmetry.com/runtimes/claude-code)** · **[Cursor](https://clawmetry.com/runtimes/cursor)** · 🐙 **[GitHub Copilot](https://clawmetry.com/runtimes/copilot)** · ⬡ **[OpenAI Codex](https://clawmetry.com/runtimes/codex)** · ♊ **[Gemini CLI](https://clawmetry.com/runtimes/gemini-cli)** · 💗 **[Lovable](https://clawmetry.com/runtimes/lovable)** · ⠕ **[Replit Agent](https://clawmetry.com/runtimes/replit)** · 🖇 **[Cline](https://clawmetry.com/runtimes/cline)** · 🙌 **[OpenHands](https://clawmetry.com/runtimes/openhands)** · 🧑‍💼 **[OpenWorker](https://clawmetry.com/runtimes/openworker)** · 🎭 **[Muse Code](https://clawmetry.com/runtimes/muse-code)** · 🏛️ **[OpenExecutive](https://clawmetry.com/runtimes/openexecutive)** · **[opencode](https://clawmetry.com/runtimes/opencode)** · **[Aider](https://clawmetry.com/runtimes/aider)** · 🔗 **[n8n](https://clawmetry.com/runtimes/n8n)** · 🅳 **[Devin](https://clawmetry.com/runtimes/devin)** · 🪐 **[Antigravity](https://clawmetry.com/runtimes/antigravity)** · **[Grok Build](https://clawmetry.com/runtimes/grok)** · 🤖 **[Grok Bot](https://clawmetry.com/runtimes/grok-bot)** · ⚡ **[Hermes](https://clawmetry.com/runtimes/hermes)** · **[Pi](https://clawmetry.com/runtimes/pi)** · **[Deep Agents](https://clawmetry.com/runtimes/deep-agents)** · 🌙 **[Kimi CLI](https://clawmetry.com/runtimes/kimi)** · 🐋 **[DeepSeek Harness](https://clawmetry.com/runtimes/deepseek-harness)** · 🦾 **[Exo](https://clawmetry.com/runtimes/exo)** · **[NanoClaw](https://clawmetry.com/runtimes/nanoclaw)** · **[PicoClaw](https://clawmetry.com/runtimes/picoclaw)** · **[QM](https://clawmetry.com/runtimes/qm)**

ทุกรันไทม์ได้แดชบอร์ดแบบเดียวกัน รันหลายตัวพร้อมกันได้
และตัวสลับที่ส่วนหัวจะปรับขอบเขตของทุกแท็บให้ตรงกับตัวที่เลือก

สร้างเอเจนต์ของคุณเองด้วย SDK แทนหรือเปล่า? ตัวสกัดกั้นก็ติดตามการเรียก LLM
ของมันได้เช่นกัน ดู [docs/SDK_TRACKING.md](docs/SDK_TRACKING.md)

## สิ่งที่คุณจะได้รับ

- **เซสชันและบทสนทนา**: สิ่งที่เอเจนต์แต่ละตัวทำ ทีละเทิร์น พร้อมการเล่นซ้ำ
- **ต้นทุนและโทเคน**: แยกตามรันไทม์ โมเดล เซสชัน และวัน พร้อมสัญญาณความผิดปกติ
- **โฟลว์**: แผนภาพสดของข้อความที่เคลื่อนผ่านช่องทาง โมเดล และเครื่องมือต่างๆ
- **สมอง (Brain)**: สตรีมเหตุการณ์การให้เหตุผลและการเรียกใช้เครื่องมือแบบเรียลไทม์
- **การล้นของบริบท**: การใช้พื้นที่หน้าต่างที่คำนวณตามผู้ให้บริการแต่ละราย เปรียบเทียบการอัดข้อมูล (compaction) กับการล้นแบบบังคับ พร้อมแผนที่ต่อรันไทม์ว่าเรา*มองไม่เห็น*อะไรบ้าง ([วิธีการ](docs/CONTEXT_BLOWOUT.md))
- **หน่วยความจำและทักษะ**: ไฟล์และทักษะที่แต่ละรันไทม์โหลดขึ้นมาใช้จริง
- **สุขภาพระบบและล็อก**: ดิสก์ หน่วยความจำ อัตราข้อผิดพลาด ขีดจำกัดอัตรา สตรีมล็อกสด
- **การแจ้งเตือน**: เพดานงบประมาณ ข้อผิดพลาดพุ่งสูง เอเจนต์ออฟไลน์ ส่งไปยัง Slack, Discord, PagerDuty, Telegram, อีเมล
- **การอนุมัติ**: หยุดการเรียกใช้เครื่องมือที่เสี่ยง*ก่อน*ที่มันจะทำงาน และอนุมัติได้จากโทรศัพท์ของคุณ ([วิธีการ](docs/APPROVALS.md))

## การล้นของบริบท และต้นทุนของการเฝ้าสังเกต

มีสองคำถามที่ควรตอบให้ได้ก่อนที่คุณจะเชื่อถือเครื่องมือเปรียบเทียบเอเจนต์ใดๆ

**มันจัดการกับการล้นของหน้าต่างบริบทข้ามรันไทม์อย่างไร?**

เปอร์เซ็นต์การใช้งานจะซื่อสัตย์ได้ก็ต่อเมื่อตัวหารของมันถูกต้อง ClawMetry
คำนวณขนาดหน้าต่างตามผู้ให้บริการแต่ละรายจาก [ตารางที่คุณอ่านและ
ส่ง PR ได้](clawmetry/context_windows.py) ครอบคลุม Anthropic, OpenAI, Google, xAI,
DeepSeek, Kimi, Qwen, Mistral, Llama และ GLM มันไม่ได้วัดรันไทม์ทั้ง 32 ตัว
ด้วยไม้บรรทัดของผู้ให้บริการรายเดียว นี่สำคัญ: เทิร์นของ GPT-5 ที่ 300K
เมื่อวัดเทียบกับ 200K ของ Anthropic จะอ่านได้ว่า ">100%, ล้นแล้ว" ทั้งที่จริงๆ
อยู่ที่ 75% ของ 400K ของ GPT-5 ไม้บรรทัดเดียวกันก็ซ่อนเทิร์นของ DeepSeek
ที่ล้นจริงที่ 130K ให้ดูเหมือนสบายๆ ที่ 65%

หน้าต่างทุกอันมาพร้อมที่มาของมัน: `model_table`, `explicit_marker`,
`observed_floor` หรือ `default` ที่ซื่อสัตย์เมื่อเราไม่รู้จักโมเดลนั้น
มาตรวัดที่สร้างจากการเดาจะไม่แสดงผลด้วยความน่าเชื่อถือเดียวกับที่สร้างจาก
การค้นหาข้อมูลจริง

ClawMetry มองเห็นเหตุการณ์การอัดข้อมูล (compaction) ได้เฉพาะในบางรันไทม์เท่านั้น
ดังนั้น `GET /api/context-coverage` จะรายงานต่อรันไทม์ว่า **เลขศูนย์หมายถึง
"รันได้สะอาด" หรือ "เรามองไม่เห็น"** ศูนย์ที่จริงๆ แล้วหมายถึงการมองไม่เห็นจะบอกไว้อย่างนั้น
[รายละเอียดทั้งหมด](docs/CONTEXT_BLOWOUT.md)

**เครื่องมือวัดผลนี้มีต้นทุนเท่าไร?**

| เส้นทาง | สิ่งที่เพิ่มเข้าไปในเอเจนต์ของคุณ | ค่าเริ่มต้น? |
|---|---|---|
| การ tail ไฟล์เซสชัน (ทั้ง 32 รันไทม์) | **0**. เป็นโปรเซสแยกต่างหาก ไม่มีโค้ด ClawMetry ในเอเจนต์ของคุณ | เปิด |
| ตัวสกัดกั้น HTTP (`CLAWMETRY_INTERCEPT=1`) | **+0.44 มิลลิวินาที** ต่อการเรียก LLM หนึ่งครั้ง หรือ 0.009% ของการเรียกที่ใช้เวลา 5 วินาที | ปิด |
| จุดตรวจก่อนเรียกเครื่องมือ (แคชอุ่นแล้ว) | **+44 มิลลิวินาที** ต่อการเรียกเครื่องมือที่ถูกตรวจสอบหนึ่งครั้ง เหนือพื้นฐานของตัวแปลภาษาที่ 36 มิลลิวินาที | ปิด |
| พร็อกซีการบังคับใช้ | **+9.7 มิลลิวินาที** ต่อการเรียก LLM หนึ่งครั้ง | ปิด |

ต้นทุนของโฮสต์ที่รันดีมอน: **2,762 เหตุการณ์/วินาที** ในการรับเข้า **710 ไบต์/เหตุการณ์**
บนดิสก์ (67.7 MB ต่อ 100,000 เหตุการณ์) และ **ประมาณ 12% ของหนึ่งคอร์** อย่างต่อเนื่อง
บนการติดตั้งที่มีการใช้งานสูง ตัวเลขสุดท้ายนั้นเกินงบประมาณ 5-10% ที่เราตั้งไว้เอง
ดังนั้นจึงเผยแพร่ไว้ในฐานะบั๊กที่ต้องไล่แก้ มากกว่าจะละไว้ไม่พูดถึง

วัดผลบน Apple M2 Pro ด้วย `benchmarks/overhead.py` ฮาร์เนสนี้รันแต่ละเงื่อนไข
ในโปรเซสแยกต่างหาก สลับลำดับของมัน และ **ปฏิเสธที่จะพิมพ์ตัวเลขออกมาเมื่อ
รอบต่างๆ ไม่เห็นตรงกันในเรื่องเครื่องหมาย (บวก/ลบ)** รันมันบนเครื่องของคุณเอง
ได้ภายในหนึ่งนาที:

```bash
pip install clawmetry && python -m benchmarks.overhead
```

ทุกเส้นทางถูกวัดผล รวมถึงจุดตรวจของเครื่องมือและพร็อกซีการบังคับใช้
และฮาร์เนสนี้รันบน Linux, macOS และ Windows ใน CI มีผลลัพธ์สองอย่างที่ควรรู้:
พร็อกซีมีต้นทุนสูงกว่าบน Windows ประมาณเจ็ดเท่าเมื่อเทียบกับ Linux และ
ดีมอนในปัจจุบันใช้งานอย่างต่อเนื่องประมาณ 12% ของหนึ่งคอร์ ซึ่งเกินงบประมาณ 5-10%
ที่เราตั้งไว้เอง ข้อมูล JSON ดิบ วิธีการ และสิ่งที่ยังไม่ได้วัดผลอยู่ใน
[docs/OVERHEAD.md](docs/OVERHEAD.md)

## ราคา

| แพลน | ครอบคลุมอะไรบ้าง | ราคา |
|---|---|---|
| **ฟรี** | OpenClaw + NVIDIA NemoClaw + Goose + Qwen Code, แดชบอร์ดเต็มรูปแบบ, เฉพาะในเครื่อง | $0 |
| **Starter** | รันไทม์ทุกตัวที่เหลือด้านบน, มุมมองกองเอเจนต์, การซิงค์กับคลาวด์ | $9 ต่อโหนด / เดือน |
| **Pro** | Starter + การควบคุมและการประเมิน: การอนุมัติ, นโยบายความเสี่ยงของเครื่องมือ, evals, การตรวจจับความผิดปกติ, ตัวปรับต้นทุนให้เหมาะสม, การส่งออก OTel, บันทึกตรวจสอบที่ป้องกันการปลอมแปลง | $19 ต่อโหนด / เดือน |

แพลนรายปี Enterprise และตัวเลขล่าสุดอยู่ที่
**[clawmetry.com/pricing](https://clawmetry.com/pricing)** คีย์ไลเซนส์แบบโฮสต์เอง
ใช้งานได้โดยไม่ต้องใช้คลาวด์ (`clawmetry license`) รายละเอียดการแบ่งฟรี/เสียเงินที่แน่ชัด
อยู่ใน [docs/ENTITLEMENTS.md](docs/ENTITLEMENTS.md)

## ข้อมูลของคุณอยู่บนเครื่องของคุณเสมอ

ClawMetry อ่านไฟล์เซสชันและล็อกในเครื่อง **ไม่มีข้อมูลเซสชันออกจากเครื่องของคุณ
เว้นแต่คุณจะรัน `clawmetry connect`** ไม่ว่าจะเป็นพรอมป์ คำตอบ อาร์กิวเมนต์ของเครื่องมือ
เนื้อหาไฟล์ หรือบรรทัดล็อก เมื่อคุณเชื่อมต่อ สแนปช็อตจะถูกเข้ารหัสแบบ end-to-end
ด้วยคีย์ที่ไม่เคยออกจากเครื่องของคุณ และถูกถอดรหัสในเบราว์เซอร์ของคุณ หากโหนด
ไม่มีคีย์ การอัปโหลดจะถูกข้ามไปแทนที่จะส่งแบบไม่เข้ารหัส และไม่มีการตอบสนองจาก
เซิร์ฟเวอร์ใดที่สามารถปิดการทำงานนี้ได้

มีสองอย่างที่ทำงานเป็นค่าเริ่มต้นก่อนที่คุณจะเชื่อมต่อ ซึ่งทั้งคู่สามารถปิดได้และ
ไม่มีข้อมูลเซสชันติดไปด้วย: การ ping การติดตั้งแบบไม่ระบุตัวตน และการตรวจสอบเวอร์ชัน
เทียบกับ PyPI การติดตั้งแบบค่าเริ่มต้นยังค้นหา IP สาธารณะของคุณหนึ่งครั้งสำหรับ
บรรทัดแบนเนอร์ตอนเริ่มต้น ปลายทางทั้งหมด สิ่งที่มันส่งไป และวิธีปิดมัน
มีรายการไว้ใน [docs/EGRESS.md](docs/EGRESS.md); การติดตั้งแบบโฮสต์เอง เปลี่ยนปลายทางใหม่
และแบบตัดขาดจากเครือข่าย จะไม่มีการเรียกออกไปภายนอกตามดุลยพินิจเลย

การถอดรหัสเกิดขึ้นในเบราว์เซอร์ของคุณ ด้วยโค้ดที่เราส่งให้คุณ เรื่องนี้เคยเป็น
เพียงคำมั่นสัญญา แต่ตอนนี้เป็นสิ่งที่คุณตรวจสอบได้ ทุกบรรทัดที่แตะต้องคีย์ของคุณ
อยู่ในไฟล์ที่อ่านได้ไฟล์เดียว [`clawmetry/static/js/cm-e2e.js`](clawmetry/static/js/cm-e2e.js)
ซึ่งบรรจุอยู่ในวีล (wheel) และถูกให้บริการตามตัวอักษร ปักหมุดด้วยแฮช Subresource
Integrity เพื่อยืนยันว่าเบราว์เซอร์รันสิ่งที่เราเผยแพร่จริง:

```bash
curl -s https://app.clawmetry.com/static/js/cm-e2e.js -o served.js
pip download --no-deps clawmetry==$(clawmetry --version | tr -d 'a-z ') -d /tmp/cm
unzip -p /tmp/cm/clawmetry-*.whl clawmetry/static/js/cm-e2e.js > published.js
diff served.js published.js && echo identical
```

สิ่งที่วิธีนี้พิสูจน์ไม่ได้: เราเป็นผู้ให้บริการหน้าเว็บที่โหลดไฟล์นี้ ดังนั้นเราจึงอาจ
ให้บริการหน้าเว็บที่แตกต่างออกไปได้ แฮชความสมบูรณ์ปกป้องคุณจาก CDN ที่ถูกบุกรุก
ไม่ใช่จากผู้ให้บริการเอง สิ่งที่คุณได้รับคือการแทนที่ใดๆ จะต้องเป็นการกระทำโดยเจตนา
มองเห็นได้ในซอร์สของหน้าเว็บ และแตกต่างจากอาร์ทิแฟกต์บน PyPI ที่ใครก็ดึงมาดูได้
การโฮสต์เองหรือใช้งานแบบเฉพาะในเครื่องจะขจัดการพึ่งพานี้ออกไปทั้งหมด

## การติดตั้ง

```bash
pip install clawmetry     # แล้วรัน: clawmetry
```

หรือแบบบรรทัดเดียว: `curl -sSL https://raw.githubusercontent.com/vivekchand/clawmetry/main/install.sh | bash`

ต้องการ Python 3.8 ขึ้นไปบน macOS, Linux หรือ Windows และมีรันไทม์เอเจนต์อย่างน้อยหนึ่งตัว
บนเครื่องเดียวกัน คำแนะนำสำหรับ Docker: [docs/DOCKER.md](docs/DOCKER.md)

หรือให้เอเจนต์ตั้งค่าให้คุณเลย ทักษะ [`agent-kill-switch`](skills/agent-kill-switch/SKILL.md)
สอนให้ Claude Code, Codex, Cursor, Gemini CLI, Copilot หรือ OpenCode
ติดตั้ง ClawMetry รายงานว่าเอเจนต์บนเครื่องกำลังทำอะไรและใช้จ่ายเท่าไร
หยุดเซสชันหนึ่งตามคำขอ และกักการเรียกใช้เครื่องมือที่เสี่ยงไว้รอการอนุมัติ:

```bash
npx skills add vivekchand/clawmetry --skill agent-kill-switch
```

## เอกสาร

| | |
|---|---|
| [ความเข้ากันได้ของรันไทม์](docs/compatibility.md) | สิ่งที่แต่ละตัวปรับใช้ (adapter) อ่านได้ และวิธีเพิ่มรันไทม์ใหม่ |
| [การล้นของบริบท](docs/CONTEXT_BLOWOUT.md) | หน้าต่างตามผู้ให้บริการแต่ละราย การอัดข้อมูลเทียบกับการล้น ความครอบคลุมต่อรันไทม์ |
| [ต้นทุนที่เพิ่มขึ้น](docs/OVERHEAD.md) | ต้นทุนของเครื่องมือวัดผล ที่วัดจริง พร้อมฮาร์เนสสำหรับทำซ้ำ |
| [สิทธิ์การใช้งาน](docs/ENTITLEMENTS.md) | ฟรีเทียบกับเสียเงิน ตารางระดับแพลน CLI สำหรับไลเซนส์ |
| [การอนุมัติและนโยบาย](docs/APPROVALS.md) | การตรวจสอบก่อนดำเนินการ การให้คะแนนความเสี่ยง การอนุมัติทางโทรศัพท์ |
| [OpenTelemetry](docs/OPENTELEMETRY.md) | ส่งออก trace ไปที่ไหนก็ได้ รับเข้า OTLP จากอะไรก็ได้ |
| [นำเอเจนต์ของคุณเองมาใช้](docs/BRING_YOUR_OWN_AGENT.md) | AWS AgentCore, Pydantic AI, LangChain แบบครบวงจร พร้อมตัวอย่างที่รันได้จริง |
| [การติดตามผ่าน SDK](docs/SDK_TRACKING.md) | การระบุต้นทุนสำหรับเอเจนต์ที่คุณสร้างขึ้นเอง |
| [ช่องทางแชท](docs/CHANNELS.md) | ตัวปรับใช้ (adapter) แชทที่แสดงในโฟลว์ |
| [NemoClaw / OpenShell](docs/NEMOCLAW.md) | การตั้งค่า NVIDIA NemoClaw แบบแซนด์บ็อกซ์ |
| [Docker](docs/DOCKER.md) | อิมเมจ, compose, การมาวนต์วอลุ่ม |
| [สถาปัตยกรรม](ARCHITECTURE.md) · [การพัฒนา](docs/DEVELOPMENT.md) | วิธีการทำงานภายใน; การรันจากซอร์สโค้ด |
| [การวัดผลระยะไกล (Telemetry)](docs/TELEMETRY.md) | การ ping การติดตั้งและการเปิดแอปเดสก์ท็อปแบบไม่ระบุตัวตน และวิธีปิดมัน |

## ภาพหน้าจอ

ทุกตัวเลขด้านล่างมาจากเครื่องจริงหนึ่งเครื่อง อ่านอย่างเดียว โดยไม่มีการปลูกข้อมูลใดๆ

**มันบอกคุณเมื่อมีบางอย่างผิดปกติ ไม่ใช่แค่บอกว่าเกิดอะไรขึ้น**
แบนเนอร์ความผิดปกติสองอันที่ด้านบน: การใช้จ่ายที่วิ่งสูงกว่าค่าเฉลี่ยรายวันถึง 7 เท่า
และการพุ่งขึ้นของต้นทุน 4.2 เท่า ด้านล่างนั้น 324 จาก 667 เซสชันล่าสุดมีสัญญาณ
ของการสูญเปล่า แจกแจงตามสาเหตุ

![Overview: spending anomaly and cost spike banners over live agent work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/overview.png)

**มันแสดงให้คุณเห็นว่าเงินไปไหนบ้าง ในทุกช่วงเวลา**
$252.47 วันนี้ $513.15 สัปดาห์นี้ $1,312.92 เดือนนี้ พร้อมโทเคนเบื้องหลังตัวเลขนั้น
และการสมัครสมาชิกของคุณครอบคลุมไปแล้วเท่าไร ด้านล่างนั้น ประมาณ $1,128/เดือน
ที่แจกแจงว่าสามารถประหยัดคืนได้ และ $17,256/เดือนที่ประหยัดไปแล้วจากการใช้แคชซ้ำ

![Cost: today, this week and this month, with an efficiency grade and itemised savings ideas](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/cost.png)

**มันวาดให้เห็นว่าข้อความหนึ่งกลายเป็นคำตอบได้อย่างไร**
แผนภาพโฟลว์แบบสด: คุณ ช่องทางที่ข้อความเข้ามา เกตเวย์ โมเดลที่กำลังตอบอยู่ตอนนี้
และเครื่องมือทุกตัวที่มันเรียกใช้ โหนดต่างๆ จะสว่างขึ้นเมื่องานเคลื่อนผ่าน

![Flow: live diagram from you through the gateway to the model and its tools](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/flow.png)

**เอเจนต์ทุกตัวบนเครื่อง อยู่ในตารางเดียว**
มันรันอะไรอยู่ ต้นทุนของมันใน 24 ชั่วโมงที่ผ่านมาและตลอดอายุการใช้งาน
เห็นครั้งล่าสุดเมื่อไร ใครเป็นเจ้าของ และมีการสมัครสมาชิกครอบคลุมบิลอยู่หรือไม่
มีเอเจนต์ 14 ตัวที่นี่ 3 เซสชันกำลังทำงาน 13 ตัวว่างเงียบ

![Agents: every runtime on the machine with cost, owner, last seen and current work](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/agents.png)

**มันแสดงให้เห็นว่าเวลาและเงินของแต่ละเทิร์นไปไหนบ้าง ทีละเครื่องมือ**
หนึ่งเทิร์นของเซสชันจริง: เครื่องมือ 11 ตัวใน 11.2 นาที คิดเป็น $1.16
การเรียก Bash และการเรียกโมเดลทุกครั้งจะมีแท่งของตัวเองบนไทม์ไลน์
ทำให้คำสั่งที่รันไป 4.1 นาทีกับคำสั่งที่รันไป 226 มิลลิวินาที แยกออกจากกันได้ในพริบตา

![Sessions: one agent turn on a timeline, every tool call with its own duration and the turn's cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/sessions.png)

**มันให้คะแนนคุณภาพของงาน ไม่ใช่แค่การใช้จ่าย**
เกรด A ในสัปดาห์นี้: 54 งานจบแบบเรียบร้อย 2 งานที่ขรุขระมีต้นทุน $48.57
และการรันที่มีกิจกรรมน้อยเกินกว่าจะตัดสินได้ ถูกไม่นับรวมในการให้เกรด
แทนที่จะถูกนับเป็นความสำเร็จ แต่ละงานที่ขรุขระเชื่อมโยงไปยัง trace ของมัน

![Quality: this week's report card with the rough runs and what they cost](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/quality.png)

**มันแสดงให้เห็นว่าทำไมหน้าต่างบริบทถึงเต็มอยู่เรื่อยๆ**
715K จากหน้าต่าง 1M โทเคนในเทิร์นล่าสุด จุดสูงสุด 83.3% การอัดข้อมูล 4 ครั้ง
ที่ทั้งหมดเกิดขึ้นแบบเชิงรุกมากกว่าจากการล้น พร้อมอัตราการใช้งานของทุกเทิร์นที่ผ่านมา

![Context usage: window utilisation per turn, compaction events and tokens reclaimed](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/context.png)

**การตรวจจับทำงานโดยที่คุณไม่ต้องตั้งค่าอะไรเลย**
ตัวตรวจจับในตัวจะทำงานตั้งแต่ติดตั้ง: เอเจนต์เงียบไป ฟีดเทเลเมทรีหยุดทำงาน
ต้นทุนพุ่งสูง โทเคนพุ่งสูง ข้อผิดพลาดเพิ่มขึ้น ข้อผิดพลาดพุ่งสูง เกินเพดานงบประมาณ
พบลายเซ็นภัยคุกคาม พบผลตรวจจากเครื่องมือความปลอดภัย ท่าทีความปลอดภัยเปลี่ยนไป
กฎของคุณเองเป็นทางเลือกเสริมเพิ่มเติม

![Alerts: built-in detectors plus optional custom rules](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/alerts.png)

**การกักการเรียกที่มีความเสี่ยงเป็นทางเลือกที่เลือกเปิดเอง และถูกปิดไว้เมื่อส่งมอบ**
การลบแบบเรียกซ้ำ (recursive delete), force push, sudo, ความลับ (secrets)
การติดตั้งแพ็กเกจ และการเรียกออกไปภายนอก แต่ละอย่างมีกฎที่คุณเปิดใช้ได้
จนกว่าคุณจะเปิด ClawMetry จะเฝ้าดูโดยไม่เปลี่ยนแปลงอะไร เมื่อเปิดข้อใดข้อหนึ่งแล้ว
การเรียกที่ตรงเงื่อนไขจะรอที่นี่ (หรือบนโทรศัพท์ของคุณ) เพื่อขออนุมัติหรือปฏิเสธ

![Approvals: protection rules for risky tool calls, all off until you enable them](https://raw.githubusercontent.com/vivekchand/clawmetry/main/screenshots/approvals.png)

เพิ่มเติม แยกตามรันไทม์: [docs/RUNTIME_SCREENSHOTS.md](docs/RUNTIME_SCREENSHOTS.md)

## การยกย่อง

<a href="https://www.producthunt.com/products/clawmetry?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-clawmetry-for-openclaw" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1081207&theme=light&period=daily&t=1771491508782" alt="ClawMetry - #5 Product of the Day on Product Hunt" width="250" height="54" /></a>


## ประวัติดาว

<a href="https://www.star-history.com/?repos=vivekchand%2Fclawmetry&type=date&legend=top-left">
 <picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&theme=dark&legend=top-left" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 <img alt="Star History Chart" src="https://api.star-history.com/image?repos=vivekchand/clawmetry&type=date&legend=top-left" />
 </picture>
</a>

## สัญญาอนุญาต

MIT · สร้างโดย [@vivekchand](https://github.com/vivekchand) · [clawmetry.com](https://clawmetry.com)

<!-- osai-verify: f3ac716d40002c1ad6dd -->
