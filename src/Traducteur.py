class Traducteur(object):
    def __init__(self, labyrinthe, depart, arrivee):
        """labyrinthe, depart, arrivée"""
        self.lab = labyrinthe
        self.tailleX = len(self.lab.getLab())
        self.tailleY = len(self.lab.getLab()[0])

        self.depart = depart
        self.arrivee = arrivee

        self.labTrad = []
        for i in range(self.tailleX * 2 + 1):
            temp = []
            for j in range(self.tailleY * 2 + 1):
                temp.append(1)
            self.labTrad.append(temp)

    def getTailleY(self):
        return len(self.labTrad[0])

    def getTailleX(self):
        return len(self.labTrad)

    def getTraducteur(self):
        return self

    def get(self, coord):
        return self.labTrad[coord[0]][coord[1]]

    def getDepart(self):
        print(0, self.depart[0] * 2 + 1, self.depart[1] * 2 + 1)
        return 0, self.depart[0] * 2 + 1, self.depart[1] * 2 + 1

    def getArrivee(self):
        print(0, self.arrivee[0] * 2 + 1, self.arrivee[1] * 2 + 1)
        return 0, self.arrivee[0] * 2 + 1, self.arrivee[1] * 2 + 1

    def traduire(self):

        for i in range(self.tailleX):
            for j in range(self.tailleY):
                N, E, S, O = 1, 2, 4, 8
                case = self.lab.getCell(i, j)
                number = case.getWall()

                self.labTrad[i * 2 + 1][j * 2 + 1] = 0

                if number & N == N:
                    self.labTrad[i * 2 + 1][j * 2] = 0

                if number & E == E:
                    self.labTrad[i * 2 + 2][j * 2 + 1] = 0

                if number & S == S:
                    self.labTrad[i * 2 + 1][j * 2 + 2] = 0

                if number & O == O:
                    self.labTrad[i * 2][j * 2 + 1] = 0

    def afficher(self, char1="1", char0="0"):
        for i in range(len(self.labTrad)):
            print("")
            for j in range(len(self.labTrad[0])):
                print([char1 if self.labTrad[i][j] == 1 else char0][0], end="")
        print("\n")
