# Lödning för nybörjare

En praktisk guide för att komma igång med lödning av elektronik, från de första lödningarna till SMD och enklare reparationer.

---

## 1. Min nuvarande utrustning

Jag har redan:

* [x] Lödkolv/lödpenna
* [x] Stativ till lödkolven
* [x] Hållare/tredje hand
* [x] Lödtenn med fluxkärna
* [x] Avlödningsfläta
* [x] Isopropanol (IPA)
* [x] Multimeter

### Bra kompletteringar

* [ ] Mässingsull/lödspetsrengöring
* [ ] Tennsug
* [ ] Elektronikpincetter
* [ ] Små sidavbitare
* [ ] Bra arbetsbelysning
* [ ] Fluxpenna
* [ ] 0,3–0,5 mm lödtenn för mindre komponenter
* [ ] Värmekrympslang
* [ ] Kaptontejp
* [ ] Förstoringsglas eller USB-mikroskop
* [ ] Rökutsug eller bra ventilation
* [ ] ESD-armband/matta om jag börjar arbeta med känsliga IC-kretsar

Jag behöver inte köpa allt på en gång. Först är pincetter, sidavbitare, mässingsull och tennsug mest användbara.

---

# 2. Lär dig i rätt ordning

Jag bör inte börja med små SMD-komponenter direkt.

Rekommenderad ordning:

1. Förstå hur lödning fungerar
2. Lära mig förtenna lödspetsen
3. Löda kablar
4. Through-hole/PTH-komponenter
5. Avlödning
6. Lära mig känna igen dåliga lödningar
7. Bygga ett enkelt elektronikprojekt
8. Börja med större SMD-komponenter
9. Gå vidare till mindre SMD
10. Lära mig reparation och felsökning

---

# 3. Första guiden – iFixit

## iFixit: Soldering 101

En mycket bra nybörjarguide som går igenom:

* verktyg
* arbetsplats
* säkerhet
* through-hole-lödning
* avlödning
* grundläggande teknik

Guide:

iFixit – Soldering 101
https://www.ifixit.com/News/6864/how-to-solder

Det finns även en samlingssida med flera olika lödguider:

iFixit – Learn How to Solder
https://www.ifixit.com/soldering

---

# 4. SparkFun – Through-Hole lödning

Det här är en av de guider jag bör följa praktiskt.

SparkFun går igenom:

* vad lödtenn är
* lödkolvar
* tillbehör
* första komponenten
* korrekt lödteknik
* felsökning
* avlödning
* vidare tekniker

Guide:

SparkFun – How to Solder: Through-Hole Soldering
https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/all

## Viktiga punkter från SparkFun

En bra grundteknik är:

1. Värm upp lödkolven.
2. Rengör och förtenna spetsen.
3. Placera komponenten.
4. Värm både komponentens ben och PCB-paden.
5. Mata in lödtenn mot den uppvärmda kontakten.
6. Ta bort lödtennet.
7. Ta bort lödkolven.
8. Låt lödningen svalna.

En bra lödning ska normalt bli en jämn liten "vulkan"/konform runt komponentens ben.

Undvik att skapa en stor rund kula av lödtenn.

---

# 5. Adafruit – Excellent Soldering

Adafruits guide är bra när jag vill förstå detaljerna bättre.

Den går bland annat igenom:

* val av lödspets
* lödstation
* verktyg
* förtenning
* teknik
* hur man får bra lödfogar

Guide:

Adafruit – Guide to Excellent Soldering
https://learn.adafruit.com/adafruit-guide-excellent-soldering

Adafruit har även en introduktion som fokuserar på praktisk lödning för nybörjare:

Getting Started with Soldering
https://www.adafruit.com/product/3715

---

# 6. Video – iFixit Soldering 101

Bra video om jag hellre vill se processen än läsa om den.

iFixit – Soldering 101
https://www.youtube.com/watch?v=rK38rpUy568

Videon går bland annat igenom:

* verktyg
* säkerhet
* through-hole
* lödning
* avlödning
* tips och tricks

---

# 7. Säkerhet

Grundregler:

### Lödkolven är mycket varm

* Rör aldrig spetsen.
* Lägg alltid tillbaka lödkolven i stativet.
* Ha en stabil arbetsyta.
* Håll kablar och annat brännbart borta från spetsen.

### Lödångor

Flux kan skapa rök när det värms.

Arbeta i ett välventilerat rum eller använd rökutsug.

Försök att inte ha ansiktet direkt ovanför lödpunkten.

### Lödtenn

Om lödtennet innehåller bly:

* tvätta händerna efter lödning
* ät och drick inte vid arbetsplatsen
* undvik att röra ansiktet under arbetet
* rengör arbetsytan efteråt

Använd gärna skyddsglasögon eftersom små mängder smält lödtenn kan stänka.

### Viktigt

Löd aldrig på en krets som är strömsatt.

Koppla bort:

* USB
* nätadapter
* batteri
* annan strömförsörjning

innan jag börjar löda.

---

# 8. Förtenna lödspetsen

En av de viktigaste grundkunskaperna.

En ren lödspets ska normalt ha ett tunt lager lödtenn på sig.

Exempel:

```text
Dåligt:

[ torr spets ]


Bra:

[ ~tenn~ ]
```

Gör ungefär:

1. Rengör spetsen.
2. Lägg lite lödtenn på spetsen.
3. Låt ett tunt lager täcka spetsen.
4. Börja löda.

Tennet hjälper till att överföra värme mellan spetsen och komponenten.

---

# 9. Använd rätt del av spetsen

Använd inte bara den allra yttersta spetsen.

Den bredare delen av spetsen kan överföra mer värme.

```text
          spets
            ↓
        /-------\
       /         \
======/===========\======

       ↑
   bra kontaktyta
```

Försök få bra fysisk kontakt mellan:

```text
lödkolv
   ↓
komponent + PCB-pad
```

inte bara mellan:

```text
lödkolv → lödtenn
```

---

# 10. Hur en bra lödning ser ut

### Bra

```text
       komponentben
           │
           │
        ╱──┴──╲
       ╱       ╲
──────●─────────●────── PCB
```

Lödtennet ska ha flutit ut över både komponentens ben och PCB-paden.

### Dåligt – för lite tenn

```text
       │
       │
───────●────────
```

### Dåligt – för mycket tenn

```text
       │
      ███
──────████──────
```

### Dåligt – kall lödning

Kan se matt, ojämn eller dåligt sammanfluten ut.

Om något ser misstänkt ut:

1. värm upp fogen igen
2. tillsätt lite flux
3. låt lödtennet flyta
4. ta bort värmen
5. låt svalna

---

# 11. Avlödning

Jag har redan avlödningsfläta.

Grundprincip:

```text
PCB
────────────────

     █████
     lödtenn
       ↓
     [fläta]
       ↑
    lödkolv
```

Placera flätan över lödtennet.

Värm flätan med lödkolven.

När tennet smälter sugs det upp i flätan.

Ta bort lödkolven och flätan tillsammans.

Klipp bort den använda delen av flätan.

---

# 12. Tennsug

Tennsug är särskilt användbart när det finns mycket lödtenn.

Princip:

```text
1. Värm lödningen

       ↓
     █████
──────●──────


2. Aktivera tennsugen

       ↓
      [←]
     █████
──────●──────


3. Tennet sugs bort
```

Avlödningsfläta och tennsug kompletterar varandra.

---

# 13. Flux

Flux hjälper lödtennet att flyta och förbättrar kontakten mellan metallerna.

Mitt lödtenn har redan fluxkärna, vilket räcker långt.

Extra flux kan ändå vara användbart vid:

* SMD
* gammal oxidation
* avlödning
* reparation
* svåra lödfogar

En fluxpenna är därför ett bra framtida inköp.

---

# 14. Isopropanol

IPA kan användas för att rengöra PCB efter lödning.

Exempel:

```text
Lödning
   ↓
Fluxrester
   ↓
IPA
   ↓
Rengör PCB
```

Använd exempelvis:

* IPA 90–99 %
* tops
* luddfri trasa

Kontrollera alltid att komponenten/kretskortet tål rengöringen.

Kom ihåg att IPA är brandfarligt och ska användas med god ventilation och borta från lödkolvens heta delar.

---

# 15. Multimetern

Multimetern kommer bli ett av mina viktigaste verktyg.

Jag bör lära mig:

### Continuity / summer

Kontrollera om två punkter har elektrisk kontakt.

```text
A ●────────● B
```

### Resistans

Kontrollera motstånd.

### DC Voltage

Kontrollera exempelvis:

```text
5 V
3.3 V
12 V
```

### Diode mode

Användbart för att testa dioder och LED.

---

# 16. Kontrollera alltid PCB:n innan ström kopplas in

Efter lödning:

### 1. Inspektera visuellt

Leta efter:

* lödtennsbryggor
* lösa komponenter
* dåliga lödningar
* felvända komponenter
* lödtenn på fel pad

### 2. Använd multimetern

Kontrollera kritiska punkter.

Exempel:

```text
5V ───────────── GND
```

ska normalt **inte** ha en kortslutning.

### 3. Kontrollera polaritet

Var extra noga med:

* LED
* dioder
* elektrolytkondensatorer
* IC-kretsar
* batterier

---

# 17. Första övningen

Jag bör inte börja med ett dyrt Raspberry Pi-, ESP32- eller Arduino-kort.

Köp ett billigt:

* perfboard
* övnings-PCB
* några motstånd
* LEDs
* kondensatorer
* headers
* lite kabel

Öva på:

```text
1. Löda en kabel
2. Löda två kablar tillsammans
3. Löda en resistor
4. Löda en LED
5. Löda headers
6. Avlöda komponenterna
7. Löda dit dem igen
```

Målet är inte att få det perfekt direkt.

Målet är att få en känsla för:

* temperatur
* hur snabbt tennet flyter
* hur mycket tenn som behövs
* hur mycket värme komponenten tål
* hur en bra lödning ser ut

---

# 18. Nästa steg – SMD

När through-hole känns enkelt kan jag börja med SMD.

Rekommenderad ordning:

```text
Through-hole
     ↓
0805 SMD
     ↓
0603 SMD
     ↓
SOIC
     ↓
TSSOP
     ↓
QFN / mindre komponenter
```

Börja inte med de allra minsta komponenterna.

SMD kräver framför allt:

* bra belysning
* pincett
* flux
* finare lödspets
* tunnare lödtenn
* förstoringsglas/mikroskop

iFixit har även en särskild introduktion till microsoldering när jag kommer till den nivån:

https://www.ifixit.com/News/98168/microsoldering-beginners-guide-its-easier-than-you-think

---

# 19. Bra resurser att spara

## Nybörjare

### iFixit – Soldering 101

https://www.ifixit.com/News/6864/how-to-solder

### SparkFun – Through-Hole Soldering

https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/all

### Adafruit – Excellent Soldering

https://learn.adafruit.com/adafruit-guide-excellent-soldering

---

## Avlödning och reparation

### iFixit – Solder & Desolder Connections

https://www.ifixit.com/Guide/How%2BTo%2BSolder%2Band%2BDesolder%2BConnections/750

---

## SMD / Microsoldering

### iFixit – Microsoldering Beginner's Guide

https://www.ifixit.com/News/98168/microsoldering-beginners-guide-its-easier-than-you-think

---

## Video

### iFixit – Soldering 101

https://www.youtube.com/watch?v=rK38rpUy568

---

# 20. Min rekommenderade inlärningsplan

## Nivå 1 – Grunder

* [ ] Förstå lödtenn
* [ ] Förstå flux
* [ ] Förtenna spetsen
* [ ] Lära mig hålla lödkolven korrekt
* [ ] Löda kablar
* [ ] Göra en enkel lödfog

## Nivå 2 – Through-hole

* [ ] Motstånd
* [ ] Kondensatorer
* [ ] LEDs
* [ ] Dioder
* [ ] Transistorer
* [ ] Headers
* [ ] Perfboard

## Nivå 3 – Avlödning

* [ ] Avlödningsfläta
* [ ] Tennsug
* [ ] Ta bort through-hole-komponent
* [ ] Rengöra PCB med IPA
* [ ] Reparera en dålig lödning

## Nivå 4 – Felsökning

* [ ] Continuity
* [ ] Mäta resistans
* [ ] Mäta DC-spänning
* [ ] Kontrollera kortslutningar
* [ ] Följa en PCB-bana
* [ ] Läsa ett enkelt kopplingsschema

## Nivå 5 – SMD

* [ ] 0805
* [ ] 0603
* [ ] SOIC
* [ ] SMD-avlödning
* [ ] SMD-reparation
* [ ] Microsoldering

---

# 21. Viktigaste regeln

Lägg inte för mycket fokus på att få lödningen perfekt direkt.

**Öva mycket på billiga komponenter.**

Efter några timmar kommer jag börja utveckla en känsla för:

> "Den här fogen är varm nog."

> "Här behöver jag lite mer flux."

> "Det där är för mycket tenn."

> "Det där ser ut som en kall lödning."

Det är den känslan som gör lödning mycket enklare.

---

# Kort checklista innan jag börjar

```text
[ ] Arbetsytan är fri
[ ] Lödkolven står stabilt
[ ] Bra ventilation
[ ] IPA finns tillgängligt
[ ] Multimeter finns
[ ] Avlödningsfläta finns
[ ] Lödtenn finns
[ ] Spetsen är ren
[ ] Spetsen är förtennad
[ ] PCB:n sitter fast
[ ] Strömmen är AV
```

När jag är klar:

```text
[ ] Kontrollera lödningarna visuellt
[ ] Leta efter lödtennsbryggor
[ ] Kontrollera polaritet
[ ] Mät kritiska punkter med multimeter
[ ] Kontrollera kortslutningar
[ ] Rengör PCB vid behov
[ ] Låt utrustningen svalna
[ ] Tvätta händerna
```

---

## Bra princip att komma ihåg

**Värm komponent + pad → mata in tenn → låt tennet flyta → ta bort tenn → ta bort värme → låt svalna.**

Det är grunden för nästan all vanlig handlödning.
