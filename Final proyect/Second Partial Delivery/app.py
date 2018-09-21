from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder


Builder.load_string('''
<Menu>:
	manager: manager
	Button:
		text: "hello"
	ScreenManager:
		id: manager
''')

class CustomDropDown(DropDown):
    pass

dropdown = CustomDropDown()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

class Menu(ScreenManager):
	pass

class BracketAndClosedMethods(Screen):
	pass

class NumericalMethodsApp(App):
	def build(self):
		root = Menu()
		root.transition = SwapTransition()
		# root.add_widget(Menu())
		# root.add_widget(BracketAndClosedMethods())
		return root

menu = NumericalMethodsApp()
menu.run()
