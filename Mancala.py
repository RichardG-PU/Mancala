import random

class Mancala:
    def __init__(self):
        self.grille = {
            "A" : 13,
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
            "A" : 13,
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
        reverseCounter = 0
        ignored = False

        if bumps == 1:
            singleBump = True # IL FAUT CHECK SI LE PROCHAIN VALUE == 0
        self.grille[id] = 0
        while bumps > 0:
            for key, value in self.grille.items():
                counter+=1
                if key == id:
                    reached=True
                if (key != id or ignored) and reached and bumps != 0 and key != "1":
                    ignored = True
                    if singleBump == True:
                        for i, v in reversed(self.grille.items()):
                            reverseCounter+=1
                            if(reverseCounter - 1 == counter):
                                self.grille["2"] = v + self.grille["2"] + value
                                self.grille[i] = 0
                    else:
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