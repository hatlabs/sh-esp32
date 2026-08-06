---
title: Finnish translation glossary and style rules (SH-ESP32)
date: 2026-08-03
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into Finnish under docs/fi/
  - Reviewing a Finnish translation for consistency
  - Adding a new term that has no established Finnish equivalent
tags:
  - translation
  - i18n
  - finnish
  - terminology
  - mkdocs-static-i18n
---

# Finnish translation glossary and style rules

## Context

The SH-ESP32 documentation is written in English under `docs/en/` and
translated into Finnish under `docs/fi/`, using the `mkdocs-static-i18n` folder
structure. Each language directory mirrors the same tree, so a translation keeps
its source's path and filename: `docs/en/hardware/index.md` becomes
`docs/fi/hardware/index.md`. Only markdown lives under `docs/fi/` — images stay
with the English source and are shared, including the per-tutorial `media/`
directories and the shared `docs/media/` at the docs root.

**This file began as a copy of the HALMET glossary and deliberately keeps its
decisions**, so two Hat Labs ESP32 boards do not describe the same part with two
different Finnish words. `carrier board` → `emolevy` is Matti Airas's call and
stands here too, as does HALMET's divergence on `power supply` → `teholähde`:
the Engine Hat implements a constant current source, so `vakiovirtalähde`
appears in this documentation as well, and `virtalähde` inside it would read as
a modifier of the same component rather than a different one. Terms below the
SH-ESP32 heading are this product's additions; a shared row changes in both
repositories or in neither.

HALMET's glossary was chosen over HALPI2's and SH-RPi's by counting rather than
by assumption. Both of those are Raspberry Pi power boards, and their additions
— supercapacitor, watchdog, daemon, safe shutdown, blackout, power management —
occur **zero times each** in the SH-ESP32 documentation. HALMET's sensor
vocabulary occurs throughout: analog input 15, digital input 16, 1-Wire 37,
I2C 21, SensESP 11, NMEA 2000 74.

Translations are produced page by page, at different times, potentially by
different people. Without a fixed terminology list the same English term drifts
across pages — *drop cable* becomes `haarakaapeli` on one page and
`pudotuskaapeli` on the next — and the result reads as machine output even when
each individual sentence is correct.

This file is the reference that prevents that drift. It is a living document:
extend it when a page introduces a term that is not listed here, rather than
inventing a one-off translation.

Unlike the other files under `solutions/`, this one has no date in its filename
because it is meant to be edited in place, not superseded.

## Names that are never translated

Product names, protocol names, hardware standards, and software UI strings stay
in English. The device's own interface is in English, so translating a menu name
would send the reader looking for something that does not exist on screen.

- **Products and software:** SH-ESP32, Sailor Hat, Engine Top Hat, HALMET,
  SensESP, Signal K, OpenPlotter, Arduino IDE, ESP-IDF, PlatformIO, VSCode,
  Grafana, InfluxDB, Hat Labs
- **Hardware and standards:** ESP32-WROOM-32E, ADS1115, NMEA 2000, CAN bus,
  I2C, 1-Wire, GPIO, JTAG, USB, ADC, TVS, PG7, PG9, SP13, M12, Phoenix MC,
  Schmitt trigger, IoT
- **Pin and signal names are copied exactly:** `D1`–`D4`, `A1`–`A4`, `SDA`,
  `SCL`, `DQ`, `TXD0`, `RXD0`, `EN`, `IO0`, `GPIO2`, `CCS`, `LP`, `VP`, `VN`,
  `3V3`, `GND`. These are printed on the board; a translated pin name sends the
  reader looking for a label that does not exist.
- **UI paths, commands, hostnames, file paths:** **Networking**, **WiFi
  (wlan0)**, **Add**, `raspi-config`, `passwd`, `shutdown`, `halos.local`,
  `can0`, `pi`, `halos`

Code blocks, command output, URLs, and image filenames are never touched.

## Style rules

### Units and numbers

Finnish follows SI spacing and uses a decimal comma. The English source does
not, so this requires an active conversion on nearly every technical page.

| English source | Finnish |
|:---------------|:--------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `1.5mm²`, `2m` | `1,5 mm²`, `2 m` |
| `120Ω` | `120 Ω` |
| `3-5A` | `3–5 A` (en dash for ranges) |

Dimensions written as a single product spec keep the tight form:
`200×130×60 mm`.

### Product names in compounds and inflections

Finnish compounds a multi-word proper name with a space and a hyphen; a
single-word name compounds directly:

- `NMEA 2000 -verkko`, `NMEA 2000 -väylä`, `Signal K -palvelin`,
  `Raspberry Pi -antenni`, `Compute Module 5 -moduuli`
- `HALPI2-kotelo`, `E7T-liitin`, `HaLOS-levykuva`, `USB-näppäimistö`

Case endings attach with a colon when the name ends in a digit or is read as
letters: `HALPI2:n`, `CM5:n`, `HaLOS:n`, `NMEA 2000:n`.

### Address form

Instructions use the **second person singular imperative** — the standard
register for Finnish consumer and installation manuals:

> Kytke virtajohto. Varmista napaisuus yleismittarilla ennen jännitteen
> kytkemistä.

Descriptive passages use the passive or a plain statement:

> Laite sammuu automaattisesti, kun virransyöttö katkaistaan.

Do not translate the English *you* literally into `sinä` — Finnish imperative
already carries it, and the explicit pronoun reads as clumsy translation.

### Admonitions

Standard admonition titles (`Note`, `Warning`, `Tip`, `Info`) are translated
centrally via the plugin's `admonition_translations` setting, not in the page
source. **Custom** titles written into the page — `!!! note "Shop Link"` — are
part of the content and must be translated: `!!! note "Linkki verkkokauppaan"`.

### Images

Image captions and alt texts are translated; filenames and paths are not.
Screenshots (`raspi-config-menu.jpg`, `networking-menu.jpg`,
`wifi-password.jpg`) show an English interface and are reused as-is. This is
intentional and correct — the reader will see English on their own screen too.

### Links

Relative links and image paths are copied from the English source unchanged. The
plugin merges the language trees, so `../user-guide/operation.md` resolves to the
Finnish page when one exists and falls back to English when it does not, and an
image path resolves to the single shared copy under `docs/en/`. Never add an
`en/` or `fi/` segment to a path inside a page — the language is decided by which
directory the file itself lives in, not by its links.

### Navigation titles

Section and page titles in the navigation are not part of any markdown file —
they live in `mkdocs.yml` under the i18n plugin's `nav_translations`. That is the
single source of truth; do not restate the full list here. Two entries are
judgement calls worth recording:

- `Errata` → **Tunnetut virheet**. The Latin term is opaque to a general reader;
  plain Finnish is clearer for a page listing known hardware defects.
- `FAQ` → **UKK** (*usein kysytyt kysymykset*). The established Finnish
  abbreviation.

When a new page is added to the nav in English, add its Finnish title to
`nav_translations` in the same change — an untranslated entry silently falls
back to English and is easy to miss.

## Glossary

### Enclosure, mounting, and installation

| English | Finnish | Note |
|:--------|:--------|:-----|
| carrier board | emolevy | Deliberate: not literally accurate, but the term readers know. Decided by Matti Airas, 2026-08-03 |
| enclosure | kotelo | |
| heat sink | jäähdytyselementti | |
| waterproof | vesitiivis | |
| rugged | kestäväksi rakennettu | Avoid the loan word *rugged* |
| wall-mount | seinäkiinnitys | |
| mounting surface | kiinnitysalusta | |
| pilot hole | esiporausreikä | |
| mounting template | porausmalline | Drill template |
| clearance | vapaa tila | |
| bilge | pilssi | |
| bulkhead | laipio | |
| cable gland | läpivientiholkki | PG7 cable gland → `PG7-läpivientiholkki` |
| cable routing | kaapelireititys | |
| service loop | johtolenkki | Slack left at both cable ends |
| chafing | hankautuminen | |
| cable tie | nippuside | |

**A note on `emolevy`.** The term was chosen for reader familiarity over literal
accuracy, and it carries one risk: *emolevy* normally means a motherboard, which
would imply the board is the computer and the CM5 an add-on — the reverse of how
HALPI2 is built. When translating passages where that relationship matters
(reseating the CM5, troubleshooting a board that will not boot), make the roles
explicit in the surrounding sentence rather than relying on the term to carry
them.

### Electrical

| English | Finnish | Note |
|:--------|:--------|:-----|
| power source | virransyöttö | |
| input voltage range | syöttöjännitealue | |
| polarity | napaisuus | |
| positive (+) / negative (−) | plus (+) / miinus (−) | |
| fuse | sulake | |
| inline fuse | linjasulake | |
| circuit breaker | johdonsuojakatkaisija | Electrical panel breaker |
| current limiting | virranrajoitus | |
| overcurrent | ylivirta | |
| voltage drop | jännitehäviö | |
| grounding | maadoitus | |
| short circuit | oikosulku | |
| wire gauge | johtimen poikkipinta-ala | Finnish uses mm², not AWG |
| marine-grade wire | merikäyttöön hyväksytty johdin | |
| strip (a wire) | kuoria | |
| wire strippers | kuorintapihdit | |
| crimping | puristusliitos | Verb: *puristaa liitin kiinni* |
| crimper | puristuspihdit | |
| heat-shrink tubing | kutistesukka | |
| heat gun | kuumailmapuhallin | |
| multimeter | yleismittari | |
| continuity test | jatkuvuusmittaus | |
| terminal | liitin | |
| terminal block | riviliitin | |
| strain relief | vedonpoisto | |
| super-capacitor | superkondensaattori | |
| real-time clock | reaaliaikakello | |
| backup battery | varaparisto | |

### Connectors and interfaces

| English | Finnish | Note |
|:--------|:--------|:-----|
| connector | liitin | |
| barrel connector | DC-pyöröliitin | Add *(barrel)* on first mention |
| header (GPIO, button) | liitin | `40-nastainen GPIO-liitin` |
| pin | nasta | |
| backbone | runkokaapeli | NMEA 2000 backbone |
| drop cable | haarakaapeli | |
| T-connector / T-adapter | T-liitin | |
| termination (120 Ω) | päätevastus | The component; the act is *terminointi* |
| front panel | etupaneeli | |
| antenna | antenni | |
| extension cable | jatkokaapeli | |
| male / female | uros / naaras | Connector gender |

### System behaviour and status

| English | Finnish | Note |
|:--------|:--------|:-----|
| boat computer | venetietokone | |
| boot / to boot | käynnistyä | |
| first boot | ensikäynnistys | |
| shutdown | sammutus | |
| graceful shutdown | hallittu sammutus | |
| power loss | jännitteen menetys | |
| blackout | sähkökatko | |
| glitch immunity | häiriönsieto | |
| power management | virranhallinta | |
| status LED | tila-LED | |
| LED bar | LED-rivi | |
| monitoring | valvonta | |
| passive cooling | passiivinen jäähdytys | |
| filesystem | tiedostojärjestelmä | |
| unmount (filesystem) | irrottaa | *tiedostojärjestelmä irrotetaan turvallisesti* |
| reseat (a module) | asettaa uudelleen paikalleen | |

### Software and networking

| English | Finnish | Note |
|:--------|:--------|:-----|
| firmware | firmware | Not *laiteohjelmisto* — Hat Labs convention |
| daemon | daemon | Not *taustaprosessi* — Hat Labs convention |
| to flash | flashata | Established Hat Labs usage |
| operating system image | levykuva | |
| headless | ilman näyttöä | First mention: `ilman näyttöä (headless)` |
| deployment | käyttöönotto | |
| container app | konttisovellus | |
| container image | konttikuva | Not *levykuva* — that is a disk image |
| dashboard | koontinäyttö | Homarr's *dashboard* view |
| WiFi Access Point | WiFi-tukiasema | |
| wired / wireless | langallinen / langaton | |
| credentials | tunnukset | |
| username / password | käyttäjätunnus / salasana | |
| default password | oletussalasana | |
| single sign-on (SSO) | kertakirjautuminen (SSO) | |
| Certificate Authority (CA) | varmenteen myöntäjä (CA) | |
| to trust (a certificate) | luottaa | |
| web interface | verkkokäyttöliittymä | |
| browser | selain | |
| system administration | järjestelmänhallinta | |

### Applications and use cases

| English | Finnish | Note |
|:--------|:--------|:-----|
| chart plotter | karttaplotteri | |
| data logging | tiedonkeruu | |
| vessel | alus | |
| engine parameters | moottorin mittaustiedot | |
| fleet management | kalustonhallinta | |
| predictive maintenance | ennakoiva kunnossapito | |
| process monitoring | prosessivalvonta | |
| remote monitoring | etävalvonta | |
| electromagnetic interference (EMI/RFI) | sähkömagneettiset häiriöt (EMI/RFI) | |
| compliance | vaatimustenmukaisuus | |
| warranty | takuu | |

## HALMET terms

HALMET is a sensor interface board, so it needs vocabulary HALPI2 never used:
input circuits, measurement, and the things printed on a small PCB. Rows above
this heading are shared with HALPI2 and should not be changed here alone.

### Board and inputs

| English | Finnish | Note |
|:--------|:--------|:-----|
| development board | kehityskortti | HALMET is sold as one; not *emolevy*, which is HALPI2's carrier board |
| digital input | digitaalitulo | `D1`–`D4` stay as printed |
| analog input | analogiatulo | `A1`–`A4` stay as printed |
| input | tulo | Not *sisääntulo* in this sense |
| output | lähtö | |
| sender | anturi | The marine sender that a gauge reads; *lähetin* would suggest radio |
| tank sender | tankkianturi | |
| resistive sender | vastusanturi | |
| gauge (engine panel gauge) | mittari | `moottoripaneelin mittari` |
| counter | laskuri | |
| chain counter | ketjulaskuri | |
| alarm signal | hälytyssignaali | |
| engine RPM | moottorin kierrosluku | Not *RPM*; the abbreviation is not used in Finnish prose |
| tachometer | kierroslukumittari | |
| alternator W terminal | laturin W-napa | |
| fuel flow | polttoaineen virtaus | |

### Measurement and circuits

| English | Finnish | Note |
|:--------|:--------|:-----|
| galvanic isolation | galvaaninen erotus | |
| isolated (section, area) | erotettu | `erotettu alue`, `erotettu osa` |
| digital isolator | digitaalinen erotin | |
| isolation barrier | erotusraja | |
| ground loop | maasilmukka | |
| analog-to-digital converter (ADC) | AD-muunnin | The abbreviation `ADS1115` stays |
| resolution (16-bit) | erotuskyky | `16-bittinen erotuskyky` |
| sampling rate | näytteenottotaajuus | |
| low-pass filter | alipäästösuodin | |
| cutoff frequency | rajataajuus | |
| noise (electrical) | häiriö | Not *melu*, which is sound |
| noise immunity | häiriönsieto | |
| voltage divider | jännitteenjakaja | |
| constant current source (CCS) | vakiovirtalähde | The header label `CCS` stays as printed |
| excitation voltage | herätejännite | |
| passive voltage measurement | passiivinen jännitemittaus | |
| active resistance measurement | aktiivinen vastusmittaus | |
| pull-up resistor | ylösvetovastus | |
| pull-down resistor | alasvetovastus | |
| threshold voltage | kynnysjännite | |
| hysteresis | hystereesi | |
| floating (input) | kelluva | `tulo jää kelluvaksi` |
| normally open / normally closed | sulkeutuva / avautuva | SFS/IEC contact terms, and easy to get backwards: a *sulkeutuva* contact is open at rest and **closes** when actuated, which is what *normally open* means. Swedish `slutande`/`brytande` and German `Schließer`/`Öffner` line up the same way. |
| self-resetting fuse | itsestään palautuva sulake | |
| reverse polarity protection | napaisuussuojaus | |
| overvoltage protection | ylijännitesuojaus | |
| switching power supply | hakkuriteholähde | |
| power supply | teholähde | **A deliberate divergence from HALPI2, which uses `virtalähde`. Do not harmonise.** On HALMET the two collide: `vakiovirtalähde` is the constant current source, an entirely different component described on the same page, and `virtalähde` is a substring of it — so a reader meets what looks like one component with a modifier. `teholähde` is also the base of `hakkuriteholähde`, which this glossary already prescribes. |
| current consumption | virrankulutus | |
| short circuit | oikosulku | |
| chafing (of a wire) | hankautuminen | |

### Board features and assembly

| English | Finnish | Note |
|:--------|:--------|:-----|
| jumper | hyppy | `hyppy` on a pin pair; see *solder jumper* for the PCB kind |
| jumper header | hyppyliitin | The pin pair a jumper is placed on |
| solder jumper | juotossilta | Closed with solder, not with a removable jumper — the distinction matters because the reader needs a soldering iron for one and not the other |
| to short (a jumper) | oikosulkea | `oikosulje nastat` |
| pad (solder pad) | juotospiste | |
| unpopulated | kalustamaton | `kalustamattomat juotospisteet` |
| pitch (2.54 mm) | nastaväli | `2,54 mm:n nastaväli` |
| pluggable terminal block | irrotettava riviliitin | Phoenix MC type; `riviliitin` alone is the shared HALPI2 term |
| silkscreen | silkkipaino | |
| to solder | juottaa | |
| soldering iron | juotin | |
| grommet | läpivientikumi | Rubber or silicone; distinct from `läpivientiholkki`, the threaded gland |
| step drill bit | porrasterä | The one that looks like a metal Christmas tree |
| conical drill bit | kartioterä | |
| panel connector | paneeliliitin | |
| reset button | reset-painike | The board's own labels `Reset` and `Boot` stay in English |
| boot button | boot-painike | |
| bootloader | käynnistyslataaja | |
| download mode | lataustila | ESP32 flashing mode |
| user-programmable LED | käyttäjän ohjattava LED | |
| open hardware | avoin laitteisto | |

### A note on `liitin`

The shared glossary renders both `connector` and `header` as `liitin`, and that
is kept. HALMET puts the two side by side more often than HALPI2 does — *1-Wire
header connector*, *analog input connectors* — so let the qualifier carry the
distinction (`1-Wire-liitin`, `analogiatulojen liittimet`) rather than inventing
a second word. Where a sentence would otherwise be ambiguous, say what the thing
is: `piirilevyn nastarima` for a bare pin strip, `kaapeliliitin` for the plug.

## SH-ESP32 terms

SH-ESP32 is a marine ESP32 development board, so it inherits HALMET's sensor
vocabulary and adds what HALMET has no need for: an OLED display, a WiFi
gateway, NMEA 2000 bus topology, and the enclosure work of a tutorial written in
the first person. Rows above this heading are shared with HALMET and should not
be changed here alone.

### The board and the enclosure

| English | Finnish | Note |
|:--------|:--------|:-----|
| development board | kehityskortti | Shared with HALMET |
| Engine Top Hat | Engine Top Hat | Product name, never translated; `Engine Hat` is the short form the source also uses |
| OLED display | OLED-näyttö | |
| enclosure lid | kotelon kansi | |
| drill template | porausmalline | |
| panel connector | paneeliliitin | Shared with HALMET |
| M12 panel connector | M12-paneeliliitin | The NMEA 2000 connector |
| Micro USB panel connector | Micro USB -paneeliliitin | Multi-word name takes the space before the hyphen |
| grommet | läpivientikumi | Distinct from `läpivientiholkki`, the threaded gland |
| standoff | välike | Shared with SH-RPi and HALPI2 |

### Wiring and assembly

| English | Finnish | Note |
|:--------|:--------|:-----|
| splice | jatkos | The joint itself |
| to splice | jatkaa | |
| rat-tail splice | kierrejatkos | The twisted joint the tutorial shows |
| wire link | johdinsilta | |
| pigtail | johtimen jatke | A short lead already fitted to a connector; never a loanword |
| to crimp | krimpata | Shared |
| heat-shrink tubing | kutistesukka | Shared |
| tinning (a wire) | tinaus | |

### Bus and network

| English | Finnish | Note |
|:--------|:--------|:-----|
| gateway | yhdyskäytävä | `NMEA 2000 -USB-yhdyskäytävä` |
| bus topology | väylätopologia | |
| backbone | runkokaapeli | The NMEA 2000 trunk; shared with HALPI2 |
| drop cable | haarakaapeli | Shared |
| T-connector | T-liitin | Shared |
| terminator / termination resistor | päätevastus | Shared |
| device list | laiteluettelo | The MFD's list of bus devices |
| PGN | PGN | Never translated |
| data browser | datan selain | Signal K's view |
| data connection | datayhteys | |

### Measurement and sensors

| English | Finnish | Note |
|:--------|:--------|:-----|
| temperature probe | lämpötila-anturi | |
| coolant temperature | jäähdytysnesteen lämpötila | |
| exhaust temperature | pakokaasun lämpötila | |
| oil pressure | öljynpaine | |
| engine gauge | moottorimittari | HALMET's `gauge` → `mittari` with the qualifier |
| sender | anturi | Shared with HALMET; not *lähetin* |
| resistive sender | vastusanturi | Shared |
| constant current source | vakiovirtalähde | Shared with HALMET, and the reason `power supply` is `teholähde` here |

### Software and tooling

| English | Finnish | Note |
|:--------|:--------|:-----|
| Signal K server | Signal K -server | Multi-word product name: space before the hyphen |
| PlatformIO | PlatformIO | Never translated; compounds directly — `PlatformIO-projekti` |
| to build (firmware) | kääntää | Not *rakentaa* for compilation |
| to upload (firmware) | siirtää | The step after building |
| serial monitor | sarjaporttimonitori | |
| access request | käyttöoikeuspyyntö | Signal K's device authorisation |
| dashboard | instrumenttipaneeli | Shared |

### A note on the first-person tutorials

Two tutorials are written in the first person — *I prepared*, *my preference*.
Finnish technical writing normally avoids this, but rewriting them into the
passive would change the register the author chose. Keep the first person where
the English has it (`valmistelin`, `oma tapani`) and the imperative where the
English instructs (`poraa`, `juota`). Do not mix the two inside one step.

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes — the same command CI runs.
2. `uv run mkdocs serve` shows the page rendering correctly in the browser, with
   lists as lists (see `../best-practices/markdown-lists-need-blank-line-2026-05-16.md`
   — the blank-line rule applies identically to Finnish pages).
3. Every term used on the page that appears in this glossary matches it.

## Related

- `solutions/best-practices/markdown-lists-need-blank-line-2026-05-16.md`
- mkdocs-static-i18n documentation: https://ultrabug.github.io/mkdocs-static-i18n/
