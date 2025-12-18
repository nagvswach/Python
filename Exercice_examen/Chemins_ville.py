EXCLUDED_POINTS = [(1,1), (3,3), (1,0)]



def chemins(m,n,prefixe = []):
    chemin = []
    if m < 0 or n < 0:
        return []
    if (m,n) in EXCLUDED_POINTS:
        return []
    prefixe = prefixe + [(m,n)]
    if m == 0 and n == 0:
        return[prefixe]
    return chemins(m-1,n,prefixe) + chemins(m,n-1,prefixe)

print(chemins(4,4))


