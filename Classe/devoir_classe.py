
class KeyPass:

    def __init__(self, codePin: list[int]):
        self.key = codePin
        self.keyPass = {}

    def add_password(self, app: str, mdp_en_clair: str):
        mdp_chiffre = self.encrypt(mdp_en_clair)
        self.keyPass[app] = mdp_chiffre

    def get_password(self, app:str):
        if app in self.keyPass:
            mdp = self.keyPass[app]
            return self.decrypte(mdp)
        return None

    def remove_password(self, app: str):
        if app in self.keyPass:
            del self.keyPass[app]

    def encrypt(self, mdp_en_clair: str) -> str:
        mdp_chiffre = ''
        for i, c in enumerate(mdp_en_clair):
            decalage = self.key[i % len(self.key)]
            lettre_code = ord(c)
            lettre_chiffre = (lettre_code + decalage) % 256
            mdp_chiffre += chr(lettre_chiffre)
        return mdp_chiffre
    
    def decrypte(self, mdp_encrypt: str) -> str:
        mdp_en_clair = ''
        for i, c in enumerate(mdp_encrypt):
            decalage = self.key[i % len(self.key)]
            lettre_code = ord(c)
            lettre_dechiffre = (lettre_code - decalage) % 256
            mdp_en_clair += chr(lettre_dechiffre)
        return mdp_en_clair

    def get_vulnerable_passwords(self, mot_de_passe: str) -> list[str]:
        liste = []
        mdp_chiffre = self.encrypt(mot_de_passe)
        for cle in self.keyPass:
            if self.keyPass[cle] == mdp_chiffre:
                liste.append(cle)
        return liste

    def export_file(self, nom_fichier: str): 
        with open(nom_fichier,"w",encoding = "utf-8" ) as f:
            for cle in self.keyPass:
                mdp_chiffre = self.keyPass[cle]
                ligne = f"{cle} : {mdp_chiffre} \n"
                f.write(ligne)








"""

retour pour le prof : 
    -la diffculté pour certaines méthode était de comprendre les tours de boucle for
     avec le modulo pour des mots de passe plus long que le code pin.

    -Utiliser la même logique que pour les for et ne pas être limité par les bornes 0 et 256 qui correspond aux nombre
     totaux des charactères, en continuant a bouclé grace a la division entière.
    
    -Après quelques recherche de savoir que l'on pouvait tranformé un caractère en code ascii avec la fonction ordinal
     pour ensuitele décaler et le retranformé en charactère.

"""

