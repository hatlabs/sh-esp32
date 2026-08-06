---
translated_from: 084cd1408161097c726316ef08ab9d19ef8fac83
---

# SH-ESP32 Engine Top Hatin aloitusopas

## Laitteiston asennus

Engine Hat on tarkoitettu käytettäväksi SH-ESP32:n kanssa.
Asenna Engine Hat kohdistamalla se SH-ESP32:n I2C- ja GPIO-liittimiin ja painamalla alas, kunnes liittimien nastat ovat täysin paikoillaan.
Katso tarkka kohdistus alla olevista kuvista.

![Engine Hatin kohdistus](assets/EH_Layout_emphasized.jpg "Engine Hatin kohdistus"){ width="50%" }

Engine Hatin ääriviivat sinisellä ja liittyvät liittimet korostettuna punaisella:

![Engine Hatin kohdistuksen ääriviivat](assets/EH_Layout_outline.jpg "Engine Hatin kohdistuksen ääriviivat"){ width="50%" }

## Tankkianturien ja muiden vastusanturien kytkentä

Analogia- ja digitaalitulot ovat kortin pinottavissa vaakaliittimissä.
Tulot ovat ylärivissä, kun taas alarivi on kytketty maahan.

Vastusanturit ovat antureita tai sähkömekaanisia laitteita, jotka muuntavat mekaanisen, lämpötila-, paine- tai muun signaalin sähköiseksi vastukseksi.
Ne ovat siis passiivisia laitteita eivätkä tuota sähköä.
Lyhyesti sanottuna vastusantureita voi ajatella hienostuneina potentiometreinä eli säädettävinä vastuksina.

Engine Hat käyttää vakiovirtalähdettä vastusarvojen mittaamiseen.
Analogiatulon nastan läpi lähetetään 10 mA:n virta, ja nastan ja maan välinen jännite mitataan.
Mitattavissa ovat vastusarvot lähes 0 ohmista noin 300 ohmiin.
Tämä alue kattaa sekä tyypilliset eurooppalaiset (0–180 ohmia) että amerikkalaiset (240–33 ohmia) tankkianturit sekä yleiset öljynpaineanturit.

Kytke anturi liittämällä anturin mittausnasta analogiatulokanavan ylempään nastaan.
Anturin maanasta kytketään alempaan nastaan.

Alla oleva valokuva havainnollistaa potentiometrin kytkemistä Engine Hatiin.

![Vastusanturin kytkentä](assets/EH_resistive_sensor_1200.jpg "Vastusanturin kytkentä"){ width="50%" }

Oletuksena analogiatulot on määritetty passiivisiksi jännitemittausantureiksi.
Analogiatulojen vakiovirtalähde on otettava erikseen käyttöön asettamalla hyppy CCS-liittimen kyseisen rivin yli alla olevan valokuvan mukaisesti:

![CCS:n käyttöönotto](assets/EH_CCS_jumper_1200.jpg "CCS:n käyttöönotto"){ width="50%" }

### Tankkianturien kytkentä olemassa olevien mittarien kanssa

Jos haluat pitää olemassa olevan polttoainetankin mittarin kytkettynä, voit turvallisesti kytkeä Engine Hatin sen rinnalle.
Tässä tapauksessa alkuperäinen mittari kuitenkin tuottaa mittausvirran, etkä **saa** ottaa vakiovirtalähdettä käyttöön.
Tällöin Engine Hat tekee yksinkertaisen jännitemittauksen.

## Jännitteiden mittaus

Engine Hatin analogiatuloja voi käyttää myös passiiviseen jännitemittaukseen.
Mittausalue on 0–29 V.

Kytke mitattava jännite samaan tapaan kuin edellä kuvattu tankkianturi, mutta jätä vakiovirtalähde pois käytöstä.
Kiinnitä huomiota napaisuuteen!
Väärä napaisuus voi vaurioittaa laitteen.

## Hälytysten ja muiden binääristen lähtöjen kytkentä

Digitaalituloilla voi havaita moottorihälytyksiä ja muita vastaavia signaaleja.
Kytke ne digitaalitulojen liittimeen siten, että jännitteellinen johdin menee ylimpään riviin ja maa alimpaan.
Tulot tukevat 0–30 V:n jännitealuetta, ja logiikkatason vaihdon kynnysjännite on kiinteä 1,65 V.
Negatiiviset jännitteet ovat sallittuja.

## Kierroslukumittarien (RPM-anturien) kytkentä

Digitaalituloilla voi mitata kierroslukumittarien kierroslukua tai muita toistuvia pulssimittauksia, kuten polttoaineen virtausmittareita.
Kytke ne kuten hälytykset: jännitteellinen johdin ylimpään riviin ja maa alimpaan.
Sekä laturin W-navat että induktiiviset kierroslukuanturit, kuten Yanmar-moottoreissa käytettävät, voi kytkeä suoraan.

**HUOMAA:** Jos mittaat kierroslukua laturin W-navasta, GND-johdin kannattaa ehkä jättää kytkemättä.
Ladattaessa laturin GND on todennäköisesti eri jännitteessä kuin akun miinusnapa (veneesi tyypillinen vertailumaa).
Negatiivisen signaalijohtimen kytkeminen laturista Engine Hatin GND-nastaan aiheuttaisi todennäköisesti maasilmukan:
jännite-eron takia GND-johtimessa kulkisi virta, mikä voi aiheuttaa runsaasti matalataajuista häiriötä.

Jotkin kierroslukuanturit, kuten laturin W-navat, ovat tunnetusti häiriöisiä, mikä johtaa epäluotettaviin mittauksiin.
Tällaisissa tapauksissa ilmoitettu kierroslukuarvo on yleensä paljon todellista suurempi.
Engine Hatissa on valinnainen alipäästösuodin, jonka rajataajuus on 2,3 kHz ja joka auttaa suodattamaan tällaista häiriötä.
Ota alipäästösuodin käyttöön digitaalitulokanavalle asettamalla hyppy LP EN -liittimen kyseisen rivin yli:

![Alipäästösuotimen käyttöönotto](assets/EH_digital_input_1200.jpg "Alipäästösuotimen käyttöönotto"){ width="50%" }

Huomaa, että laitteistosuodin auttaa vain tiettyyn rajaan asti.
Erityisen häiriöisillä tulosignaaleilla luotettavat tulokset voivat vaatia lisäksi ohjelmallista suodatusta.

## Ohjelmisto

Esimerkkifirmware löytyy [SH-ESP32-engine-hat-firmware](https://github.com/hatlabs/SH-ESP32-engine-hat-firmware) -GitHub-repositoriosta.
