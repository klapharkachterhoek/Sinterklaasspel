# 🎲 Sinterklaasspel

Een virtueel Sinterklaas-dobbelspel voor de pakjesavond, met ook een **kerstmodus**. Je gooit met een 3D-dobbelsteen en het aantal ogen bepaalt een taak, zoals "Pak een cadeau van de stapel" of "Steel een cadeau van een andere speler". Een grote timer laat zien hoeveel speeltijd er nog over is.

Het spel draait in de browser op **Windows** en op **Linux Mint**. Je hoeft niets te installeren, en het werkt ook zonder internet.

## Starten

| Systeem | Hoe |
|---|---|
| Windows | Dubbelklik `start-windows.bat` (opent schermvullend in Edge) |
| Linux Mint | `./start-linux.sh` (Chrome/Chromium, anders Firefox, in kioskmodus) |
| Overal | Open `index.html` in een browser |

Afsluiten in kioskmodus doe je met **Alt+F4**.

De startscripts starten ook `server.py` als Python aanwezig is (op Mint zit Python er standaard in). Je instellingen worden dan opgeslagen in **`config.json`**. Zonder Python bewaart de browser ze zelf. Met **Exporteren/Importeren** in het configscherm zet je ze over naar een andere computer.

## Spelen

- **Gooien:** tik op de dobbelsteen, klik op **Gooi!** of druk op **Spatie/Enter**. Welke toetsen dat zijn, stel je zelf in.
- **Timer:** de eerste worp start de klok. Met **Pauze** zet je de tijd stil, en met **Nieuw spel** begint alles opnieuw. In de laatste minuut gaat de timer knipperen.
- **Taak uitzetten:** onder elke taak staat het vinkje *"Deze taak niet meer gebruiken in dit spel"*. Handig als bijvoorbeeld het laatste cadeau van de stapel al gepakt is. Onderin het scherm staat een strook met alle taken. Tik op een taak om hem uit of weer aan te zetten. Bij *Nieuw spel* doen alle taken weer mee.

## 🎄 Kerstmodus

Met de knop **🎄 Kerst** rechtsboven (of via ⚙ → *Thema*) schakel je over naar de kerstversie. Die heeft een groene achtergrond met sneeuw, knipperende kerstlichtjes, een kerstboom, groene ogen op de dobbelsteen, een eigen titel en eindtekst, en een Jingle Bells-deuntje bij elke taak. Met **🎁 Sint** ga je terug. De keuze wordt bewaard.

Per taak bepaal je met **Thema** of hij meedoet bij Sinterklaas, bij Kerst of bij allebei. In de standaardset is het Sinterklaasliedje bij Kerst vervangen door een kerstliedje.

## Photobooth-hardware

- Een **arcade-/buzzerknop** die zich als toetsenbord gedraagt, werkt direct (standaard Spatie of Enter). Andere toetsen leg je vast via ⚙ → *Toetsen om te gooien* → *Toets toevoegen*, waarna je de knop indrukt.
- Een **USB-gamepad of arcade-encoder** (zero-delay encoder) werkt ook: elke knop gooit. Dit zet je aan of uit met de optie *Gamepad / USB-knop*.
- **Touchscreen:** tik op de dobbelsteen.
- Tijdens het spel blijft het scherm aan, als de browser dat ondersteunt.

## Instellingen (⚙ of F2)

| Instelling | Standaard |
|---|---|
| Thema | Sinterklaas (of Kerst) |
| Totale speltijd | 15 minuten |
| Duur van het gooien | 5 seconden |
| Gedrag als een getal geen taak heeft | alleen getallen gooien die nu een taak hebben |
| Geluid, pepernotenregen, gamepad | aan |

### Taken (`config.json`)

```json
{ "id": "t7", "ogen": 6, "thema": "beide", "emoji": "🕵️", "tekst": "Steel een cadeau van een andere speler",
  "beschikbaarVanaf": 5, "beschikbaarTot": null, "actief": true }
```

- `ogen`: het aantal ogen (1–6) waar de taak bij hoort. Meerdere taken per getal mag; dan kiest het spel willekeurig één van de taken die op dat moment beschikbaar zijn.
- `beschikbaarVanaf` / `beschikbaarTot`: het tijdvak waarin de taak meedoet, in minuten sinds de start. `null` betekent tot het einde. In de standaardset geeft een 6 de eerste 5 minuten "pak een cadeau en gooi nog eens", en daarna "steel een cadeau".
- `thema`: `"beide"`, `"sinterklaas"` of `"kerst"`.
- `actief`: met `false` doet de taak helemaal niet mee.

Je bewerkt de taken in het tabblad **Taken**, of direct als JSON in het tabblad **JSON**.

## Bestanden

- `index.html`: het complete spel (HTML, CSS en JavaScript in één bestand)
- `config.json`: de taken en instellingen
- `server.py`: optionele lokale server (alleen de Python-standaardbibliotheek, luistert alleen op 127.0.0.1)
- `start-windows.bat`, `start-linux.sh`: starten in kioskmodus

## Versies

Het versienummer staat onderin het scherm achter "Gemaakt door Klaphark Achterhoek" (constante `VERSIE` in `index.html`). Opbouw: datum (`jjjjmmdd`) plus een volgnummer van twee cijfers.

| Versie | Wijzigingen |
|---|---|
| 2026112301 | Alle taken passen nu altijd in beeld, ook op kleinere of lagere schermen: de takenstrook verkleint zichzelf als het nodig is, de dobbelsteen en de taakkaart schalen mee met de beschikbare ruimte, lange taakteksten worden kleiner gezet, en ook op een staand scherm past alles zonder scrollen. Versienummer toegevoegd. |

---

Gemaakt door **Klaphark Achterhoek** · versie 2026112301.
