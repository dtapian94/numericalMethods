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

class BracketMethods(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(BracketMethods, self).__init__(**kwargs)

        basebox = BoxLayout(orientation='vertical')
        inputs = BoxLayout(orientation='horizontal', size_hint=(1, .3))
        options = BoxLayout(orientation='horizontal', size_hint=(1, .3))
        results = BoxLayout(orientation='vertical')

        self.nonLinearLabel = Label(text="Use Non \nLinear Equation")
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

        inputs.add_widget(self.nonLinearLabel)
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
