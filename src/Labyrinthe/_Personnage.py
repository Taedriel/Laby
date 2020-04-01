from __const__ import *

class Perso(object):

    def __init__(self, trad, posX, posY):

        self.plateau = trad

        self.posX = posX
        self.posY = posY

        print(self.plateau.afficher())

    def moveUp(self, event):
        if self.plateau.getCell(self.posX - 1, self.posY) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX, self.posY, VOID)
            self.plateau.setCell(self.posX - 1, self.posY, PERSO)
            print("up")
            self.posX -= 1
        else:
            print("cannot move")

    def moveDown(self, event):
        if self.plateau.getCell(self.posX + 1, self.posY) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX, self.posY, VOID)
            self.plateau.setCell(self.posX + 1, self.posY, PERSO)
            print("down")
            self.posX += 1
        else:
            print("cannot move")

    def moveLeft(self, event):
        if self.plateau.getCell(self.posX, self.posY - 1) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX, self.posY, VOID)
            self.plateau.setCell(self.posX, self.posY - 1, PERSO)
            print("left")
            self.posY -= 1
        else:
            print("cannot move")

    def moveRight(self, event):
        if self.plateau.getCell(self.posX, self.posY + 1) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX, self.posY, VOID)
            self.plateau.setCell(self.posX, self.posY + 1, PERSO)
            print("right")
            self.posY += 1
        else:
            print("cannot move")
