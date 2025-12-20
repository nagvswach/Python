LOCAUX = {
        "Forum AB": 522,
        "Forum C": 261,
        "Forum D": 261,
        "NO.506": 62,
        }
PERSONNES = {
"info": [523, 208, 174, 180, 98],
"math": [103, 59, 48, 41, 37],
"geologie": [40, 32, 31, 27, 21],
}




def locaux_possibles(section, annee):
    if section not in PERSONNES:
        raise ValueError("Section inexistante")
    if annee < 1 or annee > 5:
        raise ValueError("Annee invalide")
    dispo = []
    for local,nb_places in LOCAUX.items():
        if PERSONNES[section][annee - 1] <= nb_places:
            dispo.append(local)
    return dispo


def moyenne_par_annee():
    moyennes = []
    for i in range(5):
        moy = 0
        for section in PERSONNES:
            moy += PERSONNES[section][i]
        moyennes.append(moy/len(PERSONNES))
    return moyennes
            
            
def locaux_assemblee_general(section):
    if section not in PERSONNES:
        raise ValueError("section inexistante")
    dispo = []
    total = 0 
    for personnes in PERSONNES[section]:
        total += personnes
    for local, nb_personnes in LOCAUX.items():
        if total <= nb_personnes:
            dispo.append(local)
    return dispo



print(locaux_assemblee_general("math"))
print(moyenne_par_annee())

