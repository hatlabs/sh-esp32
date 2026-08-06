---
translated_from: 86c5beca9ea749135c81d4d63a1d4e0cabfeb694
---

# Aloitusopas

## Laitteiston kokoaminen

### Revision 2 -kortit

Revision 2 -kortit (ne, joissa on vihreät irrotettavat ruuviliittimet valmiina) toimitetaan koottuina, joten juottamista ei tarvita.
Myyntipakkaus sisältää jännitetulon ja CAN-väylän irrotettavat ruuviliittimet sekä hieman johdinta kytkentöjen tekemiseen.

### Revision 1 -kortit

Hat Labsin myymät SH-ESP32-kortit ovat enimmäkseen kokoamattomia.
Toimitettaessa vain USB-liitin on juotettu paikalleen.
Loput liittimet — tai ainakin tarvitsemasi — on juotettava itse.
Myyntipakkaus sisältää liitinsarjan.
Tarpeidesi mukaan voit halutessasi vaihtaa ne johonkin muuhun.
Esimerkiksi jännitetulon ja CAN-väylän liittimet voi korvata 2,5 mm:n irrotettavilla riviliittimillä, jotka helpottavat yksittäisten johtimien irrottamista ja ovat mekaanisesti kestävämpiä.
Vastaavasti urosnastarimat voi korvata naarasrimoilla, jolloin niihin voi kytkeä laitteita, joissa on yhteensopivat urosrimat.

Liittimien kokoamiseen tarvitaan juotin ja juotostinaa.
Lämpötilasäädettävää juotinta suositellaan lämpimästi.
Myös juoksutteesta voi olla apua.
SH-ESP32:ssa on maataso jopa kolmella piirilevyn neljästä kerroksesta.
Ne johtavat lämpöä tehokkaasti pois juotoskohdasta — käytä liittimien juottamiseen niin suurta juotinkärkeä kuin pystyt vaivatta käsittelemään.
Hyvä lähtökohta juottimen lämpötilalle on 320 °C. Jos se ei toimi hyvin, nosta lämpötilaa asteittain.

Liittimet juotetaan asettamalla ne korttiin yksi kerrallaan ja kiinnittämällä ne teipillä paikoilleen, kun käännät piirilevyn ympäri juottamista varten. Urosnastat voi työntää teipin läpi, jolloin käsittely on vielä helpompaa.

Kosketa juotinkärjellä sekä nastaa että juotospistettä, ja syötä sitten juotostinaa nastan vastakkaiselle puolelle alla olevien kuvien mukaisesti.
Koko toimenpiteen pitäisi ihanteellisesti kestää vain pari sekuntia, vaikka käytännössä hieman haparointia on normaalia.
Vältä kuitenkin nastojen liian pitkää kuumentamista — liittimen tai riman muovirunko sulaa ja nasta kallistuu.
Pieni muodonmuutos ei ole vaarallinen, kunhan se ei estä liittimen kytkemistä rimaan.

![Juotinkärki nastaa ja juotospistettä vasten](assets/soldering_guide_1.jpg "Juotinkärki nastaa ja juotospistettä vasten"){ width="50%" }

*Kuumenna nastat ja juotospisteet juotinkärjellä.*

![Syötä juotostinaa vastakkaiselta puolelta](assets/soldering_guide_2.jpg "Syötä juotostinaa vastakkaiselta puolelta"){ width="50%" }

*Syötä tinaa nastoille ja juotospisteille, ei juotinkärjelle. Tosin rehellisyyden nimissä pieni määrä tinaa kärjessä voi auttaa lämmönjohtumista...*

Vähän tinaa juotinkärjessä on hyväksi lämmönsiirron kannalta, mutta jos lisäät kärkeen ison tinapisaran, kaikki juoksute palaa pois ja tinaa on vaikea käsitellä.
Silloin kärki kannattaa pyyhkiä puhtaaksi ja lisätä tuoretta tinaa.
Hankalille nastoille kannattaa lisätä reilusti juoksutetta.
Se auttaa tinaa juoksemaan helpommin.

Lopputuloksen pitäisi näyttää seuraavan kuvan kaltaiselta.

![Hyvin juotetut nastat](assets/soldering_guide_3.jpg "Hyvin juotetut nastat"){ width="50%" }

*Esimerkki hyvin juotetuista nastoista.*

## Kotelot

Veneet voivat olla elektroniikalle ikäviä ympäristöjä: siellä on suolavettä, korkea kosteus ja usein myös kondenssivettä.
SH-ESP32 kannattaa ehdottomasti pitää kotelossa "tuotantokäytössä".
Kortti on suunniteltu sopimaan alla olevan kuvan mukaiseen 100 × 68 × 50 mm:n vesitiiviiseen muovikoteloon, jota saa joko Hat Labsin verkkokaupasta tai mistä tahansa verkkokaupasta kuten Amazonista, eBaysta tai AliExpressistä.

![Vakiokotelo](assets/enclosure.jpg "Vakiokotelo"){ width="50%" }

*SH-ESP32:n vakiokotelo.*

### Kortin kiinnittäminen

Yleiskäyttöisissä koteloissa muovivälikkeiden sijainti vaihtelee hieman, joten kortin kiinnittämisessä voi joutua käyttämään luovuutta.
Alla näkyvien kaltaiset liimattavat muovivälikkeet (reikäkoko 3 mm, korkeus enintään 6 mm, saatavana verkosta) mahdollistavat kortin helpon kiinnittämisen minkälaiseen koteloon tahansa.

![Liimattavat piirilevyvälikkeet](assets/adhesive_pcb_standoffs.jpg "Liimattavat piirilevyvälikkeet"){ width="50%" }

*Liimattavat välikkeet.*

### Reikien poraaminen

Koteloissa ei ole valmiiksi porattuja reikiä liittimille tai läpivientiholkeille.
Vähintään tarvitset yhden reiän jännitetulolle tai NMEA 2000 -liitännälle.
Yleensä niitä halutaan kuitenkin useampia ulkoisten antureiden tai kaapeloinnin kytkemiseen.

Ohuen muovin poraamiseen suositellaan porrasterää (sellaista, joka näyttää pieneltä metalliselta joulukuuselta).
Tavallinen metalliporanterä puree helposti liian syvälle ja voi halkaista muovin.
Jos porrasterää ei ole käsillä, käytä tavallisia metalliteriä.
Aloita pienestä halkaisijasta ja kasvata sitä pienin askelin, niin kotelon halkeamisriski pienenee.

![Porrasterä](assets/step_drill_bit.jpg "Porrasterä"){ width="50%" }

*Esimerkki porrasteristä.*

Suunnittele reikien sijoittelu etukäteen.
Jos tarvitset vain pari reikää, niiden sijoittaminen lyhyelle sivulle voi tuottaa siisteimmän lopputuloksen.
Jos tarvitset kolme tai useampia liittimiä, sijoita ne pitkälle sivulle tai molempiin päihin.
Mikään ei estä lisäämästä liittimiä myös kanteen.
Jos suunnitellun asennuspaikan lähellä on pieninkin mahdollisuus kondenssivedelle, kansivuodolle tai muille vesipisaroille, pyri sijoittamaan liittimet niin, että ne lähtevät kotelosta alaspäin.
Näin vesi ei pääse sisään, vaikka liittimet eivät olisi täysin tiiviitä.

Kun sijoitat reiät vaakasuuntaan, varmista että liittimen mutteri mahtuu sekä kotelon kulmakohoumien että viereisten liittimien muttereiden ohi. Pystysuunnassa liitin kannattaa sijoittaa niin ylös kuin järkevästi on mahdollista. Näin liitin ohittaa piirilevyn rimat ja komponentit.
Reiän reuna voi olla 4–5 mm tai 3/16" kannen saumasta.
PG9-läpivientiholkkeja käytettäessä reikä voi joutua vielä lähemmäs kantta.
Poraa varoen!

Sopivat reikäkoot eri liittimille:

- SMA (WiFi-antenni): 6,5–7 mm tai 1/4"
- PG7-läpivientiholkki ja M12-paneeliliitin (NMEA 2000): 12 mm tai 1/2"
- SP13-paneeliliittimet (sinimustat muoviliittimet): 13–14 mm.
  1/2" toimii todennäköisesti hieman vääntelemällä.
- PG9-läpivientiholkki: 16 mm tai 5/8"

### Paneeliliittimien juottaminen

Kun juotat sisäisiä johtimia paneeliliittimiin, käytä aina kutistesukkaa yksittäisten johtimien päällä.
Muista aina pujottaa kutistesukka johtimeen _ennen_ juottamista...
Paneeliliittimiä juotettaessa pätevät osiossa FIXME annetut yleiset ohjeet.
Yleensä juotostinaa kannattaa ensin lisätä liittimen nastan koloon ja sitten sulattaa tina uudelleen ja työntää johdin paikalleen.
