---
translated_from: ef463bd6ca037c4126307af6751896845f3d4f41
---

# SH-ESP32 Engine Top Hatin laitteisto

## Analogiatulot

Engine Hatissa on neljä analogiatulokanavaa, jotka on toteutettu Texas Instrumentsin ADS1115-analogia-digitaalimuuntimella.
Analogiatulot voi määrittää yksitellen joko passiivisiksi jännitemittausantureiksi tai aktiivisiksi vastusantureiksi.
Jännitemittausantureina tulokanavat havaitsevat 0–29 V:n jännitealueen 16-bittisellä tarkkuudella.
Vastusantureina ne käyttävät 10 mA:n vakiovirtalähdettä 0–300 ohmin anturivastusten lukemiseen.

## Digitaalitulot

Engine Hatissa on neljä laajan jännitealueen digitaalituloa.
Tulot tukevat 0–30 V:n tulojännitealuetta.
Kynnysjännite on kiinteä, noin 1,65 V.

Digitaalituloja voi käyttää joko digitaalisten arvojen tuloina moottorihälytysten ja muiden vastaavien signaalien havaitsemiseen tai laskureina kierroslukusignaalien ja muiden toistuvien pulssien mittaamiseen.

Jokaisessa digitaalitulokanavassa on valinnainen, hypyllä käyttöön otettava alipäästösuodin, jonka rajataajuus on 2,3 kHz.
Alipäästösuotimella voi suodattaa häiriöisiä kierroslukusignaaleja, erityisesti laturin W-navan signaaleja.

## Kierros kortilla

Alla oleva kuva esittää Engine Hatin kaksi päätoimintolohkoa.

![Engine Hatin toimintolohkot](assets/EH_Layout_functional.jpg "Engine Hatin toimintolohkot"){ width="50%" }

Lohko 1 toteuttaa digitaalitulojen toiminnallisuuden hälytystuloja ja taajuuslaskentaa varten.

Lohko 2 toteuttaa neljä analogiatulokanavaa, niiden tulosuojauksen ja valinnaisen vakiovirtalähteen.

## Liittimet

Engine Hatin liittimet näkyvät alla.

![Engine Hatin liittimet](assets/EH_Layout_connectors.jpg "Engine Hatin liittimet"){ width="50%" }

1. Neljän digitaalitulon pinottava vaakaliitin.
   Ylärivi on digitaalitulon signaalinastoille, alarivi maadoituskytkennöille.
2. Hyppyliitin alipäästösuotimen käyttöönottoon kullekin tulokanavalle.
3. Neljän analogiatulokanavan pinottava vaakaliitin.
   Ylärivi on analogiatulon signaalinastoille, alarivi maadoituskytkennöille.
4. Hyppyliitin vakiovirtalähteen käyttöönottoon kullekin analogiatulokanavalle.
5. I2C-läpivientinaarasliitin näyttömoduulin tai muiden I2C-laitteiden kytkemiseen.
6. I2C-urosliitin pääkorttiin kytkemistä varten (piirilevyn alapuolella).
7. GPIO-naarasliitin digitaalitulojen kytkemiseen pääkorttiin (alapuolella).

## Nastajärjestys

Alla olevat osiot kuvaavat, miten tulot on kytketty ESP32:n GPIO-nastoihin.

### Digitaalitulot

| Tulo # | ESP32:n GPIO |
| -----: | -----------: |
| 1      | 15           |
| 2      | 13           |
| 3      | 14           |
| 4      | 12           |

### Analogiatulot

Analogiatulot luetaan ADS1115-analogia-digitaalimuuntimella.

Raaka tulosignaali skaalataan jännitteenjakajalla ADC:n hyväksymille jännitetasoille. Skaalauskerroin on 2,048/29.

ADS1115 käyttää I2C-väylää ESP32:n kanssa viestimiseen.
I2C-oletusosoite on 0x4b, mutta sen voi vaihtaa piirilevyn alapuolella olevilla juotossilloilla.

Huomaa, että SH-ESP32 käyttää GPIO 16:ta I2C:n SDA-linjalle ja GPIO 17:ää I2C:n SCL-linjalle. Nämä arvot poikkeavat Arduinon ESP32-kehyksen oletuksista, ja mahdollinen yleinen esimerkkikoodi on muutettava vastaavasti.

## Suunnittelutiedostot ja kytkentäkaaviot

SH-ESP32 Engine Top Hatin suunnittelutiedostot löytyvät [projektin GitHub-repositoriosta](https://github.com/hatlabs/SH-ESP32-engine-hat).

Eri laitteistoversioiden kytkentäkaaviot löytyvät täältä:

- [SH-ESP32 Engine Top Hat v1.0.0](assets/Engine_Hat_Schematics_v1.0.0.pdf)
