
def acheter(liste_courses):
    course = {}
    prix_total = 0
    with open("produits.txt", mode ='r', encoding = 'utf-8') as f:
        for ligne in f:
            produit, quantite, prix = ligne.strip().split(",")
            produit = produit.strip()
            quantite = int(quantite.strip())
            prix = float(prix.strip())
            course[produit]= [quantite,prix]

    for nom, qte in liste_courses:
        course[nom][0] -= qte
        prix_total += qte * course[nom][1]

    with open("produits.txt", mode = "w", encoding = "utf-8")as f:
        for nom in course:
            f.write(f"{nom}, {course[nom][0]}, {course[nom][1]}\n")
    print(f"le prix total est de {prix_total} euros")




liste_courses = [("pomme", 5), ("poire", 2), ("pain", 1)]
acheter(liste_courses)

