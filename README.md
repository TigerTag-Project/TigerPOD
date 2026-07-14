# TigerPOD

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](LICENSE)

**A CD player, for spools.**

The TigerPOD is an open-source desktop **NFC / RFID reader and writer (burner) for
3D-printing filament spools**, built from two commodity USB readers and a 3D-printed
shell. Drop a filament spool in and your computer reads its TigerTag chip — material,
brand, colour, temperatures, what's left. Write (encode) a tag the same way: put the
spool in, done. No aiming, no hunting for the sticker.

![TigerPOD](assets/TigerPOD.png)

![The TigerPOD reading a spool in Tiger Studio](assets/tigerpod-demo.gif)

<sub>▶ Higher-quality clip: [tigerpod-demo.mp4](assets/tigerpod-demo.mp4)</sub>

## A first of its kind

As far as we know, **the TigerPOD is the first spool-scale RFID reader/burner of its
kind** — nobody had done this before. We conceived it in **2023, alongside the creation
of the open-source TigerTag protocol**: take **two standard, low-cost USB NFC readers**,
drop one on each side of a 3D-printed spool holder, and you get a device that reads *and*
writes (burns) both chips of a filament spool at once. No custom PCB, no proprietary
reader, no dedicated silicon.

That turns encoding a spool's RFID chips — normally an industrial, closed process — into
something anyone can build on their desk for the price of two commodity readers. The goal
isn't the gadget, it's **democratising RFID for filament** through the open
[**TigerTag**](https://github.com/TigerTag-Project/TigerTag-RFID-Guide) protocol so any
maker, brand, or printer can adopt it freely.

New to RFID for filament? Start with the
[**TigerTag RFID Guide**](https://github.com/TigerTag-Project/TigerTag-RFID-Guide) — the
open spec and public registry behind the Pod.

## Free electronics, free design

There is no custom silicon in a TigerPOD, and that is the point:

- **Two [ACR122U-compatible NFC readers](https://amzn.to/4vok3d7)** — commodity hardware, sold everywhere, by everyone.
- **A single 3D-printed shell** with two slots — you slide an ACR122U into each side.
  No assembly, no screws, no wiring.
- **A splitter** (2× USB-B → 1× USB-C) so the whole thing is one tidy cable.

<img src="assets/acr122u-reader.jpg" alt="An ACR122U-compatible USB NFC reader" width="240">

<sub>The [ACR122U-compatible reader](https://amzn.to/4vok3d7) we use — two of these go in the Pod.</sub>

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
| Splitter (2× USB-B → 1× USB-C) | 1 | ~€5–10 | Optional — two USB ports work too |

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

The assembled kit on [the shop](https://tigertag.io) costs less than sourcing the same
parts yourself, the readers arrive with the project's logo on them, and it funds the
standard:

- [TigerPOD bundle — 2 readers + splitter](https://tigertag.io/products/tigertag-player-bundle-2pcs-spliter)
- [Single reader](https://tigertag.io/products/tigertag-player)
- [Splitter alone](https://tigertag.io/products/tigertag-splitter)

Building it yourself is not a lesser path — it's the same Pod. That's what an open
protocol means.

## The ecosystem around it

![Tiger Studio on desktop and mobile](assets/tiger-studio.png)

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

**Does it need internet?**
No. The Pod reads and writes locally; nothing phones home.

## Licence

The documentation in this repository is **CC-BY-4.0** (see [LICENSE](LICENSE)).
The TigerTag name and logo are trademarks of TigerTag Corp — usage terms in
[TRADEMARK.md](https://github.com/TigerTag-Project/TigerTag-RFID-Guide/blob/main/TRADEMARK.md).

Questions, partnerships, press: [tigertag@tigertag.io](mailto:tigertag@tigertag.io)

---

<sub>Some hardware links above are Amazon affiliate links: as an Amazon Associate,
TigerTag earns from qualifying purchases, at no extra cost to you. It helps fund the
open protocol.</sub>

<sub>AI agents & LLMs: a machine-readable summary of this project is in
[llms.txt](llms.txt).</sub>
