class Mancala:
    def __init__(self):
        self.grille = {
            "A": 13,
            "B": 4,
            "C": 4,
            "D": 4,
            "E": 4,
            "F": 4,
            "2": 0,
            "L": 4,
            "K": 4,
            "J": 4,
            "I": 4,
            "H": 4,
            "G": 4,
            "1": 0,
        }
        self.joueurTour = True  # bool(random.getrandbits(1))

    def nouvelleGrille(self):
        self.grille = {
            "A": 13,
            "B": 4,
            "C": 4,
            "D": 4,
            "E": 4,
            "F": 4,
            "2": 0,
            "1": 0,
            "L": 4,
            "K": 4,
            "J": 4,
            "I": 4,
            "H": 4,
            "G": 4,
        }
        self.joueurTour = True  # bool(random.getrandbits(1))

    def joueurDeplacement(self, id):
        blacklist = "GHIJKL21"
        if id in blacklist or self.joueurTour == False:
            return False

        temp = list(self.grille)
        bumps = self.grille[id]
        res = temp[temp.index(id) + bumps]
        if res == "1":
            if (temp.index(id) + bumps + 1) > 13 :
                res = temp[14 - (temp.index(id) + bumps + 1)]
            else:
                res = temp[temp.index(id) + bumps + 1]

        reached = False
        singleLeft = False
        singleBump = False
        counter = 0
        reverseCounter = 0
        ignored = False

        self.grille[id] = 0

        if res != "1" and res != "2" and self.grille[res] == 0:
            singleLeft = True
            if bumps == 0:
                singleBump = True
        self.grille[id] = 0
        while bumps > 0:
            for key, value in self.grille.items():
                counter += 1
                if key == id:
                    reached = True
                if (key != id or ignored) and reached and bumps != 0 and key != "1":
                    ignored = True
                    if singleLeft == True:
                        for i, v in reversed(self.grille.items()):
                            reverseCounter += 1
                            if reverseCounter == counter and singleBump != True:
                                print("reverse counter", reverseCounter, "\ncounter", counter)
                                print(i, self.grille[i], "AZAAAAAAAAA")
                                self.grille["2"] = v + self.grille["2"] + 1
                                self.grille[i] = 0
                            elif reverseCounter - 1 == counter and singleBump == True:
                                self.grille["2"] = v + self.grille["2"] + 1
                                self.grille[i] = 0
                    else:
                        self.grille[key] = value + 1

                    bumps -= 1
                    if bumps == 0 and key == "2":
                        self.joueurTour = True
                    else:
                        self.joueurTour = True  # False

        return True


def main():
    mancala = Mancala()
    mancala.joueurDeplacement("A")


if __name__ == "__main__":
    main()
