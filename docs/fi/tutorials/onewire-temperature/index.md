---
translated_from: 4f988e6edaf7ed9f914b7f04430b14ff37910171
---

# 1-Wire-lämpötilamittaus

---

## Johdanto

Tämä opastus käy läpi lämpötilaa mittaavan laitteen rakentamisen. Sillä voi mitata esimerkiksi moottoriöljyn, jäähdytysnesteen ja märän pakoputken lämpötiloja mistä tahansa moottorista, joka ei jo raportoi näitä lämpötiloja Signal K:hon tai N2K-verkkoosi.
Oma moottorini on Yanmar 3GM30F, mutta lähestymistapa on täysin yleinen ja sovellettavissa mihin tahansa moottoriin.
Minulla on ollut vastaava kokoonpano useita vuosia, ja se tuo lisää mielenrauhaa:
saisin varhaisen hälytyksen, jos lämpötila alkaisi nousta (minulla on ollut jäähdytysnesteongelmia aiemmin), ja jos joskus unohtaisin avata vedenoton pohjaventtiilin, saisin hälytyksen nousevasta pakokaasun lämpötilasta ennen kuin mitään peruuttamatonta ehtisi tapahtua.

Yksi SH-ESP32 tukee niin montaa lämpötila-anturia kuin siihen on käytännössä mahdollista kytkeä.

Tämän opastuksen lopputulos on tämä siisti pieni laite, joka mittaa kolmea eri lämpötilaa ja pystyy välittämään ne sekä langattomasti Signal K -protokollalla että NMEA 2000:n yli.

![SH-ESP32-lämpötila-anturin lopputulos](media/final_result.jpg "SH-ESP32-lämpötila-anturin lopputulos"){ width="50%" }

Jos sinulla on ehdotuksia, korjauksia, parannusideoita tai muuta palautetta tästä opastuksesta, kuulen niistä mielelläni osoitteessa [matti.airas@hatlabs.fi](mailto:matti.airas@hatlabs.fi).


## Tarvittavat osat

Tämän opastuksen läpikäymiseen tarvitset seuraavat osat:

* [SH-ESP32:n kotelopaketti](https://hatlabs.fi/product/sh-esp32-enclosure-bundle/)
* [1-Wire-lämpötila-anturi](https://hatlabs.fi/product/ds18b20-cable-3m/) — niin monta kuin tarvitset
* [SP13-liittimet, 3-napaiset, urospistoke](https://hatlabs.fi/product/sp13-connector-3-pin-male-plug/) — niin monta kuin haluat ulkoisia antureita
* [NMEA 2000 -urospaneeliliitin](https://hatlabs.fi/product/nmea-2000-panel-connector-male/) — jos haluat kytkeä laitteen NMEA 2000 -verkkoon; muutoin se toimii vain Signal K:n kanssa
* [OLED-näyttö](https://hatlabs.fi/product/128x64-oled-display/) (valinnainen)

## Laitteiston kokoaminen

Minulla on aiemmin ollut vastaava kokoonpano, jossa jatkoin yksittäiset anturit toisiinsa kotelon ulkopuolella ja vein ne koteloon läpivientiholkin kautta.
Tämä lähestymistapa toimii hyvin, mutta on hankala ylläpidon kannalta.
SH-ESP32:n irrottaminen muutoksia tai virheenjäljitystä varten on vaikeaa, koska kytkennät ovat pysyviä.

Tässä opastuksessa käytän sen sijaan erillisiä liittimiä, jotka mahdollistavat joustavamman asennuksen.

### Kotelon valmistelu

Koteloon on porattava reiät eri liittimille.
Reikien määrän vuoksi valmistelin [tulostettavan porausmallineen](media/enclosure_drill_template.pdf), jonka voi teipata kotelon päälle.

![SH-ESP32:n kotelo mallineen kanssa](media/enclosure_with_template.jpg "SH-ESP32:n kotelo mallineen kanssa"){ width="50%" }

Kun tulostat mallineen, varmista ettei sitä skaalata.
Mallineen paperikoko on kansainvälinen A4-standardi, joten erityisesti pohjoisamerikkalaisten kannattaa varoa, ettei tuloste vahingossa skaalaudu Letter-kokoiselle paperille tulostettaessa.

Ota malline käyttöön leikkaamalla se ensin irti reunoja pitkin.
Merkitse sitten kotelon sivujen keskipisteet huopakynällä.
Kohdista mallineen yksi sivu keskipistemerkkiin ja teippaa pää koteloon.
Vedä sitten paperi kireäksi kotelon yli ja varmista, että muut keskipistemerkit osuvat kohdalleen.
Kiinnitä malline reilulla määrällä teippiä.
Ei haittaa, vaikka teippaisit mallineen päältä: ainakin maalarinteippi on riittävän läpikuultavaa, jotta merkinnät näkyvät läpi.

Kun malline on paikallaan, päätä mihin haluat liittimet.
Jos GPIO-liitintä ei ole asennettu, SH-ESP32:n pohjoisreunalla on runsaasti tilaa liittimille. Länsireuna on myös melko vapaa. Itäpuolelle liittimet mahtuvat helposti, mutta kaakkoiskulmaan sijoitettu liitin tukkii USB:n.

Halusin asentaa laitteeni pystyyn niin, että virtaliitin osoittaa alaspäin ja lämpötila-anturien liittimet oikealle. Tulin vain tehneeksi sen virheen, että tukin USB-liittimen. Minulle taitavat siis jäädä [langattomat päivitykset](https://docs.platformio.org/en/latest/platforms/espressif32.html#over-the-air-ota-update)...

![SH-ESP32:n kotelo porattuine reikineen](media/enclosure_with_holes.jpg "SH-ESP32:n kotelo porattuine reikineen"){ width="50%" }

### Johtimien kytkentä

Useiden 1-Wire-antureiden kytkeminen yhteen laitteeseen on helppoa: sinun tarvitsee vain kytkeä kukin johdin rinnan.
Juotin liittimiin johdinpätkät seuraavalla nastajärjestyksellä:

1. Maa (musta)
2. 3,3 V (punainen)
3. Data (keltainen)

Seuraavaksi kuorin johtimesta 12 mm (1/2") ja kiersin kunkin värin päät yhteen (ylimääräisen liitinjohtimen kanssa) ja lisäsin hieman juotostinaa tehdäkseni yksinkertaisen [kierrejatkoksen](https://en.wikipedia.org/wiki/Rat-tail_splice).

Valokuvassa jatkoksissa ei ole kutistesukkaa, mutta sinun kannattaa ehdottomasti lisätä sitä suojaamaan kaikkea oikosuluilta.

**ÄLÄ TEE NÄIN:**

![1-Wire-liittimet kierrejatkoksineen](media/rat-tail_splices.jpg "1-Wire-liittimet kierrejatkoksineen"){ width="50%" }

Kerrohan nopeasti, mikä yrityksessäni meni pieleen?
No, ensinnäkin: miten saat liittimien mutterit irti?
Toiseksi: miten asennat liittimet, kun johtimet on jatkettu yhteen?
Kolmanneksi: jos onnistuisit asentamaan liittimet, miten saisit mutterin takaisin paikalleen?

Älä ole kuten minä.
Asenna sen sijaan ensin liittimet, jatka sitten johtimet ja lisää kutistesukkaa.

Jos haluat kytkeä laitteiston NMEA 2000:een, lisää M12-paneeliliitin [NMEA 2000 -USB-yhdyskäytävän opastuksen](../nmea2000-gateway/index.md) mukaisesti.
Vaihtoehtoisesti, jos elät tulevaisuudessa ja rakennat pelkän Signal K -kokoonpanon, käytä kotelopaketin mukana tulevaa SP13-virtaliitintä.
Tee siinä tapauksessa johdonmukaisuuden vuoksi maasta ensimmäinen nasta ja 12/24 V:sta toinen nasta.

NMEA 2000 -käyttöä varten SH-ESP32-laitteelle on myös syötettävä jännite. Voit tehdä sen jatkamalla jännitejohtimet ja kytkemällä ne jännitenastoihin tai kytkemällä alla olevassa valokuvassa näkyvän johdinsillan:

![Johdinsilta](media/wire_link.jpg "Johdinsilta"){ width="50%" }

Johdinsillan liittimet ovat normaalisti kalustamattomat. Oikosulje johdinsillan plus- ja GND-nastat viivojen osoittamalla tavalla. Oikosulkemisen voi tehdä juottamalla lyhyen johdinpätkän suoraan liittimiin tai, kuten itse tein, lisäämällä nastat ja kytkemällä ne toisiinsa [wire wrap -tekniikalla](https://en.wikipedia.org/wiki/Wire_wrap). (*Rakastan* wire wrapia!)

#### Vaihtoehtoinen kytkentätapa

Karkea hahmotelmakuva esittää vaihtoehtoisen ja mahdollisesti paremman kytkentätavan 1-Wire-liittimille.

![Vaihtoehtoinen kytkentä](media/alternate_wiring.jpg "Vaihtoehtoinen kytkentä"){ width="50%" }

Tässä tavassa juotat liitinrivit SH-ESP32:n prototyyppialueelle ja oikosuljet kunkin rivin nastat toisiinsa kortin alapuolella.
Liitinrivit muodostavat eräänlaiset kokoomakiskot kullekin 1-Wire-nastalle.

### Kokoonpano

Kun 1-Wiren dataliittimet ovat paikallaan, kiikuta SH-ESP32-kortti koteloon ja kiinnitä se pienillä 3 × 6 mm:n ruuveilla.
Asenna sitten virtaliitin (tai NMEA 2000 -liitin) ja kytke kaikki korttiin [vastaaviin liittimiin](../../hardware/index.md#liittimet).

Jos aiot käyttää OLED-näyttöä, nyt on aika asentaa se.

Oma lopputulokseni näkyy alla.

![Valmis kotelo](media/finished_enclosure.jpg "Valmis kotelo"){ width="50%" }

Antureiden lopullista asennusta itse moottoriin käsitellään myöhemmin tässä opastuksessa.

### 1-Wire-verkon huomioitavat asiat

1-Wire on suunniteltu väylätopologialle, jossa asiakaslaitteet ovat pitkän väyläkaapelin varrella:

![1-Wire-väylä](media/ideal_bus_topology.svg "1-Wire-väylä"){ width="80%" }

Väylän enimmäispituus riippuu ohjaimesta, käytetystä kaapelista ja väylän asiakaslaitteiden määrästä, mutta yli 100 m:n väyläpituudet 20 asiakaslaitteella ovat varsin realistisia erikoislaitteistolla. SH-ESP32:ta ei ole suunniteltu suurin verkkopituus mielessä, mutta ainakin 30 m:n väyläpituuksien pitäisi olla helposti saavutettavissa sopivalla kaapelilla.

[Springbok Digitronicsin 1-Wire-suunnitteluopas](https://www.unipi.technology/shop/product/download?fileId=142) kertoo, että 1-Wire-käyttöön suositellaan parikaapelia. Tavallinen Ethernet-kaapeli (Cat 5 tai parempi) soveltuu hyvin pitkän matkan 1-Wire-asennuksiin. Springbok Digitronics ehdottaa jopa [nastajärjestysstandardia](https://opencircuits.com/images/a/a3/A_Guide_to_the_1WRJ45_Standard.pdf) 1-Wire-laitteiden kytkemiseen tavallisilla Ethernet-RJ45-liittimillä. Toisaalta 1-Wiren kerrotaan toimivan hyvin jopa litteällä puhelinkaapelilla enintään 30 m:n etäisyyksillä.

Yksittäiset anturit voi erottaa pääväylästä haarakaapelilla (englanniksi myös *stub cable*). Dallas Semiconductorin suosittelema haarakaapelin enimmäispituus on 3 metriä.

Tässä opastuksessa oletetaan lyhyet väyläetäisyydet — itse asiassa väylämme on vain yksi kaapelijatkos kotelon sisällä, ja yksittäiset anturikaapelit ovat kaikki haarakaapeleita. Tämä toimii hyvin, kunhan haarakaapelit eivät ole liian pitkiä.

![Lyhyt väylätopologia](media/short_bus_topology.svg "Lyhyt väylätopologia"){ width="40%" }

Jos sinun on kasvatettava verkon pituutta, älä pidennä yksittäisiä haarakaapeleita yli suositellun kolmen metrin, vaan kasvata väylän pituutta.

![Pitkä väylätopologia](media/long_bus_topology.svg "Pitkä väylätopologia"){ width="80%" }

Sijoita jakorasia haluttujen anturipaikkojen lähelle, katkaise ylimääräinen haarakaapelin pituus pois ja kytke anturit väyläkaapeliin jakorasian sisällä. Väylän varrella voi olla useita jakorasioita.

## Ohjelmisto

### Esivaatimukset

Esivaatimukset ovat samat kuin [NMEA 2000 -yhdyskäytävällä](../nmea2000-gateway/index.md): tarvitset Visual Studio Coden ja PlatformIO:n sekä ajurit CH340-USB-sarjaporttipiirille.
Katso niiden asennus tuosta opastuksesta.

### Lataaminen

Lataa ohjelmisto osoitteesta [https://github.com/hatlabs/SH-ESP32-onewire-temperature](https://github.com/hatlabs/SH-ESP32-onewire-temperature).
Voit joko kloonata repositorion (jos Git on sinulle tuttu) tai ladata lähdekoodin zip-tiedostona napsauttamalla vihreää "Code"-painiketta ja valitsemalla "Download ZIP".
Pura paketti ja avaa hakemisto Visual Studio Codessa (File -> Open Workspace).

### Koodimuutokset

Esimerkkiprojekti olettaa kolme anturia, jotka mittaavat moottoriöljyn, moottorin jäähdytysnesteen ja märän pakoputken lämpötilaa.
Jos antureita on eri määrä tai mittaat eri asioita, ohjelmaa on muutettava.
Avaa tiedosto `src/main.cpp` Visual Studio Codessa.

Anturit on määritelty tiedostossa `main.cpp` rivin 97 tienoilla.
Muokkaa asetuspolkuja ja muuttujien nimiä mieleiseksesi.

Antureiden Signal K -lähtöjen metatiedot määritellään rivistä 106 alkaen.
Siinä määritellään Signal K -polkujen ihmisluettavat kuvaukset ja arvojen yksiköt.

Anturit kytketään Signal K -lähtöihin rivin 137 tienoilla.
Voit taas muokata Signal K -polkuja mieltymystesi mukaan.
Polkujen nimissä kannattaa pyrkiä noudattamaan [Signal K -määrittelyä](http://signalk.org/specification/1.5.0/doc/vesselsBranch.html), mutta jos sopivaa ei löydy, keksi rohkeasti omasi.

Esimerkissä jäähdytysnesteen lämpötila-arvo on kytketty kahteen polkuun: `propulsion.main.temperature` ja `propulsion.main.coolantTemperature`. Jäähdytysnesteen lämpötilaa pidetään tyypillisesti moottorin yleisenä lämpötilana, mutta sille on määritelty myös oma polkunsa. Tämä pieni päällekkäisyys takaa, että molemmat polut on määritetty, jos jokin myöhempi prosessi odottaa jompaakumpaa.

Jos käytät OLED-näyttöä, kannattaa muokata näytön tulosteita rivin 170 tienoilla.
Ne määrittelevät, miten lämpötila-arvot esitetään pienellä OLED-ruudulla.

Saatat tässä vaiheessa jo ihmetellä lämpötilayksiköitä.
Sekä Signal K että NMEA 2000 käyttävät sisäisesti kelvineitä, ja niin tekee myös SensESP.
Ajatuksena on, että kaikki käsitellään sisäisesti SI-perusyksiköissä ja muunnos tuttuihin yksiköihin kuten °C tai °F tehdään vasta arvoja näytettäessä.
Tavallisesti SensESP ei koskaan muuntaisi kelvineitä °C:ksi tai °F:ksi, mutta arvojen näyttäminen OLED-ruudulla on se yksi iso poikkeus sääntöön: näytettävät arvot kannattaa muuntaa tuttuihin yksiköihin.

Opastuksen ohjelmisto näyttää lämpötilat oletuksena celsiusasteina.
Jos haluat lämpötilat fahrenheiteina, palaa taaksepäin ja muokkaa rivejä 29 ja 30 vastaavasti.

#### NMEA 2000 -data

NMEA 2000 -lähdön muokkaaminen on protokollan luonteen vuoksi hieman monimutkaisempi tehtävä.
NMEA 2000 lähettää dataa [kiinteämuotoisina viesteinä](https://en.wikipedia.org/wiki/NMEA_2000#Message_format_and_parameter_group_numbers_(PGNs)).
Viestityypin määrittelee sen PGN (Parameter Group Number).
Kukin PGN voi sisältää yhden tai useamman tiedon.
Esimerkiksi PGN 130312 "Environmental Parameters" sisältää veden lämpötilan, ulkoilman lämpötilan ja ilmanpaineen kaikki yhdessä viestissä.
Useimmissa PGN:issä yksittäisiä arvoja voi myös merkitä määrittelemättömiksi — jos meillä yllä olevassa esimerkissä on vain ilman lämpötila, voimme välttää valheellisen datan lähettämisen merkitsemällä veden lämpötilan ja ilmanpaineen määrittelemättömiksi.

Yksi hyvä lähde PGN:ille ja PGN-rakenteille on `canboat`-kirjaston [PGN-määrittelyjen otsikkotiedosto](https://github.com/canboat/canboat/blob/master/analyzer/pgn.h).
Sitä voi verrata viestien kääntämiseen ja lähettämiseen käytetyn NMEA 2000 -kirjaston [NMEA 2000 -viestiluetteloon](https://github.com/ttlappalainen/NMEA2000/blob/master/src/N2kMessages.h).
Etsi tiedostosta haluamasi PGN-numero tai datatyyppi, niin löydät todennäköisesti tietoa aiheesta.

Yleistä lämpötiladataa tarjoavat PGN:t 130310, 130311, 130312 ja 130316.
Moottorin lämpötiladataa tarjoaa PGN 127489 "Engine Parameters, Dynamic" ja vaihteistodataa PGN 127493 "Transmission Parameters, Dynamic".

Tässä opastuksessa lähetämme moottoriöljyn (öljypohjan) lämpötilan, jäähdytysnesteen lämpötilan ja märän pakoputken lämpötilan.
Jotkut voisivat olla kiinnostuneempia varsinaisesta pakokaasun lämpötilasta, mutta se menee kauas käyttämiemme 1-Wire-antureiden kyvyistä ja vaatii mittaamiseen erikseen asennetun termoelementtianturin.
PGN 127489 lähettää sekä öljyn että jäähdytysnesteen lämpötilan, joten arvot on kerättävä ja lähetettävä yhdessä.
Tässä esimerkissä valitsemani lähestymistapa on, että lämpötila-arvot tallennetaan muuttujaan ja aina kun joko öljyn tai jäähdytysnesteen lämpötila päivittyy, lähetetään aina PGN 127489.
Märän pakoputken lämpötila lähetetään erikseen PGN 130312:lla.

PGN-kytkennän muuttamiseksi sinun on muokattava koodia rivien 62 ja 219 tienoilla.

## Antureiden määritys

Jokaisella 1-Wire-anturilla on yksilöllinen laiteosoite.
Kun ohjelma käynnistyy ensimmäistä kertaa, se kytkee uudet havaitut anturiosoitteet `OneWireTemperature`-anturiolioihin ja tallentaa tiedon flash-muistiin.
Laitteiden skannausjärjestys on sattumanvarainen, joten jos kaikki anturit ovat kytkettyinä yhtä aikaa, ne liitetään `OneWireTemperature`-olioihin satunnaisessa järjestyksessä.
Liitoksia voi muuttaa verkkoasetuskäyttöliittymästä, mutta on olemassa helpompi tapa: kytke anturit yksi kerrallaan.

Esimerkkiohjelma määrittelee `OneWireTemperature`-oliot seuraavassa järjestyksessä: öljy, jäähdytysneste, pakoputki. Toimi siis näin:

1. Kytke se anturi, josta tulee öljyn lämpötila-anturi.
2. Kytke laitteeseen jännite muutamaksi sekunniksi.
3. Katkaise laitteen jännite.
4. Kytke jäähdytysnesteen lämpötila-anturi.
5. Kytke laitteeseen jännite muutamaksi sekunniksi.
6. Katkaise laitteen jännite.
7. Kytke pakoputken lämpötila-anturi.
8. Kytke laitteeseen jännite.
9. Valmista!

Tätä tapaa noudattamalla anturit rekisteröityvät varmasti oikeassa järjestyksessä.

## Testaus

Testaa laitteesi ennen kuin asennat sen veneeseen. Jos kokoonpanossasi on ongelmia, ne on paljon helpompi korjata ennen kuin kaikki on kiinnitetty tukevasti paikoilleen.

### Signal K

Jos käytät laitetta Signal K:n kanssa, sinun on kytkettävä se Signal K -serveriisi. Jos sellaista ei ole vielä pystytetty, seuraa [Signal K -serverin asennusohjeita](https://github.com/SignalK/signalk-server).

Voisit asettaa WiFi- ja servertiedot koodiin, mutta tämä opastus nojaa automaattiseen palvelunetsintään (Bonjour/mDNS/DNS-DD/Avahi).

Kun laitteeseen kytketään jännite eikä sitä ole vielä määritetty, pitäisi ilmestyä langaton tukiasema nimeltä "Configure temperatures".
Kun yhdistät siihen, sinut pitäisi ohjata automaattisesti WiFiManagerin asetusnäkymään.
Jos näin ei käy, avaa selain ja siirry osoitteeseen http://192.168.4.1/.
Valitse tavallisesti käyttämäsi WiFi-verkko ja anna salasana.
Laitteen pitäisi nyt yhdistyä verkkoon automaattisesti.

>Huomaa: kun WiFi-asetukset on kerran asetettu, niiden muuttamiseen tai nollaamiseen ei tällä hetkellä ole helppoa tapaa.
Sinun on käytettävä PlatformIO:n "Erase flash" -komentoa ja siirrettävä firmware uudelleen.
Tätä [seurataan tulevana päivityksenä](https://github.com/SignalK/SensESP/issues/587).

Jos automaattinen palvelunetsintä on määritetty oikein, Signal K -serverin verkkokäyttöliittymään pitäisi heti ilmestyä laitteen käyttöoikeuspyyntö:

![Laitteen käyttöoikeuspyyntö](media/device_access_request.png "Laitteen käyttöoikeuspyyntö"){ width="50%" }

Avaa käyttöoikeuspyyntö, aseta tunnistautumisen aikakatkaisuksi "NEVER" ja napsauta Approve.
Signal K -serverin koontinäyttöön ja datan selaimeen pitäisi heti tulla uutta dataa.

SensESP-laite koontinäytöllä:

![Koontinäytön näkymä](media/dashboard_view.png "Koontinäytön näkymä")

Lämpötilalukemat datan selaimessa:

![Datan selaimen näkymä](media/data_browser_view.png "Datan selaimen näkymä")

### NMEA 2000

Testaa NMEA 2000 -yhteys kytkemällä laitteesi NMEA 2000 -verkkoosi.
Jos verkossa on karttaplotteri, sen laiteluettelossa pitäisi näkyä uusi lämpötila-anturi:

![NMEA 2000 -laiteluettelo](media/n2k_device_list.jpg "NMEA 2000 -laiteluettelo"){ width="50%" }

Kun SH-ESP32-laitteen dataa tarkastellaan, siinä pitäisi näkyä kolme eri lämpötila-arvoa:

![NMEA 2000 -dataluettelo](media/n2k_show_data.jpg "NMEA 2000 -dataluettelo"){ width="50%" }

Tämä varmistaa, että yhteys toimii.

## Antureiden asennus veneeseen

Jäljellä on enää laitteen ja anturikaapeleiden asentaminen veneeseen.
En halunnut tehdä pysyviä muutoksia Yanmar 3GM30F -dieselmoottoriini.
Anturiasennukseni oli hyvin kotikutoinen mutta silti varsin toimiva.
Öljyn lämpötila-anturi meni moottorin öljypohjan kylkeen.
Öljypohjassa oli kierteitetty pultinreikä.
Otin sopivan kokoisen neliöaluslevyn ja taivutin yhtä kulmaa hieman, ja kiinnitin sillä anturin öljypohjaa vasten.
Varo tätä tehdessäsi kiristämästä pulttia liian tiukalle, koska se todennäköisesti murskaa anturin.

![Öljyanturin asennus](media/oil_sensor_installation.jpg "Öljyanturin asennus"){ width="50%" }

Jäähdytysnesteen lämpötila mitataan jäähdytysnesteen paluuletkun pinnalta.
Anturi teipataan ensin kiinni silikoniteipillä.
Silikoniteippi kestää korkeita lämpötiloja, on erittäin hyvä eriste ja tarttuu itseensä, jolloin letkun ja anturin ympärille syntyy tiivis suojaus.
Lisäisin siitä huolimatta teipin päälle vielä letkunkiristimen varmistamaan, ettei kaapeli pääse irtoamaan ja putoamaan moottorin hihnoille.

![Jäähdytysnesteanturin asennus](media/coolant_sensor_installation.jpg "Jäähdytysnesteanturin asennus"){ width="50%" }

Pakoputkianturi meni pakomutkaan jäähdytysvesiletkun liitoksen jälkeen.
Kiinnitin sen jäähdytysnesteen lämpötila-anturin tapaan silikoniteipillä ja letkunkiristimellä.

![Pakoputkianturin asennus](media/exhaust_sensor_installation.jpg "Pakoputkianturin asennus"){ width="50%" }

Vedä kaikkien antureiden kaapelit siististi.
Kaapeleissa on hyvä olla hieman löysää moottorin tärinän varalle, mutta muutoin ne kannattaa kiinnittää johonkin noin 30 cm:n (1 ft) välein.
Kaapeli ei saa missään kohtaa päästä hankautumaan tärisevää moottoria vasten.
Varo myös, ettei kaapeli pääse koskettamaan moottorin hyvin kuumia osia, kuten pakosarjaa.

Onnittelut!
Sinulla on nyt hieno uusi lämpötila-anturi moottoriisi ja taidot rakentaa muitakin antureita!
On aika kehuskella sillä verkossa ja satamanaapureille!
