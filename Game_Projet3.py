import pygame, sys
from pygame.locals import *
from pygame import *

#Initialisation de la bibliothèque Pygame
pygame.init()
wait=0
#Ouverture  de la fenêtre Pygame
larg_fenetre=1419
haut_fenetre=731

fenetre = pygame.display.set_mode((larg_fenetre, haut_fenetre))

#Chargement et collage du fond
fond = pygame.image.load("bataille1.png").convert()
fenetre.blit(fond, (0,50))

#Chargement et collage du personnage
perso = pygame.image.load("blue.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, (0,0))
blue=(100,180,255)
white=(255,255,255)
c=[182, 246, 311, 376,440,505,569,634,698,761]
l=[79,143,207,272,336,400,464,528,592,656]
c1=[]
l1=[]
nombre_cases=0
liste=[]
liste_cases=[]




decision=''

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():	#Attente des événements
        if event.type == QUIT:          #Si on clique sur le bouton quitter
            continuer = 0               #la boucle s'arrête
        if event.type == KEYDOWN:       #Si on appuye sur une touche du clavier
            if event.key == K_ESCAPE:   #Si cette touche est la touche echap
                continuer = 0           #On arrête la boucle
            elif event.key == K_DOWN:
                position_perso = position_perso.move(0,50)
           

            elif event.key == K_UP:
                position_perso = position_perso.move(0,-50)
              

            elif event.key == K_LEFT:
                position_perso = position_perso.move(-50,0)
          
            elif event.key == K_RIGHT:
                position_perso = position_perso.move(50,0)
                
    if event.type==MOUSEBUTTONDOWN and wait==0:
      (x,y)=event.pos
      
      
 
      
      if x>=181 and x<=821 and y>=79 and y<=717:
       if nombre_cases<5:
        blanc=0
      
           
        
        a=int((x-181)/64)
        b=int((y-78)/64)
        c1.append(a)

        l1.append(b)
        
        print(nombre_cases, c[a],l[b], liste)
        
        if [c[a],l[b]] in liste:
                    pygame.draw.rect(fond,white,(c[a],l[b],62,62))
                    del l1[-1]
                    del c1[-1]
                    del liste[-1]
                    del liste[-1]
                    nombre_cases=nombre_cases-1
                    enlever = [[c[a],l[b]]]
                    liste[:] = (w for w in liste if w not in enlever)
                    print('miau', liste)
                    blanc=1
    

        liste.append([c[a], l[b]])
        if nombre_cases==0:

            pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
            nombre_cases+=1
   
        elif blanc==0:
            print('cool')
            
            if nombre_cases==1 and ((abs(l1[-1]-l1[0])==1 and abs(c1[0]-c1[-1])==0) or (abs(c1[0]-c1[-1])==1 and abs(l1[0]-l1[-1])==0)):
     
                pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
                nombre_cases+=1
      
                if abs(l1[-1]-l1[0])==1:
                        decision='colonne'
           
                        
                else:
                        decision='ligne'
    
                        

                    
                        
            elif decision=='ligne' and l1[nombre_cases-1]==l1[-1] and ((c1[-1]+1) in c1 or (c1[-1]-1) in c1):

                pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
                nombre_cases+=1
   
            elif decision=='colonne' and ((l1[-1]+1) in l1 or (l1[-1]-1) in l1):
                pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
                nombre_cases+=1
       
            
               
            else:
               
                del l1[-1]
                del c1[-1]
                

              
                
            
##        if a==c1[nombre_cases-1] and decision!='b':
##            decision='a'
##            liste_cases.append([c1[-1],l1[-1]-1])
##            liste_cases.append([c1[-1],l1[-1]+1])
##            print(liste_cases, a, b)
##            print('hi')
##        if b==l1[nombre_cases-1] and decision!='a':
##            decision='b'
##            print('b')
##            liste_cases.append([c1[-1]+1,l1[-1]])
##            liste_cases.append([c1[-1]-1,l1[-1]])
##        if nombre_cases>2:
##              klaus=klaus-1
##              print('no')
##        
##            
##              print(liste)
##        elif nombre_cases==0: 
##            liste.append([c[a],l[b]])
##            print(liste)
##            pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
##        
##        elif nombre_cases==1 and (a==c1[nombre_cases-1]+1 or a==c1[nombre_cases-1]-1 or b==l1[nombre_cases-1]+1 or b==l1[nombre_cases-1]-1):
##               liste.append([c[a],l[b]])
##               print(liste)
##               pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
##        if nombre_cases<5:
##        
##          if decision=='a' and [a,b] in liste_cases :
##              #and and len(c1)<6 and a in liste_cases_a and b in liste_cases_b (a==c1[nombre_cases-1]+1 or a==c1[nombre_cases-1]-1 or b==l1[nombre_cases-1]+1 or b==l1[nombre_cases-1]-1):
##            liste.append([c[a],l[b]])
##            print(liste, 'ko')
##            pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
##          elif decision=='b' and [a,b] in liste_cases:
##               liste.append([c[a],l[b]])
##               print(liste)
##               pygame.draw.rect(fond,blue,(c[a],l[b],62,62))
##              
##        if [c[a],l[b]] in liste:
##            pygame.draw.rect(fond,white,(c[a],l[b],62,62))
##            nombre_cases=nombre_cases-1
##            enlever = [[c[a],l[b]]]
##            liste[:] = (w for w in liste if w not in enlever)
##            print('miau')
                                 
        wait=1


    
    if event.type==MOUSEBUTTONUP:
        wait=0
    if position_perso.top < -10:
        position_perso=position_perso.move(1,0)
        
	#Re-collage
    
   
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    
	#Rafraichissement
    pygame.display.flip()

pygame.quit()
