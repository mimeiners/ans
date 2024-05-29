<!-- !split -->
<!-- jupyter-book 01_lec.md -->
# Einleitung und Motivation

<!-- !split -->
### Lernziele des Moduls

* Ein tieferes Verständnis für das Verhalten von MOS-Elementen im analogen Schaltungsentwurf entwickeln und Ausblicke auf weiterführende Kurse im Master bekommen. 
* Funktionsprinzipien und Charakterisierung von MOS-Elementen
* Fundamentale integrierte analoge Schaltungen
* Operationsverstärker
* Lernen, Grenzen und Tradeoffs analoger Schaltungen zu bewerten
* Entwickeln eines systematischen Entwurfsstils, auch anwendbar für andere Ingenieursdisziplinen
* Lernen, einen Schaltungssimulator für den Entwurf einzusetzen.
* Technisch-wissenschaftliche Dokumentation
* Konsoliderung der oberen Aspekte in Laborprojekten  

<!-- !split -->
### Voraussetzungen des Moduls
* Grundlagen der Halbleiterbauelemente
* Netzwerk- und Systemtheorie
* Regelungstechnik 

<!-- !split -->
### Wissenschaftliches Rechnen / Datenwissenschaft
* [Python](https://www.anaconda.com/download/)
* [Matlab](https://de.mathworks.com)
* [Gnu Octave](https://www.gnu.org/software/octave/)
* [Command-line tools](http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html) 

<!-- !split -->
### Schaltungssimulation (SPICE)
* [LTspice Linear Technology](http://www.linear.com/designtools/software/)
* [ngspice (open-source)](http://ngspice.sourceforge.net)
* [ELDO (Siemens EDA)](https://eda.sw.siemens.com/en-US/eldo/)
* [Spectre (cadence)](https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-simulation/spectre-simulation-platform.html)
* [PrimeSim HSPICE (SYNOPSIS)](https://www.synopsys.com/implementation-and-signoff/ams-simulation/primesim-hspice.html)

<!-- !split -->
### Betriebssystem (OS) - Werkzeuge (Tools)
  * [Shell](https://en.wikipedia.org/wiki/Shell_%28computing%29)
    * [oh-my-zsh](https://ohmyz.sh),
    * [bash-it](https://bash-it.readthedocs.io/en/latest/)
    * [SSH (Secure Shell)](https://de.wikipedia.org/wiki/Secure_Shell)

  * [GIT (Versionskontrolle)](https://git-scm.com)
  * [Cygwin](https://cygwin.com)

<!-- !split -->
### Code Editoren
  * [Visual Studio Code](https://code.visualstudio.com)
  * [Notepad++](https://notepad-plus-plus.org) (Windows)
  * [Emacs](https://www.gnu.org/software/emacs/)	
  * [Vim](https://www.vim.org)

<!-- !split -->
### Schreibst Du noch oder TeXst Du schon?
  * [MikTeX (Windows, MacOS, Linux)](https://miktex.org/)
  * [MacTeX (MacOS)](https://www.tug.org/mactex/)
  * [TeXLive (Linux)](http://tug.org/texlive/)

<!-- !split -->
### LaTeX Editoren
  * IDE's
    * [TeXStudio](http://www.texstudio.org)
    * [TeXMaker](http://www.xm1math.net/texmaker/)
    * [TeXWorks](http://www.tug.org/texworks/)

  * Kollaborative Frameworks
    * [ShareLaTeX, Online LaTeX](https://www.sharelatex.com/)
    * [CoCalc - Online LaTeX](https://cocalc.com/doc/latex-editor.html)


<!-- !split -->
### Literaturverwaltung und LaTeX
  * [Citavi im Detail > Titel exportieren > Export nach BibTeX](https://www1.citavi.com/sub/manual5/de/exporting_to_bibtex.html)
  * [RefWorks - Library Guide Univ. Melbourne](https://unimelb.libguides.com/c.php?g=565734\&p=3912294)
  * [Benutzerdefinierte BibTex-Keys mit Zotero | nerdpause](https://nerdpause.de/benutzerdefinierte-bibtex-keys-mit-zotero/)
  * [JabRef - Library Guide Univ. Melbourne](https://unimelb.libguides.com/c.php?g=565734\&p=3897117)
  * [EndNote - Library Guide Univ. Melbourne](https://unimelb.libguides.com/latexbibtex/endnote)

<!-- !split -->
### Labor
*Experimente mit dem ASLK Pro.* 
* Anwendung unterschiedlicher Beschreibungsebenen
  * Systemebene (Verhaltensmodell z.B. mit Matlab/Simulink oder Python)
  * Schaltungsebene (SPICE)
  * Charakterisierung (Messungen)

* Analog System Lab Kit &ndash; [ASLK Pro](https://aslk-pro.readthedocs.io/de/latest/)
  * Experimente 1 bis 3

* Messautomatisierung Red Pitaya [STEMlab 125-14/10](https://redpitaya.readthedocs.io/en/latest/developerGuide/125-14/top.html)



<!-- !split -->
### Data Science
* Arbeitsordner auf dem Rechner (sandboxing, virtualenv)
* Tabellenformat (ASCII, CSV)
* Datenspeicherung in speziellen Formaten, z.B. mat-files (HDF5)
* [Datenbanken](https://db-engines.com), 
  * SQL (z.B. [SQlite](https://www.sqlite.org/index.html), [DuckDB](https://duckdb.org))
  * Time-Series-DB (z.B. [InfluxDB](https://www.influxdata.com/time-series-database/))
  * [PythonDB](https://www.opensourceforu.com/2017/05/three-python-databases-pickledb-tinydb-zodb/) (z.B. PicklDB, TinyDB, ZODB)

* Exceldatei (.xlsx ) or OpenDocument (.ods)

<!-- !split -->
### Schaltungsanalyse/-entwurf $\neq$  Black Magic

*Schaltungsanalyse.* 
  * ist die Fähigkeit, Schaltungen in handhabbare Teile zu zerlegen
  * basierend auf einem einfachen, aber hinreichend genauen Modell
  * "Just-in-time" Modellierung: Verwende kein komplexes Modell, so lange es nicht benötigt wird!
  * eine Schaltung $\Rightarrow$ eine Lösung



*Schaltungsdesign/-entwurf.* 
  * ist die Fähigkeit der Schaltungssynthese auf Basis von Erfahrung und intensiver Analyse.
  * eine Spezifikation $\Rightarrow$ viele Lösungen
  * Entwurfspraktiken werden am besten durch’s "Selbermachen" ausgebildet &ndash; "Machen ist wie wollen nur krasser."



<!-- !split -->
### Schöne neue Welt
<!-- !bslidecell 00 0.9 -->

<!-- <img src="../../lecture/doconce/fig/lec_AMD@16nm@Jaguar.jpg" width="400"><p><em>AMD Jaguar APU (CPU/GPU), 16 nm, 325 qmm, 2016 <div id="fig:jaguar"></div></em></p> -->
![<p><em>AMD Jaguar APU (CPU/GPU), 16 nm, 325 qmm, 2016 <div id="fig:jaguar"></div></em></p>](../../lecture/doconce/fig/lec_AMD@16nm@Jaguar.jpg)

<!-- !eslidecell -->

<!-- !split -->
### From Sand to Silicon (Infineon, Dresden)
<!-- !bslidecell 00 0.9 -->

<iframe width="793" height="446" src="https://www.youtube.com/embed/bor0qLifjz4?list=PLO_wT97BGA6xC6hNy9VGtt1bKwVuQXI5B" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### FinFET (Intel)
<!-- !bslidecell 00 0.9 -->

<iframe width="793" height="446" src="https://www.youtube.com/embed/_VMYPLXnd7E" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### TSMC Fab (Next Gen 7/5 nm)
<!-- !bslidecell 00 0.9 -->

<iframe width="793" height="446" src="https://www.youtube.com/embed/Hb1WDxSoSec" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### Es war einmal ...
<!-- !bslidecell 00 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec_vacuum_tube.png" width="400"><p><em>1906 die Elektronenröhre</em></p> -->
![<p><em>1906 die Elektronenröhre</em></p>](../../lecture/doconce/fig/lec_vacuum_tube.png)
<!-- !eslidecell -->

<!-- !bslidecell 01 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec_1st_transistor.png" width="400"><p><em>1947 der erste Transistor, Bell Labs Foto</em></p> -->
![<p><em>1947 der erste Transistor, Bell Labs Foto</em></p>](../../lecture/doconce/fig/lec_1st_transistor.png)
<!-- !eslidecell -->

<!-- !split -->
### Damals und heute
<!-- !bslidecell 00 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec_1st_ic_kilby.png" width="400"><p><em>1958 Jack Kilby's erster IC <div id="fig:kilbyic"></div></em></p> -->
![<p><em>1958 Jack Kilby's erster IC <div id="fig:kilbyic"></div></em></p>](../../lecture/doconce/fig/lec_1st_ic_kilby.png)
<!-- !eslidecell -->

<!-- !bslidecell 01 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec_modern_ic.png" width="400"><p><em>Moderner IC <div id="fig:modernic"></div></em></p> -->
![<p><em>Moderner IC <div id="fig:modernic"></div></em></p>](../../lecture/doconce/fig/lec_modern_ic.png)
<!-- !eslidecell -->

<!-- !split -->
### Moore's Law
<!-- !bslidecell 00 0.9 -->


<embed src="https://players.brightcove.net/734546229001/default_default/index.html?videoId=4144803153001" width="793" height="446" autoplay="false" loop="true"></embed>
<p><em></em></p>


<!-- !eslidecell -->

<!-- !split -->
### Systemhierarchie
<!-- !bslidecell 00 0.85 -->
<!-- <img src="../../lecture/doconce/fig/lec_system_hierarchy.png" height="400"><p><em>Funktionsblöcke eines elektronischen Systems.</em></p> -->
![<p><em>Funktionsblöcke eines elektronischen Systems.</em></p>](../../lecture/doconce/fig/lec_system_hierarchy.png)
<!-- !eslidecell -->

* Nutzen Sie Hierarchien zur Beschreibung komplexer Systeme
* Teile und herrsche



<!-- !split -->
### System Assembly
<!-- <img src="../../lecture/doconce/fig/lec_system_assembly.png" height="400"><p><em>Bottom-up Prozess, Integration (c) Maloberti, Wiley 2011.</em></p> -->
![<p><em>Bottom-up Prozess, Integration (c) Maloberti, Wiley 2011.</em></p>](../../lecture/doconce/fig/lec_system_assembly.png)

<!-- !split -->
### Schnittstellen zur Aussenwelt
<!-- <img src="../../lecture/doconce/fig/lec_real_world_interface.png" width="400"><p><em>Interfacing (c) Maloberti, Wiley 2011.</em></p> -->
![<p><em>Interfacing (c) Maloberti, Wiley 2011.</em></p>](../../lecture/doconce/fig/lec_real_world_interface.png)

<!-- !split -->
### Meeting mit einem System
<!-- <img src="../../lecture/doconce/fig/lec_smartphone.png" width="400"><p><em>Drahtloses Kommunikationssystem (c) Maloberti, Wiley 2011.</em></p> -->
![<p><em>Drahtloses Kommunikationssystem (c) Maloberti, Wiley 2011.</em></p>](../../lecture/doconce/fig/lec_smartphone.png)

<!-- !split -->
### System in a Package (SiP)
<!-- <img src="../../lecture/doconce/fig/lec_system_in_package.png" width="400"><p><em>Beschleunigungssensor (c) Maloberti, Wiley 2011.</em></p> -->
![<p><em>Beschleunigungssensor (c) Maloberti, Wiley 2011.</em></p>](../../lecture/doconce/fig/lec_system_in_package.png)

<!-- !split -->
### Backend Phasen
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


<!-- !split -->
### Sie werden Experte
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



<!-- !split -->
### Evolution von Produkten
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


<!-- !split -->
### EDA Kompetenz
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


<!-- !split -->
### Ansichten zur Hardware (I)

<!-- <img src="fig/lec_01-views_on_hardware_1.png" width="400"> -->
![](fig/lec_01-views_on_hardware_1.png)

<!-- !split -->
### Ansichten zur Hardware (II)

<!-- <img src="../../lecture/doconce/fig/lec_01-views_on_hardware_2.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec_01-views_on_hardware_2.png)

<!-- !split -->
### Abstraktionsebenen

<!-- <img src="../../lecture/doconce/fig/lec_01-abstraction_layer.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec_01-abstraction_layer.png)

<!-- !split -->
### Entwurfsablauf

<!-- <img src="../../lecture/doconce/fig/lec_01-design_flow.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec_01-design_flow.png)

<!-- !split -->
### Verifikation

<!-- <img src="../../lecture/doconce/fig/lec_01-verification.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec_01-verification.png)

<!-- !split -->
### Frontend vs. Backend (analog)

<!-- <img src="../../lecture/doconce/fig/lec_01-front-end_back-end_analog.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec_01-front-end_back-end_analog.png)

<!-- !split -->
### Frontend vs. Backend (digital)

<!-- <img src="../../lecture/doconce/fig/lec_01-front-end_back-end_digital.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec_01-front-end_back-end_digital.png)

<!-- !split -->
### Design-/Entwurfsmethodik
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


<!-- !split -->
### Analog Design Entry

<!-- <img src="fig/lec_01-design_entry_analog.png" width="400"> -->
![](fig/lec_01-design_entry_analog.png)

<!-- !split -->
### Netlist

<!-- <img src="fig/lec_01-netlist.png" width="400"> -->
![](fig/lec_01-netlist.png)

<!-- !split -->
### Layout

<!-- <img src="fig/lec_01-inverter_layout.png" width="400"> -->
![](fig/lec_01-inverter_layout.png)

<!-- !split -->
### Digital Design Entry

<!-- <img src="fig/lec_01-design_entry_digital.png" width="400"> -->
![](fig/lec_01-design_entry_digital.png)

<!-- !split -->
### Hardwarebeschreibungssprachen

<!-- <img src="fig/lec_01-hdl_inv.png" width="400"> -->
![](fig/lec_01-hdl_inv.png)

<!-- !split -->
### Technology-Gates und Netlisting

<!-- <img src="fig/lec_01-technology_gate_netlist.png" width="400"> -->
![](fig/lec_01-technology_gate_netlist.png)

<!-- !split -->
### Standard Cell Layout

<!-- <img src="fig/lec_01-standard_cell_layout.png" width="400"> -->
![](fig/lec_01-standard_cell_layout.png)

<!-- !split -->
### Nachhaltige Elektronik ...
<!-- !bslidecell 00 0.9 -->

<iframe width="859" height="483" src="https://www.youtube.com/embed/7S5IuaKiZIY" frameborder="0" allowfullscreen></iframe>

<p><em>Geekchester.</em></p>


<!-- !eslidecell -->

<!-- !split -->
### Warum es sicht lohnt ...
<!-- !bslidecell 00 0.9 -->

<iframe width="859" height="483" src="https://www.youtube.com/embed/SwPGxwBZw6I" frameborder="0" allowfullscreen></iframe>

<p><em>Circuit Song.</em></p>


<!-- !eslidecell -->

<!-- !split -->
### Und ab an den Strand ...
<!-- !bslidecell 00 0.9 -->

<iframe width="859" height="483" src="https://www.youtube.com/embed/ekkJlQf-K4I" frameborder="0" allowfullscreen></iframe>

<p><em>Viva la Electronica.</em></p>


<!-- !eslidecell -->

<!-- !split -->
### Literaturverzeichnis


