import sys
from math import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
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
        inputs = BoxLayout(orientation='horizontal')
        options = BoxLayout(orientation='horizontal')
        results = BoxLayout(orientation='vertical')

        self.formulaTxtInput = TextInput(hint_text='formula with unknown variable x')
        self.xlowTxtInput = TextInput(hint_text='xlow')
        self.xuppTxtInput = TextInput(hint_text='xupper')
        self.tolTxtInput = TextInput(hint_text='tolerance')
        self.iterationsTxtInput = TextInput(hint_text='max iterations')

        runBtn = Button(text='run')
        runBtn.bind(on_release=self.run)
        backBtn = Button(text='Back to Menu')
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

    def bisection(self, xlow, xupper, tolerance, imax) :
        aproxRelativeError = 99999999
        iterations = 0
        xres = (xlow + xupper) / 2.0
        testing = self.f(xlow) * self.f(xres)
        if testing < 0 :
            xupper = xres
        if testing > 0 :
            xlow = xres
        elif testing == 0 :
            aproxRelativeError = 0
        while (aproxRelativeError > tolerance and iterations < imax) :
            xresOld = xres
            testing = self.f(xlow) * self.f(xres)
            if testing < 0 :
                xupper = xres
            elif testing > 0 :
                xlow = xres
            elif testing == 0 :
                aproxRelativeError = 0
            xres = (xlow + xupper) / 2.0
            if xres != 0 :
                aproxRelativeError = abs((xres - xresOld) / xres) * 100
            iterations += 1
        return "Bisection Method = " + str(iterations) + " iterations. Result: " + str(xres) + " %" + str(aproxRelativeError) + " aproximate percent relative error"
    
    def false_position(self, xlow, xupper, tolerance, imax) :
        aproxRelativeError = 99999999
        iterations = 0
        xres = xupper - ((self.f(xupper) * (xlow - xupper)) / (self.f(xlow) - self.f(xupper)))
        testing = self.f(xlow) * self.f(xres)
        if testing < 0 :
            xupper = xres
        if testing > 0 :
            xlow = xres
        elif testing == 0 :
            aproxRelativeError = 0
        while (aproxRelativeError > tolerance and iterations < imax) :
            xresOld = xres
            testing = self.f(xlow) * self.f(xres)
            if testing < 0 :
                xupper = xres
            elif testing > 0 :
                xlow = xres
            elif testing == 0 :
                aproxRelativeError = 0
            xres = xupper - ((self.f(xupper) * (xlow - xupper)) / (self.f(xlow) - self.f(xupper)))
            if xres != 0 :
                aproxRelativeError = abs((xres - xresOld) / xres) * 100
            iterations += 1
        return "False Position Method = " + str(iterations) + " iterations. Result: " + str(xres) + " %" + str(aproxRelativeError) + " aproximate percent relative error"
    
    def run(self, obj):
        self.formula = self.formulaTxtInput.text
        xlow = float(self.xlowTxtInput.text)
        xupper = float(self.xuppTxtInput.text)
        tolerance = float(self.tolTxtInput.text)
        maxIterations = int(self.iterationsTxtInput.text)
        self.bisectionResultsLabel.text = self.bisection(xlow,xupper,tolerance,maxIterations)
        self.falsePositionResultsLabel.text = self.false_position(xlow,xupper,tolerance,maxIterations)

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
        self.newtonRaphsonResultsLabel.text = self.newtonRaphson(x0,tolerance,maxIterations)
        self.secantResultsLabel.text = self.altSecant(x0,difference,tolerance,maxIterations)

    def f(self, x):
        return eval(self.formula)

    def Df(self, x):
        return eval(self.derivative)

    def newtonRaphson(self, x0, tolerance, maxIterations) :
        i = 1
        error = 100 # Start with 100% error
        while error > tolerance :
            if i == maxIterations :
                break
            x1 = x0 - self.f(x0) / self.Df(x0)
            error = abs(x1 - x0) * 100
            x0 = x1
            i = i + 1
        return "Result: " + str(x0) + " Iteration: " + str(i) + " aproximate percent relative error: " + str(error)

    def altSecant(x, diff, tol, maxAttempts):
        iteration = 1
        rError = 100 # Start with 100% error
        while rError >= tolerance:
            if iteration == maxAttempts :
                break
            xI = x - (diff*x*f(x))/(f(x+(diff*x))-f(x))
            rError = abs((xI-x)/xI) * 100
            x = xI
            iteration += 1
        return "Result: " + str(xI) + " Iteration: " + str(iteration) + "aproximate percent relative error: " + str(rError)


class GaussElimination(Screen):
    pass

class LUDecomposition(Screen):
    pass

class GaussSeidel(Screen):
    pass

class NumericalMethodsApp(App):
    def build(self):
        root = ScreenManager()
        root.transition = SwapTransition()
        root.add_widget(MainMenu())
        root.add_widget(BracketMethods(screenManager=root,name='bracket_methods'))
        root.add_widget(OpenMethods(screenManager=root,name='open_methods'))
        return root


if __name__ == '__main__':
    NumericalMethodsApp().run()
