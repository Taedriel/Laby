from tkinter import *


class Moteur():
    """inserer de la doc ici"""

    def __init__(self, grid=None):
        self.main = Tk()
        self.main.title("MoteurGraphique")
        self.main.geometry(("500x500"))
        self.main.resizable(False, False)

        self.elements = {}

        self.screen = Canvas(self.main, confine=True)
        self.screen.pack()

        if grid != None and type(grid) == type([]) and type(grid[0]) == type([]):
            self.grid = grid
        else:
            raise(TypeError)

    def run(self):
        self.main.mainloop()


if __name__ == "__main__":
    mot = Moteur()
    mot.run()
