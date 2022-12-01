import math


class SecondProblem:
    def __init__(self, carrierFrequency, heightT, heightR, distance, selectedCity, selectAreaType):
        self.carrierFrequency = carrierFrequency
        self.heightT = heightT
        self.heightR = heightR
        self.distance = distance
        self.selectedCity = selectedCity
        self.selectAreaType = selectAreaType
        self.pathLoss = self.getPathLoss()

    def getPathLoss(self):
        correctionFactor = 0
        pathLossIndB = 0
        if (self.carrierFrequency >= 150 and self.carrierFrequency <= 1500 and self.heightT >= 30 and self.heightT <= 300 and self.heightR >= 1 and self.heightR <= 10 and self.distance >= 1 and self.distance <= 20):
            if(self.selectedCity == "Small/Medium"):
                correctionFactor = (1.1 * math.log10(self.carrierFrequency) - 0.7) * self.heightR - (1.56 * math.log10(self.carrierFrequency) - 0.8)
            elif(self.selectedCity == "Large"):
                if(self.carrierFrequency >= 150) and (self.carrierFrequency <= 300):
                    correctionFactor = 8.29 * pow((math.log10(1.54 * self.heightR)), 2) - 1.1
                elif(self.carrierFrequency > 300) and (self.carrierFrequency <= 1500):
                    correctionFactor = 3.2 * pow((math.log10(11.75 * self.heightR)), 2) - 4.97

            pathLossIndB = 69.55 + 26.16 * math.log10(self.carrierFrequency) - 13.82 * math.log10(
                self.heightT) - correctionFactor + (44.9 - 6.55 * math.log10(self.heightT)) * math.log10(self.distance)

            if(self.selectAreaType == "Urban"):
                return format(pathLossIndB, ".3f")
            elif(self.selectAreaType == "Suburban"):
                newPathL = pathLossIndB - (2 * pow(math.log10(self.carrierFrequency/28), 2)) - 5.4
                return format(newPathL, ".3f")
            elif(self.selectAreaType == "Open area"):
                newPathLoss = pathLossIndB - 4.78 * pow(math.log10(self.carrierFrequency), 2) - 18.733 * math.log10(self.carrierFrequency) - 40.98
                return format(newPathLoss, ".3f")
        else:
            return 0