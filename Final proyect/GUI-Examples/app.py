from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown


class Menu(BoxLayout):
	pass

class BracketAndClosedMethods(BoxLayout):
	pass

class MenuApp(App):
	def build(self):
		root = ScreenManager()
		root.add_widget(Menu())
		root.add_widget(BracketAndClosedMethods())
		return root

menu = MenuApp()
menu.run()
