---
translated_from: 834be651f7ac729e1ea5c209458cee33a551f7b9
---

# Johdanto

Sailor Hat with ESP32 (SH-ESP32) on tehokas mikro-ohjaimen kehityskortti veneympäristöön.

![SH-ESP32 ylhäältä](media/sh-esp32_r2.0.0_top_render.jpg "SH-ESP32 Rev. 2 ylhäältä"){ width="60%" }

*SH-ESP32 Rev. 2 ylhäältä.*

SH-ESP32:lla voit helposti rakentaa kaikenlaisia antureita ja ohjausliitäntöjä veneeseesi.
Esimerkkejä ovat kierrosluku- sekä polttoaine- ja vesitankkimittarit, pilssihälyttimet, ketjulaskurit, sähköiset kompassit, asentoanturit ja niin edelleen.
Ohjausliitäntöjen esimerkkejä ovat konehuoneen puhaltimen automaattiohjaus, älykäs valaistuksen ohjaus tai älykkäät jääkaapin termostaatit.
Se integroituu helposti sekä [Signal K](https://signalk.org/):hon että NMEA 2000:een, ja sitä voi käyttää NMEA 2000 -yhdyskäytävälaitteena.

SH-ESP32:n voi kytkeä suoraan mihin tahansa 12 V:n tai 24 V:n järjestelmään.
Sähköiseen yhteensopivuuteen on kiinnitetty erityistä huomiota: kortti kestää useimmat ajoneuvo- ja veneympäristön 12 V:n ja 24 V:n järjestelmissä esiintyvät jännitepiikit.
Yhtä tärkeää on, että tulot ja lähdöt on suojattu sähköstaattisilta purkauksilta (staattiselta sähköltä), ne on suunniteltu tuottamaan mahdollisimman vähän sähkömagneettisia päästöjä (eivät häiritse muita herkkiä laitteita, kuten VHF-radioita tai GPS-antenneja) ja ne on suojattu sähkömagneettisilta häiriöiltä (VHF, SSB tai tutka ei häiritse niitä).

SH-ESP32 on avointa laitteistoa, lisensoitu Creative Commons Nimeä-JaaSamoin 4.0 Kansainvälinen -lisenssillä.
Voit tehdä siitä omia sovelluksiasi, kunhan jaat ne vastaavin ehdoin!

## Laitteiston hankkiminen

Valmiita CE-sertifioituja SH-ESP32-kortteja voi ostaa [Hat Labs Oy:ltä](https://hatlabs.fi).
Kaikki suunnittelutiedostot ovat myös saatavilla [SH-ESP32:n laitteistorepositoriossa GitHubissa](https://github.com/hatlabs/sh-esp32-hardware/).

## NMEA 2000 -yhteensopivuus

SH-ESP32 on avointa laitteistoa, ja tarjottu sekä suositeltu ohjelmisto on avointa lähdekoodia sallivilla ohjelmisto- ja laitteistolisensseillä. NMEA 2000 on National Marine Electronics Associationin (NMEA) omisteinen standardi. NMEA:n lisensointi- ja sertifiointiprosessit ovat perustavalla tavalla yhteensopimattomia avoimen lähdekoodin kehityksen kanssa, ja vaikka tässä dokumentaatiossa viitataan useaan otteeseen NMEA 2000:een, Hat Labs Oy:n tuotteita ei ole eikä tulla sertifioimaan NMEA:n toimesta.

Sekä laboratoriossa että todellisissa olosuhteissa on kuitenkin tehty paljon työtä sen varmistamiseksi, että SH-ESP32 on sähköisesti yhteensopiva NMEA 2000:n kanssa ja että toimitettu esimerkkiohjelmisto on yhteensopiva NMEA 2000 -tiedonsiirtoprotokollan kanssa.
