#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; mode: auto-fill; fill-column: 78 -*-
# Time-stamp: <2016-02-11 15:06:51 (kthoden)>

"""Auswertung
lade csv
"""
import csv
import json
import survey_data
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as image

print("config %s" % mpl.matplotlib_fname())
titles = open("titles.txt", mode="a")
# Set color transparency (0: transparent; 1: solid)
ALPHA_VALUE = 0.7
CHART_COLOUR = "#448CC7"
# using colour scheme from last year's poster
COLOURS = ['#663366', '#cc9900', '#99cccc', '#669966', '#669999', '#99cccc']
CSV_PATH = "csv_sources/"
EXTENSION = "png"                         #or pdf
WIDTH=0.75

def turnaround_dict(dictionary, value_list):
    """Turns
    ist = 'bibarchiv': {'Nein': 5, 'Ja': 93}, 'persoenlich': {'Nein': 39, 'Ja': 59}, 'eigenarchiv': {'Nein': 67, 'Ja': 31}, 'online': {'Nein': 2, 'Ja': 96}}
    into
    eigentlich = {'Nein': {'bibarchiv' : 5, 'persoenlich': 39, 'eigenarchiv': 67, 'online': 2}, 'Ja' : {'bibarchiv' : 93, 'persoenlich': 59, 'eigenarchiv': 31, 'online': 96}}
"""
    ja = {}
    nein = {}
    unsicher = {}

    for item in dictionary.keys():
        ja[item] = dictionary[item][value_list[0]]
        nein[item] = dictionary[item][value_list[1]]
        unsicher[item] = dictionary[item][value_list[2]]

    superpower = {value_list[0] : ja, value_list[1] : nein, value_list[2] : unsicher}

    return superpower
# def turnaround_dict ends here

class Scholar(object):
    def __init__(self, survey_id, software_in_phasen):
        self.survey_id = survey_id
        self.software_in_phasen = software_in_phasen
    # def __init__ ends here

    def __repr__(self):
        return 'Object representing a scholar.'
    # def __repr_ ends here

    def alle_tools(self, unique=False):
        """Gibt flache Liste aller Tools zurück"""
        tool_liste = []
        phasen = (self.software_in_phasen.values())
        for phase in phasen:
            for tool in phase:
                if unique:
                    if tool not in tool_liste and len(tool) > 0 :
                        tool_liste.append(tool)
                else:
                    tool_liste.append(tool)
        return(tool_liste)
    # def alle_tools ends here

    def tools_gesamt(self):
        """Wie viele unterschiedliche Tools werden im ganzen Prozeß benutzt?
        Gibt Liste zurück."""

        tool_liste = self.alle_tools(unique=True)

        return(tool_liste)
    # def tools_gesamt ends here

    def tool_category(self, tool):
        """In welche Kategorie fällt welches Tool? Rückgabewert ist der
        Klarname der Kategorie."""

        for category in survey_data.Kategorien:
            klarname = survey_data.Kategorien2[survey_data.Kategorien.index(category)]
            if tool in category:
                return(klarname)
    # def tool_category ends here

    def tool_scholar(self):
        """In welche Kategorie fällt welches Tool? Zurück kommt ein Tupel.
        Erster Teil ist die Liste der Kategorien, zweiter Teil ist ein
        Dictionary mit Tool:Kategorie"""

        tool_liste = self.alle_tools(unique=True)
        cat_list = []
        dict_tool_cat = {}

        for used_tool in tool_liste:
            cat_klar = self.tool_category(used_tool)
            dict_tool_cat[used_tool] = cat_klar

            if cat_klar not in cat_list:
                cat_list.append(cat_klar)

        return(cat_list, dict_tool_cat)
    # def tool_scholar ends here

    def erste_wahl(self):
        """Was wird am ehesten in der jeweiligen Phase benutzt? Rückgabe ist
        ein Dictionary Phase:Tool"""
        # print(self.erste_wahl.__doc__)

        erste_wahl_dict = {}

        for phase in survey_data.phasen:
            key = phase.capitalize()
            erste_wahl_dict[key] = self.software_in_phasen[key][0]

        return(erste_wahl_dict)
    # def erste_wahl ends here

    def tools_pro_phase(self):
        """Wie viele Tools werden pro Phase angegeben? Rückgabe ist Dictionary
        Phase:Anzahl der Tools"""
        # print(self.tools_pro_phase.__doc__)

        tpp_dict = {}

        for phase in survey_data.phasen:
            key = phase.capitalize()
            # a nifty trick: count the zero values, substract them from total
            tpp_dict[key] = str(4-self.software_in_phasen[key].count(""))

        return(tpp_dict)
    # def tools_pro_phase ends here

    def tool_ueberall(self):
        """Werden Tools in mehreren Phasen eingesetzt? Welche und wo? Rückgabe
        ist ein Tripel: Tool, welche Phasen"""
        # print(self.tool_ueberall.__doc__)

        super_liste = []
        resultat = []
        tool_liste = self.alle_tools(unique=False)

        # throw out empties
        pruned_list = [t for t in tool_liste if len(t) > 0]
        several = [t for t in pruned_list if pruned_list.count(t) > 1]
        # make a unique list
        unique = set(several)
        multi_list = list(unique)

        for tool in multi_list:
            phase_list = []
            for phase in survey_data.phasen:
                key = phase.capitalize()
                if tool in self.software_in_phasen[key]:
                    phase_list.append(key)
            resultat = [tool, str(phase_list)]

            super_liste.append(tuple(resultat))

        return(super_liste)
    # def tool_ueberall ends here
# class Scholar ends here

def category_lookup(tool):
    """In welche Kategorie fällt welches Tool? Rückgabewert ist der
    Klarname der Kategorie."""

    for category in survey_data.Kategorien:
        klarname = survey_data.Kategorien2[survey_data.Kategorien.index(category)]
        if tool in category:
            return(klarname)
# def category_lookup ends here

def eval_tsv(superlist):
    """reads the csv"""
    infile = open(CSV_PATH + superlist,'r')
    reader = csv.DictReader(infile, delimiter=(","), fieldnames = ("antwort_ID","zusatz1","zusatz2","zusatz3","zusatz4","planung1","planung2","planung3","planung4","recherche1","recherche2","recherche3","recherche4","überarbeitung1","überarbeitung2","überarbeitung3","überarbeitung4","analyse1","analyse2","analyse3","analyse4","publizieren1","publizieren2","publizieren3","publizieren4"))
    
    jsonStr = json.dumps(list(reader))
    jsonObj = json.loads(jsonStr)
    return jsonObj
# def eval_tsv ends here

data_dhaffin = eval_tsv("486724dhaffin.csv")
data_dhfern = eval_tsv("934152dhfern-ext-komplett.csv")

data = data_dhfern

def init_scholar(scholar):
    """Build object from scholar."""

    liste_zusatz = []
    liste_planung = []
    liste_recherche = []
    liste_ueberarbeitung = []
    liste_analyse = []
    liste_publizieren = []

    for number in range(1,5):
        key = survey_data.phasen[0] + str(number)
        liste_zusatz.append(scholar[key])
    for number in range(1,5):
        key = survey_data.phasen[1] + str(number)
        liste_planung.append(scholar[key])
    for number in range(1,5):
        key = survey_data.phasen[2] + str(number)
        liste_recherche.append(scholar[key])
    for number in range(1,5):
        key = survey_data.phasen[3] + str(number)
        liste_ueberarbeitung.append(scholar[key])
    for number in range(1,5):
        key = survey_data.phasen[4] + str(number)
        liste_analyse.append(scholar[key])
    for number in range(1,5):
        key = survey_data.phasen[5] + str(number)
        liste_publizieren.append(scholar[key])

    tools = {"Zusatz":tuple(liste_zusatz), "Planung":tuple(liste_planung), "Recherche":tuple(liste_recherche),
    "Überarbeitung":tuple(liste_ueberarbeitung), "Analyse":tuple(liste_analyse),
    "Publizieren": tuple(liste_publizieren)}

    tmp_sch = Scholar(scholar["antwort_ID"], tools)
    
    return tmp_sch
# def init_scholar ends here

def auswertung(tg, ts, ew, tpp, tu):
    """Die Auswertung. Ausgabe auf der Kommandozeile."""

    print("Wie viele unterschiedliche Tools werden im ganzen Prozeß benutzt?")
    print("  Insgesamt wurden %d unterschiedliche Tools genutzt" %
          len(tg))
    print("  Nämlich diese: %s" % [item for item in tg])
    print("In welche Kategorie fällt welches Tool?")
    for tool_key in ts[1]:
        print("  " + tool_key + " ist aus " + ts[1][tool_key])
    print("Die folgenden %d Kategorien kommen überhaupt vor: " % len(ts[0]))
    for item in ts[0]:
        print("  " + item)
    print("Was wird am ehesten in der jeweiligen Phase benutzt?")
    for phase in ew:
        if ew[phase]:
            print("  " + phase + ": " + ew[phase])
        else:
            print("  " + phase + ": keine Tools angegeben")
    print("Wie viele Tools werden pro Phase angegeben?")
    for tool in tpp:
        print("  " + tool + ": " + tpp[tool])
    print("Werden Tools in mehreren Phasen eingesetzt? Welche und wo?")
    for tup in tu:
        print("  %s wird in %d Phasen eingesetzt: %s" % (tup[0], len(tup[1]), tup[1]))
# def auswertung ends here

def single_scholar_overview(number):
    """Show statistics of a single scholar."""

    scholar = data[number]
    beispiel = init_scholar(scholar)

    auswertung(beispiel.tools_gesamt(), beispiel.tool_scholar(),
               beispiel.erste_wahl(), beispiel.tools_pro_phase(),
               beispiel.tool_ueberall())
# def single_scholar_overview ends here

def graph_category(list_categories, filename = "15_categories." + EXTENSION,
                   xticks = ""):
    """How often are which categories used?"""

    title = "Aus welchen Kategorien stammen die benutzten Programme?"

    cat = {x : list_categories.count(x) for x in set(list_categories)}
    # {0: 6, 1: 11, 2: 18, 3: 18, 4: 12, 5: 18, 6: 10, 7: 1, 8: 5, 9: 1, 10: 2, 11: 1}
    cat_vis = pd.Series(cat)
    cat_vis.sort_values(inplace=True,ascending=False)
    # create figure & 1 axis
    fig, axes = plt.subplots(nrows=1, ncols=1)

    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    if xticks:
        axes.set_xticks(xticks)
    axes.yaxis.set_label_coords(0, 1.08)

    # Here we go!
    cat_vis.plot(kind="barh", ax=axes, color=COLOURS[0], width=WIDTH)
    fig.savefig(filename, bbox_inches='tight')
    plt.close(fig)
    titles.write("%s: Abb. 4.:%s\n" % (filename,title))
    print("Antwort in %s" % filename)
# def graph_category ends here

def graph_tools_pro_zyklus(list_number_of_tools):
    """Create graph for tools per research cycle"""

    title = "Wie viele unterschiedliche Tools werden im gesamten Forschungskreislauf benutzt?"
    filename = "16_tools_pro_zyklus." + EXTENSION
    
    tpz = {x : list_number_of_tools.count(x) for x in set(list_number_of_tools)}
    tpz_vis = pd.Series(tpz)
    fig, axes = plt.subplots(nrows=1, ncols=1)#, figsize=(20,10))

    axes.set_ylabel("Anzahl Tools", alpha=ALPHA_VALUE, ha='left')
    axes.set_xlabel("BenutzerInnen",alpha=ALPHA_VALUE, ha='left')

    # Here we go!
    tpz_vis.plot(kind="barh", ax=axes, color=COLOURS[0], width=WIDTH)
    fig.savefig(filename, bbox_inches='tight')
    plt.close(fig)
    titles.write("%s: Abb. 4.:%s\n" % (filename,title))
    print("Antwort in %s" % filename)
# def graph_tools_pro_zyklus ends here

def graph_erste_wahl(dict_erste_wahl):
    """What tool is used preferably per phase?"""

    print(graph_erste_wahl.__doc__)

    # make a graph for each phase
    title = "Welches Tool wird vorzugsweise in einer Phase eingesetzt?"
    filename = "17_erste_wahl_bar." + EXTENSION

    count_planung = pd.Series({x : dict_erste_wahl["Planung"].count(x) for x in set(dict_erste_wahl["Planung"])})
    count_recherche = pd.Series({x : dict_erste_wahl["Recherche"].count(x) for x in set(dict_erste_wahl["Recherche"])})
    count_ueberarbeitung = pd.Series({x : dict_erste_wahl["Überarbeitung"].count(x) for x in set(dict_erste_wahl["Überarbeitung"])})
    count_analyse = pd.Series({x : dict_erste_wahl["Analyse"].count(x) for x in set(dict_erste_wahl["Analyse"])})
    count_publizieren = pd.Series({x : dict_erste_wahl["Publizieren"].count(x) for x in set(dict_erste_wahl["Publizieren"])})

    count_planung.sort_values(inplace=True,ascending=True)
    count_recherche.sort_values(inplace=True,ascending=True)
    count_ueberarbeitung.sort_values(inplace=True,ascending=True)
    count_analyse.sort_values(inplace=True,ascending=True)
    count_publizieren.sort_values(inplace=True,ascending=True)
    
    # create figure & 1 axis
    fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(10,20))

    axes[0].set_title("Planung", alpha=ALPHA_VALUE, loc='left')
    axes[0].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[1].set_title("Recherche", alpha=ALPHA_VALUE, loc='left')
    axes[1].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[2].set_title("Überarbeitung", alpha=ALPHA_VALUE, loc='left')
    axes[2].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[3].set_title("Analyse", alpha=ALPHA_VALUE, loc='left')
    axes[3].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[4].set_title("Publizieren", alpha=ALPHA_VALUE, loc='left')
    axes[4].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')

    count_planung.plot(kind="barh", ax=axes[0], color=COLOURS[0], width=WIDTH)
    count_recherche.plot(kind="barh", ax=axes[1], color=COLOURS[0], width=WIDTH)
    count_ueberarbeitung.plot(kind="barh", ax=axes[2], color=COLOURS[0], width=WIDTH)
    count_analyse.plot(kind="barh", ax=axes[3], color=COLOURS[0], width=WIDTH)
    count_publizieren.plot(kind="barh", ax=axes[4], color=COLOURS[0], width=WIDTH)

    fig.savefig(filename, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (filename,title))
    print("Wrote %s." % filename)
    plt.close(fig)

    # also as a pie chart
    filename_pie = filename.replace("bar", "pie")
    fig2, axes2 = plt.subplots(nrows=2, ncols=3, figsize=(12,9))

    count_planung.plot(kind="pie", ax=axes2[0][0], colors=COLOURS, title="Planung", label="")
    count_recherche.plot(kind="pie", ax=axes2[0][1], colors=COLOURS, title="Recherche", label="")
    count_ueberarbeitung.plot(kind="pie", ax=axes2[0][2], colors=COLOURS, title="Überarbeitung", label="")
    count_analyse.plot(kind="pie", ax=axes2[1][0], colors=COLOURS, title="Analyse", label="")
    count_publizieren.plot(kind="pie", ax=axes2[1][1], colors=COLOURS, title="Publizieren", label="")

    fig2.savefig(filename_pie, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (filename_pie,title))
    print("Wrote %s." % filename_pie)
    plt.close(fig2)
# def graph_erste_wahl ends here

def graph_tools_pro_phase(dict_tpp):
    """How many different tools are used per phase?"""

    print(graph_tools_pro_phase.__doc__)

    # make a graph for each phase
    filename = "18_tools_pro_phase." + EXTENSION

    title = "Wie viele unterschiedliche Tools werden pro Phase benutzt?"

    anzahl_tools_planung = pd.Series({x : dict_tpp["Planung"].count(x) for x in set(dict_tpp["Planung"])})
    anzahl_tools_recherche = pd.Series({x : dict_tpp["Recherche"].count(x) for x in set(dict_tpp["Recherche"])})
    anzahl_tools_ueberarbeitung = pd.Series({x : dict_tpp["Überarbeitung"].count(x) for x in set(dict_tpp["Überarbeitung"])})
    anzahl_tools_analyse = pd.Series({x : dict_tpp["Analyse"].count(x) for x in set(dict_tpp["Analyse"])})
    anzahl_tools_publizieren = pd.Series({x : dict_tpp["Publizieren"].count(x) for x in set(dict_tpp["Publizieren"])})

    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20,10))

    axes[0][0].set_title("Planung", alpha=ALPHA_VALUE, loc='left')
    axes[0][1].set_title("Recherche", alpha=ALPHA_VALUE, loc='left')
    axes[0][2].set_title("Überarbeitung", alpha=ALPHA_VALUE, loc='left')
    axes[1][0].set_title("Analyse", alpha=ALPHA_VALUE, loc='left')
    axes[1][1].set_title("Publizieren", alpha=ALPHA_VALUE, loc='left')

    axes[0][0].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[0][1].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[0][2].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[1][0].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes[1][1].set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')

    anzahl_tools_planung.plot(kind="barh", ax=axes[0][0], color=COLOURS[0], width=WIDTH)
    anzahl_tools_recherche.plot(kind="barh", ax=axes[0][1], color=COLOURS[0], width=WIDTH)
    anzahl_tools_ueberarbeitung.plot(kind="barh", ax=axes[0][2], color=COLOURS[0], width=WIDTH)
    anzahl_tools_analyse.plot(kind="barh", ax=axes[1][0], color=COLOURS[0], width=WIDTH)
    anzahl_tools_publizieren.plot(kind="barh", ax=axes[1][1], color=COLOURS[0], width=WIDTH)

    fig.savefig(filename, bbox_inches='tight')
    titles.write("%s: Abb. 4.:%s\n" % (filename,title))
    print("Wrote %s." % filename)
    plt.close(fig)
# def graph_tools_pro_phase ends here

def several_tools_per_phase(supertupel):
    """What can we gather from people who use a tool more than once?"""

    title = "Mehrfach genutzte Tools pro Forschungszyklus"

    filename = "19_tools_in_mehreren_phasen." + EXTENSION

    tisp_user_how_many = []
    einer = []
    alle = []

    for st in supertupel:
        # User benutzt %d Tools in mehreren Phasen
        tisp_user_how_many.append(len(st))
        for tool in st:
            alle.append(category_lookup(tool[0]))
                
    tisp_series2 = pd.Series(alle)
    pvc2 = pd.value_counts(tisp_series2.values)
    print("Welche Kategorien werden mehrfach genutzt?")
    # print(pvc2)

    fig, axes = plt.subplots(nrows=1, ncols=1)#, figsize=(20,10))

    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    axes.set_ylabel("Kategorien", alpha=ALPHA_VALUE, ha='left')

    # Here we go!
    pvc2.plot(kind="barh", ax=axes, color=COLOURS[0], width=WIDTH)
    fig.savefig(filename, bbox_inches='tight')
    plt.close(fig)
    print("Antwort in %s" % filename)
    titles.write("%s: Abb. 4.:%s\n" % (filename,title))
# def several_tools_per_phase ends here
    
def extraphasen():
    """Count unique answers regarding the extraphase."""

    df = pd.read_csv(CSV_PATH + 'phasesinnvoll.csv')

    filename = "20_extraphase." + EXTENSION
    title = "Halten Sie die Aufteilung des Forschungsprozesses in diese Phasen für sinnvoll?"

    p1 = pd.value_counts(df['p1'].values)
    p2 = pd.value_counts(df['p2'].values)
    p3 = pd.value_counts(df['p3'].values)
    p4 = pd.value_counts(df['p4'].values)
    p5 = pd.value_counts(df['p5'].values)

    faker = {'Planung': {'Ja': 93, 'Unsicher': 3, 'Nein': 2},
     'Recherche': {'Ja': 98, 'Unsicher': 0, 'Nein': 1},
     'Überarbeitung': {'Ja': 85, 'Unsicher': 8, 'Nein': 3},
     'Analyse': {'Ja': 90, 'Unsicher': 4, 'Nein': 3},
     'Publizieren': {'Ja': 79, 'Unsicher': 11, 'Nein': 2}}

    values = ["Ja", "Nein", "Unsicher"]
    hihi = turnaround_dict(faker, values)
    print(hihi)

    dfdf = pd.DataFrame(hihi)
    fig, axes = plt.subplots(nrows=1, ncols=1)
    axes.set_xlabel("BenutzerInnen", alpha=ALPHA_VALUE, ha='left')
    dfdf.plot(kind='barh', ax=axes, stacked=True, color=COLOURS, width=WIDTH)

    fig.savefig(filename, bbox_inches='tight')

    tools_extraphase = ["Wordpress", "Zotero", "MS Word", "coraw", "MS Excel",
    "MS Word", "MS Notes", "Zotero","Zotero", "Word", "word", "excel",
    "TUSTEP", "INDESIGN", "lesen", "schreiben", "rechnen", "Google"]

    categ_list = []
    for tool in tools_extraphase:
        categ_list.append(category_lookup(tool))
    graph_category(categ_list, filename="21_extraphase_category." + EXTENSION,
                   xticks=[1,2,3,4])
    titles.write("%s: Abb. 4.:%s\n" % (filename,title))
    print("Wrote %s." % filename)
# def extraphasen ends here

def main():
    # single_scholar_overview(81)

    list_tools_per_phase = []
    tools_pro_zyklus = []
    cat_often = []
    supertupel = []
    tools_all_phases = []
    list_erste_wahl = []

    # make statistics for the whole bunch, gather data
    for scholars in data:
        population = init_scholar(scholars)

        list_erste_wahl.append(population.erste_wahl())
        list_tools_per_phase.append(population.tools_pro_phase())
        tools_pro_zyklus.append(len(population.tools_gesamt()))
        tools_all_phases.append(population.software_in_phasen)
        # which category how often?
        # these are unique values. So per scholar each category is only
        # counted once
        for tool in population.tool_scholar()[0]:
            cat_often.append(tool)
        # tools in several phases
        tisp = population.tool_ueberall()
        if tisp:
            tum, tuum = tisp[0]
            supertupel.append(tisp)


    ##################################
    # Things that are done per phase #
    ##################################
    dict_erste_wahl = {}
    dict_tools_pro_phase = {}

    for phase in survey_data.phasen:
        tmp_list_ew = []
        tmp_list_tpp = []
        key = phase.capitalize()
        # "Was wird am ehesten in der jeweiligen Phase benutzt?"
        for item in list_erste_wahl:
            if len(item[key]) > 0:
                tmp_list_ew.append(category_lookup(item[key]))
            else:
                tmp_list_ew.append("Keine Angabe")
        dict_erste_wahl[key] = tmp_list_ew
        # number of tools used in phases
        for item in list_tools_per_phase:
            tmp_list_tpp.append(item[key])
        dict_tools_pro_phase[key] = tmp_list_tpp

    #####################
    # output the graphs #
    #####################
    graph_tools_pro_zyklus(tools_pro_zyklus)
    graph_erste_wahl(dict_erste_wahl)
    graph_tools_pro_phase(dict_tools_pro_phase)
    graph_category(cat_often)
    extraphasen()
    several_tools_per_phase(supertupel)
    titles.close()
if __name__ == "__main__":
    main()

#########
# FINIS #
#########
