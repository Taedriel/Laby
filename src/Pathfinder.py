class Pathfinder(object):

    def __init__(self, depart, arrivee, plateau):

        self.plateau = plateau
        self.depart = depart
        self.arrivee = arrivee

        self.actual = self.depart

        self.listeVoisin = []
        self.listeCircuit = {0: []}
        self.caseVisite = {0: []}

        self.getNextStep(0)
        print(self.findPath())
        self.setPath(self.findPath())

    def setPath(self, listCell):
        for cell in listCell:
            self.plateau.setCell(cell[1], cell[2], 2)


    def findPath(self):
        for key, list in self.listeCircuit.items():
            if self.arrivee in list:
                return list
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

    def getValideCell(self):
        self.getVoisin()
        caseValide = []

        for eachCase in self.listeVoisin:
            if eachCase[0] == 0 and eachCase not in self.caseVisite:
                caseValide.append(eachCase)

        return caseValide if len(caseValide) != 0 else None

    def getNextStep(self, key):
        """
        on ajoute actual au path
        on verifie si il y a d'autre case dispo
            si oui, recursivité avec caseActuel = case[random]
                des qu'on revient on copy le path et on conitnu comme ça
            si non
                on remonte
        """
        self.listeCircuit.get(key).append(self.actual)
        self.caseVisite.get(key).append(self.actual)

        print(len(self.listeCircuit))

        case = self.getValideCell()
        if case is None:
            # on est au bout d'un chemin
            return
        else:
            for each in case:
                if each not in self.caseVisite.get(key):
                    self.actual = each
                    newkey = len(self.listeCircuit)
                    self.listeCircuit[newkey] = self.listeCircuit.get(newkey - 1)
                    self.caseVisite[newkey] = self.caseVisite.get(newkey - 1)
                    self.getNextStep(newkey)
            return

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
