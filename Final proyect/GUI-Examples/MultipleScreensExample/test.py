import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class MenuScreen(Screen):
    pass
class FirstScreen(Screen):
    #create property in python
    first_screen = ObjectProperty()
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_two, 2)
    def screen_switch_two(self, dt):
        self.manager.current = 'second_screen'
class SecondScreen(Screen):
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_three, 4)
    def screen_switch_three(self, dt):
        self.manager.current = 'third_screen'
class ThirdScreen(Screen):
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_four, 6)
    def screen_switch_four(self, dt):
        self.manager.current = 'fourth_screen'
class FourthScreen(Screen):
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_one, 8)
    def screen_switch_one(self, dt):
        #change the text of the label in the first_screen
        self.manager.get_screen('first_screen').first_screen.text = "Hi I'm The Fifth Screen"
        self.manager.current = 'first_screen'

root_widget = Builder.load_string("""
#here the screens will be created
ScreenManager:
    MenuScreen:
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:
#the menu screen is created that the method on_enter in the first screen is called and the loop through the screens can begin
<MenuScreen>:
    Button:
        text: 'start'
        on_press: app.root.current = 'first_screen'
<FirstScreen>:
    #link/bind the property in the kv file 
    first_screen: first_screen
    name: 'first_screen'
    on_enter: root.starttimer()
    Label:
        id: first_screen
        text: "Hi I'm The First Screen"
<SecondScreen>:
    name: 'second_screen'
    on_enter: root.starttimer()
    Label:
        id: second_screen
        text: "Hi I'm The Second Screen"
<ThirdScreen>:
    name: 'third_screen'
    on_enter: root.starttimer()
    Label:
        id: third_screen
        text: "Hi I'm The Third Screen"
<FourthScreen>:
    name: 'fourth_screen'
    on_enter: root.starttimer()
    Label:
        id: fourth_screen
        text: "Hi I'm The Fourth Screen"
""")

class SwitchingScreenApp(App):

    def build(self):
        return root_widget

if __name__ == '__main__':
    SwitchingScreenApp().run()