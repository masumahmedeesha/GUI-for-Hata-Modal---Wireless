import math

class FirstProblem:
    def __init__(self, areaSize, cellRadius, frequencyAlotted, reuseFactor):
        self.areaSize = areaSize
        self.cellRadius = cellRadius
        self.frequencyAlotted = frequencyAlotted
        self.reuseFactor = reuseFactor
        self.numberOfCells = self.getNumberOfCells()
        self.channelsPerCell = self.getChannelsPerCell()
        self.totalCapacity = self.getTotalCapacity()

    def getNumberOfCells(self):
        areaOfHeaxgon = 1.5 * math.sqrt(3) * pow(self.cellRadius, 2)
        assumedNumberOfCells = self.areaSize / areaOfHeaxgon
        numberCells = int(assumedNumberOfCells + 0.5)
        return numberCells

    def getChannelsPerCell(self):
        numberOfChannelsPerCell = self.frequencyAlotted / self.reuseFactor
        assumed = int(numberOfChannelsPerCell+0.5)
        return assumed

    def getTotalCapacity(self):
        return self.numberOfCells * self.channelsPerCell