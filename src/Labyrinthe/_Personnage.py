from .__const__ import *

class Perso(object):

    def __init__(self, trad, posX, posY):

        self.plateau = trad

        self.posX = posX
        self.posY = posY

        print(self.plateau.afficher())

    def moveUp(self, event):
        case = self.plateau.getCell(self.posX - 1, self.posY)
        if case not in [WALL, ENNEMIE] and case is not None:
            print("up")
            self.posX -= 1
            self.plateau.setCell(self.posX + 1, self.posY, VOID)
            self.plateau.setCell(self.posX, self.posY, PERSO)
        else:
            print("cannot move")

    def moveDown(self, event):
        case = self.plateau.getCell(self.posX + 1, self.posY)
        if case not in [WALL, ENNEMIE] and case is not None:
            print("down")
            self.posX += 1
            self.plateau.setCell(self.posX - 1, self.posY, VOID)
            self.plateau.setCell(self.posX, self.posY, PERSO)
        else:
            print("cannot move")

    def moveLeft(self, event):
        case = self.plateau.getCell(self.posX, self.posY - 1)
        if case not in [WALL, ENNEMIE] and case is not None:
            print("left")
            self.posY -= 1
            self.plateau.setCell(self.posX, self.posY + 1, VOID)
            self.plateau.setCell(self.posX, self.posY, PERSO)
        else:
            print("cannot move")

    def moveRight(self, event):
        case = self.plateau.getCell(self.posX, self.posY + 1)
        if case not in [WALL, ENNEMIE] and case is not None:
            print("right")
            self.posY += 1
            self.plateau.setCell(self.posX, self.posY - 1, VOID)
            self.plateau.setCell(self.posX, self.posY, PERSO)
        else:
            print("cannot move")
