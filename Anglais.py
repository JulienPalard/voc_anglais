import random


def mot_francais(nbr_fra):
    mots = ["Rouge","Vert","Bleu","Jaune","Soleil","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche","Demain","Hier","Aujourd'hui","être","Avoir"]
   
    print()
    print(mots[nbr_fra])
    print()


def mot_anglais():
    mots =["Red","Green","Bleu","Jaune","Sun","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Tomorrow","Yesterday","Today","Be","Have"]
    Nbr = Random.Randint(0,3)
    print()
    print(mots[nbr])
    print()


   

    
print("1.  Anglais --> Français")
print()
print("2.  Français --> Anglais")
print()
choix = input("Quel est ton choix :")
def Defilement():
    if int(choix) == 1:
        nbr_fra=random.randint(0,16)
        mot_francais(nbr_fra)
        rep=input("Quel est sa traduction :")    
        if rep=="Red" and nbr_fra == 0:
            print("Bonne réponse")

        if rep == "Green" and nbr_fra == 1:
            print("Bonne réponse")
        
        if rep =="Yellow" and nbr_fra == 3:
            print("Bonne réponse")
       
        if rep == "Blue" and nbr_fra == 2:
            print("Bonne réponse")
        
        if rep == "Sun" and nbr_fra == 4:
            print("Bonne réponse")
        
            
        if rep == "Monday" and nbr_fra == 5:
            print("Bonne réponse")
        
        if rep == "Tuesday" and nbr_fra == 6:
            print("Bonne réponse")
        
        if rep == "Wednesday" and nbr_fra == 7:
            print("Bonne Réponse")
        if rep == "Thursday" and nbr_fra == 8:
            print("Bonne réponse")
        if rep == "Friday" and nbr_fra == 9:
            print("Bonne réponse")
        if rep == "Saturday" and nbr_fra == 10:
            print("Bonne réponse")
        if rep == "Sunday" and nbr_fra ==11:
            print("Bonne réponse")
        if rep == "Tomorrow" and nbr_fra == 12:
            print("Bonne réponse")
        if rep == "Yesterday" and nbr_fra == 13:
            print("Bonne réponse")
        if rep == "Today" and nbr_fra == 14:
            print("Bonne réponse")
        if rep == "Be" and nbr_fra == 15:
            print("Bonne réponse")
        if rep =="Have" and nbr_fra ==16:
            print("Bonne réponse")
                
        
        

i=0
while i < 15:
    Defilement()
    i=i+1
    
