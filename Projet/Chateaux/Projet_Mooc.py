"""
Soussi Nagui, science informatique, BA1
JEUX : "ESCAPE-GAME, PROJET MOOC"
"""

from CONFIGS import *
import turtle
import time


def lire_matrice(fichier):
    """
    Lit un fichier et cree une matrice (liste de listes) a partir de celui-ci.
    """
    matrice = []
    with open(fichier, "r", encoding="utf-8") as fich:
        for line in fich.readlines():
            d = []
            for elem in line.split():
                d.append(int(elem))
            matrice.append(d)
    return matrice


def calculer_pas(matrice):
    """
    Calcule la taille d'une case et retourne sa valeur.
    """
    largeur = (abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])) // len(matrice)
    hauteur = (abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])) // len(matrice[0])
    return min(largeur, hauteur)


def coordonnees(case, pas):
    """
    Calcule et retourne les coordonnees (x,y) de la case (i,j).
    """
    i = ZONE_PLAN_MINI[0] + case[1] * pas
    j = ZONE_PLAN_MAXI[1] - (case[0] * pas)
    return (i, j)


def tracer_carre(dimension):
    """
    Trace graphiquement un carre.
    """
    turtle.down()
    turtle.begin_fill()
    turtle.forward(dimension)
    turtle.left(90)
    turtle.forward(dimension)
    turtle.left(90)
    turtle.forward(dimension)
    turtle.left(90)
    turtle.forward(dimension)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()


def tracer_case(case, couleur, pas):
    """
    Construit graphiquement une case du plateau.
    """
    turtle.tracer(0, 0)
    turtle.up()
    turtle.goto(case)
    turtle.fillcolor(couleur)
    tracer_carre(pas)


def afficher_plan(matrice):
    """
    Attribue les couleurs a chaque case selon la valeur dans la matrice.
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            match matrice[i][j]:
                case 0:
                    tracer_case(coordonnees((i, j), pas), COULEUR_CASES, pas)
                case 1:
                    tracer_case(coordonnees((i, j), pas), COULEUR_MUR, pas)
                case 2:
                    tracer_case(coordonnees((i, j), pas), COULEUR_OBJECTIF, pas)
                case 3:
                    tracer_case(coordonnees((i, j), pas), COULEUR_OBJET, pas)
                case 4:
                    tracer_case(coordonnees((i, j), pas), COULEUR_PORTE, pas)


def deplacer_gauche():
    turtle.onkeypress(None, "Left")
    global matrice, position
    position = deplacer(matrice, position, (0, -1))
    turtle.onkeypress(deplacer_gauche, "Left")


def deplacer_droite():
    turtle.onkeypress(None, "Right")
    global matrice, position
    position = deplacer(matrice, position, (0, 1))
    turtle.onkeypress(deplacer_droite, "Right")


def deplacer_haut():
    turtle.onkeypress(None, "Up")
    global matrice, position
    position = deplacer(matrice, position, (-1, 0))
    turtle.onkeypress(deplacer_haut, "Up")


def deplacer_bas():
    turtle.onkeypress(None, "Down")
    global matrice, position
    position = deplacer(matrice, position, (1, 0))
    turtle.onkeypress(deplacer_bas, "Down")


def deplacer(matrice, position, mouvement):
    """
    Met a jour la position du personnage et declenche les reactions selon la case.
    """
    destination = (position[0] + mouvement[0], position[1] + mouvement[1])

    match matrice[destination[0]][destination[1]]:
        case 1:  # mur
            return position

        case 2:  # objectif
            position = moove(position, pas, destination)
            afficher_annonces("Vous avez gagne !!")
            time.sleep(3)
            exit()

        case 3:  # porte / question
            destination = poser_questions(matrice, destination, position)
            position = moove(position, pas, destination)
            return position

        case 4:  # objet
            ramasser_objet(destination)
            position = moove(position, pas, destination)
            return position

        case _:  # case libre
            position = moove(position, pas, destination)
            return position

    return position


def moove(position, pas, destination):
    """
    Deplace le personnage et recolorie la case parcourue.
    """
    tracer_case(coordonnees(position, pas), COULEUR_VUE, pas)

    turtle.up()
    turtle.goto(coordonnees(destination, pas))
    turtle.forward(pas / 2)
    turtle.left(90)
    turtle.forward(pas / 2)
    turtle.down()
    turtle.dot((pas * RATIO_PERSONNAGE), COULEUR_PERSONNAGE)
    turtle.right(90)
    turtle.up()

    return destination


def creer_dictionnaire_des_objets(fichier_des_objets):
    """
    Cree et retourne un dictionnaire a partir d'un fichier objets.
    """
    dico = {}
    with open(fichier_des_objets, "r", encoding="utf-8") as file:
        for line in file.readlines():
            a, b = eval(line)
            dico[a] = b
    return dico


def creer_dictionnaire_des_portes(fichier_des_questions):
    """
    Cree et retourne un dictionnaire a partir d'un fichier questions/reponses.
    """
    dico_porte = {}
    with open(fichier_des_questions, "r", encoding="utf-8") as fi:
        for ligne in fi.readlines():
            a, b = eval(ligne)
            dico_porte[a] = b
    return dico_porte


def ajouter_element(nb_objets, message):
    turtle.goto(POINT_AFFICHAGE_INVENTAIRE)
    turtle.left(180)
    turtle.forward(10 * pas)
    turtle.left(90)
    turtle.forward((nb_objets + 3) * pas)
    turtle.left(90)
    turtle.write(message, True, font=("Arial", 10, "bold"))


def ramasser_objet(destination):
    global nb_objets, matrice
    nb_objets += 2
    dico = creer_dictionnaire_des_objets(fichier_objets)
    afficher_annonces("Vous avez trouve : " + dico[destination])
    ajouter_element(nb_objets, dico[destination])
    matrice[destination[0]][destination[1]] = 0


def afficher_annonces(message):
    turtle.up()
    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.down()

    largeur = (len(matrice[0]) * pas) + (12 * pas)
    turtle.forward(largeur)
    turtle.left(90)
    turtle.forward(6 * pas)
    turtle.left(90)
    turtle.forward(largeur)
    turtle.left(90)
    turtle.forward(6 * pas)

    turtle.end_fill()
    turtle.up()
    turtle.left(90)

    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.forward(1 * pas)
    turtle.left(90)
    turtle.forward(2.5 * pas)
    turtle.right(90)

    turtle.write(message, True, font=("Arial", 9, "bold"))
    turtle.up()


def poser_questions(matrice, destination, position):
    dico_portes = creer_dictionnaire_des_portes(fichier_questions)
    reponse = turtle.textinput("Question", dico_portes[destination][0])
    turtle.listen()
    if reponse == dico_portes[destination][1]:
        matrice[destination[0]][destination[1]] = 0
        return destination
    return position


if __name__ == "__main__":
    matrice = lire_matrice(fichier_plan)
    pas = calculer_pas(matrice)
    afficher_plan(matrice)

    nb_objets = 0
    position = POSITION_DEPART

    # Cadre inventaire
    turtle.up()
    turtle.goto(POINT_AFFICHAGE_INVENTAIRE)
    turtle.down()
    turtle.right(90)
    turtle.forward(len(matrice) * pas)
    turtle.right(90)
    turtle.forward(11 * pas)
    turtle.right(90)
    turtle.forward(len(matrice) * pas)
    turtle.right(90)
    turtle.forward(11 * pas)
    turtle.up()

    turtle.left(180)
    turtle.forward(9 * pas)
    turtle.left(90)
    turtle.forward(3 * pas)
    turtle.left(90)
    turtle.write("Inventaire", True, font=("Arial", 15, "bold"))

    # Cadre annonces
    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.down()

    largeur = (len(matrice[0]) * pas) + (12 * pas)
    turtle.forward(largeur)
    turtle.left(90)
    turtle.forward(6 * pas)
    turtle.left(90)
    turtle.forward(largeur)
    turtle.left(90)
    turtle.forward(6 * pas)
    turtle.up()

    # Placement joueur
    turtle.goto(coordonnees(POSITION_DEPART, pas))
    turtle.left(90)
    turtle.forward(pas / 2)
    turtle.left(90)
    turtle.forward(pas / 2)
    turtle.down()
    turtle.dot((pas * RATIO_PERSONNAGE), COULEUR_PERSONNAGE)
    turtle.right(90)
    turtle.up()

    # Deplacements
    turtle.listen()
    turtle.onkeypress(deplacer_gauche, "Left")
    turtle.onkeypress(deplacer_droite, "Right")
    turtle.onkeypress(deplacer_haut, "Up")
    turtle.onkeypress(deplacer_bas, "Down")
    turtle.mainloop()

