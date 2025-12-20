def ouvrir_onglet(url, onglets_ouverts, cache):
    nom = url.split("//")[1].split(".")[0]
    if url in onglets_ouverts:
        onglets_ouverts[url][1] += 1
    else:
        i = 0
        trouve = False
        while i < len(cache) and not trouve:
            if cache[i][0] == url:
                onglets_ouverts[url] = [nom, cache[i][1][1]+1]
                trouve = True
                del cache[i]
            i += 1
        if url not in onglets_ouverts:
            onglets_ouverts[url] = [nom, 1]


def fermer_onglet(url, onglets_ouverts,cache):
    if url in onglets_ouverts:
        nom = url.split("//")[1].split(".")[0]
        cache.append((url,[nom, onglets_ouverts[url][1]]))
        del onglets_ouverts[url]                      
        if len(cache) > 5:
            del cache[0]


def trouver_max_requetes(onglets_ouverts):
    liste_max = []
    if len(onglets_ouverts) > 0:
        maxi = 0
        for url, liste in onglets_ouverts.items():
            if liste[1] > maxi:
                maxi = liste[1]
                liste_max = [(url,liste)]
            elif liste[1] == maxi:
                liste_max.append((url,liste))
        return liste_max


onglets_ouverts = {"https://ulb.be/science" : ["ulb", 1],
                   "http://twish.tv/content":["twish", 2],
                   "http://desacord.com/content":["desacord",2]
                }

cache = []

ouvrir_onglet("https://ulb.be/science", onglets_ouverts, cache)
ouvrir_onglet("https://ulb.be/science", onglets_ouverts, cache)
ouvrir_onglet("http://twish.tv/content", onglets_ouverts, cache)
ouvrir_onglet("http://twish.tv/content", onglets_ouverts, cache)
fermer_onglet("https://ulb.be/science", onglets_ouverts, cache)
ouvrir_onglet("https://ulb.be/science", onglets_ouverts, cache)
fermer_onglet("http://desacord.com/content",onglets_ouverts, cache)

print(cache)
print(onglets_ouverts)
print(trouver_max_requetes(onglets_ouverts))
