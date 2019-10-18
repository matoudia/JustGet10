import random  #importer la librairie random

def valeur_aleatoire(proba) :                                      #une fonction parce qu'il retourne quelque chose
    nb = random.random()
    if 0 < proba[0] and proba[0] < proba[1] and proba[1] < proba[2] and proba[2] < 1 :
        if nb < proba[0] :
            return 4
        elif proba[0] < nb and nb < proba[1] :
            return 3
        elif proba[1] < nb and nb < proba[2] :
            return 2
        else :
            return 1
    else :
        return "reverifiez vos données"


def newBoard(proba, n) :                                      #une procedure parce qu'il ne retourne rien et affiche seulement ou cree quelque chose
    lignes = []          # creer une variable tableau nommée lignes
    for i in range(n) :  #range(n) tableau de n entiers de 0 a n-1
        colonnes = []    # creer une variable tableau nommée colonnes
        for j in range (n) :
            colonnes.append(valeur_aleatoire(proba))
        lignes.append(colonnes)
    return lignes


def display(game, n):
    for i in range(n):
        tableau = ""  # initialiser tableau qui s'ecrase a chaque nouveau i
        for j in range(n):
            tableau = tableau + str(game[i][
                                        j]) + " "  # faire la somme des des elements de la tableau game[i] avec des espaces entre eux , str() permet de transformer un nombre en caractere
        print("*    ", tableau, "     *")  # les etoiles et espaces c'est juste pour mettre une marge c'est facultatif
