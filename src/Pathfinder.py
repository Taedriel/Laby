class Pathfinder(object):

    def __init__(self, depart, arrivee, plateau):

        self.plateau = plateau
        self.depart = depart
        self.arrivee = arrivee

        self.actual = self.depart

        self.listeVoisin = []
        self.circuit = []
        self.caseVisite = []

        self.getCaseDebut()
        print(self.circuit)
        print(self.isDeadCell())

    def getCaseDebut(self):
        if self.depart[2] == 1 or self.depart[2] == self.plateau.getTailleX() - 1:
            # case de depart sur l'axe y
            if self.depart[2] < int(self.plateau.getTailleY() / 2):
                # case à gauche
                case = (0, self.depart[2] - 1, self.depart[2])
                self.caseVisite.append(case)
                self.circuit.insert(0, case)
            else:
                # case à droite
                case = (0, self.depart[2] + 1, self.depart[2])
                self.caseVisite.append(case)
                self.circuit.insert(0, case)
        else:
            # case de depart sur l'axe X
            if self.depart[1] < int(self.plateau.getTailleX() / 2):
                # case à gauche
                case = (0, self.depart[1], self.depart[2] - 1)
                self.caseVisite.append(case)
                self.circuit.insert(0, case)
            else:
                # case à droite
                case = (0, self.depart[1], self.depart[2] + 1)
                self.caseVisite.append(case)
                self.circuit.insert(0, case)

    def isDeadCell(self):
        self.getVoisin()
        caseValide = []

        for eachCase in self.listeVoisin:
            print("case= ", eachCase)
            if eachCase[0] == 0 and eachCase not in self.caseVisite:
                caseValide.append(eachCase)

        return caseValide

    def getNextStep(self):
        pass

    def getVoisin(self):
        self.listeVoisin.clear()
        if self.actual[1] > 0 and self.actual[2] > 0:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1] - 1, self.actual[2] - 1)), self.actual[1] - 1, self.actual[2] - 1))

        if self.actual[1] > 0:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1] - 1, self.actual[2])), self.actual[1] - 1, self.actual[2]))

        if self.actual[1] > 0 and self.actual[2] < self.plateau.getTailleY() - 1:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1] - 1, self.actual[2] + 1)), self.actual[1] - 1, self.actual[2] + 1))

        if self.actual[2] < self.plateau.getTailleY() - 1:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1], self.actual[2] + 1)), self.actual[1], self.actual[2] + 1))

        if self.actual[1] < self.plateau.getTailleX() - 1 and self.actual[2] < self.plateau.getTailleY() - 1:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1] + 1, self.actual[2] + 1)), self.actual[1] + 1, self.actual[2] + 1))

        if self.actual[1] < self.plateau.getTailleX() - 1:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1] + 1, self.actual[2])), self.actual[1] + 1, self.actual[2]))

        if self.actual[1] < self.plateau.getTailleX() - 1 and self.actual[2] > 0:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1] + 1, self.actual[2] - 1)), self.actual[1] + 1, self.actual[2] - 1))

        if self.actual[2] > 0:
            self.listeVoisin.append(
                (self.plateau.get((self.actual[1], self.actual[2] - 1)), self.actual[1], self.actual[2] - 1))
