# TigerPOD

**A CD player, for spools.**

Drop a filament spool in the TigerPOD and your computer reads its TigerTag chip —
material, brand, colour, temperatures, what's left. Write a tag the same way: put the
spool in, done. No aiming, no hunting for the sticker.

![TigerPOD](assets/TigerPOD.png)

## Free electronics, free design

There is no custom silicon in a TigerPOD, and that is the point:

- **Two ACR122U-compatible NFC readers** — commodity hardware, sold everywhere, by everyone.
- **A 3D-printed shell** that holds a spool with one reader on each side.
- **A splitter** (2× USB-B → 1× USB-C) so the whole thing is one tidy cable.

Because there is a reader on each side, the Pod reads and writes **both chips of a
Twin Tag spool at once** — the pair stays byte-identical, and your inventory counts
one spool, not two tags.

Any NTAG 213 / 215 / 216 works. Nothing is proprietary, nothing phones home.

## Build one

1. Print the shell — the model is published on
   [MakerWorld](https://makerworld.com/fr/@TigerTag/collections/models).
2. Get two ACR122U-compatible readers, from any shop you like.
3. Plug both into your computer (the splitter makes it one cable, but two ports work too).
4. Install [Tiger Studio](https://github.com/TigerTag-Project/TigerTag-Studio-Manager) —
   it picks the readers up automatically.

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

| | |
|---|---|
| **The protocol** | [TigerTag-RFID-Guide](https://github.com/TigerTag-Project/TigerTag-RFID-Guide) — the spec and the public registry (CC-BY-4.0, irrevocable implementation grant) |
| **Tiger Studio** | [Desktop app](https://github.com/TigerTag-Project/TigerTag-Studio-Manager) (MIT) — inventory, printers, and the Pod's home |
| **SDKs** | [JS](https://github.com/TigerTag-Project/TigerTag-SDK-JS) · [Python](https://github.com/TigerTag-Project/TigerTag-SDK-Python) (Apache-2.0) |
| **Community** | [Discord](https://discord.gg/3Qv5TSqnJH) |

On a phone you don't need a Pod at all — the mobile app uses the phone's own NFC.
The Pod is the desktop's NFC.

## Licence

The documentation in this repository is **CC-BY-4.0** (see [LICENSE](LICENSE)).
The TigerTag name and logo are trademarks of TigerTag Corp — usage terms in
[TRADEMARK.md](https://github.com/TigerTag-Project/TigerTag-RFID-Guide/blob/main/TRADEMARK.md).

Questions, partnerships, press: [tigertag@tigertag.io](mailto:tigertag@tigertag.io)
