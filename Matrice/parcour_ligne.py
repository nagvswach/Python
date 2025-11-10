def check_rows(grid):
    chiffres = set(range(1, 10))
    for ligne in grid:
        if set(ligne) != chiffres:  # vérifie doublons et chiffres manquants
            return False
    return True
