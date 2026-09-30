# Soldering for Beginners

A practical beginner's guide to soldering electronics, from the first solder joint to SMD soldering and basic electronics repair.

---

# 1. My Current Equipment

I already have:

* [x] Soldering iron / soldering pen
* [x] Soldering iron stand
* [x] Helping hands / PCB holder
* [x] Solder wire with flux core
* [x] Desoldering braid
* [x] Isopropyl alcohol (IPA)
* [x] Multimeter

## Useful additions

* [ ] Brass wool / soldering tip cleaner
* [ ] Desoldering pump / solder sucker
* [ ] Electronics tweezers
* [ ] Small electronics side cutters
* [ ] Good work light
* [ ] Flux pen
* [ ] 0.3–0.5 mm solder wire for smaller components
* [ ] Heat-shrink tubing
* [ ] Kapton tape
* [ ] Magnifying glass or USB microscope
* [ ] Fume extraction or good ventilation
* [ ] ESD wrist strap / ESD mat for sensitive electronics

I do not need to buy everything immediately.

The most useful additions are:

1. Brass wool
2. Desoldering pump
3. Electronics tweezers
4. Small side cutters
5. Good lighting

---

# 2. Learn in the Right Order

I should not start with tiny SMD components immediately.

A good progression is:

1. Understand how soldering works
2. Learn how to tin a soldering tip
3. Practice soldering wires
4. Learn through-hole (THT/PTH) soldering
5. Learn desoldering
6. Learn how to identify bad solder joints
7. Build a simple electronics project
8. Start with larger SMD components
9. Move to smaller SMD components
10. Learn basic electronics repair and troubleshooting

---

# 3. First Guide – iFixit

## iFixit: Soldering 101

A very good beginner introduction covering:

* Tools
* Workspace
* Safety
* Through-hole soldering
* Desoldering
* Basic soldering technique

Guide:

https://www.ifixit.com/News/6864/how-to-solder

iFixit also has a soldering guide collection:

https://www.ifixit.com/soldering

---

# 4. SparkFun – Through-Hole Soldering

This is one of the guides I should follow practically.

SparkFun covers:

* What solder is
* Soldering irons
* Accessories
* Your first component
* Proper soldering technique
* Troubleshooting
* Desoldering
* More advanced techniques

Guide:

https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/all

## Important points

A basic soldering technique is:

1. Heat the soldering iron.
2. Clean and tin the tip.
3. Place the component.
4. Heat both the component lead and PCB pad.
5. Feed solder onto the heated joint.
6. Remove the solder.
7. Remove the soldering iron.
8. Let the joint cool.

A good solder joint should normally form a smooth, slightly conical shape around the component lead.

Avoid creating a large ball of solder.

---

# 5. Adafruit – Excellent Soldering

Adafruit's guide is useful when I want to understand the details better.

It covers:

* Choosing soldering tips
* Soldering stations
* Tools
* Tinning
* Soldering technique
* Creating good solder joints

Guide:

https://learn.adafruit.com/adafruit-guide-excellent-soldering

Adafruit also has beginner-oriented soldering resources:

https://www.adafruit.com/product/3715

---

# 6. Video – iFixit Soldering 101

A good video if I prefer seeing the process rather than just reading about it.

iFixit – Soldering 101:

https://www.youtube.com/watch?v=rK38rpUy568

The video covers:

* Tools
* Safety
* Through-hole soldering
* Soldering
* Desoldering
* Tips and techniques

---

# 7. Safety

## The soldering iron is extremely hot

* Never touch the tip.
* Always put the soldering iron back in its stand.
* Keep the work surface stable.
* Keep cables and flammable materials away from the tip.

## Soldering fumes

Flux can produce fumes when heated.

Work in a well-ventilated room or use a fume extractor.

Avoid placing your face directly above the soldering point.

## Solder

If the solder contains lead:

* Wash your hands after soldering.
* Do not eat or drink at the workbench.
* Avoid touching your face while working.
* Clean the work surface after soldering.

Safety glasses are also a good idea because small amounts of molten solder can occasionally splatter.

## Important

Never solder on a powered circuit.

Disconnect:

* USB
* Power adapters
* Batteries
* Other power supplies

before soldering.

---

# 8. Tinning the Soldering Tip

One of the most important basic skills.

A clean soldering tip should normally have a thin layer of solder on it.

```text
Bad:

[ dry tip ]


Good:

[ ~solder~ ]
```

Basic procedure:

1. Clean the tip.
2. Apply a small amount of solder.
3. Let a thin layer cover the tip.
4. Start soldering.

The solder helps transfer heat between the tip and the component.

---

# 9. Use the Correct Part of the Tip

Do not always use only the very tip of the soldering iron.

The wider part of the tip can transfer more heat.

```text
          tip
           ↓
       /-------\
      /         \
=====/===========\=====

       ↑
   contact area
```

Try to create good physical contact between:

```text
soldering iron
      ↓
component + PCB pad
```

rather than only:

```text
soldering iron → solder
```

---

# 10. What a Good Solder Joint Looks Like

## Good

```text
       component lead
             │
             │
          ╱──┴──╲
         ╱       ╲
────────●─────────●──────── PCB
```

The solder should flow over both the component lead and the PCB pad.

## Too little solder

```text
       │
       │
───────●────────
```

## Too much solder

```text
       │
      ███
     █████
──────████──────
```

## Cold solder joint

A cold solder joint may look:

* Dull
* Rough
* Uneven
* Poorly connected

If a joint looks suspicious:

1. Reheat the joint.
2. Add a small amount of flux if necessary.
3. Let the solder flow.
4. Remove the heat.
5. Let it cool.

---

# 11. Desoldering

I already have desoldering braid.

Basic principle:

```text
PCB
────────────────

     █████
     solder
       ↓
     [braid]
       ↑
 soldering iron
```

Place the braid over the solder.

Heat the braid with the soldering iron.

When the solder melts, it will be drawn into the braid.

Remove the soldering iron and braid.

Cut off the used section of braid.

---

# 12. Desoldering Pump

A desoldering pump is especially useful when there is a larger amount of solder.

Basic process:

```text
1. Heat the joint

       ↓
     █████
──────●──────


2. Activate the pump

       ↓
      [←]
     █████
──────●──────


3. Solder is removed
```

Desoldering braid and a desoldering pump complement each other.

---

# 13. Flux

Flux helps solder flow and improves the connection between metals.

My solder already contains flux in its core, which is enough for many basic jobs.

Additional flux can still be useful for:

* SMD soldering
* Oxidized components
* Desoldering
* Repairs
* Difficult solder joints

A flux pen is therefore a useful future purchase.

---

# 14. Isopropyl Alcohol

IPA can be used to clean PCBs after soldering.

Typical process:

```text
Soldering
    ↓
Flux residue
    ↓
IPA
    ↓
Clean PCB
```

Useful supplies:

* 90–99% IPA
* Cotton swabs
* Lint-free cloth

Make sure the component or PCB is compatible with IPA.

IPA is highly flammable, so keep it away from the hot soldering iron and other ignition sources.

---

# 15. Using the Multimeter

The multimeter will become one of my most important tools.

I should learn:

## Continuity / buzzer

Check whether two points have an electrical connection.

```text
A ●────────● B
```

## Resistance

Measure resistance.

Useful for checking:

* Resistors
* Wires
* Components
* Unexpected connections

## DC Voltage

Measure things such as:

```text
5 V
3.3 V
12 V
```

## Diode mode

Useful for testing:

* Diodes
* LEDs
* Some semiconductor junctions

---

# 16. Check the PCB Before Applying Power

After soldering:

## 1. Inspect visually

Look for:

* Solder bridges
* Loose components
* Bad solder joints
* Incorrectly installed components
* Solder connecting the wrong pads

## 2. Use the multimeter

Check important points.

For example:

```text
5V ───────────── GND
```

should normally **not** be shorted together.

## 3. Check polarity

Be especially careful with:

* LEDs
* Diodes
* Electrolytic capacitors
* ICs
* Batteries

---

# 17. First Practice Project

Do not start by soldering on an expensive Raspberry Pi, ESP32 or Arduino board.

Get some inexpensive:

* Perfboard
* Soldering practice PCB
* Resistors
* LEDs
* Capacitors
* Headers
* Wire

Practice:

```text
1. Solder one wire
2. Solder two wires together
3. Solder a resistor
4. Solder an LED
5. Solder headers
6. Desolder components
7. Solder them back again
```

The goal is to develop a feel for:

* Temperature
* How quickly solder melts
* How much solder is needed
* How much heat a component can tolerate
* What a good solder joint looks like

---

# 18. Moving to SMD

Once through-hole soldering feels easy, start learning SMD.

Recommended progression:

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
QFN / smaller components
```

Do not start with the smallest components.

SMD soldering benefits greatly from:

* Good lighting
* Fine tweezers
* Flux
* Fine soldering tip
* Thinner solder wire
* Magnification or microscope

iFixit has a useful introduction to microsoldering:

https://www.ifixit.com/News/98168/microsoldering-beginners-guide-its-easier-than-you-think

---

# 19. Resources to Bookmark

## Beginner

### iFixit – Soldering 101

https://www.ifixit.com/News/6864/how-to-solder

### SparkFun – Through-Hole Soldering

https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/all

### Adafruit – Excellent Soldering

https://learn.adafruit.com/adafruit-guide-excellent-soldering

---

## Desoldering & Repair

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

# 20. Recommended Learning Plan

## Level 1 – Basics

* [ ] Understand solder
* [ ] Understand flux
* [ ] Learn how to tin the tip
* [ ] Learn how to hold the soldering iron correctly
* [ ] Solder wires
* [ ] Make a basic solder joint

## Level 2 – Through-Hole

* [ ] Resistors
* [ ] Capacitors
* [ ] LEDs
* [ ] Diodes
* [ ] Transistors
* [ ] Headers
* [ ] Perfboard

## Level 3 – Desoldering

* [ ] Desoldering braid
* [ ] Desoldering pump
* [ ] Remove a through-hole component
* [ ] Clean a PCB with IPA
* [ ] Repair a bad solder joint

## Level 4 – Troubleshooting

* [ ] Continuity
* [ ] Resistance
* [ ] DC voltage
* [ ] Check for short circuits
* [ ] Follow a PCB trace
* [ ] Read a simple schematic

## Level 5 – SMD

* [ ] 0805
* [ ] 0603
* [ ] SOIC
* [ ] SMD desoldering
* [ ] SMD repair
* [ ] Microsoldering

---

# 21. The Most Important Rule

Do not focus too much on making every solder joint perfect immediately.

**Practice on cheap components.**

After some practice, I should start developing a feel for:

> "This joint is hot enough."

> "I need a little more flux."

> "That's too much solder."

> "That looks like a cold solder joint."

That feeling is what makes soldering much easier.

---

# Quick Checklist Before Starting

```text
[ ] Workbench is clear
[ ] Soldering iron is stable
[ ] Good ventilation
[ ] IPA available
[ ] Multimeter available
[ ] Desoldering braid available
[ ] Solder available
[ ] Tip is clean
[ ] Tip is tinned
[ ] PCB is secured
[ ] Power is OFF
```

## After Soldering

```text
[ ] Inspect solder joints
[ ] Look for solder bridges
[ ] Check component polarity
[ ] Check critical points with multimeter
[ ] Check for shorts
[ ] Clean PCB if necessary
[ ] Let equipment cool down
[ ] Wash hands
```

---

# The Basic Soldering Rule

Remember this sequence:

```text
Heat component + pad
        ↓
Feed in solder
        ↓
Let solder flow
        ↓
Remove solder
        ↓
Remove heat
        ↓
Let the joint cool
```

This is the foundation of almost all basic hand soldering.
