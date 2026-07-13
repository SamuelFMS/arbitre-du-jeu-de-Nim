
def askNumber(message = None, erroMessage = None):
    while True:
        number = input("Entrer un numero: " if message is None else message)
        if number.lstrip("-").isdigit():
            return int(number)
        else:
            print("Incorrect input" if erroMessage is None else erroMessage)

def askCondition(Condition, message = None, erroMessage = None):
    while True:
        saisi = input("Entrer: " if message is None else message)
        if(Condition(saisi)):
            return saisi
        else:
            print("Incorrect input" if erroMessage is None else erroMessage)

def isANumber(chaine):
    if chaine.lstrip("-").isdigit():
        return True
    return False

def convertToNumber(chaine):
    if chaine.lstrip("-").isdigit():
        return int(chaine)
    else:
        return False

if __name__ == '__main__':
    nb = askNumber()
    nb = askNumber("test: ", "nn")
    print(f"Lutilisateur a entrer le nombre {nb}")
    nb = askCondition(isANumber)