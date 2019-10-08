from tkinter import Tk as Tk


class Moteur():
    """inserer de la doc ici"""

    def __init__(self):
        self.main = Tk()
        self.main.title("MoteurGraphique")
        self.main.geometry(("500x500"))
        self.main.resizable(False, False)

    def run(self):
        self.main.mainloop()


if __name__ == "__main__":
    mot = Moteur()
    mot.run()
