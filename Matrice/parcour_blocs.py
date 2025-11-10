def check_sudoku(liste1):
    bon = True
    chiffres = list(range(1, 10))
    for i_bloc in range(0, 9, 3):    
        for j_bloc in range(0, 9, 3): 
            bloc = []
            for i in range(i_bloc, i_bloc + 3):
                for j in range(j_bloc, j_bloc + 3):
                    bloc.append(liste1[i][j])
            for elem in bloc:
                if elem not in chiffres:
                    bon = False
                    return bon

    return bon

