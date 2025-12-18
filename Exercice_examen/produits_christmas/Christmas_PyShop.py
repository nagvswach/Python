
def import_stock(fichier):
    produits = []
    id_produit = 1
    with open(fichier, mode="r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne == "":
                continue
            produit, stock, prix = ligne.split(",")

            produit = produit.strip()
            stock = int(stock.strip())
            prix = float(prix.strip())

            produits.append([id_produit, produit, stock, prix])
            id_produit += 1
    return produits


def get_product_by_id(stock, id):
    for liste in stock:
        if liste[0] == id:
            return(liste[1],liste[2],liste[3])
    return None

def add_product(stock, produit):
    id_produit = len(stock) + 1
    prod, sto, prix = produit
    stock.append([id_produit,prod,sto, prix]) 
    return stock

def get_total_stock_value(stock):
    prix_total = 0
    for line in stock:
        prix_total += line[3] * line [2]
    return prix_total


produits = import_stock("produits.txt")
add_product(produits, ("Coca", 15, 1.5))
print(produits)
print(get_total_stock_value(produits))


            
            
