# ---------------------------------------------------------------------------------
# #! CalcApp 2.0 - developed with Qt and Python                          2021-05-24
# ---------------------------------------------------------------------------------
# v0.0.1 alpha
# ---------------------------------------------------------------------------------
# File: main.py
# SubFile: calcAppUI_win.ui
# Description:  Swiss Army Knife for the PLC automation engineer in the field.
# Various calculations for PT100, sensor signals etc...
#
# https://www.programcreek.com/python/
#
# developed to fork!
# open source open mind!
# peace out!
#
# History:
# Date          Programmer              Description
# ----------    --------------------    -------------------------------------------
# 2021-05-27    tobias@haueter.one      - Created
# 2021-05-31    tobias@haueter.one      - implement Calc in extern script
#
# ---------------------------------------------------------------------------------

# Convert the resulting py file
import sys
from math import *
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton, QWidget, QLineEdit
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from calc import *
from UliEngineering.Physics.RTD import pt100_temperature, pt100_resistance

# Load the UI file
# https://www.programcreek.com/python/example/96001/PyQt5.uic.loadUi

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #uic.loadUi('calcAppUI_linux.ui', self) # Load the .ui file
        uic.loadUi('calcAppUI_win.ui', self) # Load the .ui file

        ### Pointing GUI Elements

        ## BIO SignalConverter

        # Signal Range Low Input
        sc01 = self.srLowInput01 = self.findChild(QtWidgets.QLineEdit, 'srLowInput') # Find the item
        sc01.setValidator(QDoubleValidator(-1000000, 1000000, 4)) # Input Validator

        # Signal Range High Input
        sc02 = self.srHighInput02 = self.findChild(QtWidgets.QLineEdit, 'srHighInput') # Find the item
        sc02.setValidator(QDoubleValidator(-1000000, 1000000, 4)) # Input Validator

        # Physical Range Low Input
        sc03 = self.prLowInput03 = self.findChild(QtWidgets.QLineEdit, 'prLowInput') # Find the item
        sc03.setValidator(QDoubleValidator(-1000000, 1000000, 4)) # Input Validator

        # Physical Range High Input
        sc04 = self.prHighInput04 = self.findChild(QtWidgets.QLineEdit, 'prHighInput') # Find the item
        sc04.setValidator(QDoubleValidator(-1000000, 1000000, 4)) # Input Validator

        # Calculation I/O SR -> PR
        # Signal Range to Physical Range Calculation Input
        sc05 = self.srToPrInput05 = self.findChild(QtWidgets.QLineEdit, 'srToPrCalcInput') # Find the item
        sc05.setValidator((QDoubleValidator(-1000000, 1000000, 4))) # Input Validator


        # Signal Range to Physical Range Calculation Output
        self.srToPrOutput06 = self.findChild(QtWidgets.QLabel, 'srToPrCalcOutput')  # Find the item

        # Calculation I/O PR -> SR
        # Physical Range to Signal Range Calculation Input
        sc06 = self.prToSrInput07 = self.findChild(QtWidgets.QLineEdit, 'prToSrCalcInput') # Find the item
        sc06.setValidator(QDoubleValidator(-1000000, 1000000, 4)) # Input Validator

        # Physical Range to Signal Range Calculation Output
        self.prToSrOutput08 = self.findChild(QtWidgets.QLabel, 'prToSrCalcOutput') # Find the item

        # Buttons
        self.BtnSP = self.findChild(QtWidgets.QPushButton, 'BtnSP')
        self.BtnSP.clicked.connect(self.calcSP) # QLineEdit returnPressed is assignet to click this button

        self.BtnPS = self.findChild(QtWidgets.QPushButton, 'BtnPS')
        self.BtnPS.clicked.connect(self.calcPS) # QLineEdit returnPressed is assignet to click this button


        ## BIO PT100

        # PT100 Temp In
        pt01 = self.pt100TempIn = self.findChild(QtWidgets.QLineEdit, 'pt100TempIn') # Find the item
        pt01.setValidator(QDoubleValidator(-280,1000,12)) # Input Validator

        # PT100 Temp Out
        self.pt100ResOut = self.findChild(QtWidgets.QLabel, 'pt100ResOut') # Find the item

        # PT100 Resistance In
        pt02 = self.pt100ResIn = self.findChild(QtWidgets.QLineEdit, 'pt100ResIn') # Find the item
        pt02.setValidator(QDoubleValidator(0,400,12)) # Input Validator


        # PT100 Resistance Out
        self.pt100TempOut = self.findChild(QtWidgets.QLabel, 'pt100TempOut') # Find the item

        # Buttons Temperature to Resistance
        self.BtnPt100_tempToRes = self.findChild(QtWidgets.QPushButton, 'BtnPt100_tempToRes')
        self.BtnPt100_tempToRes.clicked.connect(self.calcPt100TempToRes)  # QLineEdit returnPressed is assignet to click this button

        # Buttons Resistance to Temperature
        self.BtnPt100_resToTemp = self.findChild(QtWidgets.QPushButton, 'BtnPt100_resToTemp')
        self.BtnPt100_resToTemp.clicked.connect(self.calcPt100ResToTemp)  # QLineEdit returnPressed is assignet to click this button

        ## show MainWindows
        self.show()

        #-------------------------------------------------------------------------

        ## Var Storage; Calc/Conditioning Signal Converter
        self.srLowIn = 0
        self.srHighIn = 0
        self.prLowIn = 0
        self.prHighIn = 0
        self.srCalcIn = 0
        self.srCalcOut = 0
        self.prCalcIn = 0
        self.prCalcOut = 0

        ## Var Storage; Calc/Conditioning PT100
        self.pt100_rIN = 0
        self.pt100_tIN = 0


    def calcSP(self): # Button and returnPressed action
        #self.errorMsgInput()
        self.VarCondSignalConverter()
        # call extern script
        resultSP = calc_SP(self.srLowIn, self.srHighIn, self.prLowIn, self.prHighIn, self.srCalcIn, self.prCalcIn)
        self.srToPrOutput06.setText(f'{resultSP}')
        print(resultSP)
        print('calcSP => OK!')


    def calcPS(self): # Button and returnPressed action
        #self.errorMsgInput()
        self.VarCondSignalConverter()
        # call extern script
        resultPS = calc_PS(self.srLowIn, self.srHighIn, self.prLowIn, self.prHighIn, self.srCalcIn, self.prCalcIn)
        self.prToSrOutput08.setText((f'{resultPS}'))
        print(resultPS)
        print('calcPS => OK!')


    def calcPt100TempToRes(self):
        self.VarCondPt100()
        #self.errorMsgInput()
        # call extern script
        resistance = calcPt100_TempToRes(self.pt100_tIN)
        self.pt100ResOut.setText(f'{resistance}')
        #self.pt100ResOut.setText(str(calcPt100_TempToRes(self.pt100_tIN)))


    def calcPt100ResToTemp(self):
        self.VarCondPt100()
        #self.errorMsgInput()
        # call extern script
        temperature = calcPt100_ResToTemp(self.pt100_rIN)
        self.pt100TempOut.setText(f'{temperature}')
        #self.pt100TempOut.setText(str(calcPt100_ResToTemp(self.pt100_rIN)))


    def VarCondSignalConverter(self):
        self.srLowIn = float(self.srLowInput01.text())
        self.srHighIn = float(self.srHighInput02.text())
        self.prLowIn = float(self.prLowInput03.text())
        self.prHighIn = float(self.prHighInput04.text())
        self.srCalcIn = float(self.srToPrInput05.text())
        self.srCalcOut = float(0)
        self.prCalcIn = float(self.prToSrInput07.text())
        self.prCalcOut = float(0)
        print('VarCondSignalConverter => OK!')


    def VarCondPt100(self):
        self.pt100_tIN = float(self.pt100TempIn.text())
        self.pt100_rIN = float(self.pt100ResIn.text())


    def inputValitation(var):
        # QValidator
        # ReGex
        pass


    def errorMsgInput(self):
        ## Input Error Msg
        dlg = QMessageBox(self)
        dlg.setWindowIcon(QtGui.QIcon("warning.ico"))
        dlg.setStyleSheet("background-color: white; "
                          "color: black"
                          )
        dlg.setWindowTitle("Error Input")
        dlg.setText("Input is not valid")
        button = dlg.exec()
        if button == QMessageBox.Ok:
            print("OK!")


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application


