from tkinter import *
from CONST import *


class Moteur():
    """inserer de la doc ici"""

    def __init__(self, grid=None):
        self.main = Tk()
        self.main.title("MoteurGraphique")

        self.tailleX = 500
        self.tailleY = 500

        self.main.geometry((str(self.tailleX) + "x" + str(self.tailleY)))
        self.main.resizable(False, False)

        self.elements = {}

        self.screen = Canvas(self.main, width=self.tailleX, height=self.tailleY, bg="grey", confine=True)
        self.screen.pack()

        if grid is not None and type(grid) == type([]) and type(grid[0]) == type([]):
            self.grid = grid
        else:
            raise (TypeError("Argument grid invalide ou non existant"))

        self.paintGrid()

    def paintGrid(self):

        posX, posY = 0, 0

        for x in self.grid:
            for y in x:
                print(str(posX) + ":" + str(posY) + " = " + str(y))
                self.screen.create_rectangle(posX, posY, posX + LARGEUR, posY + HAUTEUR, fill="black", outline="blue")
                posX += LARGEUR
            posX = 0
            posY += HAUTEUR

    def run(self):
        self.main.mainloop()


if __name__ == "__main__":
    mot = Moteur([['','',''],['','',''],['','','']])
    mot.run()
