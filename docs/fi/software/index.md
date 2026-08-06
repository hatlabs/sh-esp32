# Ohjelmisto

## Johdanto

SH-ESP32:n ohjelmointiin on tarjolla runsaasti kieliä ja kehitysympäristöjä. Jos et tiedä mistä aloittaa, suositeltavat valinnat ovat Visual Studio Code, PlatformIO ja SensESP — mutta tarpeistasi ja mieltymyksistäsi riippuen voit halutessasi kokeilla muitakin vaihtoehtoja.

## SDK:t

ESP32-ympäristöön on saatavilla useita ohjelmistokehityspaketteja (SDK). Ne kaikki ovat yhteensopivia SH-ESP32:n kanssa.

[Espressif SDK](https://www.espressif.com/en/products/software/esp-sdk/overview) on virallinen C++-ohjelmointiympäristö.
Sen rajapinta on C-tyylinen eikä nojaa luokkiin tai olioihin.
Se tuo myös FreeRTOS-reaaliaikakäyttöjärjestelmän suoraan käyttöön.
Virallisena kehitysympäristönä Espressif SDK tarjoaa kattavimman pääsyn ESP32:n toiminnallisuuteen.

Espressif SDK käyttää CMakea käännösjärjestelmänään.

[Arduino Core for ESP32](https://github.com/espressif/arduino-esp32) on ESP32:n Arduino-SDK.
Sitäkin ylläpitää Espressif, ja Arduino-ekosysteemin laajuuden ja siihen liittyvän dokumentaation ansiosta se on todennäköisesti ESP32:n eniten käytetty SDK.

Arduino Corea voi käyttää joko [Arduino IDE](https://www.arduino.cc/en/software):n tai [PlatformIO](https://platformio.org/):n kanssa.

Arduino IDE on aloittelijaystävällinen ohjelmistokehitysympäristö, joka kehitettiin alun perin Arduino-merkkisille harrastajakorteille.
Sen aloittaminen on hyvin helppoa, mutta editori soveltuu huonosti vakavampaan ohjelmistokehitykseen, ja siinä on lisäksi luontaisia rajoituksia kirjastojen ja ympäristön hallinnassa.
Se käyttää myös omaa käännösjärjestelmäänsä ja projektirakennettaan, jotka eivät ole yhteensopivia muiden järjestelmien kanssa.
Se on hyvä valinta hyvin yksinkertaisiin yhden käyttötarkoituksen ohjelmiin, mutta monimutkaisempiin projekteihin tai vaikkapa Signal K:hon tai muuhun palvelinprotokollaan integroitaessa kannattaa katsoa pidemmälle.

PlatformIO on eri mikro-ohjaimille tarkoitettu alustariippumaton kehitysympäristö.
Sitä voi käyttää pelkältä komentoriviltä, mutta se integroituu hyvin myös Visual Studio Codeen, joka on erinomainen monikielinen koodieditori ja kehitysympäristö. PlatformIO hoitaa kirjastojen hallinnan ja riippuvuuksien selvittämisen, ja se tukee myös laitteistopohjaisia virheenjäljittimiä ja paljon muuta.

Jos haluat kehittää SH-ESP32:ta korkeamman tason kielillä, [MicroPython](https://micropython.org/) on hyvä valinta.
Se on hyvin yhteensopiva tavallisen Pythonin kanssa ja toimii FreeRTOS:n päällä. Monille ESP32:n alijärjestelmille ja oheislaitteille on valmiita moduuleja.

[NodeMCU](https://nodemcu.readthedocs.io/en/dev-esp32/) on vielä yksi ESP32:lle saatavilla oleva SDK. NodeMCU perustuu luaan, joka on kevyt ohjelmointikieli ja suunniteltu ensisijaisesti sulautettuun käyttöön sovellusten sisällä. NodeMCU oli aiemmin suosittu ESP8266-kehityksessä, mutta suositummat ohjelmointiympäristöt ovat sittemmin ohittaneet sen.

[Rust](https://github.com/MabezDev/rust-xtensa) on niin ikään yksi ohjelmointikielivaihtoehto Espressifin mikro-ohjaimille.
Rust on moderni kieli, jossa on erinomaiset ominaisuudet järjestelmäohjelmointiin, mutta ESP32-tuki on yhä voimakkaassa kehitysvaiheessa ja dokumentaatio puutteellista.

## Sovelluskehykset

Kun aloitat C- tai C++-sovelluksen kehittämisen Signal K:hon tai NMEA 2000:een integroitumista varten, kannattaa yleensä ottaa lähtökohdaksi jokin olemassa oleva kirjasto tai kehys.
Tällä hetkellä (maaliskuu 2021) kaksi ensisijaista vaihtoehtoa ovat [SensESP](https://github.com/SignalK/SensESP) ja [ESPHome](https://esphome.io).
SensESP, jota kuvataan alla olevassa alaosiossa, on joukko kirjastoja, jotka on suunniteltu anturilaitteiden helppoon integrointiin Signal K -järjestelmään — mutta siinä on paljon ominaisuuksia myös yleiseen sulautettuun kehitykseen.
ESPHome on järjestelmä, jolla ESP-laitteita ohjataan yksinkertaisilla asetustiedostoilla, ja se integroituu hyvin useisiin kodin automaatioalustoihin.

### SensESP

[SensESP](https://github.com/SignalK/SensESP) on ESP8266:lle ja ESP32:lle tarkoitettu anturikehitysalusta, jota voi käyttää korkean tason työkalupakkina Signal K -serverien kanssa keskustelevien laitteiden rakentamiseen.
Se on helppo integroida NMEA 2000 -verkkoihin, ja siinä on paljon hyödyllisiä ominaisuuksia asynkroniseen sulautettuun ohjelmointiin, kuten tuottaja–kuluttaja-mallin laaja käyttö sekä korkean tason käsitteet Sensors, Translations ja Consumers (Outputs).

## Lisäkortit

SH-ESP32:lle on saatavilla ja kehitteillä useita lisäkortteja.

Proto Board Top HAT on SH-ESP32:n kokoinen lisäkortti, joka kiinnittyy sen päälle ja tarjoaa runsaasti tilaa käyttäjän omille muutoksille.
Sitä myydään [Hat Labsin verkkokaupassa](https://hatlabs.fi/product/sh-esp32-protoboard-tophat/).
Suunnittelutiedostot löytyvät [SH-ESP32:n laitteistorepositoriosta](https://github.com/hatlabs/SH-ESP32-hardware/tree/main/SH-ESP-HAT-Proto).

Useita muita HAT-kortteja on kehitteillä, kuten digitaaliseen kytkentään tarkoitettu [PowerFET HAT](https://github.com/markfarnan/yacht_hardware/tree/main/SH-ESP32-PowerFET) ja [Ethernet HAT](https://github.com/markfarnan/SH-ESP32-Ethernet).

Jos haluat kehittää oman SH-ESP32-HAT-kortin, [tyhjä HAT-pohja](https://github.com/hatlabs/SH-ESP32-hardware/tree/main/SH-ESP-HAT-Blank) on saatavilla SH-ESP32:n repositoriossa.
