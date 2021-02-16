from typing import Text
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10,padding=20)
        self.qverb = Label(text = "What verb?", font_size= "25")
        self.qtense = Label(text = "Which tense?", font_size= "25")
        self.verb_input = TextInput()
        self.tense_input = TextInput()
        submit = Button(text="Conjugate!", on_press=self.submit)
        layout.add_widget(self.qverb)
        layout.add_widget(self.qtense)
        layout.add_widget(self.verb_input)
        layout.add_widget(self.tense_input)
        layout.add_widget(submit)
        return layout
    
    def submit(self, obj):
        verb = self.verb_input.text
        tense = self.tense_input.text
        import requests
        import json
        API_KEY = "tBfVpT4RMkNj"
        PROJECT_TOKEN = 'ta4TO7wT8gFJ'
        RUN_TOKEN = 'te_3iOeVXcNg'
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={'api_key': API_KEY})
        data = json.loads(response.text)
        with open('dict.json') as file: 
            dict = json.load(file) 
        output = data['french_urls'][int(dict[verb.lower()])][tense.lower()]
        lst = []
        for i in range(6):
            lst.append(str(output[i]))
        for i in lst:
            print(i[10:-2])
        print("")

if __name__ == '__main__':
    MainApp().run()