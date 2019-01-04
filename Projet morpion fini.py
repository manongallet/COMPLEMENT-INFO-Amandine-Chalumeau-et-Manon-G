class Joueur_humain:
    def _init_(self,Nom,Symbole, NoLigne, NoColonne):
        self.Nom = Nom
        self.Symbole = Symbole
        self.NoLigne = NoLigne
        self.NoColonne = NoColonne
        
class Joueur_ordi:
    def _init(self,Nom,Symbole, NoLigne, NoColonne):
        self.Nom = Nom
        self.Symbole = Symbole
        self.NoLigne = NoLigne
        self.NoColonne = NoColonne

class Gestion_du_Jeu:
    def _init(self, MaitreDuJeu):
        self.MaitreDuJeu

#Choix du Symbole
Joueur_humain.Nom=input("Entrer votre nom : ")
Joueur_humain.Symbole=str(input("Entrer le symbole que vous voulez utiliser pour jouer(X ou O): "))
while ((Joueur_humain.Symbole != "X") and (Joueur_humain.Symbole != "O")):
    print("Vous devez choisir entre X ou O, recommencez")
    Joueur_humain.Symbole=str(input("Entrer le symbole que vous voulez utiliser pour jouer(X ou O): "))
    
M=[]
from random import*

#Attribution d'un Symbole à l'ordi
Joueur_ordi.Nom = "Ordi"
if Joueur_humain.Symbole == "X":
    Joueur_ordi.Symbole = "O"
else:
    Joueur_ordi.Symbole = "X"

#fonctions utilisées dans le programme
def affiche(M,nom):
    assert isinstance(M,list) & isinstance(nom,str)
    s=nom+"="
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            s=s+"|_"+str(M[i][j])+""
        s=s+"\n  "
    return(s)

def tableau_pas_rempli(M):
    for i in range(0,2):
        for j in range(0,2):
            if (M[i][j]== "_"):
                return True


def ligne (M):
    for i in range(0,2):
        for j in range(0,2):
            if ((M[i][0]=="X") and (M[i][1]=="X") and (M[i][2]=="X")):
                if Joueur_humain.Symbole=="X":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")
            elif(((M[i][0]=="O") and (M[i][1]=="O") and (M[i][2])=="O")):
                if Joueur_humain.Symbole=="O":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")


def colonne(M):
    for i in range(0,2):
        for j in range(0,2):
            if ((M[0][j]=="X") and (M[1][j]=="X") and (M[2][j]=="X")):
                if Joueur_humain.Symbole=="X":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")
            elif((M[0][j]=="O") and (M[1][j]=="O") and (M[2][j]=="O")):
                if Joueur_humain.Symbole=="O":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")

def diagonale(M):
    for i in range(0,2):
            if ((M[0][0]=="X")and (M[1][1]=="X")and (M[2][2]=="X")):
                if Joueur_humain.Symbole=="X":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")
            elif((M[0][0]=="O")and (M[1][1]=="O")and (M[2][2]=="O")):
                if Joueur_humain.Symbole=="O":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")
            elif((M[0][2]=="X")and (M[1][1]=="X")and (M[2][0]=="X")):
                if Joueur_humain.Symbole=="X":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")
            elif((M[0][2]=="O")and (M[1][1]=="O")and (M[2][0]=="O")):
                if Joueur_humain.Symbole=="O":
                    print(Joueur_humain.Nom," a gagné")
                else:
                    print(Joueur_ordi.Nom," a gagné")


#affichage du plateau vide                
M=[["_","_","_"],
   ["_","_","_"],
   ["_","_","_"]]
nom="T"        

print(affiche(M,"T"))

#Jeu
for i in range(0,2):
    for j in range(0,2):
        while(tableau_pas_rempli(M)):
        
#Joueur Humain
            MaitreDuJeu="C'est à", Joueur_humain.Nom, "de jouer"
            print(MaitreDuJeu)
            i=int(input("Dans quelle ligne voulez-vous jouer (1,2 ou 3) ? "))
            i=i-1
            j=int(input("Dans quelle colonne voulez-vous jouer (1,2 ou 3) ? "))
            j=j-1

            while ((i<0)or(i>2)or(j<0)or(j>2)):
                print("Vous devez choisir comme numéro de lignes ou de colonnes 1,2 ou 3, recommencez")
                i=int(input("Dans quelle ligne voulez-vous jouer (1,2 ou 3) ? "))
                i=i-1
                j=int(input("Dans quelle colonne voulez-vous jouer (1,2 ou 3) ? "))
                j=j-1

            
            while (M[i][j]=="X") or (M[i][j]=="O") :
                print("Cette case est déjà remplie, rejouez !")
                i=int(input("Dans quelle ligne voulez-vous jouer (1,2 ou 3) ? "))
                i=i-1
                j=int(input("Dans quelle colonne voulez-vous jouer (1,2 ou 3) ? "))
                j=j-1

            M[i][j]=Joueur_humain.Symbole

            ligne(M)
            colonne(M)
            diagonale(M)

            print(affiche(M,"T"))

#Joueur ordi
            MaitreDuJeu="C'est à", Joueur_ordi.Nom, "de jouer"
            print(MaitreDuJeu)
            i=int(uniform(0,3))
            j=int(uniform(0,3))

            while ((i<0) or (i>3) or (j<0) or (j>3)):
                    i=int(uniform(0,3))
                    j=int(uniform(0,3))
                
            while (M[i][j]=="X") or (M[i][j]=="O") :
                i=int(uniform(0,3))
                j=int(uniform(0,3))
                
            M[i][j]=Joueur_ordi.Symbole

            ligne(M)
            colonne(M)
            diagonale(M)
            
            print(affiche(M,"T"))
                 



print("La partie est finie")
            
print(affiche(M,"T"))







