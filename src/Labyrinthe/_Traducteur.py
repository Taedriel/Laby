from .__const__ import *

class Traducteur(object):
    def __init__(self, labyrinthe, depart, arrivee):
        """labyrinthe, depart, arrivée"""
        self.lab = labyrinthe
        self.tailleX = len(self.lab.getLab())
        self.tailleY = len(self.lab.getLab()[0])

        self.observer = []
        self.perso = None

        self.depart = depart
        self.arrivee = arrivee

        self.labTrad = []
        for _ in range(self.tailleX * 2 + 1):
            temp = []
            for __ in range(self.tailleY * 2 + 1):
                temp.append(WALL)
            self.labTrad.append(temp)

    def addObserver(self, observer):
        self.observer.append(observer)

    def notifyAll(self, action):
        for obs in self.observer:
            obs.notify(action)

    def setCell(self, x, y, content):
        print(str(x) + "/" + str(y) + " = " + str(content))
        self.labTrad[x][y] = content
        self.notifyAll(UPDATE)

    def getTailleY(self):
        return len(self.labTrad[0])

    def getTailleX(self):
        return len(self.labTrad)

    def getTraducteur(self):
        return self

    def getLabTrad(self):
        return self.labTrad

    def getCell(self, x, y):
        return self.get((x, y))

    def get(self, coord):
        try:
            a = self.labTrad[coord[0]][coord[1]]
        except IndexError:
            a = None
        return a

    def doAHole(self, taille):
        midY = int(self.getTailleY() / 2)
        midX = int(self.getTailleX() / 2)

        for x in range(midX - int(taille / 2)):
            for y in range(midY - int(taille / 2)):
                self.labTrad[x][y] = VOID

    def getDepart(self):
        return VOID, self.depart[0] * 2 + 1, self.depart[1] * 2 + 1

    """return un tuple consitué de trois elements : 
        - le contenue de la cellule
        - coordonnée X
        - coordonnée Y
    """
    def getArrivee(self):
        return VOID, self.arrivee[0] * 2 + 1, self.arrivee[1] * 2 + 1

    def traduire(self):

        for i in range(self.tailleX):
            for j in range(self.tailleY):
                N, E, S, O = 1, 2, 4, 8
                case = self.lab.getCell(i, j)
                number = case.getWall()

                self.labTrad[i * 2 + 1][j * 2 + 1] = VOID

                if number & N == N:
                    self.labTrad[i * 2 + 1][j * 2] = VOID

                if number & E == E:
                    self.labTrad[i * 2 + 2][j * 2 + 1] = VOID

                if number & S == S:
                    self.labTrad[i * 2 + 1][j * 2 + 2] = VOID

                if number & O == O:
                    self.labTrad[i * 2][j * 2 + 1] = VOID

    def afficher(self, **keyword):
        for i in range(len(self.labTrad)):
            print("")
            for j in range(len(self.labTrad[0])):
                if len(keyword) != 0:
                    try:
                        char = keyword[str(self.labTrad[i][j])]
                    except KeyError:
                        char = "???"

                    print(char, end="")
                else:
                    print(self.labTrad[i][j], end="")
        print("\n")

    def setPerso(self, perso):
        self.perso = perso

    def getPerso(self):
        return self.perso
