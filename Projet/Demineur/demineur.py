"""
Prenom : Nagui
Nom : Soussi
Matricule : 000545871
Section : B1-INFO
Projet Q1, jeu, Le demineur.
"""

import sys
import random
from colorama import Fore, Style

"""
J'ai mis en commentaires dans la fonction print_board l'implementation des couleurs car il faut installer
la bibliotheque colorama, sans quoi cela ferait des erreurs. Je la laisse car selon moi, les couleurs sont tres
importantes pour la facilite de l'utilisateur et apporte un enorme + visuel.
"""


def create_board(ligne, colones):
    """
    Prend en compte deux nombres qui definiront les lignes et colonnes et retourne une matrice
    qui permettra de creer differents plateaux.
    """
    board = []
    for i in range(ligne):
        liste = []
        for y in range(colones):
            liste.append(".")
        board.append(liste)
    return board


def print_board(board):
    """
    Fonction qui permet d'imprimer un plateau encadre avec tous les parametres.
    Param : matrice qui donne les dimensions du plateau et son contenu initial.
    Retourne : ne retourne rien, affiche juste le plateau.
    """
    m = len(board[0])
    cptLine = 0
    espace = 5 * " "
    barre = m * 3

    print(espace, end="")
    for cptCol in range(int(m)):
        if cptCol < 10:
            print("   ", end="")
        else:
            print(" " + str(int(cptCol / 10) % 10) + " ", end="")
    print()

    print(espace, end="")
    for cptCol in range(int(m)):
        if cptCol < 10:
            print(" " + str(cptCol) + " ", end="")
        else:
            print(" " + str(int(cptCol) % 10) + " ", end="")
    print()

    print(espace, end="")
    print("_" * int(barre))

    for l in board:
        if cptLine < 10:
            print(" " + str(cptLine) + " |" + " ", end="")
        elif cptLine < 100:
            print(str(cptLine) + " |" + " ", end="")
        cptLine += 1

        for e in l:
            # if str(e) == "x":
            #     print(Fore.GREEN + " " + str(e) + " ", end="")
            #     print(Style.RESET_ALL, end="")
            # elif str(e) == str(1):
            #     print(Fore.RED + " " + str(e) + " ", end="")
            #     print(Style.RESET_ALL, end="")
            # elif str(e) == str(2):
            #     print(Fore.BLUE + " " + str(e) + " ", end="")
            #     print(Style.RESET_ALL, end="")
            # elif str(e) == str(3):
            #     print(Fore.YELLOW + " " + str(e) + " ", end="")
            #     print(Style.RESET_ALL, end="")
            # elif str(e) == str(4):
            #     print(Fore.MAGENTA + " " + str(e) + " ", end="")
            #     print(Style.RESET_ALL, end="")
            # else:
            print(" " + str(e) + " ", end="")
        print("|", end="")
        print()

    print(espace, end="")
    print("_" * int(barre))


def get_size(board):
    """
    Petite fonction qui retourne les dimensions du plateau sous forme de tuple.
    """
    for i in board:
        return len(i), len(board)


def get_neighbors(board, pos_x, pos_y):
    """
    Prend en compte un plateau et deux nombres, qui ensemble forment les coordonnees d'un point dans le plateau.
    Permet de calculer tous les voisins possibles de cette position sur le plateau et les retourne sous forme
    de liste de coordonnees (tuples).
    """
    voisin = [
        (pos_x - 1, pos_y),
        (pos_x, pos_y - 1),
        (pos_x + 1, pos_y),
        (pos_x, pos_y + 1),
        (pos_x + 1, pos_y + 1),
        (pos_x + 1, pos_y - 1),
        (pos_x - 1, pos_y + 1),
        (pos_x - 1, pos_y - 1),
    ]

    voisinDeux = voisin.copy()
    for tup in voisinDeux:
        if tup[0] < 0 or tup[0] > (len(board) - 1) or tup[1] < 0 or tup[1] > (len(board[0]) - 1):
            voisin.remove(tup)
    return voisin


def place_mines(boardR, nombreMine, first_pos_x, first_pos_y):
    """
    Prend en compte le board de reference, le nombre de mines et les premieres positions choisies par le joueur
    pour ensuite creer et retourner une liste des coordonnees de celles-ci en respectant certaines conditions et
    en leur attribuant la valeur 'x'.
    """
    liste = []
    voisin_first = get_neighbors(boardR, first_pos_x, first_pos_y)

    while len(liste) < nombreMine:
        bombe_x = random.randint(0, len(boardR) - 1)
        bombe_y = random.randint(0, len(boardR[0]) - 1)
        bombe = (bombe_x, bombe_y)

        if bombe_x != first_pos_x or bombe_y != first_pos_y:
            if bombe not in voisin_first and bombe not in liste:
                liste.append(bombe)
                boardR[bombe[0]][bombe[1]] = "x"
    return liste


def fill_in_board(board):
    """
    Fonction qui ne retourne rien, mais permet de placer toutes les bombes ainsi que les valeurs du reste des cases
    sur le plateau de reference.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "x":
                listV = get_neighbors(board, i, j)
                for co in listV:
                    if board[co[0]][co[1]] != "x":
                        if board[co[0]][co[1]] == ".":
                            board[co[0]][co[1]] = 0
                        board[co[0]][co[1]] += 1
            elif board[i][j] == ".":
                board[i][j] = 0


def propagate(boardG, boardR, pos_x, pos_y):
    """
    Propagation recursive : decouvre les cases voisines quand la case vaut 0.
    Modifie boardG en place.
    """
    liste = []

    if boardR[pos_x][pos_y] == "x":
        boardG[pos_x][pos_y] = boardR[pos_x][pos_y]
    if boardR[pos_x][pos_y] != "x":
        boardG[pos_x][pos_y] = boardR[pos_x][pos_y]

    if boardR[pos_x][pos_y] == 0:
        boardG[pos_x][pos_y] = boardR[pos_x][pos_y]
        voisinR = get_neighbors(boardR, pos_x, pos_y)

        for v in voisinR:
            if boardG[v[0]][v[1]] == "." and boardR[v[0]][v[1]] != "x":
                boardG[v[0]][v[1]] = boardR[v[0]][v[1]]
                liste.append(v)

        print(liste)
        for l in liste:
            propagate(boardG, boardR, l[0], l[1])


def parse_input(line, colones):
    """
    Demande a l'utilisateur de rentrer les coordonnees des coups qu'il veut jouer.
    Renvoie (action, x, y) avec action dans {c,f,C,F}.
    """
    choix = input("votre choix : ")
    liste = choix.split()

    listeN = [str(i) for i in range(line)]
    listeM = [str(i) for i in range(colones)]
    listeC = ["c", "f", "C", "F"]

    while len(liste) != 3 or liste[0] not in listeC or liste[1] not in listeN or liste[2] not in listeM:
        print("erreur, veuillez entrer des donnees correctes")
        choix = input("votre choix : ")
        liste = choix.split()

    return liste[0], int(liste[1]), int(liste[2])


def init_game(line, colones, nbMines):
    """
    Lance le premier coup et initialise les plateaux.
    """
    boardR = create_board(line, colones)
    boardG = create_board(line, colones)

    print_board(boardG)
    first_pos = parse_input(line, colones)

    mineList = place_mines(boardR, nbMines, first_pos[1], first_pos[2])
    fill_in_board(boardR)
    propagate(boardG, boardR, first_pos[1], first_pos[2])

    print()
    print()
    print_board(boardR)
    print_board(boardG)

    return boardR, boardG, mineList


def check_win(boardG, boardR, mineList, totalFlag):
    """
    Verifie si les conditions de victoire sont respectees.
    """
    nbCases = 0
    nbMines = 0
    b = 0

    for i in range(len(boardG)):
        for j in range(len(boardG[0])):
            if boardG[i][j] == ".":
                nbCases += 1
            if boardR[i][j] == "x" and boardG[i][j] == ".":
                nbMines += 1
            if boardG[i][j] == "f":
                b += 1
                if boardR[i][j] == "x":
                    totalFlag -= 1

    if b > len(mineList):
        return False
    if (nbCases == nbMines) or (totalFlag == 0):
        return True
    return False


def check_lose(boardG, mineList, totalFlag, position):
    """
    Verifie si les conditions de defaite sont respectees.
    """
    for mine in mineList:
        if boardG[position[1]][position[2]] == "x":
            boardG[mine[0]][mine[1]] = "x"
            print("Vous avez touche une bombe !!!! Vous avez perdu !")
            return True
    return False


def main():
    """
    Fonction principale.
    """
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    number_of_mines = int(sys.argv[3])

    if (4 <= n < 100) and (3 < m < 100) and (0 <= number_of_mines <= (n * m) - 9):
        total_flag = number_of_mines
        reference_board, game_board, mine_list = init_game(n, m, number_of_mines)

        conditionV = check_win(game_board, reference_board, mine_list, total_flag)
        conditionD = False

        while conditionV is False and conditionD is False:
            pos = parse_input(n, m)

            if pos[0] == "c" or pos[0] == "C":
                propagate(game_board, reference_board, pos[1], pos[2])

            if pos[0] == "f" or pos[0] == "F":
                if game_board[pos[1]][pos[2]] != "f":
                    game_board[pos[1]][pos[2]] = "f"
                else:
                    game_board[pos[1]][pos[2]] = "."

            print_board(game_board)

            conditionV = check_win(game_board, reference_board, mine_list, total_flag)
            conditionD = check_lose(game_board, mine_list, total_flag, pos)

        if conditionD is True:
            for i in range(len(game_board)):
                for j in range(len(game_board[0])):
                    if reference_board[i][j] == "x":
                        game_board[i][j] = "x"
            print_board(game_board)
            print("merci d'avoir joue, Aurevoir")
            return 0

        if conditionV is True:
            print("Bravo")
            print_board(reference_board)
            print("vous avez gagne")
            return 1

    else:
        print(
            "recommencer en rentrant des valeurs comprises entre 4 et 99 pour n et m et dont la limite \n"
            + "de bombes pour n = "
            + str(n)
            + " et m = "
            + str(m)
            + " est de "
            + str(n * m - 9)
        )


if __name__ == "__main__":
    main()

