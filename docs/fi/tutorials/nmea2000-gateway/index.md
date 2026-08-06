---
translated_from: cea41f03495fa0446327fab51aad0ea47674d733
---

# NMEA 2000 -USB-yhdyskäytävä

---

## Johdanto

Tässä opastuksessa näytän, miten SH-ESP32:sta ja parista liittimestä rakennetaan Actisense&trade;[^1] NGT-1 -yhteensopiva NMEA 2000 -USB-yhdyskäytävä.
SH-ESP32:n integroidun CAN-liitännän ansiosta ulkoista laitteistoa ei tarvita.
Lopputuloksena on erotettu NMEA 2000 -yhdyskäytävä, joka sekä lukee että kirjoittaa NMEA 2000 -paketteja ja antaa tietokoneesi keskustella veneesi elektroniikan kanssa.
NMEA 2000 -yhdyskäytävällä voi liittää minkä tahansa merkittävän PC-pohjaisen navigointiohjelmiston NMEA 2000 -verkkoosi, kytkeä Raspberry Pi -pohjaisen Signal K -serverin NMEA 2000 -väylään tai jopa etsiä NMEA 2000 -vikoja sopivalla ohjelmistolla.

Jos sinulla on ehdotuksia, korjauksia, parannusideoita tai muuta palautetta tästä opastuksesta, kuulen niistä mielelläni osoitteessa [matti.airas@hatlabs.fi](mailto:matti.airas@hatlabs.fi).

[^1]: Actisense on Active Research Limitedin tavaramerkki.

## Tarvittavat osat

Tämän opastuksen läpikäymiseen tarvitset seuraavat osat:

- [SH-ESP32:n kotelopaketti](https://hatlabs.fi/product/sh-esp32-enclosure-bundle/)
- [NMEA 2000 -urospaneeliliitin](https://hatlabs.fi/product/nmea-2000-panel-connector-male/)
- USB-paneeliliitin (tulossa pian myyntiin osoitteessa hatlabs.fi) tai [PG9-läpivientiholkki](https://hatlabs.fi/product/pg9-cable-gland/)
- [OLED-näyttö](https://hatlabs.fi/product/128x64-oled-display/) (valinnainen)

## Laitteiston kokoaminen

### Tarvittavat tarvikkeet

Käytämme tässä projektissa SH-ESP32:n vesitiivistä vakiokoteloa.

![SH-ESP32:n kotelo](media/SH-ESP32_enclosure.jpg "SH-ESP32:n kotelo"){ width="50%" }

Laite on kytkettävä sekä NMEA 2000:een että USB:hen.
NMEA 2000:ta varten käytetään tavanomaista M12 micro -liitintä.

![M12-paneeliliitin](media/M12_panel_connector.jpg "M12-paneeliliitin"){ width="50%" }

USB-liitännässä paras vaihtoehto on käyttää valmista Micro USB -paneeliliitintä:

![Micro USB -paneeliliitin](media/Micro_USB_panel_connector.jpg "Micro USB -paneeliliitin"){ width="50%" }

Toinen vaihtoehto on viedä Micro USB -kaapeli koteloon läpivientiholkin kautta.
Valitsin itse tämän vaihtoehdon, lähinnä koska odottamani paneeliliitinlähetys ei ollut vielä saapunut.
Läpivientiholkin käyttö valmiin kaapelin kanssa on kuitenkin näpertelyä.
Jouduin poraamaan läpivientiholkin sisäkauluksen auki ja suurentamaan holkin kiristysmutterin reikää.
Jotta iso PG9-läpivientiholkki saisi otteen ohuesta USB-kaapelista, kiersin kaapelin ympärille muutaman kierroksen PVC-teippiä.
Lopputulos on hieman viritys, mutta riittävän hyvä!

### Reikien poraaminen

Sinun on päätettävä, mihin kohtaan koteloa liittimet sijoitetaan.
Oma tapani on sijoittaa molemmat liittimet samalle lyhyelle sivulle.
Silloin kotelon voi asentaa seinään liittimet alaspäin.
Tämä asento minimoi riskin, että vettä vuotaa liittimen tiivisteen läpi.

Liittimet mahtuvat paikoilleen tiukasti.
Kun merkitset keskipisteet, ota huomioon sekä kotelon sisäkulmat että se väli, jonka liittimien mutterit tarvitsevat pyöriäkseen.
Esimerkki lopputuloksesta näkyy alla olevassa valokuvassa.

![Kotelon reiät](media/Enclosure_holes.jpg "Kotelon reiät"){ width="50%" }

### Johtimien kytkentä NMEA 2000 -paneeliliittimeen

NMEA 2000 -liittimeen on juotettava johtimet.
Käytän mukana toimitettuja JST XH -liittimiä ja johtimen jatkeita.
Johtimen jatke noudattaa NMEA 2000 -standardin väritystä sillä poikkeuksella, että L-signaalijohdin on keltainen standardin sinisen sijaan.

Liittimen nastoissa on pienet kolot, kuten alla olevasta valokuvasta näkyy:

![M12-paneeliliittimen nastat](media/M12_pins.jpg "M12-paneeliliittimen nastat"){ width="50%" }

Kuumenna nastat yksi kerrallaan juottimella ja lisää koloihin hieman juotostinaa.

Ennen kuin kiinnität johtimet, leikkaa lyhyet pätkät kutistesukkaa ja pujota ne johtimiin.
Kutistesukka kannattaa ottaa mukaan, koska se tuo johtimille mekaanista tukea ja estää lisäksi vahingossa syntyvät oikosulut.

Kiinnitä tarkkaa huomiota nastojen oikeaan järjestykseen. Oikea nastajärjestys _siltä puolelta katsottuna, jolta johtimet juotetaan_, on esitetty alla olevassa kuvassa.
(Kuvassa lukee "female connector", mutta se pätee, kun katsot liitintä etupuolelta.)

> Toistan: kiinnitä tarkkaa huomiota nastojen oikeaan järjestykseen.
> Tätä opastusta valmistellessani kytkin ensin kaikki nastat peilikuvana (urosliittimen nastajärjestyskaavion mukaan).
> Se ei tietenkään toiminut.
> Seuraavalla yrittämällä H- ja L-nastat olivat vaihtaneet paikkaa. Ei toiminut sekään.
> Kolmannella yrittämällä nastat olivat oikeassa järjestyksessä, mutta olin unohtanut vaihtaa kutistesukan.
> Neljännellä yrittämällä sain sen oikein.
> Älä ole kuten minä!
> Keskity, kun juotat liittimiä!

![NMEA 2000 micro C -naarasliittimen nastajärjestys](media/nmea_2000_female_pinout.png "NMEA 2000 micro C -naarasliittimen nastajärjestys"){ width="50%" }

Juota johtimet nastoihin ottamalla johtimen jatke ja kuumentamalla nasta kerrallaan niin, että tina sulaa, ja työntämällä johtimen pää tinan täyttämään koloon.
Aloita keskimmäisestä nastasta, koska se on helpompi tehdä ennen kuin muut johtimet ovat tiellä.

Kun kaikki johtimet on kiinnitetty, anna liitosten jäähtyä hetki ja liu'uta sitten kutistesukat nastojen päälle.
Sukkien kuumentamiseen kuumailmajuotosasema tai kuumailmapuhallin on ihanteellinen, mutta sytyttimen liekkikin kelpaa.
Jos käytät liekkiä, älä vain liioittele. Kutistesukkiin ei haluta palamisjälkiä.

Esimerkki lopputuloksesta näkyy seuraavassa kuvassa.

![Juotettu NMEA 2000 -paneeliliitin](media/M12_soldered.jpg "Juotettu NMEA 2000 -paneeliliitin"){ width="50%" }

Valokuvasta näkyy myös yksi oma niksini: monenlaisia liittimiä juotettaessa tukevat pihdit ja kuminauha pitävät liittimen täysin paikallaan juottamisen ajan.
Se on mielestäni helpompaa kuin käyttää halpoja apukäsiäni.

### Kokoonpano

Ruuvaa lopuksi NMEA 2000 -paneeliliitin paikalleen.
Sen kunnollinen kiristäminen voi olla työlästä, mutta älä missään tapauksessa käytä liittimessä lukitetta.
Jos lukitetta pääsee ABS-muoville, se haurastuu kokonaan ja hajoaa pienimmästäkin tuulahduksesta!
Usko pois!
Sen sijaan pisara pikaliimaa voi toimia, kunhan olet ensin varmistanut, että kaikki toimii.
Tai ehkä pikkuruinen pisara asetonia kotelon muovin ja liittimen rungon väliin.
Asetoni pehmentää ABS:ää ja muuttaa sen tahmeaksi, liimamaiseksi aineeksi.

Asenna myös läpivientiholkki ja USB-kaapeli (tai USB-paneeliliitin).
Suoraliittiminen kaapeli mahtuu hieman tiukasti, mutta epäilen, että kulmaliitin ei olisi mahtunut läpivientiholkin läpi lainkaan.
Kahdesta mittaamisesta huolimatta olin silti porannut reiät liian lähelle toisiaan, eikä mutteri pyörinyt vapaasti.
Sen sijaan sain kiristettyä holkin kiertämällä sen runkoa. Se ei ole täydellistä, mutta toimii hyvin.

Jos haluat käyttää OLED-näyttöä, kytke se nyt paikalleen.

Lopputulos näkyy alla olevassa valokuvassa.

![Valmis laitteiston kokoonpano](media/finished_assembly.jpg "Valmis laitteiston kokoonpano"){ width="50%" }

Toinen, kiistatta siistimpi tapa viedä USB-yhteys kotelon läpi on käyttää [USB-paneeliliitintä](https://hatlabs.fi/product/micro-usb-panel-connector/). Näin vältät kaiken näpertelyn läpivientiholkkien kanssa. Samat huomiot reikien poraamisesta liian lähelle toisiaan pätevät kuitenkin edelleen...

![Valmis kokoonpano Micro USB -paneeliliittimillä.](media/sh-esp32-n2k-gw-micro-usb-conx-overview.jpg "Valmis kokoonpano Micro USB -paneeliliittimillä."){ width="50%" }

![Micro USB -liittimen yksityiskohta](media/sh-esp32-n2k-gw-micro-usb-conx.jpg "Micro USB -liittimen yksityiskohta"){ width="50%" }

## Ohjelmisto

### Esivaatimukset

Jotta voit asentaa ohjelmiston laitteeseen, sinun on ensin [asennettava Visual Studio Code ja PlatformIO](https://platformio.org/install/ide?install=vscode).

Toinen esivaatimus on CH340-USB-sarjaporttipiirin ajuri. Linux tukee sitä valmiiksi, mutta Windows- ja Mac-käyttäjien on ladattava ja asennettava ajuri [valmistajan sivustolta](http://www.wch.cn/download/CH341SER_EXE.html). Ajuria käytetään sekä ohjelmiston asentamiseen että sen käyttöön.

### Asennus

SH-ESP32:n NMEA 2000 -USB-yhdyskäytävän ohjelmisto löytyy täältä: [https://github.com/hatlabs/SH-ESP32-nmea2000-gateway](https://github.com/hatlabs/SH-ESP32-nmea2000-gateway)


Kun PlatformIO on asennettu, kloonaa repositorio (jos Git on sinulle tuttu) tai lataa lähdekoodi zip-tiedostona napsauttamalla vihreää "Code"-painiketta ja valitsemalla "Download ZIP".
Pura paketti ja avaa hakemisto Visual Studio Codessa (File -> Open Workspace).
Kytke USB-kaapeli tietokoneeseesi.
Napsauta sitten vasemman reunan työkalupalkin PlatformIO-kuvaketta (kuva alla).
Valitse Default -> Upload.
Näytön alaosassa pitäisi vieriä käännösjärjestelmän ja kääntäjän tulostetta, kun PlatformIO lataa riippuvuudet ja kääntää kaiken.
Kun kaikki on käännetty, PlatformIO:n pitäisi jatkaa ohjelmiston siirtämiseen SH-ESP32:llesi.

![PlatformIO-kuvake](media/platformio_button.png "PlatformIO-kuvake")

Jos haluat mukauttaa laitettasi, avaa tiedosto `src/main.cpp` VS Codessa ja muokkaa laitetietojen merkkijonoja rivin 74 tienoilla.
Nämä merkkijonot näkyvät verkon muille NMEA 2000 -laitteille.

Jos kaikki meni hyvin, sinisen LEDin pitäisi alkaa vilkkua hitaasti.
Jos sinulla on näyttö, siinäkin pitäisi näkyä jonkin verran tilatietoa.

### Testaus

Kun kytket laitteen NMEA 2000 -verkkoosi ja tietokoneeseesi, näytön RX-rivin pitäisi muuttua välittömästi.
Se kertoo, montako NMEA 2000 -viestiä on vastaanotettu sekunnissa.
TX-rivi kertoo, montako viestiä on lähetetty, mutta jos et vielä aja mitään ohjelmistoa, se on nolla.

Päätin testata laitetta Signal K -serverillä.
Signal K -serverin voi asentaa Raspberry Pille, mutta tähän tarkoitukseen asensin sen Mac-läppärilleni.
Linuxin ja Windowsin pitäisi toimia myös.
Perusasennusohjeet löytyvät serverin GitHub-repositoriosta: https://github.com/SignalK/signalk-server

Oletan, että olet onnistunut asentamaan ja käynnistämään serverin ja selannut nyt sen verkkokäyttöliittymään.
Eikö niin?

Laitteen käyttöönotto vaatii NMEA 2000 -datayhteyden lisäämisen.
Valitse Server -> Data Connections.
Napsauta sinistä Add-painiketta.

Nyt pitäisi näkyä seuraava lomake.

![Datayhteyden asetukset](media/data_connection_config.png "Datayhteyden asetukset")

Valitse datatyypiksi "NMEA 2000".
Provider ID voi olla mikä tahansa merkkijono.
`can0` käy hyvin.
NMEA 2000 Source -kohtaan valitaan "Actisense NGT-1 (canboatjs)".
Napsauta sarjaportin valintaa (oletuksena "Enter manually").
Jos laitteesi tunnistettiin, siinä pitäisi näkyä laitteen nimi.
Laitenimet ovat aika epähavainnollisia.
Omassa Macissani laite näkyy nimellä `/dev/tty.usbserial-14130` tai vastaavalla.
Linuxissa sen pitäisi olla suurin piirtein samankaltainen.
Windowsissa muoto on `COMn:`.
Valitse laite.
Kaiken muun voi jättää ennalleen.
Tallenna muutokset napsauttamalla Apply.

Käynnistä sitten serveri uudelleen napsauttamalla yläpalkin Restart-linkkiä.
Jos olit käynnistänyt Signal K -serverin käsin, se voi nyt olla käynnistettävä uudelleen komentoriviltä.

Jos kaikki meni hyvin, "Connection & Plugin Status" -osiossa pitäisi näkyä `can0`.

![Signal K -server vastaanottaa dataa](media/sk-server-online.png "Signal K -server vastaanottaa dataa")

Jos yhteyden tila on vihreä, avaa datan selain ja ihastele vastaanotettua NMEA 2000 -dataa!

![Datan selain näyttää dataa](media/pgns_received.png "Datan selain näyttää dataa")

Melkein valmista.
Haluat vielä testata, että myös datan lähetys toimii.
Jotta Signal K -server lähettäisi NMEA 2000 -dataa, sinun on asennettava `signalk-to-nmea2000`-lisäosa.
Valitse Appstore -> Available ja vaihda sitten tyypin pudotusvalikon arvoksi New/Updated tilalle All.
Kirjoita hakukenttään `nmea2000`.
Oikean lisäosan pitäisi näkyä ainoana tuloksena.
Asenna se napsauttamalla rivin oikeassa päässä olevaa pientä pilvilatauskuvaketta.
Käynnistä serveri taas uudelleen.

Määritä lopuksi lisäosan asetukset: Server -> Plugin Config.
Avaa osio "Signal K to NMEA 2000".
Serverin oletusasennuksessa ei ole paljon lähetettävää dataa, mutta jotain kuitenkin: järjestelmän aika!
Vieritä kohtaan "System Time (126992)" ja ota se käyttöön.

![Järjestelmän ajan asetukset](media/system_time_config.png "Järjestelmän ajan asetukset"){ width="50%" }

Aseta Resend time -arvoksi 1 sekunti.
Vieritä sivun alaosaan ja valitse Submit.

Jos kaikki edellä kuvatut vaiheet menivät hyvin, näytön TX-rivin pitäisi muuttua nollasta ykköseksi:

![Yhdyskäytävä toiminnassa](media/gateway_in_action.jpg "Yhdyskäytävä toiminnassa")

Jos NMEA 2000 -verkossasi on monitoiminäyttö (karttaplotteri), selaa sen verkkoasetuksiin.
Laiteluettelosivulla pitäisi nyt näkyä "SH-ESP32 NMEA 2000 USB GW" muiden laitteiden joukossa!
Kun napautat sitä, siinä pitäisi näkyä myös kellonaika ja päivämäärä tarjottuna datana.
Tämä tarkoittaa, että asennuksesi onnistui ja dataa kulkee molempiin suuntiin!
On aika kehuskella sillä verkossa ja satamanaapureille!

![Monitoiminäytön näkymä](media/mfd_view.jpg "Monitoiminäytön näkymä")
