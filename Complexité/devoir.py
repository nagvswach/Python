"""
devoir complexité 
Soussi Nagui
cours isolé 
matircule : 00545871
"""

def swap(blist, i, j):
    blist[i], blist[j] = blist[j], blist[i]

def permutation(liste, taille, result):
    if taille == 1:
        result.append(tuple(liste))
    else:
        for i in range(taille):
            swap(liste, i, taille-1)
            permutation(liste, taille-1,result)
            swap(liste, i, taille-1)

def permutations(ensemble):
    result = []
    permutation(ensemble, len(ensemble), result)
    return result


def longueur_itineraire(itineraire, distance):
    n = len(itineraire)
    total = 0
    for i in range(n):
        depart = itineraire[i]
        arrivee = itineraire[(i + 1) % n]     
        total += distance[depart][arrivee]
    return total



def voyageuse(distance):
    n = len(distance)
    villes = list(range(n))

    tous_les_itineraires = permutations(villes)

    meilleur_itineraire = None
    meilleure_distance = None

    for itineraire in tous_les_itineraires:
        d = longueur_itineraire(itineraire, distance)

        if meilleure_distance is None or d < meilleure_distance:
            meilleure_distance = d
            meilleur_itineraire = itineraire

    return meilleur_itineraire

#dist = [
#[0 , 6, 4, 4, 5] ,
#[6 , 0, 8, 4, 4] ,
#[4 , 8, 0, 6, 4] ,
#[4 , 4, 6, 0, 5] ,
#[5 , 4, 4, 5, 0]
#]

#print(voyageuse(dist))

"""
(Heureusement pour moi, j'avais déjà étudié la technique de permutation pour la récursivité 
dans mon cours d’algorithmique avant le devoir précédent, 
et j’avais aussi déjà vu le backtracking, bien que ça n'en soit pas vraiment dans ce cas
ça m'avait permit de voir déjà comment marchait l’algorithme du TSP auparavant.)

Dans mon résultat (voir énoncé), je trouve le chemin inverse, 
ce qui correspond exactement à la phrase : « unique, à une symétrie près ». 
Je suppose donc qu’il n’est pas nécessaire de rajouter une fonction qui remet l’itinéraire 
dans l’ordre “classique”, puisque le cycle optimal est bien correct dans les deux sens.

Le nombre de permutations est n factorielle, et ce n’est pas en O(c exposant n) pour une constante c,
car n! grandit plus vite que n’importe quelle exponentielle. 
Notre algorithme a donc une complexité en O(n!), ce qui le rend encore plus coûteux 
qu’un algorithme exponentiel classique. D’après ce que j’ai vu, 
on appelle cela une complexité super-exponentielle (factorielle).
"""

