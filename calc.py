from math import *
from UliEngineering.Physics.RTD import pt100_temperature, pt100_resistance

def calc_PS(self):  # Button and returnPressed action
    ## Calculation PR -> SR
    srOutput = ((self.srHighIn - self.srLowIn) / (self.prHighIn - self.prLowIn) * (
            self.prCalcIn - self.prLowIn)) + self.srLowIn
    self.prToSrOutput08.setText(str(srOutput))
    print(srOutput)


def calc_SP(self):  # Button and returnPressed action
    ## Calculation SR -> PR
    # prOutput = (((srCalcIn - srLowIn) * (prHighIn - prLowIn)) / (srHighIn - srLowIn)) + prLowIn
    prOutput = (((self.srCalcIn - self.srLowIn) * (self.prHighIn - self.prLowIn)) / (
            self.srHighIn - self.srLowIn)) + self.prLowIn
    self.srToPrOutput06.setText(str(prOutput))
    print(prOutput)






def calcPt100_ResToTemp(resistanceIn):
    print('calcPt100ToRes -> OK')
    # Calculate temperature with the calculation when temp equal or upper than 0°C
    return pt100_temperature({resistanceIn})


def calcPt100_TempToRes(temperaturIn):
    print('calcPt100ToTemp -> OK')
    # Calculate temperature with the calculation when temp equal or upper than 0°C
    return pt100_resistance({temperaturIn})




