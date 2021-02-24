import os
import sys
import random 

player_vie = 50
player_potion = 3

ennemi_vie = 50

tour = 0

while player_vie > 0 and ennemi_vie > 0 :
    option = 3
    while option not in(1,2) :
        option = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "))
        if player_potion <= 0 and option == 2 :
            print("Vous n'avez plus de potion !")
            option = 3
                
        if option == 1 :
            attack_player = round(random.randint(5,10))
            ennemi_vie -= attack_player
            if ennemi_vie < 0:
                ennemi_vie = 0
            print("-----------------------------------------------------------------------")
            print('Vous attaquez avec ',attack_player,'points')
            print('La vie de l\'ennemi est de :',ennemi_vie)
            print("-----------------------------------------------------------------------")
            tour = 1
        elif option == 2 and player_potion > 0 :
            potion = round(random.randint(15,50))
            player_vie += potion
            player_potion -= 1
            print("-----------------------------------------------------------------------")
            print('la valeur de la potion :',potion,' !')
            print('Votre vie passe à :',player_vie)
            print('Il vous reste ',player_potion, 'potions')
            print("-----------------------------------------------------------------------")
            tour = 2
            
        compteur = 0
        while compteur < tour :
            attack_ennemi = round(random.randint(5,15))
            player_vie -= attack_ennemi
            if player_vie < 0:
                player_vie = 0
            print("-----------------------------------------------------------------------")
            print("l'ennemi attaque")
            print('l\'ennemi attaque avec ',attack_ennemi,'points')
            print('Votre vie passe à :',player_vie)
            print("-----------------------------------------------------------------------")
            compteur +=1
        tour=0

if player_vie <= 0 :
    print("-----------------------------------------------------------------------")
    print('Vous avez perdu ! ')
    print("-----------------------------------------------------------------------")
elif ennemi_vie <= 0 : 
    print("-----------------------------------------------------------------------")
    print('Vous avez perdu ! ')
    print("-----------------------------------------------------------------------")
else :
    print("-----------------------------------------------------------------------")
    print('nul ! ')
    print("-----------------------------------------------------------------------")
