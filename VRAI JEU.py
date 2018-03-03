import pygame, sys
from pygame.locals import *
from pygame import *

# Initialisation de la bibliothèque Pygame
pygame.init()
wait = 0
# Ouverture  de la fenêtre Pygame
larg_fenetre = 1419
haut_fenetre = 731

fenetre = pygame.display.set_mode((larg_fenetre, haut_fenetre))

# Chargement et collage du fond
fond = pygame.image.load("bataille1.png").convert()
fenetre.blit(fond, (0, 50))

# Chargement et collage du personnage
perso = pygame.image.load("blue.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, (0, 0))
blue = (100, 180, 255)
white = (255, 255, 255)
c = [182, 246, 311, 376, 440, 505, 569, 634, 698, 761]
l = [79, 143, 207, 272, 336, 400, 464, 528, 592, 656]
c1 = []
l1 = []
nombre_cases = 0
liste = []
liste_cases = []

rouge = (255, 0, 0)
rouge2 = (250, 200, 200)
vert = (0, 255, 0)
vert2 = (200, 250, 200)
jaune = (255, 255, 0)
jaune2 = (250, 250, 200)
cyan = (0, 255, 255)
cyan2 = (200, 250, 250)
violet = (255, 0, 255)
violet2 = (250, 200, 250)

pygame.draw.rect(fond, rouge, (845, 159, 62, 62))
pygame.draw.rect(fond, vert, (845, 262, 62, 62))
pygame.draw.rect(fond, jaune, (845, 369, 62, 62))
pygame.draw.rect(fond, cyan, (845, 480, 62, 62))
pygame.draw.rect(fond, violet, (845, 589, 62, 62))

chiffre = 0
nombre = 0
decision = ''

# Rafraîchissement de l'écran
pygame.display.flip()

couleur = 0
couleur2 = 0


def clic1(couleur, chiffre, couleur2):
    nombre = 0
    (x, y) = event.pos
    print(x, y)

    a = int((x - 181) / 64)
    b = int((y - 78) / 64)
    pygame.draw.rect(fond, couleur, (c[a], l[b], 62, 62))

    if a < 10 - chiffre:
        pygame.draw.rect(fond, (couleur2), (c[a + chiffre], l[b], 62, 62))
    if a >= chiffre:
        pygame.draw.rect(fond, (couleur2), (c[a - chiffre], l[b], 62, 62))
    if b < 10 - chiffre:
        pygame.draw.rect(fond, (couleur2), (c[a], l[b + chiffre], 62, 62))
    if b >= chiffre:
        pygame.draw.rect(fond, (couleur2), (c[a], l[b - chiffre], 62, 62))

    nombre = 1
    return nombre, a, b


def clic2(a, b, chiffre, couleur):
    (x, y) = event.pos
    a1 = int((x - 181) / 64)
    b1 = int((y - 78) / 64)
    if (a1 == a + chiffre and b1 == b):
        for i in range(1, chiffre + 1):
            pygame.draw.rect(fond, (couleur), (c[a + i], l[b], 62, 62))
        if a > chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a - chiffre], l[b], 62, 62))
        if b > chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a], l[b + chiffre], 62, 62))
        if b < 10 - chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a], l[b - chiffre], 62, 62))
    if (a1 == a - chiffre and b1 == b):
        for i in range(1, chiffre + 1):
            pygame.draw.rect(fond, (couleur), (c[a - i], l[b], 62, 62))
        if a < 10 - chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a + chiffre], l[b], 62, 62))
        if b > chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a], l[b + chiffre], 62, 62))
        if b < 10 - chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a], l[b - chiffre], 62, 62))
    if (a1 == a and b1 == b + chiffre):
        for i in range(1, chiffre + 1):
            pygame.draw.rect(fond, (couleur), (c[a], l[b + i], 62, 62))
        if a > chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a - chiffre], l[b], 62, 62))
        if a < 10 - chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a + chiffre], l[b], 62, 62))
        if b < 10 - chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a], l[b - chiffre], 62, 62))
    if (a1 == a and b1 == b - chiffre):
        for i in range(1, chiffre + 1):
            pygame.draw.rect(fond, (couleur), (c[a], l[b - i], 62, 62))
        if a > chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a - chiffre], l[b], 62, 62))
        if b > chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a], l[b + chiffre], 62, 62))
        if a < 10 - chiffre:
            pygame.draw.rect(fond, (255, 255, 255), (c[a + chiffre], l[b], 62, 62))
    nombre = 0
    return nombre


##        c1.append(a)
##
##        l1.append(b)
##        
##        print(nombre_cases, c[a],l[b], liste)
##        
##        if [c[a],l[b]] in liste:
##                    pygame.draw.rect(fond,white,(c[a],l[b],62,62))
##                    del l1[-1]
##                    del c1[-1]
##                    del liste[-1]
##                    del liste[-1]
##                    nombre_cases=nombre_cases-1
##                    enlever = [[c[a],l[b]]]
##                    liste[:] = (w for w in liste if w not in enlever)
##                    print('miau', liste)
##                    blanc=1
##    
##
##        liste.append([c[a], l[b]])
##        if nombre_cases==0:
##
##            pygame.draw.rect(fond,blue,(c[a],l[b],62,62))


# BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:  # Si on clique sur le bouton quitter
            continuer = 0  # la boucle s'arrête
        if event.type == KEYDOWN:  # Si on appuye sur une touche du clavier
            if event.key == K_ESCAPE:  # Si cette touche est la touche echap
                continuer = 0  # On arrête la boucle
            elif event.key == K_DOWN:
                position_perso = position_perso.move(0, 50)


            elif event.key == K_UP:
                position_perso = position_perso.move(0, -50)


            elif event.key == K_LEFT:
                position_perso = position_perso.move(-50, 0)

            elif event.key == K_RIGHT:
                position_perso = position_perso.move(50, 0)

    if event.type == MOUSEBUTTONDOWN and wait == 0:
        (x, y) = event.pos
        print(x, y)
        if x >= 845 and x <= 907:
            if y >= 159 and y <= 221:
                couleur = rouge
                chiffre = 5
                couleur2 = rouge2
                print('rouge=couleur')

            elif y >= 262 and y <= 324:
                couleur = vert
                couleur2 = vert2
                print('couleur=vert')
                chiffre = 4
            elif y >= 369 and y <= 431:
                couleur = jaune
                couleur2 = jaune2
                chiffre = 3
            elif y >= 480 and y <= 512:
                couleur = cyan
                couleur2 = cyan2
                chiffre = 2
            elif y >= 589 and y <= 618:
                couleur = violet
                couleur2 = violet2
                chiffre = 1

        elif x >= 181 and x <= 821 and y >= 79 and y <= 717:
            if nombre == 0:
                nombre_a_b = clic1(couleur, chiffre, couleur2)
                nombre = nombre_a_b[0]
                a = nombre_a_b[1]
                b = nombre_a_b[2]
                print(nombre_a_b, 'nombre')
            elif nombre == 1:
                print('miau')
                clic2(a, b, chiffre, couleur)
                nombre = clic2(a, b, chiffre, couleur)
                wait = 1

    ##             else:

    if event.type == MOUSEBUTTONUP:
        wait = 0

    ##
    ##      if x>=181 and x<=821 and y>=79 and y<=717:
    ##       if nombre_cases<5:
    ##        blanc=0
    ##
    ##
    ##
    ##        a=int((x-181)/64)
    ##        b=int((y-78)/64)
    ##        c1.append(a)
    ##
    ##        l1.append(b)
    ##
    ##        print(nombre_cases, c[a],l[b], liste)
    ##
    ##        if [c[a],l[b]] in liste:
    ##                    pygame.draw.rect(fond,white,(c[a],l[b],62,62))
    ##                    del l1[-1]
    ##                    del c1[-1]
    ##                    del liste[-1]
    ##                    del liste[-1]
    ##                    nombre_cases=nombre_cases-1
    ##                    enlever = [[c[a],l[b]]]
    ##                    liste[:] = (w for w in liste if w not in enlever)
    ##                    print('miau', liste)
    ##                    blanc=1
    ##
    ##
    ##        liste.append([c[a], l[b]])
    ##        if nombre_cases==0:
    ##
    ##            pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
    ##            nombre_cases+=1
    ##
    ##        elif blanc==0:
    ##            print('cool')
    ##
    ##            if nombre_cases==1 and ((abs(l1[-1]-l1[0])==1 and abs(c1[0]-c1[-1])==0) or (abs(c1[0]-c1[-1])==1 and abs(l1[0]-l1[-1])==0)):
    ##
    ##                pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
    ##                nombre_cases+=1
    ##
    ##                if abs(l1[-1]-l1[0])==1:
    ##                        decision='colonne'
    ##
    ##
    ##                else:
    ##                        decision='ligne'
    ##
    ##
    ##
    ##
    ##
    ##            elif decision=='ligne' and l1[nombre_cases-1]==l1[-1] and ((c1[-1]+1) in c1 or (c1[-1]-1) in c1):
    ##
    ##                pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
    ##                nombre_cases+=1
    ##
    ##            elif decision=='colonne' and ((l1[-1]+1) in l1 or (l1[-1]-1) in l1):
    ##                pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
    ##                nombre_cases+=1
    ##
    ##
    ##
    ##            else:
    ##
    ##                del l1[-1]
    ##                del c1[-1]
    ##
    ##
    ##        wait=1
    ##

    if event.type == MOUSEBUTTONUP:
        wait = 0
    if position_perso.top < -10:
        position_perso = position_perso.move(1, 0)

    # Re-collage

    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)

    # Rafraichissement
    pygame.display.flip()

pygame.quit()
