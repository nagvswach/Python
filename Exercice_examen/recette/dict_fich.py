def quantite_par_ingrediant(emplacement_recette):
    dico = {}
    for fichier in emplacement_recette: 
        with open(fichier, mode = "r",encoding="utf-8")as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne == "":
                    continue
                quantite, unite, ingrediant = ligne.split(",")
                quantite = float(quantite.strip())
                unite = unite.strip()
                ingrediant =  ingrediant.strip()
                unite_cible = UNITES_PREDILECTION[ingrediant]
                facteur = CONVERSIONS[unite][unite_cible]
                quantite = quantite * facteur
                if ingrediant not in dico:
                    dico[ingrediant] = quantite
                else:
                    dico[ingrediant] += quantite
    return dico


UNITES_PREDILECTION = {
    "farine": "kg",
    "oeuf": "unité",
    "lait": "ml",
    "passata de tomates": "ml",
    "sel": "g",
    "mozzarella": "g"
}

CONVERSIONS = {
    # masses
    "kg": {
        "kg": 1,
        "g": 1000
    },
    "g": {
        "g": 1,
        "kg": 1 / 1000
    },

    # volumes
    "l": {
        "ml": 1000,
        "l": 1
    },
    "ml": {
        "ml": 1,
        "l": 1 / 1000
    },

    # autres
    "unité": {
        "unité": 1
    },
    "pincée": {
        "g": 5
    }
}
    

courses = quantite_par_ingrediant(["recette_un.txt", "recette_deux.txt"])
print(courses)
