# coding=<utf-8>
from sys import argv
from os import getcwd

import Labyrinthe as Lab_Pack

if __name__ == "__main__":

    if len(argv) == 1:  
        lab1 = Lab_Pack.Labyrinthe(10, 10)
        lab1.generate(False)
    else:
        if argv[1] == "-h":
            print("help: python3 Labyrinthe.py [-h] | [-x (number) -y (number)] | [-step] | [-solve] | [-graph]")
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

        lab = Lab_Pack.Labyrinthe(tailleX, tailleY)
        lab.generate(stepByStep)
        trad = Lab_Pack.Traducteur(lab, lab.getDepart(), lab.getArrive())
        trad.traduire()
        trad.afficher()

        if "-solve" in argv:
            path = Lab_Pack.Pathfinder(trad.getDepart(), trad.getArrivee(), trad.getTraducteur())
            path.findGoodPath()
            path.bindPath()
            trad.afficher(w="███", v="   ", p=" 0 ")

        if "-graph" in argv:
            mot = Lab_Pack.Moteur(trad.getLabTrad())
            mot.run()
