import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.properties import StringProperty

from scr.valid_api import is_api_key_valid



def api_validation(self,instance):
    pass
    """first_input = self.ids.input_1

    api_key = self.ids.input_1.text  # api wird durch Benutzer eingegeben
    # is_api_key_valid(api_key):
    if True:
        self.manager.current = 'second'
        MyBoxLayout.ids.chat_input_disabled = False
    else:
        self.manager.current = 'tree'"""


class MyBoxLayout(BoxLayout):
    pass

    def on_button_stelle(self):
        self.ids.chat_input(text='öhdlksh')
        pass


class MyBox(BoxLayout):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class TreeScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass


class OberFApp(App):
    def build(self):
        # print(MyBoxLayout.__dict__)
        return

print(OberFApp.__dict__)
OberFApp().run()
