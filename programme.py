if __name__ == '__main__':
    number_match = 21
    while True:
        # Autour du premier joueur
        print("Autour de joueur 1")
        nb = 0
        while nb > 4 or nb <= 0 :
            nb = int(input("Entrez un nombre entre 1 et 4 : "))
        number_match -= nb
        if number_match <= 0:
            print("Joueur 1 Vous avez perdus")
            break
        print(f"Il reste {number_match}")
        print()

        # Autour du deuxieme robot
        print("Autour du robot")
        nb = 5-nb
        print(f"Le robot a choisis: {nb}")
        number_match -= nb
        if number_match <= 0:
            print("Robot perdus")
            break
        print(f"Il reste {number_match}")
        print()

