import pandas as pd
import sqlite3 as sql


database = sql.connect("concours.db")
c = database.cursor()

# data = pd.read_excel('Inscription.xlsx', header=1)
# liste_etat_dossier = []
# liste_concours = []
# liste_autres_prenoms = []
# liste_serie_bac = []

####### initialisation de la table ep_option pour 0/NULL/NULL
# liste_ep_option = []
# c.execute("INSERT INTO ep_option(id) VALUES (0);")
# database.commit()

# dictionnaires des épreuves
dico_epreuves = {

    ##### ECRITES #####
    "Langue": 28,
    "Informatique ou Sciences industrielles": 599,
    "Mathématiques 1": 600,
    "Mathématiques 2": 601,
    "Physique 1": 602,
    "Physique 2": 603,
    "Chimie": 604,
    "Français": 605,
    "Sciences industrielles": 606,
    "Informatique": 1050,
    "bonification_ecrit": 9898,
    "total_ecrit": 9899,

    ##### SPECIFIQUES CMT #####
    "QCM info/physique": 1,
    "Entretien nouvelles technologies": 2,
    "QCM anglais": 3,
    "Mathématiques": 4,

    ##### ORALES CMT #####
    "Physique ou Sciences industrielles": 5,
    "Entretien": 6,
    "Anglais": 7,
    "Mathématiques": 8,

    ##### ORALES CCMP #####
    "Physique": 9,
    "Français": 10,
    "Anglais": 11,
    "Mathématiques": 12,

    ##### TOTAL ORAL #####
    "Mathématiques (harmonisé)": 400,
    "Mathématiques (affichée)":401,
    "max_physique": 9900,
    "max_anglais": 9901,
    "bonification_oral": 9998,
    "total_oral": 9999,

    ##### TOTAL (ECRIT+ORAL) ######
    "total": 10000,

    ##### CLASSEMENT #####
    "bonus_interclassement": 10198,
    "total_avec_interclassement": 10199,
    "note_entretien_exaequo": 10200,
    "note_anglais_exaequo": 10201,

    ##### ECRITES PT #####
    "Mathématiques B": 700,
    "Mathématiques C": 701,
    "Physique A": 702,
    "Physique B": 703,
    "Informatique modélisation": 704,
    "Sciences industrielles A": 705,
    "Français B": 706,
    "Langue A": 707,

    ##### ECRITES TSI #####
    "Mathématiques 1": 800,
    "Mathématiques 2": 801,
    "Physique 1": 802,
    "Physique 2": 803,
    "Français": 804,
    "Langue": 805,
    "Sciences industrielles": 806,
    "Informatique": 807,

    ##### ORALES CCS #####
    "Mathématiques 1": 13,
    "Mathématiques 2": 14,
    "Physique-chimie 1": 15,
    "Physique-chimie 2": 16,
    "Langue vivante": 17,
    "TP Physique-chimie": 18,
    "S2I": 19,

}

for i in range(len(data)):
    """
    ####### etat_dossier
    code_etat_dossier = data['CODE_ETAT_DOSSIER'][i]
    lib_etat_dossier = data['LIBELLE_ETAT_DOSSIER'][i]
    if code_etat_dossier not in liste_etat_dossier:
        liste_etat_dossier.append(code_etat_dossier)
        consigne_sql = "INSERT INTO etat_dossier VALUES (?, ?);"
        c.execute(consigne_sql, (int(code_etat_dossier), lib_etat_dossier))

    ####### concours
    code_concours = data['CODE_CONCOURS'][i]
    lib_concours = data['LIBELLE_CONCOURS'][i]
    voie_concours = data['VOIE'][i]
    if code_concours not in liste_concours:
        liste_concours.append(code_concours)
        consigne_sql = "INSERT INTO concours VALUES (?, ?, ?);"
        c.execute(consigne_sql, (int(code_concours), lib_concours, voie_concours))
    
    ####### autres_prenoms
    code_etudiant = data['CODE_CANDIDAT'][i]
    autre_prenom = data['AUTRES_PRENOMS'][i]
    couple = [code_etudiant, autre_prenom]
    if (type(autre_prenom) == str) & (couple not in liste_autres_prenoms):
        liste_autres_prenoms.append(couple)
        consigne_sql = "INSERT INTO autres_prenoms VALUES (?, ?);"
        c.execute(consigne_sql, (int(code_etudiant), autre_prenom))
    
    ####### serie_bac
    code_serie = data['CODE_SERIE'][i]
    nom_serie = data['SERIE'][i]
    if code_serie not in liste_serie_bac:
        liste_serie_bac.append(code_serie)
        consigne_sql = "INSERT INTO serie_bac VALUES (?, ?);"
        c.execute(consigne_sql, (int(code_serie), nom_serie))

    ####### ep_option
    for j in range(1, 5):
        ep, op = data[f'EPREUVE{j}'][i], data[f'OPTION{j}'][i]
        if ((type(ep) == str) or (type(op) == str)) & ([ep, op] not in liste_ep_option):
            liste_ep_option.append([ep, op])
            consigne_sql = "INSERT INTO ep_option(epreuve, option) VALUES (?, ?);"
            c.execute(consigne_sql, (ep, op))
    """
    ####### epreuve


database.commit()
database.close()


""" Aides utiles
    file_path = 'D:\JCZ-Profil\Documents\Mes devoirs\1A Telecom Nancy\PPII\ppii2k21\dow\data\public\Inscription.xlsx'
    str_test = "insert into candidat(code, nom, date_de_naissance) values (?, ?, ?)"
    str = "INSERT INTO candidat(code, civilite, nom, prenom, date_de_naissance, classe, puissance, voie_concours, etablissement, adresse1, adresse2, code_postal, commune, code_adr_pays, mail, tel, por) VALUES (CODE_CANDIDAT, CIVILITE, nom, PRENOM, DATE_DE_NAISSANCE, CLASSE, PUISSANCE, VOIE, CODE_ETABLISSEMENT, ADRESSE1, ADRESSE2, CP, VILLE, CODE_PAYS, EMAIL, TELEPHONE, TEL_PORTABLE)"
    data = data.values()
"""
