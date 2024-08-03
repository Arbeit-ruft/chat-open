import openai
import requests
import pandas as pd
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
from scr.valid_api import text_prompt
from scr.Bearbeitung_in_exel import read_text_file
from scr.Bearbeitung_in_exel import write_to_excel

engine = 'gpt-3.5-turbo-instruct'
prompt = 'Hauptstadt China?'


class MyBoxLayout(BoxLayout):
    text_stelle = StringProperty('')
    text_Lebe = StringProperty('')
    disabTI = BooleanProperty(True)
    chat_input = ObjectProperty()

    def on_button_stelle(self):
        self.text_stelle = "Gebe hier den Text der aus der Stellenausschreibung ein"
        self.disabTI = False

    def on_button_lebe(self):
        self.disabTI = False
        self.text_stelle = "Gebe hier den Text aus dem CV ein / kopiere den Text aus dem Lebenslauf in dieses Textfeld"

    def open_ok(self):
        prompt_2 = text_prompt(self.chat_input.text)
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt_2,
            max_tokens=500
        )
        antwort = response["choices"][0]["text"]
        self.chat_input.text = antwort
        with open('antwort.txt', 'w', encoding='utf-8') as file:
            file.write(antwort)
        data = [antwort.split('|')]
        df = pd.DataFrame(data, columns=None)
        df.to_excel('outputfile.xlsx', index=False)


class MyBoxLayout_1(BoxLayout):
    pass


class MyBox(BoxLayout):
    pass


class FirstScreen(Screen):
    def api_validation(self, instance):
        api_key = self.ids.input_1.text# api wird durch Benutzer eingegeben
        if is_api_key_valid(api_key):
            self.manager.current = 'second'
        else:
            self.manager.current = 'first'


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


OberFApp().run()
