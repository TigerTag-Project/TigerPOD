# TigerPOD

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](LICENSE)

**A CD player, for spools.**

The TigerPOD is an open-source desktop **NFC / RFID reader and writer (burner) for
3D-printing filament spools**, built from two commodity USB readers and a 3D-printed
shell. Drop a filament spool in and your computer reads its TigerTag chip — material,
brand, colour, temperatures, what's left. Write (encode) a tag the same way: put the
spool in, done. No aiming, no hunting for the sticker.

![The TigerPOD, printed in every colour, each cradling a filament spool](assets/pods/TigerPOD-rainbow-9.jpg)

![The TigerPOD reading a spool in Tiger Studio](assets/TigerPOD-demo.gif)

<sub>▶ Higher-quality clip: [TigerPOD-demo.mp4](assets/TigerPOD-demo.mp4)</sub>

> **Fits ~99% of 1 kg spools**, whatever the type — plastic masterspools, cardboard
> spools, and non-reusable plastic or refill spools all drop right in.

**Contents:** [A first of its kind](#a-first-of-its-kind) ·
[Why it exists](#why-it-exists) ·
[Free electronics, free design](#free-electronics-free-design) ·
[A universal NFC station](#more-than-tigertag--a-universal-nfc-station) ·
[Ecosystem comparison](#how-the-filament-rfid-ecosystems-compare) ·
[Build one](#build-one) · [Or buy the kit](#or-buy-the-kit) ·
[The ecosystem](#the-ecosystem-around-it) ·
[Read a tag in your own code](#read-a-tag-in-your-own-code) · [FAQ](#faq) ·
[Contributing](#contributing) · [Licence](#licence)

## A first of its kind

As far as we know, **the TigerPOD is the first spool-scale NFC/RFID reader/burner of its
kind** — nobody had done this before. It was imagined by **Benoit Michaut**, a French
maker who has been passionate about 3D printing since 2015, in **2023, alongside the
creation of the open-source TigerTag protocol**: take **two standard, low-cost USB NFC
readers**,
drop one on each side of a 3D-printed spool holder, and you get a device that reads *and*
writes (burns) both chips of a filament spool at once. No custom PCB, no proprietary
reader, no dedicated silicon.

That turns encoding a spool's NFC chips — normally an industrial, closed process — into
something anyone can build on their desk for the price of two commodity readers. The goal
isn't the gadget, it's **democratising RFID for filament** through the open
[**TigerTag**](https://github.com/TigerTag-Project/TigerTag-RFID-Guide) protocol so any
maker, brand, or printer can adopt it freely.

### From the factory to the kitchen table

This is the part that matters. The TigerPOD is the **first consumer-grade device for
material identification in 3D printing** — it took a capability that belonged to industry
and put it on a desk.

|  | Before the TigerPOD | After the TigerPOD |
|---|---|---|
| **Who could encode material chips** | Large manufacturers only | Anyone, at home |
| **What it took** | Industrial encoders, proprietary hardware, closed tooling, vendor contracts | Two commodity USB readers and a 3D print |
| **Skills required** | Specialist | None — no electronics, no soldering |
| **Cost** | Capital expenditure | The price of two cheap readers |

Today, at home and for very little money, **anyone can read a chip, write a new one, change
what's already on it, and wipe it clean again.** Before this, that technology was reserved
for big industry. That shift, not the plastic shell, is what the TigerPOD really is.

And it works **for filament, in Dual NFC** — both chips of a spool at once — on **standard
spools of any brand**, with **any chip technology the ACR122U supports** (MIFARE, NTAG and
others). Not one vendor's ecosystem: all of them.

<sub>*(Developers: that's full **CRUD** — create, read, update, delete — on an NFC tag.)*</sub>

New to RFID for filament? Start with the
[**TigerTag RFID Guide**](https://github.com/TigerTag-Project/TigerTag-RFID-Guide) — the
open spec and public registry behind the Pod.

## Why it exists

The Pod was first imagined for **mass programming at third-party filament factories**. The
brief was demanding: a way to encode spools that is **cheap, easy to build locally, and
duplicable in large quantities at the lowest possible cost**, without giving up any
capability. With commodity readers and a printed shell, the **development cost is
essentially zero** — a Pod can be produced anywhere in the world, locally, in quantity.

The ACR122U is deliberate: it's an extremely common reader, **easy to find anywhere for
very little money**. And there's nothing to learn — **no electronics knowledge, no
soldering, no difficulty**. Print the shell, slide in two readers: a five-year-old could
assemble a TigerPOD.

From that factory-floor origin, we then **brought the Pod to everyone** with the launch of
the [**Tiger Studio Manager**](https://github.com/TigerTag-Project/TigerTag-Studio-Manager)
desktop app — the same encoding power on any maker's desk, not just a production line.

This is the founding premise of an open-source project that is **neutral and agnostic —
tied to no printer maker and no filament brand**. The point is to put maximum value in
everyone's hands and offer a genuinely low-cost path for users **everywhere on the
planet**.

That's also why it works with **every NTAG — down to the small NTAG 213**: we optimised
every byte of the chip to pack the most data into the least space. And because a TigerTag
chip is a standard NFC tag, **any phone with an NFC reader can read it** — so you can read
*and write* TigerTag chips with nothing but a smartphone, no Pod required.

## Free electronics, free design

There is no custom silicon in a TigerPOD, and that is the point:

- **Two [ACR122U-compatible NFC readers](https://amzn.to/4vok3d7)** — commodity hardware, sold everywhere, by everyone.
- **A single 3D-printed shell** with two slots — you slide an ACR122U into each side.
  No assembly, no screws, no wiring.
- **A splitter** (2× USB-B → 1× USB-C) so the whole thing is one tidy cable.

<p>
  <img src="assets/TigerPOD-reader-acr122u.jpg" alt="ACR122U-compatible USB NFC reader" width="200">
  <img src="assets/TigerPOD-reader-acr122u.jpg" alt="ACR122U-compatible USB NFC reader" width="200">
  <img src="assets/TigerPOD-splitter.jpg" alt="2-to-1 USB splitter" width="200">
</p>

<sub>The three parts we use: two [ACR122U-compatible readers](https://amzn.to/4vok3d7) + one [USB splitter](https://amzn.to/4plgsv8) — two readers go in each Pod.</sub>

### Why two chips and two readers

The recommended setup is **two NFC chips per spool and two NFC readers** — one chip on
each side of the spool, one reader facing each chip:

- **No aiming.** Whichever way you drop the spool in, a chip is always in front of a
  reader. Nothing to line up.
- **Twin Tag stays in sync.** With a reader on each side, the Pod reads and writes
  **both chips at once** — the pair stays byte-identical, and your inventory counts
  one spool, not two tags.

A single chip and a single reader still work, but you lose the drop-and-go convenience
(you have to present the tagged side) and the automatic Twin Tag sync.

Any [NTAG 213 / 215 / 216](https://amzn.to/3TzxGc7) works. Nothing is proprietary, nothing phones home.

### It's a concept, not a fixed product

Strip it down and the TigerPOD is one idea: **two ACR122U readers facing each other, held
at the right distance by a 3D-printed support.** That's it.

The shell we publish simply happens to cradle a **standard 1 kg spool** — but **the shape
is yours to change.** Redesign the support for another spool format, another object, or a
completely different use, and it's still a Pod. Only the two facing readers matter; the
holder around them is an implementation detail. Remix it — and
[share what you make](CONTRIBUTING.md).

And since you print it yourself, **it comes in whatever colour you load.** Same Pod, your filament:

<p>
  <img src="assets/pods/TigerPOD-red.jpg" width="108" alt="Red TigerPOD">
  <img src="assets/pods/TigerPOD-orange.jpg" width="108" alt="Orange TigerPOD">
  <img src="assets/pods/TigerPOD-yellow.jpg" width="108" alt="Yellow TigerPOD">
  <img src="assets/pods/TigerPOD-green.jpg" width="108" alt="Green TigerPOD">
  <img src="assets/pods/TigerPOD-cyan.jpg" width="108" alt="Cyan TigerPOD">
  <img src="assets/pods/TigerPOD-blue.jpg" width="108" alt="Blue TigerPOD">
  <img src="assets/pods/TigerPOD-purple.jpg" width="108" alt="Purple TigerPOD">
  <img src="assets/pods/TigerPOD-pink.jpg" width="108" alt="Pink TigerPOD">
  <img src="assets/pods/TigerPOD-gold.jpg" width="108" alt="Gold TigerPOD">
  <img src="assets/pods/TigerPOD-copper.jpg" width="108" alt="Copper TigerPOD">
  <img src="assets/pods/TigerPOD-silver.jpg" width="108" alt="Silver TigerPOD">
  <img src="assets/pods/TigerPOD-grey.jpg" width="108" alt="Grey TigerPOD">
  <img src="assets/pods/TigerPOD-black.jpg" width="108" alt="Black TigerPOD">
  <img src="assets/pods/TigerPOD-white.jpg" width="108" alt="White TigerPOD">
  <img src="assets/pods/TigerPOD-glow.jpg" width="108" alt="Glow-in-the-dark TigerPOD">
</p>

<sub>A few of the colours it's been printed in — plus brown, milk, pastel green and light grey in
[`assets/pods/`](assets/pods).</sub>

And whatever your filament does, the Pod does too — silk, galaxy, marble,
glow-in-the-dark:

<p>
  <img src="assets/pods/TigerPOD-silk-red.jpg" width="108" alt="Silk red TigerPOD">
  <img src="assets/pods/TigerPOD-silk-pink.jpg" width="108" alt="Silk pink TigerPOD">
  <img src="assets/pods/TigerPOD-silk-yellow.jpg" width="108" alt="Silk yellow TigerPOD">
  <img src="assets/pods/TigerPOD-silk-blue.jpg" width="108" alt="Silk blue TigerPOD">
  <img src="assets/pods/TigerPOD-silk-black.jpg" width="108" alt="Silk black TigerPOD">
  <img src="assets/pods/TigerPOD-silk-gold.jpg" width="108" alt="Silk gold TigerPOD">
  <img src="assets/pods/TigerPOD-silk-copper.jpg" width="108" alt="Silk copper TigerPOD">
  <img src="assets/pods/TigerPOD-silk-silver.jpg" width="108" alt="Silk silver TigerPOD">
  <img src="assets/pods/TigerPOD-galaxy-purple.jpg" width="108" alt="Galaxy purple TigerPOD">
  <img src="assets/pods/TigerPOD-marble.jpg" width="108" alt="Marble TigerPOD">
  <img src="assets/pods/TigerPOD-rainbow-linear.jpg" width="108" alt="Linear rainbow TigerPOD">
  <img src="assets/pods/TigerPOD-rainbow-multi.jpg" width="108" alt="Multicolour rainbow TigerPOD">
  <img src="assets/pods/TigerPOD-glow-green-dark.jpg" width="108" alt="Green glow-in-the-dark TigerPOD, lights off">
  <img src="assets/pods/TigerPOD-glow-blue-dark.jpg" width="108" alt="Blue glow-in-the-dark TigerPOD, lights off">
  <img src="assets/pods/TigerPOD-glow-red-dark.jpg" width="108" alt="Red glow-in-the-dark TigerPOD, lights off">
</p>

<sub>Full-resolution originals live in [`assets/pods/hd/`](assets/pods/hd), and transparent
(background-removed) PNG cut-outs in [`assets/pods/cutout/`](assets/pods/cutout).</sub>

## More than TigerTag — a universal NFC station

The Pod is **not locked to the TigerTag protocol**. It is, quite literally, two standard
PC/SC readers in a spool-shaped holder: **anything an ACR122U can do, the Pod can do.**

**You control the chip, completely.** Read what's on a tag, write something new to it,
change what's already there, and erase it back to blank. The Pod does all four — no
one-way street, no write-once, no vendor lock. *(Developers: that's full **CRUD** —
create, read, update, delete.)*

To be precise about the scope, that means full read/write/erase control **for filament, in
Dual NFC** — both chips of a spool handled together — on **standard filament spools**,
across **any brand** and **any chip technology the ACR122U supports** (MIFARE, NTAG, and
the rest). Not one brand's spools. Not one chip family. Any of them.

**A universal reader/writer.** The ACR122U handles far more than NTAG. It covers
**ISO 14443 Type A and B**, **MIFARE** (Classic 1K/4K, Ultralight, DESFire), **FeliCa**,
**Topaz/Jewel**, and **NFC Forum tag types 1–4**. Whatever you can read or write with an
ACR122U, you can read or write in the Pod.

**Never locked, endlessly reusable.** A TigerTag is **never write-locked**. When a spool is
done, erase and rewrite its chips as fresh TigerTags — as many times as you want.

**Give end-of-life spool chips a second life.** Recycle them into something else entirely:
reprogram an NTAG as a plain **NDEF** tag and use it for **home automation, connected
objects, Wi-Fi hand-off, a URL, a business card** — any NFC use case you like. And you can
turn it back into a TigerTag whenever you want. The Pod writes **both ways**. The chip is a
reusable asset, not single-use packaging — **zero e-waste**.

## How the filament RFID ecosystems compare

Most printer makers tag their spools. Almost all of them lock the tag. Here's the landscape,
and where TigerTag sits in it:

| Ecosystem | Chip | Can you write your own tag? | Android | iOS |
|---|---|---|:---:|:---:|
| **TigerTag** | NTAG 213 / 215 / 216 | **Yes** — never locked, erase and rewrite forever | ✅ | ✅ |
| [Elegoo Canvas](https://github.com/ELEGOO-3D/ELEGOO-RFID-Tag-Guide) | NTAG213 | Yes — no encryption, no password, publicly documented | ✅ | ✅ |
| [Anycubic ACE](https://help.simplyprint.io/en/article/all-about-nfc-rfid-for-filament-spools-bambu-openprinttag-creality-qidi-anycubic-more-19luyni/) | NTAG215 / 216 | Yes | ✅ | ✅ |
| [Bambu Lab](https://github.com/Bambu-Research-Group/RFID-Tag-Guide) | MIFARE Classic 1K | **No** — data is encrypted *and* RSA-signed; the printer rejects any tag without a valid signature | ⚠️ | ❌ |
| [Creality CFS](https://help.simplyprint.io/en/article/the-creality-material-standard-nfcrfid-for-the-creality-cfs-1crrofa/) | MIFARE Classic 1K | Not officially — proprietary and undocumented; only reverse-engineered community tools can | ⚠️ | ❌ |
| [QIDI Box](https://help.simplyprint.io/en/article/the-qidi-material-standard-nfcrfid-for-the-qidi-box-ns0c8d/) | MIFARE Classic 1K | Not officially — proprietary format | ⚠️ | ❌ |
| [Snapmaker U1](https://snapmakeru1-extended-firmware.pages.dev/rfid_support) | MIFARE Classic 1K | **No** — proprietary + RSA signature, official tags only | ⚠️ | ❌ |

<sub>✅ works · ⚠️ only on Android phones whose NFC chipset supports MIFARE Classic (an NXP-family
chipset — it is not guaranteed on every Android device) · ❌ impossible: Apple does not expose
MIFARE Classic to apps, on any iPhone.</sub>

Don't take our word for the split — two independent projects sort it the same way.

[**OpenRFID**](https://github.com/suchmememanyskill/OpenRFID), a third-party library that
parses filament tags from every major brand, routes Bambu Lab, Creality, QIDI and Snapmaker
through its *authenticated MIFARE Classic* path (keys required), while Elegoo, Anycubic and
**TigerTag** go through its plain *NTAG* path — no keys, no authentication.

[**xspool**](https://github.com/xperiments/xspool), a spool manager supporting Bambu Lab,
Creality CFS, Anycubic ACE Pro and TigerTag, publishes its own capability table. This is
**their table, not ours** — we didn't write a line of it:

| Format | Tag type | Readable | Writable | Extra metadata |
|---|---|:---:|:---:|:---:|
| **TigerTag** | NTAG 213/215/216 | ✅ | ✅ | ✅ |
| BambuLab Official | MIFARE 1K | ✅ | ❌ | ❌ |
| Creality CFS | MIFARE 1K | ✅ | ✅ | ❌ |
| Anycubic ACE PRO | NTAG 213/215/216 | ✅ | ✅ | ❌ |

<sub>Source: [xspool — supported formats](https://github.com/xperiments/xspool/blob/main/docs/vendors/vendors.md)</sub>

Bambu Lab is the only one that can't be written. And TigerTag is the only format in that
table with **read, write *and* extra metadata** all supported.

TigerTag is implemented in both projects — alongside the majors, by people with no stake
in it.

Two things fall out of that table.

**The lock is cryptographic, not physical.** A MIFARE Classic 1K chip is perfectly
rewritable — but Bambu Lab and Snapmaker sign their payload, so a tag you write yourself is
refused by the printer. The chip in your hand is fine; the ecosystem simply won't accept it.
TigerTag signs nothing you can't reproduce and locks nothing: the tag stays yours.

**MIFARE Classic locks out your phone.** Apple does not allow apps to talk to MIFARE Classic
tags, so **no iPhone can read a Bambu, Creality, QIDI or Snapmaker spool tag** — ever. That
rules out roughly half the phones on the planet, permanently, by platform policy. Even on
Android it isn't a given: MIFARE Classic is an NXP technology, and phones whose NFC chipset
isn't from that family can't read it either.

**So we chose NTAG on purpose.** This is the reason TigerTag is built on NTAG and not MIFARE:
an NTAG is read by **every NFC smartphone, with no restriction, no app whitelist, no vendor
permission** — Android and iPhone alike. A tag anyone can read with the device already in
their pocket isn't a vendor ecosystem; it's a **public, universal standard**. That was the
whole point.

<sub>One honest limit: Prusa's OpenPrintTag uses NXP ICODE SLIX (ISO 15693), a family the
ACR122U doesn't cover — those tags are outside the Pod's range.</sub>

## Build one

1. Print the shell — one part, the model is published on
   [MakerWorld](https://makerworld.com/fr/models/1289152-tigertag-io-open-spool-pod-for-rfid-filament).
2. Get two [ACR122U-compatible readers](https://amzn.to/4vok3d7), from any shop you like
   (and some [NTAG 213 / 215 / 216 tags](https://amzn.to/3TzxGc7) to write on).
3. Slide one reader into each slot — no screws, no glue, no wiring.
4. Plug both into your computer (the splitter makes it one cable, but two ports work too).
5. Install [Tiger Studio](https://github.com/TigerTag-Project/TigerTag-Studio-Manager) —
   it picks the readers up automatically.

### Bill of materials

Rough prices, sourced separately — your mileage will vary by shop and region.

| Part | Qty | Approx. price | Notes |
|---|---|---|---|
| [ACR122U-compatible NFC reader](https://amzn.to/4vok3d7) | 2 | ~€15–25 each | One per side of the spool |
| [NTAG 213 / 215 / 216 tags](https://amzn.to/3TzxGc7) | 1 pack | ~€10–20 | Two chips per spool; a pack tags many spools |
| 3D-printed shell | 1 | filament only | [Print it](https://makerworld.com/fr/models/1289152-tigertag-io-open-spool-pod-for-rfid-filament) yourself |
| [USB splitter (2× USB-A F → 1× USB-A M)](https://amzn.to/4plgsv8) | 1 | ~€5–10 | Optional — two USB ports work too |

### Reader compatibility

The ACR122U talks over **PC/SC** (PC/SC is the OS-level smart-card standard every reader
of this class implements). Because the Pod builds on PC/SC rather than a vendor driver,
the same setup runs on every desktop OS, and any PC/SC library can drive it:

- **Windows** — recognised out of the box; the PC/SC service (`SCardSvr`) ships with
  Windows. If a card-emulation "helper" driver hijacks the reader, remove it so the
  device shows up as a plain PC/SC reader.
- **macOS** — works with the built-in PC/SC stack (`pcscd`); no extra driver needed.
- **Linux** — install PC/SC and the ACS/CCID driver, e.g.
  `sudo apt install pcscd libacsccid1`, then make sure the `pcscd` service is running.

## Or buy the kit

The electronics kit on [the shop](https://tigertag.io) costs less than sourcing the same
parts yourself, the readers arrive with the project's official logo on them, and it funds
the standard:

- [TigerPOD bundle — 2 readers + splitter](https://tigertag.io/products/tigertag-player-bundle-2pcs-spliter)
- [Single reader](https://tigertag.io/products/tigertag-player)
- [Splitter alone](https://tigertag.io/products/tigertag-splitter)

The bundle is the **electronics only** — two official-logo readers and the splitter. You
still [print the TigerPOD shell](https://makerworld.com/fr/models/1289152-tigertag-io-open-spool-pod-for-rfid-filament)
yourself and slide the readers in. Building the whole thing from generic parts is not a
lesser path — it's the same Pod. That's what an open protocol means.

## The ecosystem around it

![The TigerTag system — the TigerPOD, the Tiger Studio desktop app, and the mobile app all sharing one spool](assets/TigerPOD-hero-system.png)

| | |
|---|---|
| **The protocol** | [TigerTag-RFID-Guide](https://github.com/TigerTag-Project/TigerTag-RFID-Guide) — the spec and the public registry (CC-BY-4.0, irrevocable implementation grant) |
| **Tiger Studio** | [Desktop app](https://github.com/TigerTag-Project/TigerTag-Studio-Manager) (MIT) — inventory, printers, and the Pod's home |
| **SDKs** | [JS](https://github.com/TigerTag-Project/TigerTag-SDK-JS) · [Python](https://github.com/TigerTag-Project/TigerTag-SDK-Python) (Apache-2.0) |
| **Community** | [Discord](https://discord.gg/3Qv5TSqnJH) |

On a phone you don't need a Pod at all — the mobile app uses the phone's own NFC.
The Pod is the desktop's NFC.

## Read a tag in your own code

TigerTag stores everything **on the chip** — no lookup, no network. Reading is always the
same two steps, whatever the language:

1. **Get the raw bytes** from the tag with any NFC library: the **7-byte UID** and the
   **user memory, pages `0x04`–`0x27`** (36 pages × 4 bytes = **144 bytes**).
2. **Decode offline** by handing those to the TigerTag SDK — `fromPages(uid, payload)` in
   JS, `from_pages(uid, payload)` in Python. The SDK returns material, brand, colour,
   temperatures, weight, and (optionally) verifies the signature.

The SDK never touches the reader — you bring the bytes, it parses them. So you pair it
with whichever NFC library fits your platform:

| Platform | NFC library | Notes |
|---|---|---|
| **Desktop — Node / Electron** | [`nfc-pcsc`](https://www.npmjs.com/package/nfc-pcsc) | What Tiger Studio uses to drive the Pod's ACR122U readers over PC/SC |
| **Desktop — Python** | [`nfcpy`](https://nfcpy.readthedocs.io) or [`pyscard`](https://pyscard.sourceforge.io) (PC/SC) | `pyscard` matches the ACR122U's PC/SC path directly |
| **Android** | `MifareUltralight` / `NfcA` (built-in) | `readPages(4)`, four pages at a time |
| **iOS** | CoreNFC (`NFCTagReaderSession`) | Raw MiFare read of pages 4–39 |
| **Flutter** | [`flutter_nfc_kit`](https://pub.dev/packages/flutter_nfc_kit) | `transceive` the NTAG `READ` command (`0x30`) |
| **Arduino / ESP32** | [`MFRC522`](https://github.com/miguelbalboa/rfid) | `MIFARE_Read` page by page, ship UID + payload over serial |

Runnable, copy-paste examples for each are in the SDK repos:
[JS](https://github.com/TigerTag-Project/TigerTag-SDK-JS/blob/main/examples/integrate_nfc_sdk.js)
· [Python](https://github.com/TigerTag-Project/TigerTag-SDK-Python/blob/main/examples/integrate_nfc_sdk.py).

### Test the Pod with the built-in playground

Both SDKs ship a **playground** — a small local server plus a web page — so you can try a
Pod without writing any code first:

- **[JS SDK](https://github.com/TigerTag-Project/TigerTag-SDK-JS)** — `npm install ws nfc-pcsc`
  then `npm run playground` and open `http://localhost:7432/tools/playground.html`. It
  connects straight to the ACR122U over PC/SC and pushes **live card events** to the page:
  drop a spool in the Pod and watch it decode in the browser.
- **[Python SDK](https://github.com/TigerTag-Project/TigerTag-SDK-Python)** — run
  `python3 tools/server.py` and open the same page to inspect and diff payloads.

It's the fastest way to confirm your readers are seen and your tags parse correctly.

## FAQ

**Can I use just one reader?**
Yes, but you lose the drop-and-go convenience and the automatic Twin Tag sync — see
[Why two chips and two readers](#why-two-chips-and-two-readers).

**My reader isn't detected.**
Make sure it's a genuine ACR122U-compatible (PC/SC) reader. On Linux, start the `pcscd`
service and install the CCID driver. Unplug/replug once, then relaunch Tiger Studio.

**NTAG 213 vs 215 vs 216 — which one?**
They differ only in memory: 213 (~144 B), 215 (~504 B), 216 (~888 B). Any of them holds a
TigerTag record; pick 215/216 if you want more headroom. All three work in the Pod.

**Which spools fit?**
About **99% of 1 kg spools**, regardless of type — plastic masterspools, cardboard
spools, non-reusable plastic spools, and refills all sit in the Pod.

**Can I reuse the tags?**
Yes — TigerTags are never locked. Erase and rewrite them as new TigerTags indefinitely,
or convert them to a plain NDEF tag for another NFC use — home automation, connected
objects, a URL, a business card — and back again. The chip is a reusable asset, not
disposable packaging.

**Can I use the Pod for non-TigerTag NFC work?**
Yes. It's two standard ACR122U readers, so it can read, write, rewrite and erase anything
an ACR122U supports (full CRUD, in developer terms): ISO 14443 A/B, MIFARE (Classic,
Ultralight, DESFire), FeliCa, Topaz/Jewel, and NFC Forum types 1–4. The Pod is a universal
NFC read/write station that happens to be spool-shaped.

**Does it need internet?**
No. The Pod reads and writes locally; nothing phones home.

## Contributing

Remixes of the shell, build photos, doc fixes, and translations are all welcome — see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

The documentation in this repository is **CC-BY-4.0** (see [LICENSE](LICENSE)).
The TigerTag name and logo are trademarks of TigerTag Corp — usage terms in
[TRADEMARK.md](https://github.com/TigerTag-Project/TigerTag-RFID-Guide/blob/main/TRADEMARK.md).

`assets/` also carries the official "Tiger" icon kit: neutral (no text) and
"TIGER TAG"-marked variants, each shipped as overflow (display as-is), contained, and
square (for masked contexts like round favicons or adaptive icons) compositions. Same
trademark terms apply — full usage guidelines are in
[brand/README.md](https://github.com/TigerTag-Project/TigerTag-RFID-Guide/blob/main/brand/README.md)
of the main protocol repo.

Questions, partnerships, press: [tigertag@tigertag.io](mailto:tigertag@tigertag.io)

---

<sub>Some hardware links above are Amazon affiliate links: as an Amazon Associate,
TigerTag earns from qualifying purchases, at no extra cost to you. It helps fund the
open protocol.</sub>

<sub>AI agents & LLMs: a machine-readable summary of this project is in
[llms.txt](llms.txt).</sub>
