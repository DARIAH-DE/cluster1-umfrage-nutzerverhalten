#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; mode: auto-fill; fill-column: 78 -*-
# Time-stamp: <2016-01-26 16:07:40 (kthoden)>

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as image

print("config %s" % mpl.matplotlib_fname())
ALPHA_VALUE = 0.7
CHART_COLOUR = "#448CC7"
# using colour scheme from last year's poster
COLOURS = ['#663366', '#cc9900', '#99cccc', '#669966', '#669999', '#99cccc']
CSV_PATH = "csv_sources/"
EXTENSION = "png"                         #or pdf
titles = open("titles.txt", mode="w")
WIDTH = 0.75

def turnaround_dict(dictionary, value_list):
    """Turns
    ist = 'bibarchiv': {'Nein': 5, 'Ja': 93}, 'persoenlich': {'Nein': 39, 'Ja': 59}, 'eigenarchiv': {'Nein': 67, 'Ja': 31}, 'online': {'Nein': 2, 'Ja': 96}}
    into
    eigentlich = {'Nein': {'bibarchiv' : 5, 'persoenlich': 39, 'eigenarchiv': 67, 'online': 2}, 'Ja' : {'bibarchiv' : 93, 'persoenlich': 59, 'eigenarchiv': 31, 'online': 96}}
"""
    ja = {}
    nein = {}

    for item in dictionary.keys():
        ja[item] = dictionary[item][value_list[0]]
        nein[item] = dictionary[item][value_list[1]]
        
    superpower = {value_list[0] : ja, value_list[1] : nein}

    return superpower
# def turnaround_dict ends here

def d01_recherchewo(csv_file, other=True):

    frame = pd.read_csv(CSV_PATH + csv_file)
    outputfile = csv_file.replace("csv", EXTENSION)

    title="Wo recherchieren Sie Quellen/Materialien?"
    values = ["Ja", "Nein"]
    sonstiges = ["Feldforschung", "Internet (aber nachrangig)", "Online-Ressourcen", "Private Sammlungen", "Twitter", "was mir so über den Weg läuft"]

    fieldlist = []
    fields = frame.columns.tolist()

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))

    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", fontsize=12, alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')

    print("Wrote %s." % outputfile)

    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
# def d01_recherchewo ends here

def d02_pubform(csv_file):
    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fieldlist = []
    fields = frame.columns.tolist()
    title="In welcher Form publizieren Sie Ihre Ergebnisse?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))

    values = ["Würde ich gern noch mehr publizieren","Publiziere ich vorwiegend"]

    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    print(maior)
    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Publiziere ich vorwiegend"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    dfdf.plot(kind='barh', ax=axes, stacked=False, color=COLOURS, width=WIDTH)
    axes.set_xlabel("BenutzerInnen", fontsize=12, alpha=ALPHA_VALUE, ha='left')
    fig.savefig(outputfile, bbox_inches='tight')

    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s " % (outputfile))
# def d02_pubform ends here

def d03_pubart(csv_file, other=True):
    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fieldlist = []
    fields = frame.columns.tolist()

    title="Wie publizieren Sie Ihre Ergebnisse?"
    
    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["Blog", "Datenbank", "Ist alles noch in Arbeit", "Kongressakten", "Online", "Online (Blog, epub)", "online über Hochschulseiten (repositories oder Projektportale)) ", "Onlinepublikationen", "unabh. online-journal", "Vom Lehrstuhl", "Webseite", "Zeitschriftenpublikation"]

    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", fontsize=12, alpha=ALPHA_VALUE, ha='left')

    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d03_pubart ends here

def d04_pubkanal(csv_file, other=True):
    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fieldlist = []
    fields = frame.columns.tolist()

    title="Über welche Kanäle verbreiten Sie Ihre Publikationen?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["Buchhandel", "Buchhandel", "Buchhandel", "Digitale Plattform der universität", "gar nicht", "Instituts-/Verbandswebsites", "Literaturverzeichnis anderer Publikation ", "Online zeitschriften", "Onlinebibliographien wiss. Verbände oder staatl. Organismen", "persönliche Kontakte", "Rezeption durch Kollegen ", "Sonderdrucke per Post", "Über den Verlag", "Verbreitung wird von der Abt. Öffentlichkeitsarbeit übernommen", "Verlag", "Verlag", "VerlagsPR", "Verlagswerbung", "Verlagswerbung", "Werbung durch den verlag"]

    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()

    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", fontsize=12, alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d04_pubkanal ends here

def d05_mitwem(csv_file, other=True):
    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fields = frame.columns.tolist()
    fieldlist = []

    title="Mit wem besprechen Sie Ihre Arbeitsergebnisse?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["Betreuer", "Familie, Freunde", "Freunde", "Kolloquia, Konferenzen", "Konferenzen", "Konferenzteilnehmern", "mit anderen Wissenschaftlern/Studierenden", "mit Freunden", "mit nahen Angehörigen", "privat", "Professoren", "Publikation ", "Tagungen", "Von der Uni auf einer personalseite"]

    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})
    
    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", fontsize=15, alpha=ALPHA_VALUE, ha='left')

    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d05_mitwem ends here

def d06_datenfinden(csv_file, other=True):

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fields = frame.columns.tolist()
    fieldlist = []

    title="Wie stellen Sie die (Wieder-)Auffindbarkeit Ihrer Daten sicher?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["Ausdrucke", "Datenbank", "Datenbank für Exzerpte (Dokumente), Schlagworte für Dateien", "Eingabe in unsere Datenbank", "Eintrag in Datenbank(en)", "Ich lasse die Daten auf einem separaten Server im hauseigenen Archiv archivieren.", "Institutionelles Datenrepositpory", "redundanter externer Festplattenspeicher"]
    
    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d06_datenfinden ends here

def d07_hilfe(csv_file, other=True):

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fields = frame.columns.tolist()
    fieldlist = []

    title="Welche Form der Unterstützung bei der Nutzung von Software wünschen Sie sich?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["Internetforen", "Menüs und Handbücher, die nicht von Ingenieuren, sondern von Nutzern für Nutzern geschrieben sind. ", "online Wiki", "Online- bzw. Videotutorials", "other", "Regelmäßige Fortbildungen", "Schulungen", "Stack Overflow", "Video-Tutorials", "vollständige Hilfetexte (diese sollten existieren, bevor die Software an Nutzer weitergegeben wird - ja, auch bereits in der beta-Phase!)"]
    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d07_hilfe ends here

def d08_zwischenergeb(csv_file, other=True):

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fields = frame.columns.tolist()
    fieldlist = []

    title="Wo legen Sie (Zwischen-)Ergebnisse Ihrer Arbeit ab?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["Eigener Server, redundante USB-Stick-Kopien an verschiedenen Standorten", "USB-Stick, Festplatte, privates Wiki", "redundanter externer Festplattenspeicher", "Festplatten und USB-Sticks zur Sicherung", "Festplatte", "Mobiler Arbeitsrechner, Backups", "Externe Festplatte", "Externe Festplatten", "externe Festplatte", "Speichermedien (kopieren)", "Externe Festplatte ", "Externes Laufwerk ", ""]
    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d08_zwischenergeb ends here

def d10_disziplin(csv_file, other=True):

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fields = frame.columns.tolist()
    fieldlist = []

    title="In welcher Disziplin arbeiten Sie primär?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["Gedenkstätte", "Geowissenschaften, Zoologie, wissenschaftgeschichte", "Kommunikations- und Medienwissenschaft", "Numismatik", "Politikwissnschaft", "Schueler", "Schüler", "Übergreifend", "Wissenschafts- und Technikgeschichte"]
    
    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')

    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d10_disziplin ends here

def d11_wielange(csv_file):

    title="Wie lange sind Sie schon in der geisteswissenschaftlichen Forschung tätig?"

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    p2 = pd.value_counts(frame["wie_lange"].values)
    p2.sort_values(inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    p2.plot(kind="barh", ax=axes, color=COLOURS[0], width=WIDTH, label="")
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d11_wielange ends here

def d12_derzeit(csv_file):

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fields = frame.columns.tolist()
    fieldlist = []

    title="Ich bin derzeit ...?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]

    ursa=pd.concat(fieldlist[:-1], axis=1)
    ursa.columns = fields[:-1]

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d12_derzeit ends here

def d13_arbeitsplatz(csv_file, other=True):

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)
    fields = frame.columns.tolist()
    fieldlist = []

    title="Wo arbeiten Sie?"

    for field in fields:
        fieldlist.append(pd.value_counts(frame[field].values))
    values = ["Ja", "Nein"]
    sonstiges = ["'arbeitslos'", "Bodendenkmalamt", "Denkmalamt", "derzeit ohne Anstellung", "Gar nicht", "Grabungsfirma", "in Nebentätigkeit", "Infoterm ", "Max Weber Stiftung", "Max weber Stiftung", "Schule", "Schule", "Stiftung", "Stiftung", "Stipendiat", "zu Hause"]
    
    ursa=pd.concat(fieldlist, axis=1)
    ursa.columns = fields

    turnaround = ursa.to_dict()
    maior = turnaround_dict(turnaround, values)
    maior.pop("Nein")
    # others interlude
    nana=maior["Ja"]
    nana.update({"Sonstiges":len(sonstiges)})

    dfdf = pd.DataFrame(maior)
    dfdf.sort_values(["Ja"],inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, color=COLOURS[0], legend=False, width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d13_arbeitsplatz ends here

def d14_aufmerksam(csv_file):

    outputfile = csv_file.replace("csv", EXTENSION)
    frame = pd.read_csv(CSV_PATH + csv_file)

    title="Wie sind Sie auf die Umfrage aufmerksam geworden?"

    p1 = pd.value_counts(frame["aufmerksam"].values)
    p1.sort_values(inplace=True,ascending=True,na_position='first')
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    p1.plot(kind="barh", ax=axes, label="", color=COLOURS[0], width=WIDTH)
    fig.savefig(outputfile, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (outputfile,title))
    print("Wrote %s." % outputfile)
# def d14_aufmerksam ends here

def main():
    small_csv = ["01_recherchewo.csv", "02_pubform.csv",
                  "03_pubart.csv", "04_pubkanal.csv", "05_mitwem.csv",
                  "06_datenfinden.csv", "07_hilfe.csv", "08_zwischenergeb.csv",
                  "09_geraete.csv", "10_disziplin.csv", "11_wielange.csv",
                  "12_derzeit.csv", "13_arbeitsplatz.csv", "14_aufmerksam.csv"]

    d01_recherchewo(small_csv[0])
    d02_pubform(small_csv[1])
    d03_pubart(small_csv[2])
    d04_pubkanal(small_csv[3])
    d05_mitwem(small_csv[4])
    d06_datenfinden(small_csv[5])
    d07_hilfe(small_csv[6])
    d08_zwischenergeb(small_csv[7])
    # d09_geraete(small_csv[8])
    d10_disziplin(small_csv[9])
    d11_wielange(small_csv[10])
    d12_derzeit(small_csv[11])
    d13_arbeitsplatz(small_csv[12])
    d14_aufmerksam(small_csv[13])

    titles.close()
# def main ends here

if __name__ == "__main__":
    main()

#########
# FINIS #
#########
