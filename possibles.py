def existe_case_adj(tableau, i, j, n):  # parametres n , une tableau a deux dimensions, i et j
    if i <= 0:                          # on donne des conditions pour exclure le test sur les cases qui depassent la grille ou deborden
        if j <= 0:
            return tableau[i + 1][j] == tableau[i][j] or tableau[i][j + 1] == tableau[i][j]
        elif j >= n - 1:
            return tableau[i + 1][j] == tableau[i][j] or tableau[i][j - 1] == tableau[i][j]
        else:
            return tableau[i + 1][j] == tableau[i][j] or tableau[i][j - 1] == tableau[i][j] or tableau[i][j + 1] == tableau[i][j]
    elif i >= n - 1:
        if j <= 0:
            return tableau[i - 1][j] == tableau[i][j] or tableau[i][j + 1] == tableau[i][j]
        elif j >= n - 1:
            return tableau[i - 1][j] == tableau[i][j] or tableau[i][j - 1] == tableau[i][j]
        else:
            return tableau[i - 1][j] == tableau[i][j] or tableau[i][j - 1] == tableau[i][j] or tableau[i][j + 1] == tableau[i][j]
    else:
        if j <= 0:
            return tableau[i - 1][j] == tableau[i][j] or tableau[i + 1][j] == tableau[i][j] or tableau[i][j + 1] == tableau[i][j]
        elif j >= n - 1:
            return tableau[i - 1][j] == tableau[i][j] or tableau[i + 1][j] == tableau[i][j] or tableau[i][j - 1] == tableau[i][j]
        else:
            return tableau[i - 1][j] == tableau[i][j] or tableau[i + 1][j] == tableau[i][j] or tableau[i][j - 1] == tableau[i][j] or \
               tableau[i][j + 1] == tableau[i][j]


        # il faut tester les cases i-1,j   i+1,j   i,j-1  i,j+1 et eviter les cases qui ont comme indice n ou plus de n et 0 ou moins de 0


# n-1 parce que la taille de la tableau est de n ligne et n colonne donc les indices varient de 0 a n-1
# les conditions renvoient True ou False (avec premiere lettre majuscule) donc la fonction sera de type booleen


def reste_coup(tableau, n):
    resultat = False  # on debut on a rien trouvé on sait pas si une case a une meme valeur adjacente
    for i in range(n):
        for j in range(n):
            if existe_case_adj(tableau, i, j, n):  # si la case a une case adjacente de la meme valeur
                resultat = True  # le resultat change et devient vrai
    return resultat  # a la sortie de la boucle soit on a trouvé et resultat devient vrai soit on a rien trouvé et le resultat reste faux


def max_liste(tableau, n):
    maximum = 0  # on debute par la valeur minimale 0 sachant que la tableau contient que des valeurs positives
    for i in range(n):
        for j in range(n):
            if tableau[i][j] > maximum:  # si la case est superieur a maximum
                maximum = tableau[i][j]  # maximum prends sa valeur
    return maximum  # a la sortie de la boucle on recupere la valeur maximale

