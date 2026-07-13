import utils

def verifSaisie(chaine: str):
    if len(chaine) == 2:
        if "A" <= chaine[0] <= "Z":
            if utils.isANumber(chaine[1]):
                return True
    return False

def verificationFinDePartie(matchs):
    for _, match in matchs.items():
        if(match > 0):
            return False
    return True

def displayMatch(matchs, max = 9):
    for key, match in matchs.items():
        print(key + " "+ " " * (int((max - match)/2)) + "I"*match)
if __name__ == '__main__':
    number_match = {"A":1,"B":3,"C":5, "D":7,"E":9}
    while True:
        # Autour du premier joueur
        displayMatch(number_match)
        print("Autour de joueur 1")
        nb = 0
        while True:
            nb = utils.askCondition(verifSaisie, "Enter (exemple: B1): ")
            if(number_match[nb[0]]):
                if(int(nb[1]) <= number_match[nb[0]]):
                    number_match[nb[0]] -= int(nb[1])
                    break
                else:
                    print("Il ne reste plus assez de I")
            else:
                print(f"La ligne {nb[0]} est incorrect")
        if verificationFinDePartie(number_match):
            print("Joueur 1 a perdus")
            break

        # Autour du deuxieme joueur
        displayMatch(number_match)
        print("Autour de joueur 2")
        nb = 0
        while True:
            nb = utils.askCondition(verifSaisie, "Enter (exemple: B1): ")
            if(number_match[nb[0]]):
                if(int(nb[1]) <= number_match[nb[0]]):
                    number_match[nb[0]] -= int(nb[1])
                    break
                else:
                    print("Il ne reste plus assez de I")
            else:
                print(f"La ligne {nb[0]} est incorrect")
        if verificationFinDePartie(number_match):
            print("Joueur 2 a perdus")
            break

