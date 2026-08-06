---
translated_from: 2409b481ada0cca8731f54bcc0dc22fb28d05756
---

# SH-ESP32 Engine Top Hat

![SH-ESP32 Engine Top Hatin renderöinti](assets/EH_perspective.jpg "SH-ESP32 Engine Top Hatin renderöinti")

SH-ESP32 Engine Top Hat (Engine Hat) on SH-ESP32:n lisäkortti.
Sillä voi mitata tavallisimpia moottorin lähtöjä:

- Kierroslukuanturit (RPM), joko varsinaisilla kierroslukuantureilla tai laturin W-navasta
- Digitaalitulot, kuten moottorihälytykset
- Tankkianturit
- Muut vastusanturit, kuten öljynpaineanturit, joiden vastusalue on 0–300 ohmia

Engine Hat on kehittäjälaite.
Vaikka esimerkkiohjelmisto on saatavilla verkossa, Engine Hatin käyttö edellyttää perustuntemusta antureiden ja mikro-ohjainten kanssa työskentelystä.

Laitteiston asennus- ja kytkentäohjeet löytyvät [Aloitusopas](getting-started/index.md) -sivulta.

[Laitteisto](hardware/index.md) -sivulla on tarkempaa tietoa Engine Hatin laitteistosta.

SH-ESP32 Engine Top Hat on avointa laitteistoa, ja suunnittelutiedostot löytyvät [projektin GitHub-repositoriosta](https://github.com/hatlabs/SH-ESP32-engine-hat). Tuotetta myydään osoitteessa [hatlabs.fi](https://hatlabs.fi/product/sh-esp32-engine-top-hat-kit/).

## Tekniset tiedot

- Yhteensopiva SH-ESP32:n kanssa (kaikki versiot)
- 4 digitaalitulokanavaa (1–4)
  - tulojännitealue: -30 V…+30 V
  - kynnysjännite: 1,65 V
  - valinnainen ensimmäisen asteen alipäästösuodin, rajataajuus 2,3 kHz
- 4 analogiatulokanavaa (A–D)
  - tulojännitealue: 0–29 V
  - AD-muunnin: AD1115
  - AD-muuntimen erotuskyky: 16 bittiä
  - valinnainen vakiovirtalähde, virta 10 mA
  - vastusmittausalue: 0–300 ohmia
