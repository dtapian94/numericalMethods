import sys
import numpy as np
from math import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

class Regression(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(Regression, self).__init__(**kwargs)
        self.basebox = BoxLayout(orientation='vertical')
        self.numPointsInputs = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.xPointsInputs = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.yPointsInputs = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.options = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.results = BoxLayout(orientation='vertical', size_hint=(1, 0.7))

        self.numPointsLabel = Label(text='Number of Points')
        self.numPointsTxtInput = TextInput(hint_text='Number of points')
        okBtn = Button(text='OK')
        okBtn.bind(on_release=self.onClickOK)
        self.resultsLabel = Label(text='')

        self.numPointsInputs.add_widget(self.numPointsLabel)
        self.numPointsInputs.add_widget(self.numPointsTxtInput)
        self.numPointsInputs.add_widget(okBtn)
        self.results.add_widget(self.resultsLabel)
        self.basebox.add_widget(self.numPointsInputs)
        self.basebox.add_widget(self.options)
        self.basebox.add_widget(self.xPointsInputs)
        self.basebox.add_widget(self.yPointsInputs)
        self.basebox.add_widget(self.results)
        self.add_widget(self.basebox)

    def onClickOK(self, obj):
        # clear child widgets that may repeat
        self.options.clear_widgets()
        self.xPointsInputs.clear_widgets()
        self.yPointsInputs.clear_widgets()

        self.numPoints = int(self.numPointsTxtInput.text)
        for i in range(self.numPoints):
            self.xPointsInputs.add_widget(TextInput(hint_text="x" + str(i)))
            self.yPointsInputs.add_widget(TextInput(hint_text="y" + str(i)))

        # add buttons to options
        backBtn = Button(text='Back to Menu')
        backBtn.bind(on_release=self.backToMenu)
        linearBtn = Button(text='Linear')
        linearBtn.bind(on_release=self.linear)
        polynomialBtn = Button(text='Polynomial')
        polynomialBtn.bind(on_release=self.polynomial)
        exponentialBtn = Button(text='Exponential')
        exponentialBtn.bind(on_release=self.exponential)
        logarithmicBtn = Button(text='Logarithmic')
        logarithmicBtn.bind(on_release=self.logarithmic)

        self.options.add_widget(backBtn)
        self.options.add_widget(linearBtn)
        self.options.add_widget(polynomialBtn)
        self.options.add_widget(exponentialBtn)
        self.options.add_widget(logarithmicBtn)

    def backToMenu(self, obj):
        self.screenManager.current = 'menu'

    def getInputData(self):
        self.xPoints = []
        for child in self.xPointsInputs.children:
            self.xPoints = [float(child.text)] + self.xPoints
        print(self.xPoints)
        self.yPoints = []
        for child in self.yPointsInputs.children:
            self.yPoints = [float(child.text)] + self.yPoints
        print(self.yPoints)

    def linear(self, obj):
        self.getInputData()
        xy = []
        x2 = []
        sumX = 0
        sumY = 0
        sumXY = 0
        sumX2 = 0
        for i in range(self.numPoints):
            sumX += self.xPoints[i]
            sumY += self.yPoints[i]
            xy.append(self.xPoints[i] * self.yPoints[i])
            sumXY += xy[i]
            x2.append(self.xPoints[i] * self.xPoints[i])
            sumX2 += x2[i]

        # Calculation starts
        a1 = ((self.numPoints * sumXY) - (sumX * sumY)) / ((self.numPoints * sumX2) - np.power(sumX, 2))
        a0 = (sumY / self.numPoints) - a1 * (sumX / self.numPoints)

        print("R1 = " + str(a0) + " + " + str(a1) + " X")
        self.resultsLabel.text = "R1 = " + str(a0) + " + " + str(a1) + " X"
        print('linear')

    def polynomial(self, obj):
        self.getInputData()
        numPoints = self.numPoints
        x = self.xPoints
        y = self.yPoints
        xy = []
        x2 = []
        x3 = []
        x4 = []
        x5 = []
        x6 = []
        x7 = []
        x8 = []
        x2y = []
        x3y = []
        x4y = []

        sumX = 0
        sumY = 0
        sumXY = 0
        sumX2 = 0
        sumX3 = 0
        sumX4 = 0
        sumX5 = 0
        sumX6 = 0
        sumX7 = 0
        sumX8 = 0
        sumX2Y = 0
        sumX3Y = 0
        sumX4Y = 0

        for i in range(numPoints):
            sumX += x[i]
            sumY += y[i]
            xy.append(x[i] * y[i])
            sumXY += xy[i]
            x2.append(x[i] * x[i])
            sumX2 += x2[i]
            x3.append(np.power(x[i], 3))
            sumX3 += x3[i]
            x4.append(np.power(x[i], 4))
            sumX4 += x4[i]
            x5.append(np.power(x[i], 5))
            sumX5 += x5[i]
            x6.append(np.power(x[i], 6))
            sumX6 += x6[i]
            x7.append(np.power(x[i], 7))
            sumX7 += x7[i]
            x8.append(np.power(x[i], 8))
            sumX8 += x8[i]
            x2y.append(x2[i] * y[i])
            sumX2Y += x2y[i]
            x3y.append(x3[i] * y[i])
            sumX3Y += x3y[i]
            x4y.append(x4[i] * y[i])
            sumX4Y += x4y[i]

        # QUADRATIC
        # matrix of coefficients
        matrix = np.zeros((3, 3))
        vector = np.zeros(3)

        matrix[0, 0] = numPoints
        matrix[0, 1] = sumX
        matrix[0, 2] = sumX2

        for r in range(1, 3):
            for c in range(0, 2):
                matrix[r, c] = matrix[r - 1, c + 1]

        matrix[1, 2] = sumX3
        matrix[2, 2] = sumX4
        matrix[2, 1] = matrix[1, 2]

        vector[0] = sumY
        vector[1] = sumXY
        vector[2] = sumX2Y

        # inverse matrix multiplication
        inverse = np.linalg.inv(matrix)
        self.v2 = np.zeros(3)
        self.v2 = np.matmul(inverse, vector)

        # Calculation of error begins
        e2 = 0
        st = 0
        for i in range(numPoints):
            e2 += np.power(y[i] - self.quadFunc(x[i]), 2)
            st += np.power((y[i] - sumY / numPoints), 2)

        r2 = (st - e2) / st
        r = np.power(r2, 1 / 2)

        result = ''
        result += "Cuadratic\nf(x)= " + str(self.v2[0]) + " + " + str(self.v2[1]) + "x  + " + str(self.v2[2]) + "x2 "
        result += "f(x)= " + str(self.v2[0]) + " + " + str(self.v2[1]) + "x  + " + str(self.v2[2]) + "x2 \n"
        result += "r2 = " + str(r2) + '   '
        result += "r = " + str(r) + '\n'

        #       CUBIC
        # matrix of coefficients
        matrix2 = np.zeros((4, 4))
        vector2 = np.zeros(4)
        matrix2[0, 0] = numPoints
        matrix2[0, 1] = sumX
        matrix2[0, 2] = sumX2
        matrix2[0, 3] = sumX3

        for c in range(0, 3):
            matrix2[1, c] = matrix2[0, c + 1]

        matrix2[1, 3] = sumX4

        for c in range(0, 3):
            matrix2[2, c] = matrix2[1, c + 1]

        matrix2[2, 3] = sumX5

        for c in range(0, 3):
            matrix2[3, c] = matrix2[2, c + 1]

        matrix2[3, 3] = sumX6

        vector2[0] = sumY
        vector2[1] = sumXY
        vector2[2] = sumX2Y
        vector2[3] = sumX3Y

        # inverse matrix multiplication
        inverse2 = np.linalg.inv(matrix2)
        self.v2 = np.zeros(4)
        self.v2 = np.matmul(inverse2, vector2)

        # Calculation of error begins
        e2 = 0
        st = 0
        for i in range(numPoints):
            e2 += np.power(y[i] - self.cubFunc(x[i]), 2)
            st += np.power((y[i] - sumY / numPoints), 2)

        r2 = (st - e2) / st
        r = np.power(r2, 1 / 2)

        result += "Cubic:\nf(x)= " + str(self.v2[0]) + " + " + str(self.v2[1]) + "x  + " + str(self.v2[2]) + "x2 + " + str(self.v2[3]) + "x3 \n"
        result += "r2 = " + str(r2) + '    '
        result += "r = " + str(r) + '\n'

        #       QUARTIC
        # matrix of coefficients
        matrix3 = np.zeros((5, 5))
        vector2 = np.zeros(5)
        matrix3[0, 0] = numPoints
        matrix3[0, 1] = sumX
        matrix3[0, 2] = sumX2
        matrix3[0, 3] = sumX3
        matrix3[0, 4] = sumX4

        for c in range(0, 4):
            matrix3[1, c] = matrix3[0, c + 1]

        matrix3[1, 4] = sumX5

        for c in range(0, 4):
            matrix3[2, c] = matrix3[1, c + 1]

        matrix3[2, 4] = sumX6

        for c in range(0, 4):
            matrix3[3, c] = matrix3[2, c + 1]

        matrix3[3, 4] = sumX7

        for c in range(0, 4):
            matrix3[4, c] = matrix3[3, c + 1]

        matrix3[4, 4] = sumX8

        print(matrix3)
        vector2[0] = sumY
        vector2[1] = sumXY
        vector2[2] = sumX2Y
        vector2[3] = sumX3Y
        vector2[4] = sumX4Y

        # inverse matrix multiplication
        inverse2 = np.linalg.inv(matrix3)
        self.v2 = np.zeros(5)
        self.v2 = np.matmul(inverse2, vector2)

        # Calculation of error begins
        e2 = 0
        st = 0
        for i in range(numPoints):
            e2 += np.power(y[i] - self.quartFunc(x[i]), 2)
            st += np.power((y[i] - sumY / numPoints), 2)

        r2 = (st - e2) / st
        r = np.power(r2, 1 / 2)

        result += "Cuartic:\nf(x)= " + str(self.v2[0]) + " + " + str(self.v2[1]) + "x  + " + str(self.v2[2]) + "x2 + " + str(self.v2[3]) + "x3 +" + str(self.v2[4]) + "x4" + '\n'
        result += "r2 = " + str(r2) + '    '
        result += "r = " + str(r) + '\n'
        self.resultsLabel.text = result
        print('polynomial')

    def quadFunc(self, x):
        result = self.v2[0] + self.v2[1] * x + (self.v2[2] * np.power(x, 2))
        return result

    def cubFunc(self, x):
        result = self.v2[0] + self.v2[1] * x + (self.v2[2] * np.power(x, 2)) + (self.v2[3] * np.power(x, 3))
        return result

    def quartFunc(self, x):
        result = self.v2[0] + self.v2[1] * x + (self.v2[2] * np.power(x, 2)) + (self.v2[3] * np.power(x, 3)) + (self.v2[4] * np.power(x, 4))
        return result

    def exponential(self, obj):
        self.getInputData()
        print("Exponential Regression Method")

        numPoints = self.numPoints

        x = self.xPoints
        y = self.yPoints
        lny = []
        xlny = []
        x2 = []

        sumX = 0
        sumY = 0
        sumXlnY = 0
        sumlnY = 0
        sumX2 = 0

        for i in range(numPoints):
            sumX += x[i]
            sumY += y[i]

            lny.append(m.log(y[i]))
            sumlnY += lny[i]

            xlny.append(x[i] * lny[i])
            sumXlnY += xlny[i]

            x2.append(x[i] * x[i])
            sumX2 += x2[i]

        # Calculation of the linear formula begins
        a1 = ((numPoints * sumXlnY) - (sumlnY * sumX)) / ((numPoints * sumX2) - np.power(sumX, 2))
        a0 = (sumlnY / numPoints) - a1 * (sumX / numPoints)

        # Calculation of error begins
        e2 = 0
        st = 0
        for i in range(numPoints):
            e2 += np.power(lny[i] - self.linearFunc(x[i]), 2)
            st += np.power((lny[i] - sumlnY / numPoints), 2)

        r2 = (st - e2) / st
        r = np.power(r2, 1 / 2)

        normA0 = m.exp(a0)
        result = ''
        result += "f(x) = " + str(a0) + " + " + str(a1) + "x\n"
        result += "r2 = " + str(r2) + '    '
        result += "r = " + str(r) + '\n'
        result += "Real equation: " + str(normA0) + "exp(" + str(a1) + "x)"
        print('exponential')

    def linearFunc(self, x):
        result = a0 + a1 * x
        return result

    def logarithmic(self, obj):
        self.getInputData()

        print('logarithmic')
