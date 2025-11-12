def file_histogram(fileName):
    dict = {}
    with open(fileName, mode = "r", encoding = "utf 8")as f:
        for line in f:
            for char in line:
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
    return dict

def words_by_length(fileName):
    accents = "àâçéèêëïîôùûüÿœæñ"
    d = {}
    with open(fileName, mode = "r", encoding = "utf 8")as f:
        mot =''
        dico = {}
        for line in f:
            for char in line:
                if char.isalpha() or char in "àâçéèêëîïôûùüÿñæœ":
                    mot += char.lower() 
                else:
                    if mot:
                        longueur = len(mot)
                        if longueur not in d:
                            d[longueur] = []
                        if mot not in d[longueur]:
                            d[longueur].append(mot)
                        mot =''
            if mot:
                longueur = len(mot)
                if longueur not in d:
                    d[longueur] = []
                if mot not in d[longueur]:
                    d[longueur].append(mot)
                mot = ''
    for longueur in d:
        d[longueur].sort()
    return d

                  
                    
    



print(words_by_length('Zola.txt'))
