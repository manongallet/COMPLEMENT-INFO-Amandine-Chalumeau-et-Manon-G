# -*- coding: utf-8 -*-

from MaBase_MIB import*

###Question 1 : Quel est l'ensemble des gardiens ?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}
print(les_gardiens)

###Question 2 : Quelle est la ville d'origine des agents ? 
In[16]: les_villes_agents = {agent.Ville for agent in BaseAgents}

In[17]\ les_villes_agents
Out[17]: {'Hesperos', 'Kalgan', 'Terminus', 'Uco'}

###Question 3 : Quel est l'ensemble des triplets (n° de cabine, alien, gardien) pour chaque cabine ?
In [18]: triples = {(alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

In [19]: triples
Out[19]
{('1', 'Zorglub', 'Branno'),
 ('2', 'Blorx', 'Darell'),
 ('3', 'Urxiz', 'Demerzel'),
 ('4', 'Darneurane', 'Seldon'),
 ('4', 'Zbleurdite', 'Seldon'),
 ('6', 'Mulzo', 'Hardin'),
 ('7', 'Zzzzzz', 'Trevize'),
 ('8', 'Arghh', 'Pelorat'),
 ('9', 'Joranum', 'Riose')}

###Question 4 : Quel l'ensemble des couples (alien,allée) pour chaque alien ?
couples_alien_allée = {(alien.Nom, alien.NoAllee) for alien in BaseAliens for NoAllee in BaseCabines } 
print(couples_aliens_allée)

###Question 5: Quel est  l'ensemble de tous les aliens de l'allée 2 ?
aliens_allée_2 = {(alien.deux) for alien in BaseAliens for NoAllee in BaseCabines }
print(alien_allée_2)

###Question 6: Quel est l'ensemble de toutes les planètes dont sont originaires les aliens habitant une cellule de numéro pair ?

###Question 7: Quel est l'ensemble des aliens dont les gardiens sont originaires de Terminus ?
aliens_Gardiens_Terminus = { (alien.Gardien) for Gardien in BaseGardiens for alien in BaseAliens for Terminus in BaseAgents if gardien.Terminus == agent.Terminus }
print(aliens_Gardiens_Terminus)

###Question 8: Quel est l'ensemble des gardiens des aliens féminins qui mangent du bortsch ?
Gardiens_F_bortsch = {(gardien.alien) for Gardien in BaseGardien for alien in BaseAlien if alien.sexe == alien.femme if alien.miam == alien.bortsch }
print(Gardiens_F_bortsch)

#####Question 9: Quel est l'ensemble des cabines dont les gardiens sont originaires de Terminus ou dont les aliens sont des filles ?
Cabines_GardiensTerminus_ou_aliensF = {(Cabine.NoCabine) for Cabine in BaseCabine if alien.sexe == alien.femme if gardien.planète == gardien.Terminus }
print(Cabines_GardiensTerminus_ou_aliensF)

###Question 10: Y a-t-il des aliments qui commencent par la même lettre que le nom du gardien qui surveille l'alien qui les mange ?

###Question 11: Y a-t-il des aliens originaires d'Euterpe ?
aliens_Euterpe = {(alien.Euterpe) for alien in BaseAliens
print(aliens_Euterpe)

###Question 12: Est-ce que tous les aliens ont un 'x' dans leur nom ?
P= {(alien.Nom)for alien in BaseAliens }
for i in range(0,len (P)):
    if P[i]==x:
        print(P)
    else:
        print(" ")
        
###Question 13: Est-ce que tous les aliens qui ont un 'x' dans leur nom ont un gardien qui vient de Terminus ?
        

###Question 14: Existe-t-il un alien masculin originaire de Trantor qui mange du Bortsch ou dont le gardien vient de Terminus ?
alien = {(alien.Nom) for alien in BaseAliens if alien.sexe == alien.homme if alien.miam == alien.bortsch if gardien.planète == gardien.Terminus }
print(alien)


