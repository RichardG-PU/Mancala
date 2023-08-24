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
    
    def joueurDeplacement(self, id):
        blacklist = "GHIJKL21"
        if id in blacklist:
            return False
        
        reached = False
        bumps = self.grille[id]
        self.grille[id] = 0
        while bumps > 0:
            for key, value in self.grille.items():
                if key == id:
                    reached=True
                if key != id and reached and bumps != 0 and key != "1":
                    self.grille[key] = value + 1
                    bumps-=1
            print(self.grille)
        
        return True

def main():
    mancala = Mancala()
    mancala.joueurDeplacement("A")

if __name__ == "__main__":
    main()