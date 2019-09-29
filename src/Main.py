from Labyrinthe import Labyrinthe
from Pathfinder import Pathfinder
from Traducteur import Traducteur
from sys import argv

if __name__ == "__main__":
    """
    if len(argv) == 1:
        lab1 = Labyrinthe(10, 10)
        lab1.generate(False)
    else:
        if argv[1] == "-h":
            print("help: python3 Labyrinthe.py [-h] | [-x (number) -y (number)] | [-step]")
            exit(0)

        if "-x" in argv:
            try:
                tailleX = int(argv[argv.index("-x") + 1])
            except ValueError:
                tailleX = 10
        else:
            tailleX = 10

        if "-y" in argv:
            try:
                tailleY = int(argv[argv.index("-y") + 1])
            except ValueError:
                tailleY = 10
        else:
            tailleY = 10

        if "-step" in argv:
            stepByStep = True

        else:
            stepByStep = False

        lab = Labyrinthe(tailleX, tailleY)
        lab.generate(stepByStep)
    """

    lab1 = Labyrinthe(10, 10)
    lab1.generate(False)
    trad = Traducteur(lab1, lab1.getDepart(), lab1.getArrive())
    trad.traduire()
    trad.afficher("███", "   ", "...")
    path = Pathfinder(trad.getDepart(), trad.getArrivee(), trad.getTraducteur())
    trad.afficher("███", "   ", "...")
