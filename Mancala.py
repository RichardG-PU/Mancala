import random

class Mancala:
    def __init__(self):
        self.grille = {
            "A" : 4,
            "B" : 4,
            "C" : 4,
            "D" : 4,
            "E" : 4,
            "F" : 4,
            "2" : 0,
            "L" : 4,
            "K" : 4,
            "J" : 4,
            "I" : 4,
            "H" : 4,
            "G" : 4,
            "1" : 0
        }
        self.joueurTour = True # bool(random.getrandbits(1))
    
    def nouvelleGrille(self):
        self.grille = {
            "A" : 4,
            "B" : 4,
            "C" : 4,
            "D" : 4,
            "E" : 4,
            "F" : 4,
            "2" : 0,
            "L" : 4,
            "K" : 4,
            "J" : 4,
            "I" : 4,
            "H" : 4,
            "G" : 4,
            "1" : 0
        }
        self.joueurTour = True # bool(random.getrandbits(1))
    
    def joueurDeplacement(self, id):
        blacklist = "GHIJKL21"
        if id in blacklist or self.joueurTour == False:
            return False
        
        reached = False
        bumps = self.grille[id]
        singleBump = False
        counter = 0

        if bumps == 1:
            singleBump = True
        self.grille[id] = 0
        while bumps > 0:
            for key, value in self.grille.items():
                counter+=1
                if key == id:
                    reached=True
                if key != id and reached and bumps != 0 and key != "1":
                    if singleBump == True:
                        for key, value in reversed(self.grille.items()):
                            print(key, value)
                        # BROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoo
                        # faut faire un algorithme but i gotchu tkt
                    self.grille[key] = value + 1
                    bumps-=1
                    if bumps == 0 and key == "2":
                        self.joueurTour = True
                    else:
                        self.joueurTour = True # False
            print(self.grille)
        
        return True

def main():
    mancala = Mancala()
    mancala.joueurDeplacement("A")

if __name__ == "__main__":
    main()