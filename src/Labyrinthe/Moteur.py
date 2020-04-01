from __const__ import *
from tkinter import *

from _Pathfinder import Pathfinder
from _Personnage import Perso
from _Traducteur import Traducteur
from Labyrinthe import Labyrinthe


class Moteur():
    """inserer de la doc ici"""

    def __init__(self, grid=None, perso=None):
        self.main = Tk()
        self.main.title("MoteurGraphique")

        if grid is not None and type(grid) == type([]) and type(grid[0]) == type([]):
            self.grid = grid
        else:
            raise (TypeError("Argument grid invalide ou non existant"))

        self.tailleY = len(self.grid) * LARGEUR
        self.tailleX = len(self.grid[0]) * HAUTEUR

        self.main.geometry(str(self.tailleX + 1) + "x" + str(self.tailleY + 1))
        self.main.resizable(False, False)

        self.elements = {}

        self.screen = Canvas(self.main, width=self.tailleX, height=self.tailleY, bg="grey", confine=True)
        if perso is not None:
            print("bind")
            self.perso = perso
            self.main.bind("<z>", self.perso.moveUp)
            self.main.bind("<q>", self.perso.moveLeft)
            self.main.bind("<s>", self.perso.moveDown)
            self.main.bind("<d>", self.perso.moveRight)

        self.screen.pack()
        self.paintGrid()

    def test(self):
        print(42)

    def getGrid(self):
        return self.grid

    def notify(self, action):
        if action == UPDATE:
            self.paintGrid()

    def paintGrid(self):

        for item in self.screen.find_all():
            self.screen.delete(item)

        posX, posY = 0, 0

        for x in self.grid:
            for y in x:

                if y == WALL:
                    self.screen.create_rectangle(posX, posY, posX + LARGEUR, posY + HAUTEUR, fill="black")
                if y == PERSO:
                    self.screen.create_oval(posX, posY, posX + LARGEUR, posY + HAUTEUR, fill="red")
                if y == PATH:
                    self.screen.create_oval(posX + LARGEUR / 3, posY + HAUTEUR / 3, posX + 2 * LARGEUR / 3,
                                            posY + 2 * HAUTEUR / 3, fill="blue")
                if y == ENNEMIE:
                    self.screen.create_oval(posX + LARGEUR / 3, posY + HAUTEUR / 3, posX + 2 * LARGEUR / 3,
                                            posY + 2 * HAUTEUR / 3, fill="black")

                posX += LARGEUR
            posX = 0
            posY += HAUTEUR

    def run(self):
        self.main.mainloop()


if __name__ == "__main__":
    lab = Labyrinthe(10, 30)
    lab.generate(False)

    trad = Traducteur(lab, lab.getDepart(), lab.getArrive())
    trad.traduire()

    perso = Perso(trad, trad.getDepart()[1], trad.getDepart()[2])
    trad.setPerso(perso)

    mot = Moteur(trad.getLabTrad(), trad.getPerso())
    trad.addObserver(mot)


    pathfinder = Pathfinder(trad.getDepart(), trad.getArrivee(), trad)
    pathfinder.findGoodPath()
    pathfinder.bindPath()

    trad.setCell(trad.getDepart()[1], trad.getDepart()[2], PERSO)

    mot.run()
