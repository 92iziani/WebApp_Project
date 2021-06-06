from pathlib import Path
import pandas as pd
import sqlite3 as sql


def run_verif(database: sql.Connection, path: Path):
    c = database.cursor()
    with open(Path('headers.txt'), 'r') as file:
        for line in file:
            if line[0] == '\t':
                ldata = line[1:-1].split(sep=';')
                column = ldata.pop(0)
                if "inscription" in column:
                    column = tableurs[0].columns[0]
                if ldata[0] == 'pk':
                    pkey = column
                else:
                    select_req = f'SELECT {ldata[2]} FROM {ldata[0]} AS {ldata[1]} '
                    ldata = ldata[3:]
                    if ldata.pop(0)=='J':
                        select_req += f'JOIN {ldata[0]} AS {ldata[1]} ON {ldata[2]} '
                        ldata = ldata[3:]
                    select_req += f'WHERE {ldata[-1]} = ?'
                    for tabl in tableurs:
                        for i in range(len(tabl)):
                            if repr(tabl[pkey][i]) != 'nan':
                                c.execute(f"SELECT ca.code FROM candidat AS ca JOIN classe AS cl ON ca.classe=cl.code WHERE (ca.type_admissible NOT NULL OR cl.lib='ATS') AND ca.code = ?", (int(tabl[pkey][i]),))
                                if c.fetchone() is not None:
                                    try:
                                        c.execute(select_req, (int(tabl[pkey][i]),))
                                    except:
                                        print(select_req, int(tabl[pkey][i]))
                                    res = c.fetchone()
                                    if res is None and repr(tabl[column][i]) != 'nan':
                                        print("\tDonnée non présente :", tabl[pkey][i], column, tabl[column][i], res)
                                    elif not (repr(tabl[column][i])=='nan' and (res is None or res[0] is None) or tabl[column][i] == res[0]):
                                        print("\tDonnées non égales :", int(tabl[pkey][i]), column, tabl[column][i], res[0])
            else:
                if 'XXXX.xlsx' in line:
                    nheader = 1
                else:
                    nheader = 0
                if 'CMT_Oraux' in line:
                    complement_select = ' etat_classes = 7 AND'
                else:
                    complement_select = ''
                print(line[:-1])
                tableurs = [pd.read_excel(path/f, header=nheader, converters={'n_demi': lambda x: str(x)+'/2'}, dtype={'code_postal': str, 'Can _cod _pos': str}) if 'xlsx' in f else pd.read_csv(path/f, sep=";", header=nheader, decimal=',') for f in line[:-1].split(sep=';')]

if __name__ == '__main__':
    pathdb = Path("concours.db")
    db = sql.Connection(pathdb)
    pathfiles = Path('../PPII_ressources/data/public')
    run_verif(db, pathfiles)