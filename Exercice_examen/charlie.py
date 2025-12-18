def ou_est_charlie(dossier,chemin = None):
    res = []
    for nom, contenu in dossier.items():
        if chemin != None:
            new_chemin = chemin + '/'+ nom
        else:
            new_chemin = nom

        
        if isinstance(contenu, dict):
            res.extend(ou_est_charlie(contenu, new_chemin))
        else:
            if contient_charlie(new_chemin):
                res.append(new_chemin)
    return res


def contient_charlie(chemin_fichier):
    with open(chemin_fichier, mode ='r', encoding = 'utf-8')as f:
        return "Charlie" in f.read()


filesystem = {
"root": {
"home": {
"Documents": {
"email.txt": 1515,
"projet_chateau.txt": 1024,
"Reponse.txt": 33
},
"Report": {
"report1.txt": 2345,
"report2.txt": 2936,
"report3.txt": 2434,
"report4.txt": 1929
}
},
"apps": {
"Teams": 34332,
"FireFox": 234432
}
}
}

print(ou_est_charlie(filesystem))
