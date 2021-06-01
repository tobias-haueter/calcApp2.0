from math import *
#from cmath import *

def calcPS(self):  # Button and returnPressed action
    ## Calculation PR -> SR
    srOutput = ((self.srHighIn - self.srLowIn) / (self.prHighIn - self.prLowIn) * (
            self.prCalcIn - self.prLowIn)) + self.srLowIn
    self.prToSrOutput08.setText(str(srOutput))
    print(srOutput)


def calcSP(self):  # Button and returnPressed action
    ## Calculation SR -> PR
    # prOutput = (((srCalcIn - srLowIn) * (prHighIn - prLowIn)) / (srHighIn - srLowIn)) + prLowIn
    prOutput = (((self.srCalcIn - self.srLowIn) * (self.prHighIn - self.prLowIn)) / (
            self.srHighIn - self.srLowIn)) + self.prLowIn
    self.srToPrOutput06.setText(str(prOutput))
    print(prOutput)


## PT100 Calculation

# Constants
A = 0.0039083
B = -0.0000005775
C = -0.000000000004183
r0 = 100.0




def calcPt100ToRes(self):
    print('calcPt100ToRes -> OK')


def calcPt100ToTemp(self):
    # ValueError: math domain error????
    print('calcPt100ToTemp -> OK')
    # Calculate temperature with the calculation when temp equal or upper than 0°C
    r = self.pt100_rIN

    t_temp = -(A - sqrt(A ** 2.0 * r0 + 4.0 * B * r - 4.0 * B * r0) / sqrt(r0)) / (2.0 * B)

    if t_temp == -7.509625437129035e-13:
        t = 0
    else:
        t = t_temp

    if t < 0:
        t = -0.50000*sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) - 0.50000*sqrt(-(1.3333*B)/C - (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) - (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) - (0.25000*(-(8*A)/C - (400*B)/C + 1000000))/sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) + 5000) + 25
        #t = -0.50000*sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) + 0.50000*sqrt(-(1.3333*B)/C - (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) - (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) - (0.25000*(-(8*A)/C - (400*B)/C + 1000000))/sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) + 5000) + 25
        #t =  0.50000*sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) - 0.50000*sqrt(-(1.3333*B)/C - (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) - (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + (0.25000*(-(8*A)/C - (400*B)/C + 1000000))/sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) + 5000) + 25
        #t =  0.50000*sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) + 0.50000*sqrt(-(1.3333*B)/C - (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) - (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + (0.25000*(-(8*A)/C - (400*B)/C + 1000000))/sqrt(-(0.66667*B)/C + (0.26457*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3))/(C*r0) + (0.41997*(r0*B**2 - 12*C*r + 300*A*C*r0 + 12*C*r0))/(C*(2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2 + sqrt((2*B**3*r0**3 + 27*A**2*C*r0**3 + 900*A*B*C*r0**3 + 270000*C**2*(r0 - r)*r0**2 - 72*B*C*(r0 - r)*r0**2)**2 - 4*(B**2*r0**2 + 300*A*C*r0**2 + 12*C*(r0 - r)*r0)**3))**(1/3)) + 2500) + 5000) + 25

        print(t)
    else:
        print('t>=0')
        pass

    self.pt100TempOut.setText(str(t))



