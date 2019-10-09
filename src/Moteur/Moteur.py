from tkinter import *
from CONST import *
from Labyrinthe.Labyrinthe import Labyrinthe
from Labyrinthe.Traducteur import Traducteur


class Moteur():
    """inserer de la doc ici"""

    def __init__(self, grid=None):
        self.main = Tk()
        self.main.title("MoteurGraphique")

        if grid is not None and type(grid) == type([]) and type(grid[0]) == type([]):
            self.grid = grid
        else:
            raise (TypeError("Argument grid invalide ou non existant"))

        self.tailleX = len(self.grid) * LARGEUR
        self.tailleY = len(self.grid[0]) * HAUTEUR

        self.main.geometry(str(self.tailleX) + "x" + str(self.tailleY))
        self.main.resizable(False, False)

        self.elements = {}

        self.screen = Canvas(self.main, width=self.tailleX, height=self.tailleY, bg="grey", confine=True)
        self.screen.pack()

        self.paintGrid()

    def paintGrid(self):

        posX, posY = 0, 0

        for x in self.grid:
            for y in x:
                if y == WALL:
                    self.screen.create_rectangle(posX, posY, posX + LARGEUR, posY + HAUTEUR, fill="black")

                posX += LARGEUR
            posX = 0
            posY += HAUTEUR

    def run(self):
        self.main.mainloop()


if __name__ == "__main__":
    lab = Labyrinthe(10, 10)
    lab.generate(False)
    trad = Traducteur(lab, lab.getDepart(), lab.getArrive())
    trad.traduire()
    mot = Moteur(trad.getLabTrad())

    mot.run()
