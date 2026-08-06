---
translated_from: 3b83f2f7ac97ee531b9280fa6ad26f439fe7d588
---

# Laitteistoversiot

## Johdanto

Tällä sivulla kuvataan kortin eri versiot ja tarjotaan linkit kytkentäkaavioihin. Suunnittelutiedostojen koko historia on saatavilla [SH-ESP32-hardware -GitHub-repositoriossa](https://github.com/hatlabs/SH-ESP32-hardware).

## Versio 0.3.1

Ensimmäinen versio, jota myytiin osoitteessa [hatlabs.fi](https://hatlabs.fi).

Kytkentäkaaviot: [SH-ESP32-0.3.1-schema.pdf](assets/SH-ESP32-0.3.1-schema.pdf)

## Versio 1.0.0

Muutokset versioon 0.3.1:

- Ohituskondensaattorit siirretty kauemmas kiinnitysrei'istä
- Korjattu GPIO 1:n ja 3:n juotossiltojen virheelliset silkkipainomerkinnät
- Parannettu 2×3-virtaliittimen silkkipainoa
- Vaihdettu joitakin komponentteja saatavuuden mukaan

Kytkentäkaaviot: [SH-ESP32-1.0.0-schema.pdf](assets/SH-ESP32-1.0.0-schema.pdf)


## Versio 2.0.0

Muutokset versioon 1.0.0:

- Vaihdettu jännitetulon alentava hakkuri XL1509:ään osien paremman saatavuuden vuoksi
- ISO1050-erotetun CAN-lähetinvastaanottimen tilalla käytetään erillistä digitaalista erotinta ja lähetinvastaanotinta
- Käytetään Phoenix MC -tyyppisiä 3,81 mm:n irrotettavia ruuviliittimiä jännitetulon ja CAN-väylän liittiminä. Nämä liittimet ovat mekaanisesti kestävämpiä ja helpompikäyttöisiä kuin aiemmin käytetyt JST XH -tyyppiset liittimet.
- Liittimet ja nastarimat on nyt juotettu valmiiksi korttiin

Kytkentäkaaviot: [SH-ESP32-2.0.0-schema.pdf](assets/SH-ESP32-2.0.0-schema.pdf)

## Versio 2.0.1

- Pieniä osamuutoksia saatavuuden parantamiseksi

Kytkentäkaaviot: [SH-ESP32-2.0.1-schema.pdf](assets/SH-ESP32-2.0.1-schema.pdf)

## Versio 2.0.2

- Pieniä parannuksia ESD-suojaukseen
- Pieniä osamuutoksia valmistajan osasaatavuuden mukaan

## Versio 2.0.3

- Pieniä osamuutoksia valmistajan osasaatavuuden mukaan

Kytkentäkaaviot: [SH-ESP32-2.0.3-schema.pdf](assets/SH-ESP32-2.0.3-schema.pdf)
