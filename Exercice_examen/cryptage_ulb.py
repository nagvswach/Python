class KeyPass:
    def __init__(self, codePin):
        self.code = codePin
        self.KeyPass = {}

    def encrypt(self, mdp_en_clair):
        mdp_crypt = ''
        for i in range(len(mdp_en_clair)):
            char = chr((ord(mdp_encrypt[i]) + self.code[i % len(self.code)]) % 256)
            mdp_crypt += char
        return mdp_crypt
    
    def decrypt(self, mdp_encrypt):
        mdp_en_clair = ''
        for i in range(len(mdp_encrypt)):
            char = chr((ord(mdp_encrypt[i]) - self.code[i % len(self.code)]) % 256)
            mdp_en_clair += char
        return mdp_en_clair

    def add_password(self, app, mdp_en_clair):
        mdp_crypt = self.encrypt(mdp_en_clair)
        self.KeyPass[app] = mdp_crypt

    def remove_password(self, app):
        if app in KeyPass:
            del self.KeyPass[app]

    def get_passeword(self, app):
        return self.KeyPass[app]
    
    def get_vulnerable_passwords(self, mot_de_passe):
        mdp = self.encrypt(mot_de_passe)
        mdp_vul = []
        for app, mdp_crypt in self.KeyPass.items():
            if mdp_crypt == mdp:
                mdp_vul.append(app)
        return mdp_vul

    def export_file(self, nom_de_fichier):
            with open(nom_de_fichier, "w", encoding="utf-8") as f:
                for app, mdp in self.KeyPass.items():
                    f.write(f"{app}:{mdp}\n")




            
