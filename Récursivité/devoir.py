
"""
Soussi Nagui, cours isolé, INFO-F101
ULB
Matricule : 00545871
Devoir: Arbre récursif 

"""



import turtle
import random


"""
étape 1 : j'ai choisi mon cas de base, celui qui arrête la récursivité.

étape 2 : dessiner la branche principale, avant le if, parce que même s'il n'y a 
          pas de sous arbre il reste la branche seule.

étape 3 : on détermine le nombre de sous-arbres aléatoirement.

étape 4 : l'écart entre les angles va dépendre du nombre de sous-arbres et de 
          l'intervalle. On va simplement diviser l’intervalle par le nombre de 
          sous arbres pour déterminer l’angle entre chaque branche.

étape 5 : on rentre dans le for. Pour chaque sous-arbre, on va replacer la tortue 
          à sa position initiale avant quoi que ce soit, et récursivement dessiner 
          les sous arbres de i = 0 jusqu'à ce que la sous branche de cette branche 
          soit trop fine. Ensuite on passera à i = 1 (sous branche 2) en répétant 
          la récursivité pour chaque i.
"""


def dessiner_arbre (longueur : float ,
                    angle_min : float , angle_max : float ,
                    nombre_sous_arbres_min : int , nombre_sous_arbres_max : int ,
                    facteur_min : float , facteur_max : float ,
                    longueur_min : float ):
    turtle.forward(longueur)
    if longueur <= longueur_min:
        return
    pos_depart = turtle.position()
    angle_depart = turtle.heading()
    nb_sous_arbres = random.randint(nombre_sous_arbres_min, nombre_sous_arbres_max)
    ecart_angle = (angle_max - angle_min) / (nb_sous_arbres - 1)
    for i in range(nb_sous_arbres):
        turtle.penup()
        turtle.goto(pos_depart)
        turtle.setheading(angle_depart)
        turtle.pendown()
        angle = angle_min + i * ecart_angle
        turtle.left(angle)
        facteur = random.uniform(facteur_min, facteur_max)
        longueur_branche = longueur * facteur
        dessiner_arbre(longueur_branche,
                       angle_min, angle_max,
                       nombre_sous_arbres_min, nombre_sous_arbres_max,
                       facteur_min, facteur_max,
                       longueur_min)


# Config affichage et vitesse
turtle.speed(0)        
turtle.tracer(False)
turtle.left(90)

# Tests de l'énoncé

# (a) Test 1
#dessiner_arbre(120, -50, 50, 2, 5, .3, .7, 5)

# (b) Test 2
dessiner_arbre(120, -10, 10, 2, 2, .4, .99, 5)

# (c) Test 3
#dessiner_arbre(80, -20, 60, 2, 4, .5, .7, 5)

turtle.update()
turtle.done()

