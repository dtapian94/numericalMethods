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

class OpenMethods(Screen):

    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(OpenMethods, self).__init__(**kwargs)
        self.basebox = BoxLayout(orientation='vertical')
        # Add two buttons that will display the correct inputs for Secant or Newton Rhapson
        self.inputs = BoxLayout(orientation='horizontal', size_hint=(1, 0.7))
        self.options = BoxLayout(orientation='horizontal', size_hint=(1, 0.3))
        self.results = BoxLayout(orientation='vertical')

        self.nonLinearLabel = Label(text="Use Non \nLinear Equation")
        self.formulaTxtInput = TextInput(hint_text='formula with unknown variable x')
        self.derivativeTxtInput = TextInput(hint_text='derivative (for Newton Raphson Method)')
        self.x0TxtInput = TextInput(hint_text='x0')
        self.differenceTxtInput = TextInput(hint_text='difference: 0.5 or 1 (for Secant Method)')
        self.tolTxtInput = TextInput(hint_text='tolerance')
        self.iterationsTxtInput = TextInput(hint_text='max iterations')

        secantBtn = Button(text='Secant')
        secantBtn.bind(on_release=self.onClickSecant)
        newtonRaphsonBtn = Button(text='Newton Raphson')
        newtonRaphsonBtn.bind(on_release=self.onClickNewton)
        backBtn = Button(text='Back to Menu')
        backBtn.bind(on_release=self.backToMenu)
        self.newtonRaphsonResultsLabel = Label(text='')
        self.secantResultsLabel = Label(text='')

        self.options.add_widget(newtonRaphsonBtn)
        self.options.add_widget(secantBtn)
        self.options.add_widget(backBtn)

        self.results.add_widget(self.newtonRaphsonResultsLabel)
        self.results.add_widget(self.secantResultsLabel)

        self.basebox.add_widget(self.options)
        self.basebox.add_widget(self.inputs)
        self.basebox.add_widget(self.results)

        self.add_widget(self.basebox)

    def backToMenu(self, obj):
        self.screenManager.current = 'menu'

    def onClickSecant(self, obj):
        # clear child widgets that may repeat
        self.inputs.clear_widgets()

        # create personalized run button
        self.runSecantBtn = Button(text='run')
        self.runSecantBtn.bind(on_release=self.runSecant)

        self.inputs.add_widget(self.nonLinearLabel)
        self.inputs.add_widget(self.formulaTxtInput)
        self.inputs.add_widget(self.differenceTxtInput)
        self.inputs.add_widget(self.x0TxtInput)
        self.inputs.add_widget(self.tolTxtInput)
        self.inputs.add_widget(self.iterationsTxtInput)
        self.inputs.add_widget(self.runSecantBtn)

    def onClickNewton(self, obj):
        # clear child widgets that may repeat
        self.inputs.clear_widgets()
        # create personalized run button
        self.runNewtonBtn = Button(text='run')
        self.runNewtonBtn.bind(on_release=self.runNewton)

        self.inputs.add_widget(self.nonLinearLabel)
        self.inputs.add_widget(self.formulaTxtInput)
        self.inputs.add_widget(self.derivativeTxtInput)
        self.inputs.add_widget(self.x0TxtInput)
        self.inputs.add_widget(self.tolTxtInput)
        self.inputs.add_widget(self.iterationsTxtInput)
        self.inputs.add_widget(self.runNewtonBtn)

    def runSecant(self, obj):
        self.formula = self.formulaTxtInput.text
        x0 = float(self.x0TxtInput.text)
        difference = float(self.differenceTxtInput.text)
        tolerance = float(self.tolTxtInput.text)
        maxIterations = int(self.iterationsTxtInput.text)
        self.secantResultsLabel.text = self.altSecant(x0, difference, tolerance, maxIterations)

    def runNewton(self, obj):
        self.formula = self.formulaTxtInput.text
        self.derivative = self.derivativeTxtInput.text
        x0 = float(self.x0TxtInput.text)
        tolerance = float(self.tolTxtInput.text)
        maxIterations = int(self.iterationsTxtInput.text)
        self.newtonRaphsonResultsLabel.text = self.newtonRaphson(x0, tolerance, maxIterations)

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
        return "Newton Rahpson:\n " + str(x0) + " Iteration: " + str(i) + " aproximate percent relative error: " + str(error)

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
        return "Secant:\n" + str(xI) + " Iteration: " + str(iteration) + "aproximate percent relative error: " + str(rError)
