import bases
import possibles
import merge
import pygame, os

#fond = pygame.image.load("background.jpg")                     # des codes qu'on a utilisé qui marchent juste a moitié
#pygame.draw.rect(fenetre,COLOR,(x,y,l,h),	epaisseur)
#case = pygame.Rect(x_case, y_case, taille_case, taille_case)
#pygame.draw.rect(fenetre, couleur, case)

longueur_fentre = 1000                  #la longueur de la fenetre du jeu
largeur_fentre = 500                    #la largeur de la fenetre du jeu
marge_gauche = longueur_fentre / 5      # une marge de gauche pour que ca colle pas a la fenetre
marge_haut = largeur_fentre / 5         # une marge de haut pour que ca colle pas a la fenetre
taille_case = 50

WHITE = (255,255,255)                   #quelques couleur qu'on va utiliser
BLUE = (0,0,255)
GREEN = (0,255,0)
GREEN2 = (32,178,170)
RED = (255,0,0)
BLACK = (0,0,0)
ORANGE = (255,127,80)
FUSCHIA = (255,0,255)
IVORY = (255,255,150)
SILVER = (192,192,192)
VIOLET = (238,130,238)
YELLOW = (255,255,0)
AQUA = (0,255,255)


#import pygame.locals.*
from pygame.locals import *   #vu dans le cours , c'est un module de pygame qui contient les fonctions qu'on a besoin
pygame.init()            #initialisation du pygame

def affiche_cellule(tableau, surface, i, j, n) :  #pour affichee une seule cellule ou case

    if tableau[i][j] == 1:            #calcule de couleur selon la valeur de la case
        couleur = GREEN
    elif tableau[i][j] == 2:
        couleur = BLUE
    elif tableau[i][j] == 3:
        couleur = ORANGE
    elif tableau[i][j] == 4:
        couleur = RED
    elif tableau[i][j] == 5:
        couleur = IVORY
    elif tableau[i][j] == 6:
        couleur = SILVER
    elif tableau[i][j] == 7:
        couleur = VIOLET
    elif tableau[i][j] == 8:
        couleur = AQUA
    elif tableau[i][j] == 9:
        couleur = GREEN2
    elif tableau[i][j] == 10:
        couleur = FUSCHIA
    else:
        couleur = YELLOW

    # a partir d'ici on joue sur des regles mathematiques pour calculer les positions des cases a afficher,
    # pour connaitre la case où on a cliqué ou bien si on a cliqué sur quit ou play again pour lui indiquer ce qu'il faut faire dans chaque cas

    fontObj = pygame.font.Font(None, 40)             #creer une police avec sa taille, ici on a pas specifié la police(None)
    valeur_case = fontObj.render(str(tableau[i][j]), True, BLACK, couleur) #cree le texte avce la police precedente, la couleur du texte(BLACK )et une couleur de fond
    x_case = marge_gauche + (j * taille_case)       #cree la l'abscisse de la case (le j sur les x_case pour ne pas avoir un affichage inversé)
    y_case = marge_haut + (i* taille_case)         #cree l'ordonnée de la case (le j sur les x_case pour ne pas avoir un affichage inversé)

    #caseprof = valeur_case.get_rect()    #pour transformer le texte en rectangle mais la taille n'est pas specifiée et ca ne nous arrange pas
                                          #on a besoin de la taille des cases pour pouvoir calculer plus tard les coordoonées de la case qu'on a cliqué

    case = pygame.Rect(x_case, y_case, taille_case, taille_case) #cree le rectangle ou on va l'afficher avec sa position(x_case et y_case) et sa taille
    surface.blit(valeur_case, case) #mets le texte dans le rectangle et colle le tout a la surface

def affiche_grille(tableau, surface, n):       # affiche toutes les cases
    for i in range(n):
        for j in range(n):
            affiche_cellule(tableau, surface, i, j, n)  #appelle de la fonction pour afficher une case


    fontObj = pygame.font.Font(None, 40)

    valeurScore1 = fontObj.render(" Current Score ", True, BLACK, WHITE)   #a chaque affichage de la grille, Current score est affichée
    caseScore1 = pygame.Rect(marge_gauche * 3, marge_haut, 200, 200)
    surface.blit(valeurScore1, caseScore1)


    valeurScore2 = fontObj.render(str(possibles.max_liste(tableau, n)), True, BLACK, WHITE)  #a chaque affichage de la grille, le max du tableau est affichée
    caseScore2 = pygame.Rect(marge_gauche * 3 + 75, marge_haut+ 50, 200, 200)
    surface.blit(valeurScore2, caseScore2)

    quitter = fontObj.render("Quit", True, BLACK, WHITE)   #a chaque affichage de la grille, le Quit est affichée
    caseQuit = pygame.Rect(marge_gauche * 3 + 50, marge_haut+ 200, 200, 200)
    fenetre.blit(quitter, caseQuit)

    pygame.display.flip()  # raffraichissement de la page




n = 5
proba = (0.05, 0.3, 0.6)  # (x1,x2,x3)
gameBoard = bases.newBoard(proba, n)  #nouveau tableau
bases.display(gameBoard, n)           #affichage simple sur la fentre de Pycharm
print()


fenetre = pygame.display.set_mode((longueur_fentre,largeur_fentre))    # cree une nouvelle surface appelée ici fenetre
pygame.display.set_caption('justGetTenGUI')                            # donne le nom de la surface
affiche_grille(gameBoard, fenetre, n)                                  # affiche la grille en mode graphique


inProgress = True     #on mets la condition d'arret de la boucle(inProgress) a True pour que la boucle demarre
while inProgress:     # si a condition d'arret de la boucle est a True
    for event in pygame.event.get():   # pour tous les evenements dans le tableau pygame.event.get()
        if event.type == QUIT:         # si l'evenement est un quit
            inProgress = False         # on mets le inProgress a False pour qu'il ne rentre plus dans la boucle

        elif not possibles.reste_coup(gameBoard, n) :   #s'il n'y a plus de coup possible
            jouer = fontObj.render("Play again", True, BLACK, WHITE)   #on affiche Play again pour demander de rejouer
            caseJouer = pygame.Rect(marge_gauche * 3 + 50, marge_haut + 150, 200, 200)
            fenetre.blit(jouer, caseJouer)

            pygame.display.flip() #raffraichissement de la page


        elif event.type == MOUSEBUTTONUP:  # si l'evenement est un clic
            x = event.pos[0]  # recupere le x de la position de la souris ( event.pos seulement renvoie un tuple qui contient le x et le y de la souris)
            y = event.pos[1]  # recupere le y de la position de la souris

            if not possibles.reste_coup(gameBoard, n) and x >= marge_gauche * 3 + 50 and x <= marge_gauche * 3 + 50 + 200 and y >= marge_haut + 150 and y <= marge_haut + 150 + 200 : # si il ya plus de coup possible et on clique sur le rectangle qui contient Play again
                gameBoard = bases.newBoard(proba, n)   #creer un nouveau tableau
                affiche_grille(gameBoard, fenetre, n)  #afficher le nouveau tableau
            if x >= marge_gauche * 3 + 50 and x <= marge_gauche * 3 + 50 + 200 and y >= marge_haut + 200 and y <= marge_haut + 200 + 200:  # si on clique sur le rectangle qui contient Quit
                inProgress = False  # on mets le inProgress a False pour qu'il ne rentre plus dans la boucle

            else :
                taillex = marge_gauche + (n * taille_case)  #calcule la longueur de la grille + sa marge gauche
                tailley = marge_haut + (n * taille_case)    #calcule la hauteur de la grille + sa marge haut
                if x >= 0 and x < taillex and y >= 0 and y < tailley :  #test pour connaitre si on a cliqué a l'interieur de la grille
                    i = int((y - marge_haut)/taille_case)            # on calcule a partir du y de la souris(qui est en pixel ) le i de la case selectionnée
                    j = int((x - marge_gauche) / taille_case)        # on calcule a partir du x de la souris(qui est en pixel ) le j de la case selectionnée
                                                                     #on calcule le i sur y et j sur x puisque a l'affichage de la grille on avait utilisé les i qur les y_case et les j sur les x_case pour ne pas se retrouver avec un tableau inversé
                    current = (i, j)                                 # c'est la case selectionée
                    L = [current]                                    # on l'ajoute a notre liste de tuple L
                    merge.propagation(gameBoard, L, current, n)      #on appelle la procedure propagation pour obtenir toutes les cases adjacentes
                    print(L)                                         #affichage simple de L
                    if possibles.existe_case_adj(gameBoard, i, j, n) : #si la case selectionée a une case adjacente de meme valeur
                        for tuple in L :                              #pour toutes les cases adjacente
                            fontObj = pygame.font.Font(None, 40)
                            valeur_case = fontObj.render(str(gameBoard[tuple[0]][tuple[1]]), True, BLACK, WHITE) #creer un nouveau rectangle avec la meme valeur et du fond blanc
                            x_case = marge_gauche + (tuple[1] * taille_case)  #ici aussi tuple[1] repesente le y du tuple donc c'est un j qu'on utilie avec le x_case
                            y_case = marge_haut + (tuple[0] * taille_case)    #ici aussi tuple[0] repesente le x du tuple donc c'est un i qu'on utilie avec le y_case
                            case = pygame.Rect(x_case, y_case, taille_case, taille_case)
                            fenetre.blit(valeur_case, case)                   #et on colle le nouveau texte avec du fond blanc au bon endroit
                    pygame.display.flip()                         #pour raffraichir l'ecran
                    pygame.event.wait()    #pause jusqu'a un autre evenement

                    if event.type == MOUSEBUTTONUP :
                        if possibles.existe_case_adj(gameBoard, i, j, n):
                            merge.modification(gameBoard, L, n)    #appelle procedure modification pour incrementer et mettre les 0
                            merge.gravity(gameBoard, proba, n)     #appelle procedure gravity
                            affiche_grille(gameBoard, fenetre, n)  #afficage la grille avec les nouvelles valeurs
                            bases.display(gameBoard, n)                   #affichage simple dans fenetre pycharm


    pygame.display.update()                        # mise a jour de l'ecran(la surface fenetre)

# sortie de la boucle
pygame.quit()   #quitter le programme


# to be continued by improving the design
#also 1 important thing, option play again should be added when score reach 10