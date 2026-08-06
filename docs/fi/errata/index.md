---
translated_from: 35671f1b525327fd13864d1a07c971b5c93752e1
---

# Tunnetut virheet

Tällä sivulla luetellaan kaikki tunnetut laitteistoviat SH-ESP32:n eri versioissa.

## Silkkipainon virheet

### GPIO 1:n ja 3:n juotossiltojen merkinnät

Kortin alapuolen juotossiltojen silkkipainomerkinnät GPIO-nastoille 1 ja 3 ovat virheelliset.
USB-sarjaliikenteeseen käytettävien TXD0- ja RXD0-nastojen juotossillat on merkitty numeroilla 3 ja 34, vaikka niiden pitäisi olla 1 ja 3.

<figure markdown="span">
![Juotossillat, alapuoli](assets/sh-esp32_r0.3.1_bottom_jumpers_errata_1_3.jpg "SH-ESP32:n GPIO 1:n ja 3:n silkkipainovirhe")
<figcaption>Ympyröidyn alueen juotossiltojen merkintöjen 3 ja 34 pitäisi olla 1 ja 3.</figcaption>
</figure>

Koskee kortteja versioon 0.3.1 asti.
