


""" Fonction de vérification """

def check_lignes(grille):
    chiffres = set(range(1, 10))
    for ligne in grille:
        if set(ligne) != chiffres:
            return False
    return True


def check_colonnes(grille):
    chiffres = set(range(1, 10))
    for j in range(9):
        colonne = []
        for i in range(9):
            colonne.append(grille[i][j])
        if set(colonne) != chiffres:
            return False
    return True


def check_regions(grille):
    bon = True
    chiffres = set(range(1, 10))
    for i_bloc in range(0, 9, 3):    
        for j_bloc in range(0, 9, 3): 
            bloc = []
            for i in range(i_bloc, i_bloc + 3):
                for j in range(j_bloc, j_bloc + 3):
                    bloc.append(grille[i][j])
            if set(bloc) != chiffres:
                bon = False
                return bon
    return bon

def une_ligne(grille, i, x):
    ligne = []
    for j in range(9):
        if grille[i][j] != 0:
            ligne.append(grille[i][j])
    if x not in ligne:
        return True
    return False 

def une_colonne(grille, j, x):
    colonne = []
    for i in range(9):
        if grille[i][j] != 0:
            colonne.append(grille[i][j])
    if x not in colonne:
        return True
    return False

def un_bloc(grille, i,j, x):
    debut_ligne = (i//3)*3
    debut_col = (j//3)*3
    for li in range(debut_ligne, debut_ligne + 3):
        for co in range(debut_col, debut_col +3):
            if grille[li][co] == x:
                return False
    return True


def naked_single(grid):
    changement = True
    while changement:
        changement = False
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    solution = []
                    for num in range(1,10):
                        if une_ligne(grid, i, num) and une_colonne(grid, j, num) and un_bloc(grid, i, j, num):
                            solution.append(num)
                    if len(solution) == 1:
                        grid[i][j] = solution[0]
                        changement = True
    if check_lignes(grid) and check_colonnes(grid) and check_regions(grid):
        return True, grid
    else:
        return None



                        
                

print(naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
              [0, 0, 2, 8, 0, 1, 0, 0, 3],
              [0, 1, 0, 0, 0, 0, 0, 0, 7],
              [0, 4, 0, 7, 0, 0, 0, 2, 6],
              [5, 0, 7, 0, 1, 0, 4, 0, 9],
              [1, 2, 0, 0, 0, 3, 0, 8, 0],
              [2, 0, 0, 0, 0, 0, 0, 7, 0],
              [7, 0, 0, 2, 0, 9, 8, 0, 0],
              [0, 6, 0, 1, 5, 0, 3, 0, 2]]))
