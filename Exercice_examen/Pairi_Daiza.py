animaux = {}

def add_animaux(animaux, classe, famille, espece, nombre):
    if classe not in animaux:
        animaux[classe] = {}
    if famille not in animaux[classe]:
        animaux[classe][famille] = {}
    if espece not in animaux[classe][famille]:
        animaux[classe][famille][espece] = nombre
    else:
        animaux[classe][famille][espece] += nombre

def len_famille(animaux, classe, famille):
    total = 0
    if classe in animaux and famille in animaux[classe]:
        for espece in animaux[classe][famille]:
            total += animaux[classe][famille][espece]
    return total

def len_classe(animaux, classe):
    total = 0
    if classe in animaux:
        for famille in animaux[classe]:
            for espece in animaux[classe][famille]:
                total += animaux[classe][famille][espece]
    return total
            
def len_animaux(animaux):
    total = 0
    for classe in animaux:
        total += len_classe(animaux, classe)
    return total



add_animaux(animaux, "MAMMIFERES","Elephantides", "Elephant", 3)
add_animaux(animaux, "MAMMIFERES","Felides", "Tigre", 3)
add_animaux(animaux, "MAMMIFERES","Elephantides", "Elephant", 2)
add_animaux(animaux, "MAMMIFERES","Felides", "Lion", 6)
add_animaux(animaux, "OISEAUX", "Sphenisciformes", "Manchot du Cap", 25)
print("dictionnaire animaux :", animaux)
print("Nombre d'animaux", len_animaux(animaux))
print("Nombre de mammiferes :", len_classe(animaux, "MAMMIFERES"))
print("Nombre d'elephantides :", len_famille(animaux, "MAMMIFERES","Elephantides"))
print("Nombre de Felides :", len_famille(animaux, "MAMMIFERES","Felides"))
