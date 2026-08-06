---
translated_from: 871be0004eacb37c55a0e5bfbf665ef8957e08f5
---

# Laitteiston kuvaus

*Huomaa: Alla olevat kuvat esittävät Revision 1 -korttia. Rev. 2 -kortit ovat toiminnallisesti samanlaisia, mutta niissä on eri jännite- ja CAN-liittimet sekä pieniä komponenttimuutoksia.*

## Kierros kortilla

SH-ESP32:n eri toimintolohkot näkyvät alla.

<figure markdown="span">
![Toimintolohkot](assets/sh-esp32_r0.3.1_top_func_annotated.jpg "SH-ESP32:n toimintolohkot")
<figcaption>SH-ESP32:n toimintolohkot.</figcaption>
</figure>

1. **ESP32-WROOM-32-moduuli**:
   ESP32-mikro-ohjainmoduuli on laitteen sydän.
   Se sisältää kaksiytimisen mikro-ohjaimen integroituine RAM-muisteineen, flash-piirin sekä WiFi/Bluetooth-antennin (tai SH-ESP32-ufl:n tapauksessa U.FL-liittimen antennia varten).

2. **Teholähde**:
   SH-ESP32:ssa on integroitu hakkuriteholähde, joka muuntaa 8 V:n ja 32 V:n väliset tulojännitteet kortilla käytettäväksi 3,3 V:n jännitteeksi.
   Teholähteeseen sisältyy myös itsestään palautuva 500 mA:n sulake, napaisuussuojaus ja ylijännitesuojaus.

3. **CAN-väylän lähetinvastaanotin**:
   SH-ESP32:ssa on erotettu CAN-lähetinvastaanotin, joka noudattaa NMEA 2000 -määrittelyä.
   CAN-väyläpiiristöön kuuluu myös päälähteen kaltainen suojaus sekä 5 V:n lineaarisäädin, joka syöttää lähetinvastaanottimen tehon NMEA 2000 -väylästä kortin omasta teholähteestä riippumatta.

4. **Optoerottimen tulo ja lähtö**:
   Optoerotintuloilla ja -lähdöillä SH-ESP32:n voi kytkeä turvallisesti häiriöisiin ulkoisiin tuloihin tai lähtöihin, kuten laturin signaaliin tai releisiin.

5. **I2C- ja 1-Wire-liitännät**:
   SH-ESP32 tukee 1-Wireä ja I2C:tä erillisissä 2,54 mm:n liittimissä.
   Lisäksi kortilla on kalustamaton juotoskuvio Qwiic-yhteensopivalle JST SH -liittimelle.
   Molemmat liitännät on suojattu sähköstaattisilta purkauksilta, ja niissä on häiriönsuodatus.

6. **USB-liitäntä**:
   SH-ESP32:ssa on USB 2.0 -yhteensopiva Micro B -liitin ja -liitäntä.
   Isäntätietokoneeseen kytkettynä kortti näkyy USB-sarjaporttilaitteena.
   USB-liitäntää voi käyttää kortin virransyöttöön, ESP32-moduulin flashaamiseen ja laitteen kanssa viestimiseen sarjaporttiprotokollalla.

7. **Käyttöliittymä**:
   Kortille on integroitu kaksi painiketta ja kaksi LEDiä.
   Reset-painike palauttaa kortin alkutilaan.
   Boot-painikkeella ESP32:n voi pakottaa flashaustilaan, ja muutoin sitä voi käyttää yleiskäyttöisenä painiketulona GPIO0:ssa.
   Punainen LED on kytketty kiinteästi 3,3 V:n jännitteeseen ja osoittaa, että laitteessa on jännite, kun taas sininen LED on kytketty GPIO2:een ja on ohjelmallisesti ohjattavissa.

## Liittimet

Alla oleva kuva havainnollistaa SH-ESP32:n eri liittimiä.
Liittimet ovat seuraavat:

1. **Jänniteliitin**:
   JST XH -yhteensopiva virtaliitin.
   Samaan juotoskuvioon voi asentaa 2,5 mm:n riviliittimen.

2. **CAN-väyläliitin**:
   Nelinastainen JST XH -liitin, joka on suunniteltu kytkettäväksi kotelossa olevaan NMEA 2000 -yhteensopivaan DeviceNet M12 -liittimeen.

3. **Optoerottimen liitäntäliitin**:
   Optoerottimen tulo ja lähtö ovat käytettävissä tämän liitännän kautta. Näiden neljän nastan merkinnät ovat kortilla hieman "pohjoisessa": GND, Vext, IN ja OUT.

4. **1-Wire-liitin**:
   1-Wire-liitäntä, jossa on suojaus sähköstaattisia purkauksia vastaan, häiriönsuodatus sekä pidempien verkkojen vaatima alipäästösuodatus.
   1-Wire-laitteiden kytkemiseen SH-ESP32:een ei tarvita muuta piiristöä. 1-Wiren datatulon nasta (kortilla merkinnällä "DQ") on kytketty GPIO 4:ään, joten käytä ohjelmassasi GPIO 4:ää 1-Wiren tulonastana.

5. **I2C-liitin**:
   Nelinastainen liitin I2C-orjalaitteiden kytkemiseen SH-ESP32:een.
   Naarasliittimeen käyvät sellaisenaan monet suositut edulliset SSD1306-ohjainta käyttävät OLED-näyttömoduulit.

   2,54 mm:n liittimen vieressä on lisäksi kalustamaton Qwiic-yhteensopiva JST SH -juotoskuvio.

6. **USB**:
   Tavanomainen USB Micro B -liitin.

7. **Suojattu jännite**:
   Näillä juotospisteillä voi ottaa käyttöön tulojännitteen, joka on suojattu väärältä napaisuudelta ja ylijännitteeltä.
   Jos esimerkiksi syötät kortille noin 12 V, näiden pisteiden +-nasta tarjoaa noin 12 V.
   Huomioi napaisuus: se on päinvastainen kuin viereisessä jännitetuloliittimessä.

8. **Jännitesilta**:
   Jos aiot syöttää kortille tehon NMEA 2000 -liitännän kautta etkä tarvitse galvaanisia yhteyksiä ulkoisiin järjestelmiin, voit yhdistää nämä juotospisteet toisiinsa ja johtaa tehon CAN-väyläliittimestä pääteholähteelle.

9. **Prototyyppialue**:
   Tätä aluetta voi käyttää omiin muutoksiisi.

10. **Ylimääräinen jännitelähtö**:
    Näistä juotospisteistä saat ylimääräisen GND- ja 3,3 V:n jännitelähdön tarvitsemiisi muutoksiin.
    Huomaa, että silkkipainon antamasta vaikutelmasta huolimatta ylimmät kolme nastaa ovat kaikki GND ja alimmat kolme kaikki 3,3 V.

11. **GPIO-liitin**:
    GPIO-liitin tarjoaa kytkennät kaikkiin ESP32-moduulissa käytettävissä oleviin GPIO-nastoihin.
    Osa nastoista on oletuksena muiden oheislaitteiden käytössä, ja ne on otettava käyttöön
    juotossilloilla.

<figure markdown="span">
![Liittimet](assets/sh-esp32_r0.3.1_top_conx_annotated.jpg "SH-ESP32:n liittimet")
<figcaption>SH-ESP32:n liittimet.</figcaption>
</figure>

## ESP32-moduuli

ESP32 on sarja edullisia ja vähän virtaa kuluttavia mikro-ohjaimia ja mikro-ohjainmoduuleja, jotka on luonut ja kehittänyt shanghailainen kiinalainen yritys Espressif Systems.
ESP32-WROOM-32-moduuli rakentuu tehokkaan kaksiytimisen Tensilica Xtensa LX6 -mikroprosessorin ympärille, ja siinä on integroitu WiFi, kaksitoimintoinen Bluetooth ja huomattava määrä oheislaitteita.

SH-ESP32:ssa on ESP32-WROOM-32E-moduuli integroituine piirilevyantenneineen, kun taas SH-ESP32-ufl käyttää ESP32-WROOM-32U:ta, jossa on U.FL-liitin ulkoista antennia varten.

Lisätietoja saat [ESP32:n Wikipedia-artikkelista](https://en.wikipedia.org/wiki/ESP32), [Espressifin tuotesivuilta](https://www.espressif.com/en/products/modules/esp32) tai [moduulin datalehdestä](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf).

## Teholähde

SH-ESP32 on suunniteltu mahdollisimman helppokäyttöiseksi veneessä, ja siinä on 8–32 V:n hakkuriteholähde, jonka enimmäishyötysuhde on lähes 90 %. Teholähteen 3,3 V:n lähdössä on riittävä virranantokyky sekä ESP32:n huippukulutukselle että kohtuullisille lisäkorteille.

Teholähteeseen kuuluu itsestään palautuva 500 mA:n sulake, napaisuussuojaus ja järeä TVS-suojadiodi, jonka läpilyöntijännite on 36,7–40,6 V ja suurin pulssitehon sietokyky yli 600 W.
Lisäksi teholähteessä on EMC-suodatus, joka on suunniteltu pitämään hakkuriteholähteen johtuvat päästöt säädösrajojen alapuolella.

Hakkuripiiri on Silergy SY8401, jonka tuloalue on laaja 4,5–60 V ja suurin lähtövirta 0,8 A.

## Oheislaitteet

### Painikkeet ja LEDit

SH-ESP32:ssa on kaksi painiketta ja kaksi LEDiä. Painikkeet on merkitty Reset ja Boot. Reset-painike palauttaa kortin alkutilaan vetämällä ESP32:n Enable-nastan alas.
Boot-painike on kytketty GPIO0:aan, ja sillä voi laitteen käynnistyksen aikana pakottaa moduulin lataustilaan. Muutoin sitä voi käyttää tavallisena painiketulona.

Kahta LEDiä ei ole erikseen merkitty.
Punainen LED palaa aina, kun kortilla on 3,3 V:n jännite.
Sininen LED on kytketty GPIO2:een (nasta, jota ESP32-kehityskorteissa yleisesti käytetään LEDille).
Käyttäjän ohjelmat voivat ohjata sitä osoittamaan laitteen tilaa.

### USB

USB-liitännällä voi ohjelmoida ESP32-moduulin uudelleen ja viestiä käyttäjän sovelluksen kanssa. Kytkettynä se myös syöttää kortille tehon. Korttia voi turvallisesti syöttää samanaikaisesti sekä päävirtaliittimestä että USB:stä — tasasuuntausdiodit varmistavat, että käytössä on vain suurijännitteisin syöttö.

USB-liitäntä on toteutettu edullisella CH340C USB–sarjaporttimuunninpiirillä.
Se emuloi tavanomaista sarjaporttiliitäntää jopa 2 Mbit/s:n siirtonopeuksilla.

Linux-ytimet tukevat CH340-piirejä natiivisti, mutta Macissa ja Windowsissa tarvitaan ajuri.
Ajurin voi ladata [valmistajan sivustolta](http://www.wch-ic.com/downloads/CH341SER_ZIP.html).

### CAN-väylä (NMEA 2000)

NMEA 2000 on kaikkialla käytetty tiedonsiirtostandardi, jolla kytketään anturi-, ohjaus- ja näyttölaitteita veneissä ja laivoissa.
Se perustuu CAN-väylään (Controller Area Network), joka on ajoneuvoväylästandardi ja suunniteltu mahdollistamaan laitteiden keskinäinen viestintä ilman isäntätietokonetta.

SH-ESP32:ssa on erotettu CAN-väyläliitäntä, joka mahdollistaa laitteiden turvallisen ja NMEA 2000 -yhteensopivan kytkennän.
CAN-väyläliitännällä voi lähettää anturilukemat suoraan NMEA 2000 -verkkoon tai rakentaa NMEA 2000 -yhdyskäytäviä tai vastaavia laitteita.

CAN-liitäntä käyttää ESP32:n integroitua CAN-ohjainta ja Texas Instrumentsin erotettua ISO1050DUB-CAN-lähetinvastaanotinta. Se tukee suuria erotusjännitteitä ja transientteja sekä jopa 1 Mbit/s:n siirtonopeuksia.

CAN-väyläliitännällä voi myös syöttää tehon koko laitteelle, jos galvaanisia yhteyksiä muihin ulkoisiin järjestelmiin ei ole. (FIXME: Vaatii perusteellisemman kuvauksen ja havainnekuvan.)

CAN-liitännässä on sisäänrakennettu päätevastus, jonka voi ottaa käyttöön sulkemalla kortin alapuolella olevan "CAN term" -juotossillan.

### I2C

I2C (Inter-Integrated Circuit) on hyvin suosittu synkroninen sarjaliikenneväylä, jota käytetään yleisesti liitäntöihin monien eri mikropiirien kanssa.
Se käyttää jännitteen ja maan lisäksi kahta datajohdinta.

I2C:llä voi kytkeä SH-ESP32:een suuren määrän laitteita.
Laitetyyppejä ovat esimerkiksi AD-muuntimet, asentoanturit, lämpötila- ja kosteusanturit, näytöt, näppäimistöt ja GPS.
Mitä tahansa SparkFunin Qwiic-yhteensopivaa korttia voi käyttää SH-ESP32:n kanssa jatkamalla johtimet tai lisäämällä JST SH -yhteensopivan liittimen vapaaseen juotoskuvioon.

I2C-väylän enimmäisetäisyydet riippuvat kuormasta, mutta niiden tulisi olla alle 3–4 m. Pitkän matkan tiedonsiirtoon on paremmin soveltuvia protokollia.

### 1-Wire

1-Wire on Dallas Semiconductorin suunnittelema laitteiden tiedonsiirtoväyläjärjestelmä; yritys on sittemmin siirtynyt Maxim Integrated Productsille.
Vaikka 1-Wire on hidas protokolla ja tukee vain enintään 16,3 kbit/s:n nopeuksia, se on hyvin yksinkertainen toteuttaa ja käytettävissä pitkillä etäisyyksillä.
Sitä käytetään yleisesti lämpötila-antureissa ja vastaavissa yksinkertaisissa mittalaitteissa.

SH-ESP32:n 1-Wire-toteutuksessa on suojaus sähköstaattisia purkauksia ja radiotaajuista häiriötä vastaan sekä alipäästösuodatus verkon luotettavuuden parantamiseksi.

Huomaa, että 1-Wiren datanasta (merkinnällä "DQ") on fyysisesti kytketty GPIO4:ään, joten käytä ohjelmassasi GPIO4:ää kaikelle 1-Wire-datalle.

### Optoerottimen tulo ja lähtö

Optoerottimen tulo ja lähtö on suositeltu tapa lisätä yksinkertaista digitaalisen signaalin tuloa, lähtöä ja havainnointia eri ulkoisiin järjestelmiin.
Sitä voi käyttää esimerkiksi laturin pulssien laskemiseen kierroslukumittausta varten tai releiden kytkemiseen päälle ja pois.

Lisäksi SH-ESP32:n optoerotinliitännän pitäisi kyetä ohjaamaan hitaita yksisuuntaisia NMEA 0183 -liitäntöjä.

Optoerottimen tulon suurin sallittu jännite on 18 V, mutta sitä voi kasvattaa lisäämällä tuloon sarjaan virtaa rajoittavan vastuksen.

Jos syötät ISO IN -nastaan noin 2,5 V:n ja 18 V:n välisen jännitteen, tulo-optoerottimen lähtö vedetään ylös, eli OPTO_IN (GPIO 35) vedetään ylös.

Vastaavasti jos vedät OPTO_OUT-nastan (GPIO 33) ylös, ISO_OUT-nasta ohjautuu siihen jännitteeseen, jonka olet syöttänyt Vext-nastaan.

Optoerottimen lähdöllä voi ohjata pieniä ajoneuvoreleitä. Siinä tapauksessa releen käämin nastat kytketään Vext- ja OUT-nastoihin.

### GPIO-liitin

GPIO-liittimen kautta pääsee käsiksi kaikkiin ESP32-moduulin GPIO-nastoihin.
Liittimen viereiset silkkipainomerkinnät viittaavat nastojen GPIO-numeroihin.

![GPIO-liitin](assets/sh-esp32_r0.3.1_gpio.jpg "SH-ESP32:n GPIO-liittimen merkinnät")

Ympyröidyt numerot ovat oletuksena muiden oheislaitteiden käytössä, ja ne on kytkettävä juotossiltoja asettamalla (katso lisätietoja osiosta "[GPIO-määritysten mukauttaminen](#gpio-maaritysten-mukauttaminen)").

Suorakulmion sisään merkitty nastaryhmä, johon kuuluvat GPIO 16 ja 17, on käytettävissä toisena I2C-liittimenä, jos vastaavat juotossillat suljetaan.

Nastaryhmää GPIO 12–15 voi käyttää JTAG-liittimenä [yksinkertaisella ulkoisella laitteistolla ja ohjelmistolla](http://openocd.org/doc/html/Debug-Adapter-Hardware.html).
JTAG on mikro-ohjainten ja muiden ohjelmoitavien laitteiden alan vakiintunut virheenjäljitysliitäntä, joka mahdollistaa virheenjäljityksen suoraan piirillä: laitteistokeskeytyskohtien asettamisen, koodin askeltamisen ja muuttujien arvojen tarkastelun ajon aikana.

Lopuksi liittimen oikeassa päässä olevan 14 nastan ryhmä tulee Ethernet-lisäkortin käyttöön.

GPIO-liittimen nastoille ei ole tarjolla suojausta sähköstaattisia purkauksia tai radiotaajuista häiriötä vastaan eikä muuta suodatusta.

### Prototyyppialue

SH-ESP32:n keskellä oleva laaja avoin alue on prototyyppialue.
Sillä voi lisätä uutta toiminnallisuutta kolmannen osapuolen moduuleilla tai läpiladottavalla piiristöllä.
Sisempien kuparikerrosten täytöt ja vedot väistävät prototyyppialuetta tarkoituksella, ja aluetta voi tarvittaessa turvallisesti porata tai muokata suurempien komponenttien mahduttamiseksi.
Aivan alueen lähellä on kuitenkin vetoja, joten alueen reunalla olevia juotospisteitä muokatessa kannattaa olla varovainen.

<figure markdown="span">
![Prototyyppialue](assets/sh-esp32_r0.3.1_top_proto_area.jpg "SH-ESP32:n prototyyppialue")
<figcaption>SH-ESP32:n prototyyppialue.</figcaption>
</figure>

Vasemmalla puolella olevat pyöreät juotospisteet, jotka on merkitty 1–7, on kytketty vaakasuunnassa toisiinsa. Toisin sanoen merkinnän "1" vasemmalla puolella oleva pyöreä juotospiste
on kytketty merkinnän "1" oikealla puolella olevaan pyöreään juotospisteeseen, ja sama pätee merkintöihin 2–7. Näin liittimen sijoittaminen piirilevyn reunaan on helpompaa.
Voit sijoittaa liittimen reunimmaiselle riville ja tehdä kytkennät sisempään pyöreiden juotospisteiden riviin.

## Oheislaitteiden nastajärjestykset

ESP32:ssa on GPIO-matriisi, joka sallii useimpien digitaalisten GPIO-toimintojen vapaan kytkemisen mihin tahansa GPIO-nastaan.
Tätä hyödynnetään SH-ESP32:ssa laajasti, ja harva oheislaite on kytketty vakionastoihinsa.
Eri oheislaitteiden GPIO-nastajärjestys on esitetty alla. Luettelemattomat nastat eivät ole SH-ESP32:n käytössä, ja niitä voi käyttää vapaasti.

Ne GPIO-nastat, joilla on merkintä Silta-sarakkeessa, on oletuksena kytketty vastaavaan oheislaitteeseen ja irrotettu GPIO-liittimestä.
Näitä kytkentöjä voi muuttaa muokkaamalla siltoja osiossa "[GPIO-määritysten mukauttaminen](#gpio-maaritysten-mukauttaminen)" kuvatulla tavalla.
Esimerkiksi GPIO4 on ympyröity kortilla, ja alla olevassa taulukossa Silta-sarakkeessa on "X" ja Toiminto-sarakkeessa "1-Wire-data". Tämä tarkoittaa, että ellet tee juotostyötä, numerolla 4 merkitty nasta ei ole kytketty mihinkään, koska
1-Wiren datanasta ("DQ") on oletuksena kytketty GPIO4:ään.

ADC-sarake luettelee nastat, jotka on kytketty jompaankumpaan ESP32:n kahdesta AD-muuntimesta.
ADC2 on WiFin käytössä, joten jos WiFi on käytössä, ADC2:ta ei voi käyttää.

Merkintä Touch *N* viittaa kapasitiivisen kosketusanturin tuloihin.

| GPIO #  | Silta | ADC | Toiminto | Valinnainen toiminto |
| ------: | :---: | --: | -------- | -------------------- |
| 00      |        | 2   | BOOT | Ethernet REF_CLK; Touch 1 |
| 01      | x      |     | Sarjaportti TXD0 |  |
| 02      |        | 2   | Sininen LED | Touch 2 |
| 03      | x      |     | Sarjaportti RXD0 |  |
| 04      | x      | 2   | 1-Wire-data | Touch 0 |
| 05      |        |     | Vapaa | Ethernet Reset_N  |
| 12      |        | 2   | Vapaa | JTAG TDI; Touch 5 |
| 13      |        |     | Vapaa | JTAG TCK; Touch 4 |
| 14      |        | 2   | Vapaa | JTAG TMS; Touch 6 |
| 15      |        | 2   | Vapaa | JTAG TDO; Touch 3 |
| 16      | x      |     | I2C SDA |  |
| 17      | x      |     | I2C SCL |  |
| 18      |        |     | Vapaa | Ethernet MDIO |
| 19      |        |     | Vapaa | Ethernet TXD[0] |
| 21      |        |     | Vapaa | Ethernet TX_EN |
| 22      |        |     | Vapaa | Ethernet TXD[1] |
| 23      |        |     | Vapaa | Ethernet MDC |
| 25      |        | 2   | Vapaa | Ethernet RXD[0] |
| 26      |        | 2   | Vapaa | Ethernet RXD[1] |
| 27      |        | 2   | Vapaa | Ethernet CRS_DV; Touch 7 |
| 32      | x      | 1   | CAN TX | Touch 9 |
| 33      | x      | 1   | Opto OUT | Touch 8 |
| 34      | x      | 1   | CAN RX, vain tulo |  |
| 35      | x      | 1   | Opto IN, vain tulo |  |
| 36 (VP) |        | 1   | Vapaa, vain tulo |  |
| 39 (VN) |        | 1   | Vapaa, vain tulo |  |

[Tämä sivu](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) kuvaa erinomaisesti ESP32:n eri GPIO-nastoja ja niiden käytettävyyttä.

### GPIO-määritysten mukauttaminen

Lähes kaikki kiinteästi kytketyt oheislaitteet voi irrottaa juottamalla irti 0R-vastussillan kortin yläpuolelta.
Vastaavasti kortin alapuolella olevat juotossillat voi sulkea, jolloin GPIO-nasta kytkeytyy vastaavaan GPIO-liittimen nastaan.
Vastus- ja juotossillat on esitetty alla olevissa kuvissa.

<figure markdown="span">
![Sillat, yläpuoli](assets/sh-esp32_r0.3.1_top_jumpers_annotated.jpg "SH-ESP32:n sillat yläpuolella")
<figcaption>Vastussillat kortin yläpuolella. Irrota GPIO-nasta oheislaitteesta juottamalla vastaava silta irti.</figcaption>
</figure>

<figure markdown="span">
![Sillat, alapuoli](assets/sh-esp32_r0.3.1_bottom_jumpers_annotated.jpg "SH-ESP32:n sillat alapuolella")
<figcaption>Juotossillat kortin alapuolella. Kytke GPIO-nasta GPIO-liittimeen sulkemalla juotossilta lisäämällä tinapisara sillan alueen päälle.</figcaption>
</figure>

Jos esimerkiksi et tarvitse CAN-liitäntää ja haluat ottaa GPIO-liittimen nastat 32 ja 34 muuhun käyttöön, juota irti ESP32-moduulin vieressä olevat vastukset 32 ja 34, jolloin moduuli irtoaa CAN-liitännästä.
Sulje sitten juotossillat 32 ja 34, jolloin GPIO-nastat kytkeytyvät GPIO-liittimeen.

Vastaavasti jos haluat ottaa I2C:n käyttöön sekä GPIO-liittimessä että erillisessä I2C-liittimessä, sulje kortin alapuolella olevat juotossillat 16 ja 17.

Kummankin puolen silloilla voi lopuksi mukauttaa GPIO-määrityksiä. Jos esimerkiksi haluat siirtää 1-Wiren datanastan GPIO4:stä GPIO15:een, voit juottaa irti GPIO4:n vastussillan ja lisätä hyppyjohtimen joko ESP32-moduulin juotospisteestä tai GPIO-liittimestä alempaan vastussillan juotospisteeseen.

**Huomaa:** GPIO 1:n ja 3:n juotossiltojen silkkipainomerkinnät ovat virheelliset revision 0.3.1 -laitteissa. Ne on merkitty 3 ja 34, vaikka oikea merkintä olisi 1 ja 3.
