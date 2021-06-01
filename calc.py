from UliEngineering.Physics.RTD import pt100_temperature, pt100_resistance
from math import *

def calc_PS(srLowIn, srHighIn, prLowIn, prHighIn, srCalcIn, prCalcIn):  # Button and returnPressed action
    ## Calculation PR -> SR
    psOutput = (((prCalcIn - srLowIn) * (prHighIn - prLowIn)) / (srHighIn - srLowIn)) + prLowIn
    return psOutput
    #self.prToSrOutput08.setText(str(srOutput))
    #print(srOutput + 'OK')


def calc_SP(srLowIn, srHighIn, prLowIn, prHighIn, srCalcIn, prCalcIn):  # Button and returnPressed action
    ## Calculation SR -> PR

    spOutput = ((srHighIn - srLowIn) / (prHighIn - prLowIn) * (srCalcIn - prLowIn)) + srLowIn
    print('calc_SP => OK')
    return spOutput


def calcPt100_ResToTemp(resistanceIn):
    print('calcPt100_ResToTemp -> OK')
    # Calculate temperature with UliEngineering RTD script
    return pt100_temperature(resistanceIn)


def calcPt100_TempToRes(temperaturIn):
    print('calcPt100_TempToRes -> OK')
    # Calculate temperature with UliEngineering RTD script
    return pt100_resistance(temperaturIn)




