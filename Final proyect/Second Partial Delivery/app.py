from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Menu(BoxLayout):
	pass

class BracketAndClosedMethods(BoxLayout):
	pass

class NumericalMethodsApp(App):
	def build(self):
		root = ScreenManager()
		root.add_widget(Menu())
		root.add_widget(BracketAndClosedMethods())
		return root

# class CustomDropDown(DropDown):
#     pass

# dropdown = CustomDropDown()
# mainbutton = Button(text='Hello', size_hint=(None, None))
# mainbutton.bind(on_release=dropdown.open)
# dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

menu = NumericalMethodsApp()
menu.run()
