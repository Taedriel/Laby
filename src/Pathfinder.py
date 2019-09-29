from random import random


class Pathfinder(object):

    def __init__(self, depart, arrivee, plateau):

        self.plateau = plateau
        self.depart = depart
        self.arrivee = arrivee

        self.listeVoisin = []
        self.listeCircuit = []
        self.caseVisite = []
        self.circuit = []

        self.testOneWay(0)
        self.setPath(self.circuit)

    def setPath(self, listCell):
        for cell in listCell:
            self.plateau.setCell(cell[1], cell[2], 2)

    """
    def getCaseDebut(self):
        if self.depart[2] == 1 or self.depart[2] == self.plateau.getTailleX() - 1:
            # case de depart sur l'axe y
            if self.depart[2] < int(self.plateau.getTailleY() / 2):
                # case à gauche
                case = (0, self.depart[2] - 1, self.depart[2])
                self.caseVisite.append(case)
                self.listeCircuit.insert(0, case)
            else:
                # case à droite
                case = (0, self.depart[2] + 1, self.depart[2])
                self.caseVisite.append(case)
                self.listeCircuit.insert(0, case)
        else:
            # case de depart sur l'axe X
            if self.depart[1] < int(self.plateau.getTailleX() / 2):
                # case à gauche
                case = (0, self.depart[1], self.depart[2] - 1)
                self.caseVisite.append(case)
                self.listeCircuit.insert(0, case)
            else:
                # case à droite
                case = (0, self.depart[1], self.depart[2] + 1)
                self.caseVisite.append(case)
                self.listeCircuit.insert(0, case)
    """

    def getValideCell(self, coord):
        self.getVoisin(coord)
        caseValide = []

        for eachCase in self.listeVoisin:
            if eachCase[0] == 0 and eachCase not in self.caseVisite:
                caseValide.append(eachCase)

        return caseValide if len(caseValide) != 0 else None

    def testOneWay(self, id):
        """
        on verifie si il y a d'autre case dispo
            si non
                on remonte
            si oui, recursivité avec caseActuel sur chacun des cases
                on ajoute a la liste actuelle
        """

        cell = self.depart
        cases = self.getValideCell(cell)

        while len(cases) > 0:
            self.circuit.insert(0, cell)
            cell  = cases[int(random() * len(cases) - 1)]
            cases = self.getValideCell(cell)
            for case in cases:
                if case in self.circuit:
                    cases.remove(case)


    def getVoisin(self, coord):
        self.listeVoisin.clear()
        if coord[1] > 0 and coord[2] > 0:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] - 1, coord[2] - 1)), coord[1] - 1, coord[2] - 1))

        if coord[1] > 0:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] - 1, coord[2])), coord[1] - 1, coord[2]))

        if coord[1] > 0 and coord[2] < self.plateau.getTailleY() - 1:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] - 1, coord[2] + 1)), coord[1] - 1, coord[2] + 1))

        if coord[2] < self.plateau.getTailleY() - 1:
            self.listeVoisin.append(
                (self.plateau.get((coord[1], coord[2] + 1)), coord[1], coord[2] + 1))

        if coord[1] < self.plateau.getTailleX() - 1 and coord[2] < self.plateau.getTailleY() - 1:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] + 1, coord[2] + 1)), coord[1] + 1, coord[2] + 1))

        if coord[1] < self.plateau.getTailleX() - 1:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] + 1, coord[2])), coord[1] + 1, coord[2]))

        if coord[1] < self.plateau.getTailleX() - 1 and coord[2] > 0:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] + 1, coord[2] - 1)), coord[1] + 1, coord[2] - 1))

        if coord[2] > 0:
            self.listeVoisin.append(
                (self.plateau.get((coord[1], coord[2] - 1)), coord[1], coord[2] - 1))
