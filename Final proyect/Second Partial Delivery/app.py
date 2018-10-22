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

Builder.load_file("numericalmethods.kv")

class MainMenu(Screen):
    pass

class BracketMethods(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(BracketMethods, self).__init__(**kwargs)

        basebox = BoxLayout(orientation='vertical')
        inputs = BoxLayout(orientation='horizontal', size_hint=(1, .3))
        options = BoxLayout(orientation='horizontal', size_hint=(1, .3))
        results = BoxLayout(orientation='vertical')

        self.formulaTxtInput = TextInput(hint_text='formula with unknown variable x')
        self.xlowTxtInput = TextInput(hint_text='xlow')
        self.xuppTxtInput = TextInput(hint_text='xupper')
        self.tolTxtInput = TextInput(hint_text='tolerance')
        self.iterationsTxtInput = TextInput(hint_text='max iterations')

        runBtn = Button(text='RUN')
        runBtn.bind(on_release=self.run)
        backBtn = Button(text='BACK')
        backBtn.bind(on_release=self.backToMenu)
        self.bisectionResultsLabel = Label(text='')
        self.falsePositionResultsLabel = Label(text='')

        inputs.add_widget(self.formulaTxtInput)
        inputs.add_widget(self.xlowTxtInput)
        inputs.add_widget(self.xuppTxtInput)
        inputs.add_widget(self.tolTxtInput)
        inputs.add_widget(self.iterationsTxtInput)

        options.add_widget(runBtn)
        options.add_widget(backBtn)

        results.add_widget(self.bisectionResultsLabel)
        results.add_widget(self.falsePositionResultsLabel)

        basebox.add_widget(inputs)
        basebox.add_widget(options)
        basebox.add_widget(results)

        self.add_widget(basebox)

    def backToMenu(self, obj):
        self.screenManager.current = 'menu'

    def f(self, x):
        return eval(self.formula)

    def bisection(self, xlow, xupper, tolerance, imax):
        aproxRelativeError = 99999999
        iterations = 0
        xres = (xlow + xupper) / 2.0
        testing = self.f(xlow) * self.f(xres)
        if testing < 0:
            xupper = xres
        if testing > 0:
            xlow = xres
        elif testing == 0:
            aproxRelativeError = 0
        while (aproxRelativeError > tolerance and iterations < imax):
            xresOld = xres
            testing = self.f(xlow) * self.f(xres)
            if testing < 0:
                xupper = xres
            elif testing > 0:
                xlow = xres
            elif testing == 0:
                aproxRelativeError = 0
            xres = (xlow + xupper) / 2.0
            if xres != 0:
                aproxRelativeError = abs((xres - xresOld) / xres) * 100
            iterations += 1
        return "Bisection Method = " + str(iterations) + " iterations. Result: " + str(xres) + " %" + str(aproxRelativeError) + " aproximate percent relative error"

    def false_position(self, xlow, xupper, tolerance, imax):
        aproxRelativeError = 99999999
        iterations = 0
        xres = xupper - ((self.f(xupper) * (xlow - xupper)) / (self.f(xlow) - self.f(xupper)))
        testing = self.f(xlow) * self.f(xres)
        if testing < 0:
            xupper = xres
        if testing > 0:
            xlow = xres
        elif testing == 0:
            aproxRelativeError = 0
        while (aproxRelativeError > tolerance and iterations < imax):
            xresOld = xres
            testing = self.f(xlow) * self.f(xres)
            if testing < 0:
                xupper = xres
            elif testing > 0:
                xlow = xres
            elif testing == 0:
                aproxRelativeError = 0
            xres = xupper - ((self.f(xupper) * (xlow - xupper)) / (self.f(xlow) - self.f(xupper)))
            if xres != 0:
                aproxRelativeError = abs((xres - xresOld) / xres) * 100
            iterations += 1
        return "False Position Method = " + str(iterations) + " iterations. Result: " + str(xres) + " %" + str(aproxRelativeError) + " aproximate percent relative error"

    def run(self, obj):
        self.formula = self.formulaTxtInput.text
        xlow = float(self.xlowTxtInput.text)
        xupper = float(self.xuppTxtInput.text)
        tolerance = float(self.tolTxtInput.text)
        maxIterations = int(self.iterationsTxtInput.text)
        self.bisectionResultsLabel.text = self.bisection(xlow, xupper, tolerance, maxIterations)
        self.falsePositionResultsLabel.text = self.false_position(xlow, xupper, tolerance, maxIterations)

class OpenMethods(Screen):

    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(OpenMethods, self).__init__(**kwargs)
        basebox = BoxLayout(orientation='vertical')
        inputs = BoxLayout(orientation='horizontal')
        secantInputs = BoxLayout(orientation='horizontal')
        options = BoxLayout(orientation='horizontal')
        results = BoxLayout(orientation='vertical')

        self.formulaTxtInput = TextInput(hint_text='formula with unknown variable x')
        self.derivativeTxtInput = TextInput(hint_text='derivative (for Newton Raphson Method)')
        self.x0TxtInput = TextInput(hint_text='x0')
        self.differenceTxtInput = TextInput(hint_text='difference: 0.5 or 1 (for Secant Method)')
        self.tolTxtInput = TextInput(hint_text='tolerance')
        self.iterationsTxtInput = TextInput(hint_text='max iterations')

        runBtn = Button(text='run')
        runBtn.bind(on_release=self.run)
        backBtn = Button(text='Back to Menu')
        backBtn.bind(on_release=self.backToMenu)
        self.newtonRaphsonResultsLabel = Label(text='')
        self.secantResultsLabel = Label(text='')

        inputs.add_widget(self.formulaTxtInput)
        inputs.add_widget(self.derivativeTxtInput)
        inputs.add_widget(self.x0TxtInput)
        inputs.add_widget(self.differenceTxtInput)
        inputs.add_widget(self.tolTxtInput)
        inputs.add_widget(self.iterationsTxtInput)

        options.add_widget(runBtn)
        options.add_widget(backBtn)

        results.add_widget(self.newtonRaphsonResultsLabel)
        results.add_widget(self.secantResultsLabel)

        basebox.add_widget(inputs)
        basebox.add_widget(options)
        basebox.add_widget(results)

        self.add_widget(basebox)

    def backToMenu(self, obj):
        self.screenManager.current = 'menu'

    def run(self, obj):
        self.formula = self.formulaTxtInput.text
        self.derivative = self.derivativeTxtInput.text
        x0 = float(self.x0TxtInput.text)
        difference = float(self.differenceTxtInput.text)
        tolerance = float(self.tolTxtInput.text)
        maxIterations = int(self.iterationsTxtInput.text)
        self.newtonRaphsonResultsLabel.text = self.newtonRaphson(x0, tolerance, maxIterations)
        self.secantResultsLabel.text = self.altSecant(x0, difference, tolerance, maxIterations)

    def f(self, x):
        return eval(self.formula)

    def Df(self, x):
        return eval(self.derivative)

    def newtonRaphson(self, x0, tolerance, maxIterations):
        i = 1
        error = 100  # Start with 100% error
        while error > tolerance:
            if i == maxIterations:
                break
            x1 = x0 - self.f(x0) / self.Df(x0)
            error = abs(x1 - x0) * 100
            x0 = x1
            i = i + 1
        return "Result: " + str(x0) + " Iteration: " + str(i) + " aproximate percent relative error: " + str(error)

    def altSecant(self, x, diff, tol, maxAttempts):
        iteration = 1
        rError = 100  # Start with 100% error
        while rError >= tol:
            if iteration == maxAttempts:
                break
            xI = x - (diff * x * self.f(x)) / (self.f(x + (diff * x)) - self.f(x))
            rError = abs((xI - x) / xI) * 100
            x = xI
            iteration += 1
        return "Result: " + str(xI) + " Iteration: " + str(iteration) + "aproximate percent relative error: " + str(rError)


class SystemOfEquations(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(SystemOfEquations, self).__init__(**kwargs)

        self.basebox = BoxLayout(orientation='vertical')
        self.sizeInputs = BoxLayout(orientation='horizontal', size_hint=(1, .06))
        self.options = BoxLayout(orientation='horizontal', size_hint=(1, .06))
        self.matrixLabels = BoxLayout(orientation='horizontal', size_hint=(1, .06))
        self.matrixInputs = BoxLayout(orientation='horizontal', size_hint=(1, .45))
        self.variableInputs = BoxLayout(orientation='horizontal')
        self.answerInputs = BoxLayout(orientation='horizontal')
        self.seidelExtraOptions = BoxLayout(orientation='horizontal', size_hint=(1, .06))
        self.resultsString = BoxLayout(orientation='vertical', size_hint=(1, .31))

        matrixSizeLabel = Label(text='Number of Equations')
        self.numEquationsTxtInput = TextInput(hint_text="Number of equations")
        okBtn = Button(text='OK')
        okBtn.bind(on_release=self.onClickOK)

        backBtn = Button(text='Back to Menu')
        backBtn.bind(on_release=self.backToMenu)

        self.finalResultsLabel = Label()

        self.sizeInputs.add_widget(matrixSizeLabel)
        self.sizeInputs.add_widget(self.numEquationsTxtInput)
        self.sizeInputs.add_widget(okBtn)

        self.options.add_widget(backBtn)

        self.resultsString.add_widget(self.finalResultsLabel)

        self.basebox.add_widget(self.sizeInputs)
        self.basebox.add_widget(self.options)
        self.basebox.add_widget(self.seidelExtraOptions)
        self.basebox.add_widget(self.matrixLabels)
        self.basebox.add_widget(self.matrixInputs)
        self.basebox.add_widget(self.resultsString)

        self.add_widget(self.basebox)

    def onClickOK(self, obj):
        # get size of matrix
        self.numEquations = int(self.numEquationsTxtInput.text)

        # initialize member square matrix
        self.squareMatrix = np.zeros([self.numEquations, self.numEquations])
        self.variables = []
        self.results = np.zeros(self.numEquations)

        # clear child widgets that may repeat
        self.options.clear_widgets()
        self.matrixInputs.clear_widgets()
        self.matrixLabels.clear_widgets()
        # add buttons to options
        backBtn = Button(text='Back to Menu')
        backBtn.bind(on_release=self.backToMenu)
        gaussElimBtn = Button(text='Gauss Elimination')
        gaussElimBtn.bind(on_release=self.gauss)
        LUDecompositionBtn = Button(text='LU Decomposition')
        LUDecompositionBtn.bind(on_release=self.LUDecomposition)
        gaussSeidelBtn = Button(text='Gauss Seidel')
        gaussSeidelBtn.bind(on_release=self.gaussSeidel)

        self.options.add_widget(backBtn)
        self.options.add_widget(gaussElimBtn)
        self.options.add_widget(LUDecompositionBtn)
        self.options.add_widget(gaussSeidelBtn)

        # add labels
        matrixLabels = BoxLayout(orientation="horizontal")
        squareMatrixLabel = Label(text='Square Matrix')
        varLabel = Label(text='Variables', size_hint=(.3, 1))
        resultsLabel = Label(text='Results', size_hint=(.3, 1))
        self.matrixLabels.add_widget(squareMatrixLabel)
        self.matrixLabels.add_widget(varLabel)
        self.matrixLabels.add_widget(resultsLabel)

        # add square matrix inputs
        self.squareMatrixInputs = BoxLayout(orientation='vertical')
        self.matrixGrid = GridLayout(rows=self.numEquations, cols=self.numEquations)
        for i in range(self.numEquations):
            for j in range(self.numEquations):
                self.matrixGrid.add_widget(TextInput(hint_text="(" + str(i) + "," + str(j) + ")"))
        self.squareMatrixInputs.add_widget(self.matrixGrid)

        # add variable name inputs
        self.varInputs = BoxLayout(orientation='vertical', size_hint=(.3, 1))
        for i in range(self.numEquations):
            self.varInputs.add_widget(TextInput(hint_text="v" + str(i)))
        # add result inputs
        self.resultsInputs = BoxLayout(orientation='vertical', size_hint=(.3, 1))
        for i in range(self.numEquations):
            self.resultsInputs.add_widget(TextInput(hint_text="r" + str(i)))

        seidelExtraOptionsLabel = Label(text='Gauss Seidel Options')
        self.toleranceTxtInput = TextInput(hint_text='tolerance')
        self.iterationsTxtInput = TextInput(hint_text='iterations')
        self.seidelExtraOptions.add_widget(seidelExtraOptionsLabel)
        self.seidelExtraOptions.add_widget(self.toleranceTxtInput)
        self.seidelExtraOptions.add_widget(self.iterationsTxtInput)

        # add widgets
        self.matrixInputs.add_widget(self.squareMatrixInputs)
        self.matrixInputs.add_widget(self.varInputs)
        self.matrixInputs.add_widget(self.resultsInputs)

    def receiveTextInputValues(self):
        values = []
        for child in self.matrixGrid.children:
            values = [float(child.text)] + values
        valIndex = 0
        for i in range(self.numEquations):
            for j in range(self.numEquations):
                self.squareMatrix[i][j] = values[valIndex]
                valIndex += 1
        for child in self.varInputs.children:
            self.variables = [child.text] + self.variables
        results = []
        for child in self.resultsInputs.children:
            results = [float(child.text)] + results
        for i in range(self.numEquations):
            self.results[i] = results[i]
        print(type(self.toleranceTxtInput.text))
        if self.toleranceTxtInput.text and self.iterationsTxtInput.text:
            self.tolerance = float(self.toleranceTxtInput.text)
            self.iterations = int(self.iterationsTxtInput.text)

    def gauss(self, obj):
        self.receiveTextInputValues()
        x = np.zeros(self.numEquations)
        for k in range (0,self.numEquations):
            for r in range (k+1,self.numEquations):
                factor = (self.squareMatrix[r,k]/self.squareMatrix[k,k])
                self.results[r]=self.results[r]-(factor*self.results[k])
                for c in range (0,self.numEquations):
                    self.squareMatrix[r,c]=self.squareMatrix[r,c]-(factor*self.squareMatrix[k,c])

        #Sustitucion en reversa

        x[self.numEquations-1]=self.results[self.numEquations-1]/self.squareMatrix[self.numEquations-1,self.numEquations-1]
        print (x[self.numEquations-1])

        for r in range (self.numEquations-2,-1,-1):
            suma = 0
            for c in range (0,self.numEquations):
                suma = suma + self.squareMatrix[r,c]*x[c]
            x[r]=(self.results[r]-suma)/self.squareMatrix[r,r]

        resFinal = "Matriz Resultante:\n"
        # resFinal = ( self.squareMatrix ,  self.results ,  x)

        for i in self.squareMatrix:
            for j in i:
                resFinal+=str(j)+" "
            resFinal+="\n"
        resFinal+="\nResultados de matriz:\n"
        for i in self.results:
            resFinal+=str(i)+" "
        resFinal+="\n"
        resFinal+="\nResultados:\n"
        for i in x:
            resFinal+=str(i)+" "
        resFinal+="\n"
        self.finalResultsLabel.text = resFinal

    def LUDecomposition(self, obj):
        self.receiveTextInputValues()

    def gaussSeidel(self, obj):
        self.receiveTextInputValues()
        self.tolerance = float(self.toleranceTxtInput.text)
        self.iterations = int(self.iterationsTxtInput.text)
        print("Your equations must be diagonally greater than 0 and heavy.")
        print("Otherwise convergence won't occur.")
        x = np.zeros(self.numEquations)  # vector that holds each x reflection once it is completely calculated
        error = np.zeros((self.numEquations, 2))  # matrix to store x error for past iterations
        i = 0
        while i < self.iterations:
            tError = 0
            i += 1
            for row in range(0, self.numEquations):
                clearForXRes = 0
                for col in range(0, self.numEquations):
                    if col != row:  # this if st. prevents the denominator coef. of the current row to be subtracting from o
                                    # its own reflection
                        clearForXRes += self.squareMatrix[row, col] * x[col]  # the other coefs. are added to the reflection
                x[row] = (self.results[row] - clearForXRes) / self.squareMatrix[row, row]
                # when clearForXRes contains every other coef. it is divided by the current coef. number equal to the row num
                # Error calculation starts
                error[row, 1] = x[row]
                err = (abs(((error[row, 1] - error[row, 0]) / error[row, 1]) * 100))
                print("Error x" + str(row + 1) + ":" + str(err))
                error[row, 0] = error[row, 1]
                tError += err
                if tError < self.tolerance and row == self.numEquations - 1:
                    break
            else:
                # print("The total error for iteration " + str(i) + " is :" + str(tError))
                # print("\n")
                continue
            # print("The total error for iteration " + str(i) + " is :" + str(tError))
            # print("\n")
            break
        if self.tolerance < tError:
            print("The number of max iterations was reached but the tolerance wasn't met. ")

        resFinal = ""
        for row in range(0, self.numEquations):
            resFinal += ("x" + str(row + 1) + " " + str(x[row]))
            resFinal += " "

        resFinal += ("# iterations : " + str(i) + " error: " + str(tError))
        self.finalResultsLabel.text = resFinal

    def backToMenu(self, obj):
        self.screenManager.current = 'menu'

class Interpolation(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(Interpolation, self).__init__(**kwargs)
        self.basebox = BoxLayout(orientation='vertical')
        self.numPointsInputs = BoxLayout(orientation='horizontal')
        self.xPointsInputs = BoxLayout(orientation='horizontal')
        self.yPointsInputs = BoxLayout(orientation='horizontal')
        self.options = BoxLayout(orientation='horizontal')
        self.evalAt = BoxLayout(orientation='horizontal')

        self.numPointsLabel = Label(text='Number of Points')
        self.numPointsTxtInput = TextInput(hint_text='Number of points')
        okBtn = Button(text='OK')
        okBtn.bind(on_release=self.onClickOK)

        self.numPointsInputs.add_widget(self.numPointsLabel)
        self.numPointsInputs.add_widget(self.numPointsTxtInput)
        self.numPointsInputs.add_widget(okBtn)
        self.basebox.add_widget(self.numPointsInputs)
        self.basebox.add_widget(self.options)
        self.basebox.add_widget(self.evalAt)
        self.basebox.add_widget(self.xPointsInputs)
        self.basebox.add_widget(self.yPointsInputs)
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
        lagrangeBtn = Button(text='Lagrange')
        lagrangeBtn.bind(on_release=self.lagrange)
        dividedDifferencesBtn = Button(text='Divided Differences')
        dividedDifferencesBtn.bind(on_release=self.dividedDifferences)
        powerSeriesBtn = Button(text='Power Series')
        powerSeriesBtn.bind(on_release=self.powerSeries)

        self.options.add_widget(backBtn)
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
            self.xPoints = [child.text] + self.xPoints
        print(self.xPoints)
        self.yPoints = []
        for child in self.yPointsInputs.children:
            self.yPoints = [child.text] + self.yPoints
        print(self.yPoints)

    def lagrange(self, obj):
        self.getInputData()
        print('lagrange')

    def dividedDifferences(self, obj):
        self.getInputData()
        print('dividedDifferences')

    def powerSeries(self, obj):
        self.getInputData()
        print('powerSeries')


class NumericalMethodsApp(App):
    def build(self):
        root = ScreenManager()
        root.transition = SwapTransition()
        root.add_widget(MainMenu())
        root.add_widget(BracketMethods(screenManager=root, name='bracket_methods'))
        root.add_widget(OpenMethods(screenManager=root, name='open_methods'))
        root.add_widget(SystemOfEquations(screenManager=root, name='system_equations'))
        root.add_widget(Interpolation(screenManager=root, name='interpolation'))

        return root


if __name__ == '__main__':
    NumericalMethodsApp().run()
