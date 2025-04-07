# Einleitung und Übersicht

Im Modul **M 6.9 Analoge Schaltungen (ANS)**, im Bachelorstudiengang (B.Eng.) Elektrotechnik (ET) der Fakultät 4 der
Hochschule Bremen (HSB), werden aus der Theorie des Schaltungsentwurfs gewonnene Kenntnisse im Labor experimentell
erprobt ([ASLK Pro Experimente](https://aslk-pro.readthedocs.io)) und mit [KiCAD](https://www.kicad.org) als eigene
PCB-Designs umgesetzt. Für die erste Erprobung von Schaltungen wird das [ASLK (Analog System Lab Kit)
Pro](https://www.mikroe.com/aslk-pro-kit) der Firma [MikroElektronika](https://www.mikroe.com/) eingesetzt.

Zur Simulation werden Schaltungssimulatoren wie
[LTSpice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html) und 
[ngspice](https://ngspice.sourceforge.io/index.html) verwendet.

Des Weiteren kommen die [MATLAB Campus-Lizenz](https://de.mathworks.com/products/matlab.html) und
[Python](https://www.python.org) als leistungsstarke Instrumente zur Modellierung und Verhaltensanalyse 
von Filtern- und Verstärkern beim Schaltungsentwurf zum Einsatz.

Für die Charakterisierung der Schaltungen stehen im Labor sechs Meßplätze mit gängigen Gerätschaften wie Quellen,
Signalgeneratoren, Oszilloskopen und dem integrierten Meßlabors [STEMlab](https://www.redpitaya.com/) von RedPitaya zur 
Verfügung.


## Lernziele des Moduls

* Ein tieferes Verständnis für das Verhalten von MOS-Elementen im analogen Schaltungsentwurf entwickeln und Ausblicke
  auf weiterführende Kurse im Master bekommen.
  
* Funktionsprinzipien und Charakterisierung von MOS-Elementen

* Fundamentale integrierte analoge Schaltungen

* Operationsverstärker

* Lernen, Grenzen und Tradeoffs analoger Schaltungen zu bewerten

* Entwickeln eines systematischen Entwurfsstils, auch anwendbar für andere Ingenieursdisziplinen

* Lernen, einen Schaltungssimulator für den Entwurf einzusetzen.

* Technisch-wissenschaftliche Dokumentation

* Konsoliderung der oberen Aspekte in Laborprojekten


## Voraussetzungen des Moduls
* Digitaltechnik

* Grundlagen der Halbleiterbauelemente

* Netzwerk- und Systemtheorie

* Regelungstechnik 

## Wissenschaftliches Rechnen / Datenwissenschaft
* [Python](https://www.anaconda.com/download/)
* [Matlab](https://de.mathworks.com)
* [Gnu Octave](https://www.gnu.org/software/octave/)
* [Command-line tools](http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html) 


## Schaltungssimulation (SPICE)
* [LTspice Linear Technology](http://www.linear.com/designtools/software/)
* [ngspice (open-source)](http://ngspice.sourceforge.net)
* [ELDO (Siemens EDA)](https://eda.sw.siemens.com/en-US/eldo/)
* [Spectre (cadence)](https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-simulation/spectre-simulation-platform.html)
* [PrimeSim HSPICE (SYNOPSIS)](https://www.synopsys.com/implementation-and-signoff/ams-simulation/primesim-hspice.html)


## Betriebssystem (OS) - Werkzeuge (Tools)
  * [Shell](https://en.wikipedia.org/wiki/Shell_%28computing%29)
    * [oh-my-zsh](https://ohmyz.sh),
    * [bash-it](https://bash-it.readthedocs.io/en/latest/)
    * [SSH (Secure Shell)](https://de.wikipedia.org/wiki/Secure_Shell)

  * [GIT (Versionskontrolle)](https://git-scm.com)
  * [Cygwin](https://cygwin.com)


## Code Editoren
  * [Visual Studio Code](https://code.visualstudio.com)
  * [Notepad++](https://notepad-plus-plus.org) (Windows)
  * [Emacs](https://www.gnu.org/software/emacs/)	
  * [Vim](https://www.vim.org)


## Schreibst Du noch oder TeXst Du schon?
  * [MikTeX (Windows, MacOS, Linux)](https://miktex.org/)
  * [MacTeX (MacOS)](https://www.tug.org/mactex/)
  * [TeXLive (Linux)](http://tug.org/texlive/)


## LaTeX Editoren
  * IDE's
    * [TeXStudio](http://www.texstudio.org)
    * [TeXMaker](http://www.xm1math.net/texmaker/)
    * [TeXWorks](http://www.tug.org/texworks/)

  * Kollaborative Frameworks
    * [ShareLaTeX, Online LaTeX](https://www.sharelatex.com/)
    * [CoCalc - Online LaTeX](https://cocalc.com/doc/latex-editor.html)



## Literaturverwaltung und LaTeX
  * [Citavi im Detail > Titel exportieren > Export nach BibTeX](https://www1.citavi.com/sub/manual5/de/exporting_to_bibtex.html)
  * [RefWorks - Library Guide Univ. Melbourne](https://unimelb.libguides.com/c.php?g=565734\&p=3912294)
  * [Benutzerdefinierte BibTex-Keys mit Zotero | nerdpause](https://nerdpause.de/benutzerdefinierte-bibtex-keys-mit-zotero/)
  * [JabRef - Library Guide Univ. Melbourne](https://unimelb.libguides.com/c.php?g=565734\&p=3897117)
  * [EndNote - Library Guide Univ. Melbourne](https://unimelb.libguides.com/latexbibtex/endnote)


## Labor
* Anwendung unterschiedlicher Beschreibungsebenen
  * Systemebene (Verhaltensmodell z.B. mit Matlab/Simulink oder Python)
  * Schaltungsebene (SPICE)
  * Charakterisierung (Messungen)

* Analog System Lab Kit &ndash; [ASLK Pro](https://aslk-pro.readthedocs.io/de/latest/)

* Messautomatisierung Red Pitaya [STEMlab 125-14/10](https://redpitaya.readthedocs.io/en/latest/developerGuide/125-14/top.html)



## Data Science
* Arbeitsordner auf dem Rechner (sandboxing, virtualenv)
* Tabellenformat (ASCII, CSV)
* Exceldatei (.xlsx ) oder OpenDocument (.ods)
* Datenspeicherung in speziellen Formaten, z.B. Apache Parquet
* Datenanalyse mit [Datenbanken](https://db-engines.com), z.B. [DuckDB](https://duckdb.org))


## Schaltungsanalyse/-entwurf $\neq$  Black Magic

*Schaltungsanalyse.* 
  * ist die Fähigkeit, Schaltungen in handhabbare Teile zu zerlegen
  * basierend auf einem einfachen, aber hinreichend genauen Modell
  * "Just-in-time" Modellierung: Verwende kein komplexes Modell, so lange es nicht benötigt wird!
  * eine Schaltung $\Rightarrow$ eine Lösung



*Schaltungsdesign/-entwurf.* 
  * ist die Fähigkeit der Schaltungssynthese auf Basis von Erfahrung und intensiver Analyse.
  * eine Spezifikation $\Rightarrow$ viele Lösungen
  * Entwurfspraktiken werden am besten durch’s "Selbermachen" ausgebildet &ndash; "Machen ist wie wollen nur krasser."



## Schöne neue Welt

![<p><em>AMD Jaguar APU (CPU/GPU), 16 nm, 325 qmm, 2016 <div id="fig:jaguar"></div></em></p>](../images/lec_AMD@16nm@Jaguar.jpg)



## From Sand to Silicon (Infineon, Dresden)

{{< video "https://www.youtube.com/embed/bor0qLifjz4?list=PLO_wT97BGA6xC6hNy9VGtt1bKwVuQXI5B" width="793" height="446" >}}


## FinFET (Intel)

{{< video "https://www.youtube.com/embed/_VMYPLXnd7E" width="793" height="446" >}}


## TSMC Fab (Next Gen 7/5 nm)

{{< video "https://www.youtube.com/embed/Hb1WDxSoSec" width="793" height="446" >}}


## Es war einmal ...
![<p><em>1906 die Elektronenröhre</em></p>](../images/lec_vacuum_tube.png)

![<p><em>1947 der erste Transistor, Bell Labs Foto</em></p>](../images/lec_1st_transistor.png)


## Damals und heute
![<p><em>1958 Jack Kilby's erster IC <div id="fig:kilbyic"></div></em></p>](../images/lec_1st_ic_kilby.png)

![<p><em>Moderner IC <div id="fig:modernic"></div></em></p>](../images/lec_modern_ic.png)



## Systemhierarchie
![<p><em>Funktionsblöcke eines elektronischen Systems.</em></p>](../images/lec_system_hierarchy.png)

* Nutzen Sie Hierarchien zur Beschreibung komplexer Systeme
* Teile und herrsche



## System Assembly
![<p><em>Bottom-up Prozess, Integration (c) Maloberti, Wiley 2011.</em></p>](../images/lec_system_assembly.png)


## Schnittstellen zur Aussenwelt
![<p><em>Interfacing (c) Maloberti, Wiley 2011.</em></p>](../images/lec_real_world_interface.png)


## Meeting mit einem System
![<p><em>Drahtloses Kommunikationssystem (c) Maloberti, Wiley 2011.</em></p>](../images/lec_smartphone.png)


## System in a Package (SiP)
![<p><em>Beschleunigungssensor (c) Maloberti, Wiley 2011.</em></p>](../images/lec_system_in_package.png)


## Backend Phasen
* Packaging
* Zuverlässigkeit = Qualität auf Zeit
* Testing auf Wafer Level, known good die (KGD)
  * Burn-in und Accelerated Aging (thermischer Stress, Arrhenius Gesetz)
  * Automatic Test Equipment (ATE)
    * System Probe
    * Interconnect Test
    * Build-in Self-Test (BIST)


* Statistische Datenanalyse und Yield Prognosen
  * Ausfallrate FIT (failure in time)
  * Badewannenkurve


## Sie werden Experte
*Leistungsmerkmale.* 
* Hintergrundwissen
  * Systemverständnis, Architektur, Herstellungsverfahren, Implementation

* Unterbewusste Kompetenz
  * Abgespeicherte Erfahrungen aus Erfolgsgeschichten und Misserfolgen

* Spezialwissen
  * Berufsspezifisches Wissen

* Teamwork Haltung
  * Kommunikationsfähigkeit, Berichtswesen und technische Präsentation

* Kreativität
* Tool-Kenntnisse

## Evolution von Produkten
* Angetrieben durch Technologieverbesserung
  * Kosten (größere Chips, geringere Größe der Merkmale, bessere Ausbeute)
  * Leistung (neue Bauteile, höhere Geschwindigkeit, weniger Stromverbrauch)

* Angetrieben durch Verbesserung der Entwurfsmethodik
  * Architektur (Leistung, Funktionen)
  * CAD (Entwicklungskosten, Time-to-Market)

* Komplexität der Designs verdoppelt sich jedes Jahr (Moore's Gesetz)
* Rolle von CAD
  * Verbesserung der Produktivität von Konstruktionsprozessen
  * Reduzierung der Komplexität für den Konstrukteur
  * Sicherstellung des ordnungsgemäßen Betriebs der Geräte


## EDA Kompetenz
* EDA-Anbieter (Tool-Entwickler)
  * Identifikation von Entwurfsaufgaben, Bedarf an Werkzeugen
  * Entwicklung von Strategien und Algorithmen
  * Implementierung von Software-Werkzeugen
  * Verifikation der Stabilität und Funktionalität der Software-Tools

* IC-Hersteller
  * Entscheidungsplanung, welches Tool die Produktivität steigern könnte
  * EDA-Tool-Manager, Installation und Wartung
  * Experten für Softwareeinsatz, Anwendung in Produktdesign und -entwicklung

* Dozenten und Studenten
  * Jobchancen
  * Notwendigkeit, auf dem Laufenden zu bleiben

## Ansichten zur Hardware (I)

![](fig/lec_01-views_on_hardware_1.png)


## Ansichten zur Hardware (II)

![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../images/lec_01-views_on_hardware_2.png)


## Abstraktionsebenen

![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../images/lec_01-abstraction_layer.png)


## Entwurfsablauf

![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../images/lec_01-design_flow.png)


## Verifikation

![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../images/lec_01-verification.png)


### Frontend vs. Backend (analog)

![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../images/lec_01-front-end_back-end_analog.png)


## Frontend vs. Backend (digital)

![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../images/lec_01-front-end_back-end_digital.png)


## Design-/Entwurfsmethodik
* Full Custom - vollständig manuell: ASIC
  * Überwiegend analoge Schaltungen
  * Einfache digitale Gatter
  * Volle Kontrolle, aber lange Entwicklungszeit (bis zu Jahren)

* Semi-custom: ASIC-Fertigung mit Verwendung von vorgefertigten Teilen
  * Standardzellen, Makrozellen, IP's
  * Wiederverwendung von vordefinierten Blöcken oder Maskensätzen
  * Eingeschränkte Kontrolle/Flexibilität, aber kürzere Entwicklungszeit (bis zu Wochen)

* Vollständig automatisiert: Keine Fertigung, reprogrammierbare ASICs
  * FPGA, PLA
  * Ausschließlich digitale Schaltungen
  * Schnelles Prototyping


## Analog Design Entry

![](../images/lec_01-design_entry_analog.png)

## Netlist

![](../images/lec_01-netlist.png)

## Layout

![](../images/lec_01-inverter_layout.png)

## Digital Design Entry

![](../images/lec_01-design_entry_digital.png)

## Hardwarebeschreibungssprachen

![](../images/lec_01-hdl_inv.png)

## Technology-Gates und Netlisting

![](../images/lec_01-technology_gate_netlist.png)

## Standard Cell Layout

![](../images/lec_01-standard_cell_layout.png)

## Nachhaltige Elektronik ...

{{< video "https://www.youtube.com/embed/7S5IuaKiZIY" width="859" height="483" >}}

<p><em>Geekchester.</em></p>


## Warum es sicht lohnt ...

{{< video "https://www.youtube.com/embed/SwPGxwBZw6I" width="859" height="483" >}}

<p><em>Circuit Song.</em></p>


## Und ab an den Strand ...

{{< video "https://www.youtube.com/embed/ekkJlQf-K4I" width="859" height="483" >}}

<p><em>Viva la Electronica.</em></p>
