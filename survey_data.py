#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; mode: auto-fill; fill-column: 78 -*-
# Time-stamp: <2015-12-22 17:29:21 (kthoden)>

phasen = ["zusatz", "planung", "recherche", "überarbeitung", "analyse", "publizieren"]

Textverarbeitung = ['App Pages', 'pages', 'GoogleDocs', 'Open Office Writer',
                    'LibreOffice Writer', 'MS WORD', 'MS Word', 'MS Word ', 'Ms word', 'Ms Word',
                    'Ms-word', 'Mellel', 'ms word', 'Word', 'WORD 2010', 'Microsoft Word', 
                    'Word (von Apple)', 'word', 'Scrivener', 'Textverarbeitung ', 'Google Docs',
                    'Google docs', 'Focuswriter', 'MS Word für Mac', 'MSWord für Mac',
                    'Schreibprogramm (wie Word)', 'Textverarbeitung', 'Word (weil man muss)',
                    'textverarbeitung']
Literaturverwaltung = ["zotero", "Zoteri", "Zotero", "Zotero ", "Bookends",
                       "citavi", "Citav", "CITAVI", "Citavi", "Datenbank LitLink",
                       "EndNote", "Endnote", "endnote", "end note",
                       "JabRef", "Jabref", "LitLink", "Litlink", "Litlink ",
                       "Mendeley", "litlink", "Papers"]
Tabellenkalkulation = ["MS Excel", "Excel", "Excell", "MS Excell", "MS Exel",
                       "excell", "excel", "OpenOfficeCalc", "LibreOffice Calc",
                       "Ms excel", "tabellenkalkulation"]
Datenbank = ["MS Access", "Access", "ms access", "access", "allegro-C",
             "Allegro", "Datenbanken", "Recherchetools von Datenbanken",
             "Datenbanken der Archive", "FileMaker Pro", "Filemaker", "My sql", "SQLite", "Tellico"]
Browser = ["Browser", "Chrome", "Firefox", "Internetbrowser", "Mozilla Firefox",
           "Opera", "firefox", "firefox browser", "internetbrowser"]
Onlinedatenbank = ["Annee philologique", "Bibliothekskatalog",
                   "Bibliothekskataloge", "Bibliothekssoftware", "Deutsches digitales archiv",
                   "Gnomon online", "Google Books", "Google Scholar",
                   "Internet Explorer/OPAC", "KVK", "Mla Datenbank",
                   "MuseumPlus", "OPAC", "Opac", "Ub katalog", "Wikipedia",
                   "jstor", "online Kataloge", "wikipedia", "Bilddatenbanksystem"]
PDFBetrachter = ["Acrobat Reader" ,"Acrobat Reader u.ä. ", "Adobe Acrobat Reader",
                 "Adobe Acrobat", "acrobat", "acrobat pro", "Adobe", "Good Reader",
                 "Good Reader (iPad)", "PDF Expert 9", "Acrobat PDF"]
Analyse = ["Berlin Text System", "IPython", "IPython Notebook", "Maxqda", "R",
           "R Studio", "Textstat", "beluga", "knitr", "AntConc", "ParaConc",
           "Sketch Engine", "TreeTagger"]
Mindmap = ["App BigMind", "FreeMind", "Mind Map Creator ", "Mindjet",
           "Mindmanager", "Mindmapping Tools", "Omni Focus", "Scapple",
           "TheBrain", "mind map", "mindnote", "xMind", "Mindmapping-Tools", "Zettelkasten"]
Notizen = ["App Index Card", "App iA Writer", "Evernote", "Ms One Note", 
           "One Note", "Onenote", "MS OneNote", "MS Notes"]
Sonstige = ["Eigene Webseite, TLA", "Digimagazine", "Excellence", "Lidos",
            "Omni Cloud", "Proterm ", "lidos", "vPn", "coraw"]
Bildbearbeitung = ["Adobe CS", "Adobe Lightroom", "Adobe Photoshop",
                   "Bilderverarbeitung", "Corall Photopaint", "Gimp",
                   "Photohop", "Photoshop"]
Praesentation = ["App Keynote", "MS Powerpoint", "ms powerpoint", "Ms powerpoint", "pp", "Prezi"]
Textsatz = ["Kile", "LaTeX", "Texmaker (LaTeX)", "LaTeX editor (texmaker)",
            "LaTeXeditor (texmaker)", "LaTex", "Latex", "TUSTEP", "TeX",
            "tustep", "LaTex", "Lyx/Tex"]
DesktopPublishing = ["Adobe Illustrator", "Adobe Indesign", "Illustrator", "In Design",
                     "InDesign", "InDesign", "Indesign", "Adobe Photoshop/Indesign", "INDESIGN"]
Geo = ["ARCMap", "ArcMap", "QGIS", "GIS"]
Suite = ["Adobe Suite", "LibreOffice", "Open Office", "MS Office", 
         "Microsoft Office", "Open Office /word", "Open office", "Open/Libre Office",
         "OpenOffice", "openoffice", "Libre Office"]
Email = ["Mozilla Thunderbird", "Outlook", "Thunderbird"]
OCR = ["Abbyy Finereader"]
Blog = ["Twitter", "Wordpress"]
Suchmaschine = ["Copernic Desktop Search", "Google", "Google ", "regain", "yacy"]
Wiki = ["DokuWiki", "Lexican", "Redmine", "Issue Tracker (Redmine)"]
Bildbetrachter = ["Adobe Bridge", "IrfanView"]
XMLEditor = ["oXygen -ditoor", "oXygen xml Editor", "Copyxml Editor", "Oxygen XML Editor"]
Lesezeichen = ["Delicious", "Pinterest"]
Texteditor = ["Texteditor (gedit)", "Win Editor", "TextEdit"]
Webseiteneditor = ["Dreamweaver", "HTML"]
Betriebssystem = ["Windows"]
CAD = ["AutoCAD", "CAD"]
Onlinespeicher = ["Dropbox", "alfresco"]
Projektmanagement = ["Things", "Datenmanagementplan"]
Textkonversion = ["pandoc"]
Infrastruktur = ["Edirom", "Textgrid", "Speicherplatz für Forschungsdaten"]
RSS = ["Feedly"]
Kalender = ["Google Kalender"]
Diagramme = ["MS Visio"]
Ungültig = ["lesen", "rechnen", "schreiben", "s. o.", "siehe oben", "dfg",
             "dgy", "ygg"]

Kategorien = (Textverarbeitung, Literaturverwaltung, Tabellenkalkulation,
              Datenbank, Browser, Onlinedatenbank, PDFBetrachter, Analyse,
              Mindmap, Notizen, Sonstige, Bildbearbeitung, Praesentation,
              Textsatz, DesktopPublishing, Geo, Suite, Email, OCR, Blog,
              Suchmaschine, Wiki, Bildbetrachter, XMLEditor, Lesezeichen,
              Texteditor, Webseiteneditor, Betriebssystem, CAD,
              Onlinespeicher, Projektmanagement, Textkonversion,
              Infrastruktur, RSS, Kalender, Diagramme, Ungültig)

Kategorien2 = ["Textverarbeitung", "Literaturverwaltung",
               "Tabellenkalkulation", "Datenbank", "Browser",
               "Onlinedatenbank", "PDFBetrachter", "Analyse", "Mindmap",
               "Notizen", "Sonstige", "Bildbearbeitung", "Praesentation",
               "Textsatz", "DesktopPublishing", "Geo", "Suite", "Email",
               "OCR", "Blog", "Suchmaschine", "Wiki", "Bildbetrachter",
               "XMLEditor", "Lesezeichen", "Texteditor", "Webseiteneditor",
               "Betriebssystem", "CAD", "Onlinespeicher", "Projektmanagement",
               "Textkonversion", "Infrastruktur", "RSS", "Kalender",
               "Diagramme", "Ungültig"]
