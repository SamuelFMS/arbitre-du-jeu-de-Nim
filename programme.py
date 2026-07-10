if __name__ == '__main__':
    number_match = 21
    while True:
        # Autour du premier joueur
        print(f"Il reste {number_match}")
        print("Autour de joueur 1")
        nb = 0
        while nb > 4 or nb <= 0 :
            nb = int(input("Entrez un nombre entre 1 et 4 : "))
        number_match -= nb
        if number_match < 0:
            print("Joueur 1 Vous avez perdus")
            break
        elif number_match == 0:
            print("Joueur 2 Vous avez perdus")
            break

        # Autour du deuxieme joueur
        print(f"Il reste {number_match}")
        print("Autour de joueur 2")
        nb = 0
        while nb > 4 or nb <= 0:
            nb = int(input("Entrez un nombre entre 1 et 4 : "))
        number_match -= nb
        if number_match < 0:
            print("Joueur 2 Vous avez perdus")
            break
        elif number_match == 0:
            print("Joueur 1 Vous avez perdus")
            break

