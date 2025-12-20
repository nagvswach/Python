def parcours_spirale(matrice: list[list[int]]) -> list[int]:
    if not matrice or not matrice[0]:
        return []

    resultat = []

    haut = 0
    bas = len(matrice) - 1
    gauche = 0
    droite = len(matrice[0]) - 1

    while haut <= bas and gauche <= droite:
        # 1) gauche -> droite (ligne du haut)
        for j in range(gauche, droite + 1):
            resultat.append(matrice[haut][j])
        haut += 1

        # 2) haut -> bas (colonne de droite)
        for i in range(haut, bas + 1):
            resultat.append(matrice[i][droite])
        droite -= 1

        # 3) droite -> gauche (ligne du bas)
        if haut <= bas:
            for j in range(droite, gauche - 1, -1):
                resultat.append(matrice[bas][j])
            bas -= 1

        # 4) bas -> haut (colonne de gauche)
        if gauche <= droite:
            for i in range(bas, haut - 1, -1):
                resultat.append(matrice[i][gauche])
            gauche += 1

    return resultat





matrice = [
[ 1, 2, 3, 4],
[ 5, 6, 7, 8],
[ 9, 10, 11, 12],
[13, 14, 15, 16]
]
print(parcours_spirale(matrice))
