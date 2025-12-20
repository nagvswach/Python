import random

def KeyPass(mdp):
    code = ''
    indice = []
    for c in mdp:
        char = ord(c)
        decalage, direction = random.randint(0,1000), random.randint(0,1)
        if direction == 0:
            char -= decalage % 256
        else:
            char += decalage % 256
        char = char % 256
        code += chr(char)
        indice.append((decalage, direction))
    return code,indice



mot = "NagIsm2213"

print(KeyPass(mot))
        

