def dupliquer_fichier(fichiers, dossier_destination, chemin_fichier_source):
    nom_fichier = chemin_fichier_source.split("/")[-1]
    dest = dossier_destination + "/" + nom_fichier
    try:
        with open(chemin_fichier_source,"r", encoding="utf-8") as source:
            contenu = source.read()
        
        with open(dest, "w", encoding ="utf-8") as copie:
            copie.write(contenu)

    except:
        return False

    i = 0
    while i < len(fichiers) and nom_fichier > fichiers[i]:
        i += 1
    fichiers.insert(i, nom_fichier)

    return True
