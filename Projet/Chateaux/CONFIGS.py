# CONFIGS.py
# ------------------------------------------------------------
# Config "valable" pour ton projet Turtle (plateau + inventaire + annonces)
# Ajuste uniquement les noms de fichiers si tes extensions sont differentes.
# ------------------------------------------------------------

# ========== FICHIERS ==========
# Mets ici les vrais noms EXACTS (avec extension si tu en as une)
fichier_plan = "plan_chateau.txt"      # ou "plan_chateau"
fichier_objets = "dico_objets.txt"     # ou "dico_objets"
fichier_questions = "dico_portes.txt"  # ou "dico_portes"


# ========== ZONE DE DESSIN DU PLATEAU ==========
# Le plateau sera dessine dans ce rectangle (en "monde turtle")
# Si ton plateau est grand, augmente un peu ces valeurs.
ZONE_PLAN_MINI = (-320, -280)
ZONE_PLAN_MAXI = (320, 280)


# ========== COULEURS ==========
COULEUR_CASES = "white"       # sol
COULEUR_MUR = "black"         # murs
COULEUR_OBJECTIF = "green"    # sortie / objectif
COULEUR_OBJET = "yellow"      # objets (cases a ramasser)
COULEUR_PORTE = "brown"       # portes / questions

COULEUR_VUE = "lightgrey"     # cases deja visitees
COULEUR_PERSONNAGE = "red"    # pion joueur


# ========== PERSONNAGE ==========
# Taille du point joueur par rapport a la taille d'une case
RATIO_PERSONNAGE = 0.50

# Position de depart (ligne, colonne) dans la matrice
# IMPORTANT: adapte si ton plan n'a pas un depart a (1,1)
POSITION_DEPART = (1, 1)


# ========== UI (INVENTAIRE / ANNONCES) ==========
# Ces points sont choisis pour etre VISIBLES avec la zone de dessin ci-dessus.
# Si tu changes ZONE_PLAN_MINI/MAXI, tu peux ajuster ici.

# Coin haut-gauche du cadre inventaire (ton code dessine ensuite le rectangle)
POINT_AFFICHAGE_INVENTAIRE = (360, 220)

# Coin bas-gauche du cadre annonces
POINT_AFFICHAGE_ANNONCES = (-320, -330)

