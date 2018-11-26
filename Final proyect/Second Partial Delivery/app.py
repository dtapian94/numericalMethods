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
import BracketMethods as bm
import OpenMethods as om
import SystemOfEquations as soe
import Interpolation as ip
import Regression as rg

Builder.load_file("numericalmethods.kv")

class MainMenu(Screen):
    pass

class NumericalMethodsApp(App):
    def build(self):
        root = ScreenManager()
        root.transition = SwapTransition()
        root.add_widget(MainMenu())
        root.add_widget(bm.BracketMethods(screenManager=root, name='bracket_methods'))
        root.add_widget(om.OpenMethods(screenManager=root, name='open_methods'))
        root.add_widget(soe.SystemOfEquations(screenManager=root, name='system_equations'))
        root.add_widget(ip.Interpolation(screenManager=root, name='interpolation'))
        root.add_widget(rg.Regression(screenManager=root, name='regression'))
        return root

if __name__ == '__main__':
    NumericalMethodsApp().run()
