N_LEVEL = 10
list_result = (N_LEVEL + 1) * [0]


def galton(level, position, nb_billes, list_result):
    if level == N_LEVEL:
        indice = position - (N_LEVEL * (N_LEVEL + 1)) // 2
        list_result[indice] += nb_billes
        return
    galton(level + 1, position + level + 1, nb_billes // 2, list_result)
    galton(level + 1, position + level + 2, nb_billes // 2 + nb_billes % 2, list_result)




galton(0, 0, 4096, list_result)
print(list_result)
