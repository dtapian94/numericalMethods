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

    def onClickLoad(self, obj):
        self.mat = np.loadtxt("matrix.txt")
        print(self.mat)
        for i in range(self.numEquations):
            for j in range(self.numEquations):
                self.squareMatrix[i][j] = self.mat[i][j]
        self.mat = self.mat[::-1]
        for i in range(len(self.mat)):
            print(self.mat[i])
            self.mat[i] = self.mat[i][::-1]
        print(self.matrixInputs.children)
        i=0
        j=0
        mult=1
        print(len(self.matrixGrid.children))
        #child.text = str(self.mat[i][j])
        for child in self.matrixGrid.children:
            child.text = str(self.mat[i][j])
            print(str(i)+' '+str(j))
            j+=1
            if mult % self.numEquations == 0:
                i+=1
                j=0
            mult+=1

        self.res = np.loadtxt("res.txt")
        print(self.res)
        self.res = self.res[::-1]
        k=0
        for child in self.resultsInputs.children:
            child.text = str(self.res[k])
            k+=1
        print("loading file")

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
        self.seidelExtraOptions.clear_widgets()

        # add buttons to options
        backBtn = Button(text='Back to Menu')
        backBtn.bind(on_release=self.backToMenu)
        gaussElimBtn = Button(text='Gauss Elimination')
        gaussElimBtn.bind(on_release=self.gauss)
        LUDecompositionBtn = Button(text='LU Decomposition')
        LUDecompositionBtn.bind(on_release=self.LUDecomposition)
        gaussSeidelBtn = Button(text='Gauss Seidel')
        gaussSeidelBtn.bind(on_release=self.gaussSeidel)
        loadFileBtn = Button(text='Load Matrix')
        loadFileBtn.bind(on_release=self.onClickLoad)

        self.options.add_widget(backBtn)
        self.options.add_widget(gaussElimBtn)
        self.options.add_widget(LUDecompositionBtn)
        self.options.add_widget(gaussSeidelBtn)
        self.options.add_widget(loadFileBtn)

        # add labels
        matrixLabels = BoxLayout(orientation="horizontal")
        squareMatrixLabel = Label(text='Square Matrix')
        # varLabel = Label(text='Variables', size_hint=(.3, 1))
        resultsLabel = Label(text='Results', size_hint=(.3, 1))
        self.matrixLabels.add_widget(squareMatrixLabel)
        # self.matrixLabels.add_widget(varLabel)
        self.matrixLabels.add_widget(resultsLabel)

        # add square matrix inputs
        self.squareMatrixInputs = BoxLayout(orientation='vertical')
        self.matrixGrid = GridLayout(rows=self.numEquations, cols=self.numEquations)
        for i in range(self.numEquations):
            for j in range(self.numEquations):
                self.matrixGrid.add_widget(TextInput(hint_text="(" + str(i) + "," + str(j) + ")"))
        self.squareMatrixInputs.add_widget(self.matrixGrid)

        # add variable name inputs
        # self.varInputs = BoxLayout(orientation='vertical', size_hint=(.3, 1))
        # for i in range(self.numEquations):
        #     self.varInputs.add_widget(TextInput(hint_text="v" + str(i)))
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
        # self.matrixInputs.add_widget(self.varInputs)
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
        # for child in self.varInputs.children:
        #     self.variables = [child.text] + self.variables
        results = []
        for child in self.resultsInputs.children:
            results = [float(child.text)] + results
        for i in range(self.numEquations):
            self.results[i] = results[i]
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

        u = np.zeros([self.numEquations,self.numEquations])
        l = np.zeros([self.numEquations,self.numEquations])
        for k in range (0,self.numEquations):
            for r in range (0,self.numEquations):
                if (k == r):
                    l[k,r] = 1
                if (k < r):
                    factor = (self.squareMatrix[r,k] / self.squareMatrix[k,k])
                    l[r,k] = factor
                    for c in range (0,self.numEquations):
                        self.squareMatrix[r,c] = self.squareMatrix [r,c] - (factor*self.squareMatrix[k,c])
                        u[r,c] = self.squareMatrix [r,c]

        matrizr = np.zeros([self.numEquations,self.numEquations])
        for r in range (0,self.numEquations):
            for c in range (0,self.numEquations):
                for k in range (0,self.numEquations):
                    matrizr[r,c] += (l[r,k] * u[k,c])

        result = "Matrix L:\n"+str(l)+"Matrix U:\n"+str(u)+"\nComprobación:\n"+str(matrizr)
        self.finalResultsLabel.text = result

    def gaussSeidel(self, obj):
        self.receiveTextInputValues()
        # Catch error
        if self.toleranceTxtInput.text :
            print("there is something tol")
        else :
            print("isEmpty")
            
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