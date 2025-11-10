def gagnant(grille):
    taille_li = len(grille)
    taille_col = len(grille[0])
    for i in range(taille_li):
        for j in range(taille_col):
            if grille[i][j] != 'V':
                couleur = grille[i][j]

                # Vers la droite
                compteur = 1
                y = j + 1
                while y < taille_col and grille[i][y] == couleur:
                    compteur += 1
                    y += 1
                if compteur >= 4:
                    return couleur

                # Vers le bas
                compteur = 1
                x = i + 1
                while x < taille_li and grille[x][j] == couleur:
                    compteur += 1
                    x += 1
                if compteur >= 4:
                    return couleur

                # Diagonale bas-droite
                compteur = 1
                x, y = i + 1, j + 1
                while x < taille_li and y < taille_col and grille[x][y] == couleur:
                    compteur += 1
                    x += 1
                    y += 1
                if compteur >= 4:
                    return couleur

                # Diagonale bas-gauche
                compteur = 1
                x, y = i + 1, j - 1
                while x < taille_li and y >= 0 and grille[x][y] == couleur:
                    compteur += 1
                    x += 1
                    y -= 1
                if compteur >= 4:
                    return couleur

    return None

