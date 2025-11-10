def check_cols(grid):
    chiffres = set(range(1, 10))
    for j in range(9):
        colonne = []
        for i in range(9):
            colonne.append(grid[i][j])
        if set(colonne) != chiffres:
            return False

    return True
