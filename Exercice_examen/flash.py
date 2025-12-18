def ajout_des_plaques_du_jour(dossier_imma, attribution):
    for elem in attribution:
        if elem[0] not in dossier_imma:
            dossier_imma[elem[0]] = [elem[1],10]
        else:
            if dossier_imma[elem[0]][-1] > 0:
                dossier_imma[elem[0]].insert(-1,elem[1])


def ajout_des_points_du_jour(dossier_imma, infractions):
    tombes = []
    for elem in infractions:
        for registre, liste in dossier_imma.items():
            if elem[0] in liste[:-1]:
                if liste[-1] > 0 and liste[-1] - elem[1] <= 0 and registre not in tombes:
                    tombes.append(registre)
                liste[-1] -= elem[1]
    return tombes


def statistiques(dossier_imma):
    positif = 0
    vehicules = 0
    maxi = 0
    personne_max = []
    liste_neg = []
    for registre, liste in dossier_imma.items():
        if liste[-1] > 0:
            positif += 1
        else:
            liste_neg.append(registre)
        vehicules += len(liste)-1
        if len(liste)-1 == maxi:
            personne_max.append(registre)
        elif len(liste)-1 > maxi:
            maxi = len(liste)-1
            personne_max.clear()
            personne_max.append(registre)
    return[positif, vehicule, vehicule/len(dossier_imma), personne_max, liste_neg]


            
