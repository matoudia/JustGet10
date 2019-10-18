import bases
import possibles

def propagation(tableau, liste_tuple, tuple, n):   # fonction pour calculer toutes les cases adjacentes d'une cellule
    i = tuple[0]  #recupere le i du tuple
    j = tuple[1]  #recupere le j du tuple
    if possibles.existe_case_adj(tableau, i, j, n) :

        if i <= 0:                     # on donne des conditions pour exclure le test sur les cases qui depassent la grille ou debordent
            if j <= 0:

                if tableau[i + 1][j] == tableau[i][j] :  # si la valeur de la cellule(case) est egale a la cellule selectionnée (tuple)
                    if (i + 1, j) not in liste_tuple :   # si cette cellule n'est pas dans la liste liste_tuple (L plus tard)
                        liste_tuple.append((i + 1, j))   # on ajoute la cellule
                        propagation(tableau, liste_tuple, (i + 1, j), n) # et la on excute fonction propagation sur la cellule
                                                                         # qu'on vient de trouver (c'est la recusivité)
                if tableau[i][j + 1] == tableau[i][j] :   # meme principe que le bloc precedent et sur tous les autres cases
                    if (i, j + 1) not in liste_tuple :
                        liste_tuple.append((i, j + 1))
                        propagation(tableau, liste_tuple, (i, j + 1), n)

            elif j >= n - 1 :

                if tableau[i + 1][j] == tableau[i][j] :
                    if (i + 1, j) not in liste_tuple :
                        liste_tuple.append((i + 1, j))
                        propagation(tableau, liste_tuple, (i + 1, j), n)
                if tableau[i][j - 1] == tableau[i][j] :
                    if (i, j - 1) not in liste_tuple :
                        liste_tuple.append((i, j - 1))
                        propagation(tableau, liste_tuple, (i, j - 1), n)

            else:

                if tableau[i + 1][j] == tableau[i][j] :
                    if (i + 1, j) not in liste_tuple :
                        liste_tuple.append((i + 1, j))
                        propagation(tableau, liste_tuple, (i + 1, j), n)
                if tableau[i][j - 1] == tableau[i][j] :
                    if (i, j - 1) not in liste_tuple :
                        liste_tuple.append((i, j - 1))
                        propagation(tableau, liste_tuple, (i, j - 1) , n)
                if tableau[i][j + 1] == tableau[i][j] :
                    if (i, j + 1) not in liste_tuple :
                        liste_tuple.append((i, j + 1))
                        propagation(tableau, liste_tuple, (i, j + 1), n)

        elif i >= n - 1:
            if j <= 0:

                if tableau[i - 1][j] == tableau[i][j] :
                    if (i - 1, j) not in liste_tuple:
                        liste_tuple.append((i - 1, j))
                        propagation(tableau, liste_tuple, (i - 1, j), n)
                if tableau[i][j + 1] == tableau[i][j] :
                    if (i, j + 1) not in liste_tuple :
                        liste_tuple.append((i, j + 1))
                        propagation(tableau, liste_tuple, (i, j + 1), n)

            elif j >= n - 1 :

                if tableau[i - 1][j] == tableau[i][j] :
                    if (i - 1, j) not in liste_tuple :
                        liste_tuple.append((i - 1, j))
                        propagation(tableau,liste_tuple, (i - 1, j), n)
                if tableau[i][j - 1] == tableau[i][j] :
                    if (i, j - 1) not in liste_tuple :
                        liste_tuple.append((i, j - 1))
                        propagation(tableau,liste_tuple, (i, j - 1), n)

            else :
                if tableau[i - 1][j] == tableau[i][j] :
                    if (i - 1, j) not in liste_tuple :
                        liste_tuple.append((i - 1, j))
                        propagation(tableau, liste_tuple, (i - 1, j), n)
                if tableau[i][j - 1] == tableau[i][j] :
                    if (i, j - 1) not in liste_tuple :
                        liste_tuple.append((i, j - 1))
                        propagation(tableau, liste_tuple, (i, j - 1), n)
                if tableau[i][j + 1] == tableau[i][j] :
                    if (i, j + 1) not in liste_tuple :
                        liste_tuple.append((i, j + 1))
                        propagation(tableau, liste_tuple, (i, j + 1), n)

        else :
            if j <= 0:

                if tableau[i - 1][j] == tableau[i][j] :
                    if (i - 1, j) not in liste_tuple :
                        liste_tuple.append((i - 1, j))
                        propagation(tableau, liste_tuple, (i - 1, j), n)
                if tableau[i + 1][j] == tableau[i][j] :
                    if (i + 1, j) not in liste_tuple :
                        liste_tuple.append((i + 1, j))
                        propagation(tableau, liste_tuple, (i + 1, j), n)
                if tableau[i][j + 1] == tableau[i][j] :
                    if (i, j + 1) not in liste_tuple :
                        liste_tuple.append((i, j + 1))
                        propagation(tableau, liste_tuple, (i, j + 1), n)

            elif j >= n - 1:

                if tableau[i - 1][j] == tableau[i][j] :
                    if (i - 1, j) not in liste_tuple :
                        liste_tuple.append((i - 1, j))
                        propagation(tableau, liste_tuple, (i - 1, j), n)
                if tableau[i + 1][j] == tableau[i][j] :
                    if (i + 1, j) not in liste_tuple :
                        liste_tuple.append((i + 1, j))
                        propagation(tableau, liste_tuple, (i + 1, j), n)
                if tableau[i][j - 1] == tableau[i][j] :
                    if (i, j - 1) not in liste_tuple :
                        liste_tuple.append((i, j - 1))
                        propagation(tableau, liste_tuple, (i, j - 1), n)
            else:

                if tableau[i - 1][j] == tableau[i][j]:
                    if (i - 1, j) not in liste_tuple:
                        liste_tuple.append((i - 1, j))
                        propagation(tableau, liste_tuple, (i - 1, j), n)
                if tableau[i + 1][j] == tableau[i][j]:
                    if (i + 1, j) not in liste_tuple:
                        liste_tuple.append((i + 1, j))
                        propagation(tableau, liste_tuple, (i + 1, j), n)
                if tableau[i][j - 1] == tableau[i][j]:
                    if (i, j - 1) not in liste_tuple:
                        liste_tuple.append((i, j - 1))
                        propagation(tableau, liste_tuple, (i, j - 1), n)
                if tableau[i][j + 1] == tableau[i][j]:
                    if (i, j + 1) not in liste_tuple:
                        liste_tuple.append((i, j + 1))
                        propagation(tableau, liste_tuple, (i, j + 1), n)

def modification(tableau, liste_tuple, n) : # fonction incrementer et pour mettre un 0 sur toutes cases adjacentes qu'on a trouvé
    x = liste_tuple[0][0]                   # recupere l'abcisse du premier tuple de la liste liste_tuple qui va correspondre a la case selectionné
    y = liste_tuple[0][1]                   # recupere l'ordonnée du premier tuple de la liste liste_tuple qui va correspondre a la case selection
    tableau[x][y] += 1                      # incremente la case correspondante dans la grille qui est la case selectionnée
    for coordonnées in liste_tuple[ 1 : ] : # pour tous les autres elements de liste_tuple sauf le premier
        x = coordonnées[0]                  # recupere leur abscisse
        y = coordonnées[1]                  # recupere leur ordonnée
        tableau[x][y] = 0                   # met un 0 a la case correspondante dans la grille

def gravity(tableau, proba, n) :            # pour deplacer les cases vers le bas s'il ya des 0 et ajouter de nouvelles valeurs aleatoires
    for i in range(n) :
        for j in range(n) :
            if tableau[i][j] == 0 :
                for element in reversed(range(i)) : # on parcours les i d'une case dont la valeur = 0 dans le sens inverse
                    tableau[element+1][j] = tableau[element][j] #on affecte sa valeur a une case en bas pour le faire descendre
                tableau[0][j] = bases.valeur_aleatoire(proba) # du coup la derniere case en haut n'aura rien et on y met une valeur aleatoire


#n = 5
#proba = (0.05, 0.3, 0.6)  # (x1,x2,x3)
#gameBoard = bases.newBoard(proba, n)
#bases.display(gameBoard, n)
#print()
#current = (3,2)
#L = [current]
#propagation(gameBoard, L, current, n)
#print(L)
#print()
#modification(gameBoard, L, n)
#bases.display(gameBoard, n)
#print()
#gravity(gameBoard, proba, n)
#bases.display(gameBoard, n)
