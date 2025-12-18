def lire_point(ficher):
    point = []
    with open(fichier,mode ='r', encoding='utf-8')as f:
        for ligne in f:
            x_str, y_str = ligne.strip().split(",")
            x = int(x_str.strip())
            y = int(y_str.strip())
            point.append((x,y))
    return point


def calcule_air(lst):
    air = (lst[1][0] - lst [0][0]) * (lst[0][1] - lst[2][1])
    return air


def analyser_rectangle(liste_fichier):
    aires = 0 
    infos = []
    for nom in liste_fichier:
        pts = lire_point(nom)
        air = calcule_air(pts)
        infos.append(air,nom)
    infos.sort()
    liste_fichier.clear()
    for air, nom in infos:
        liste_fichier.append(nom)
        aires += air
    return aires / len(liste_fichier)


