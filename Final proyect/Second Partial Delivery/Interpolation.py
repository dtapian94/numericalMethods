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
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

class Interpolation(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(Interpolation, self).__init__(**kwargs)
        self.basebox = BoxLayout(orientation='vertical')
        self.numPointsInputs = BoxLayout(orientation='horizontal', size_hint=(1, 0.12))
        self.xPointsInputs = BoxLayout(orientation='horizontal', size_hint=(1, 0.12))
        self.yPointsInputs = BoxLayout(orientation='horizontal', size_hint=(1, 0.12))
        self.options = BoxLayout(orientation='horizontal', size_hint=(1, 0.12))
        self.evalAt = BoxLayout(orientation='horizontal', size_hint=(1, 0.12))
        self.results = BoxLayout(orientation='vertical', size_hint=(1, 0.8))

        self.numPointsLabel = Label(text='To improve the result you should\n try to insert more points')
        self.numPointsTxtInput = TextInput(hint_text='Number of points')
        okBtn = Button(text='OK')
        okBtn.bind(on_release=self.onClickOK)

        self.resultsLabel = Label(text='')

        self.backBtn = Button(text='Back to Menu')
        self.backBtn.bind(on_release=self.backToMenu)
        self.options.add_widget(self.backBtn)

        self.numPointsInputs.add_widget(self.numPointsLabel)
        self.numPointsInputs.add_widget(self.numPointsTxtInput)
        self.numPointsInputs.add_widget(okBtn)

        self.results.add_widget(self.resultsLabel)
        self.basebox.add_widget(self.numPointsInputs)
        self.basebox.add_widget(self.options)
        self.basebox.add_widget(self.evalAt)
        self.basebox.add_widget(self.xPointsInputs)
        self.basebox.add_widget(self.yPointsInputs)
        self.basebox.add_widget(self.results)
        self.add_widget(self.basebox)

    def onClickOK(self, obj):
        # clear child widgets that may repeat
        self.options.clear_widgets()
        self.xPointsInputs.clear_widgets()
        self.yPointsInputs.clear_widgets()
        self.evalAt.clear_widgets()

        self.numPoints = int(self.numPointsTxtInput.text)
        for i in range(self.numPoints):
            self.xPointsInputs.add_widget(TextInput(hint_text="x" + str(i)))
            self.yPointsInputs.add_widget(TextInput(hint_text="y" + str(i)))

        # add buttons to options
        lagrangeBtn = Button(text='Lagrange')
        lagrangeBtn.bind(on_release=self.lagrange)
        dividedDifferencesBtn = Button(text='Divided Differences')
        dividedDifferencesBtn.bind(on_release=self.dividedDifferences)
        powerSeriesBtn = Button(text='Power Series')
        powerSeriesBtn.bind(on_release=self.powerSeries)

        self.options.add_widget(self.backBtn)
        self.options.add_widget(lagrangeBtn)
        self.options.add_widget(dividedDifferencesBtn)
        self.options.add_widget(powerSeriesBtn)

        xToEvalLabel = Label(text='Evaluate at x: ')
        self.xToEvalTxtInput = TextInput(hint_text='X to Evaluate')
        self.evalAt.add_widget(xToEvalLabel)
        self.evalAt.add_widget(self.xToEvalTxtInput)

    def backToMenu(self, obj):
        self.screenManager.current = 'menu'

    def getInputData(self):
        self.xToEval = float(self.xToEvalTxtInput.text)
        self.xPoints = []
        for child in self.xPointsInputs.children:
            self.xPoints = [float(child.text)] + self.xPoints
        print(self.xPoints)
        self.yPoints = []
        for child in self.yPointsInputs.children:
            self.yPoints = [float(child.text)] + self.yPoints
        print(self.yPoints)
        self.degree = self.numPoints - 1

    def lagrange(self, obj):
        self.getInputData()
        n = self.numPoints
        deg = self.degree
        x = self.xToEval
        # Points selection process
        sumC = [None] * (n - deg)
        for j in range(0, n - deg):
            sumC[j] = 0
            for k in range(j, (deg + 1 + j)):
                sumC[j] += self.xPoints[k]
            sumC[j] /= (deg + 1)

        lesser = abs(sumC[0] - x)
        m = 0
        for l in range(1, n - deg):
            if abs(sumC[l] - x) < lesser:
                lesser = abs(sumC[l] - x)
                m = l

        # Method begins
        result = 0
        result = float(result)
        returnVal = ""
        for i in range(m, n):
            pie = 1
            for j in range(m, n):
                if i != j:  # this if st. prevents the current x to be subtracted by itself in the denominator
                    pie *= (x - self.xPoints[j]) / float(self.xPoints[i] - self.xPoints[j])  # This var represents the iterative product notation letter "pi"
            pie *= self.yPoints[i]
            result += pie
            print(result)
            returnVal += ("LF" + str(i - m) + ":" + str(result))
            returnVal += " "
        returnVal += ("X: " + str(x) + "\nf(" + str(x) + "): " + str(result))
        print('The value at x = ' + str(x) + " is " + str(result))
        self.resultsLabel.text = returnVal
        return returnVal
        print('lagrange')

    def dividedDifferences(self, obj):
        self.getInputData()
        accum = None
        temp = None
        k = 0
        f = None
        n = self.numPoints
        result = ""
        self.matrix = np.zeros((self.numPoints, 10))
        for i in range(n):
            self.matrix[0][i] = self.yPoints[i]
        for i in range(1, n):
            k = i
            for j in range(0, n - i):
                self.matrix[i][j] = (self.matrix[i - 1][j + 1] - self.matrix[i - 1][j]) / (self.xPoints[k] - self.xPoints[j])
                k += 1
        for i in range(0, n):
            result += "\n " + str(self.xPoints[i])
            for j in range(0, n - i):
                result += "    " + str(self.matrix[j][i])
            result += '\n'
        i = 0
        while(1):
            if self.xPoints[i] < self.xToEval and self.xToEval < self.xPoints[i + 1]:
                k = 1
            else:
                i += 1
            if k != 1:
                break
        f = i

        accum = 0
        for i in range(0, n - 1):
            k = f
            temp = 1
            for j in range(0, i):
                temp *= self.xToEval - self.xPoints[k]
                k += 1
            accum = accum + float(temp) * float(self.matrix[i][f])
        result += "\n\n f(" + str(self.xToEval) + ") = " + str(accum) + '\n'
        print(result)
        self.resultsLabel.text = result
        print('dividedDifferences')

    def powerSeries(self, obj):
        self.getInputData()
        self.matrix = np.zeros((self.numPoints, self.numPoints))
        for i in range(self.numPoints):
            self.matrix[i][0] = 1
        power = 1
        for i in range(self.numPoints):
            for j in range(1, self.numPoints):
                self.matrix[i][j] = pow(self.xPoints[i], power)
                power += 1
            power = 1

        inverse = np.linalg.inv(self.matrix)
        result = np.matmul(inverse, self.yPoints)
        result = "Resultant Matrix:" + str(self.matrix) + '\nResult:' + str(result) + '\n'
        self.resultsLabel.text = result
        print('powerSeries')
