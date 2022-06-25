import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
kivy.require('2.1.0')

kv_file = Builder.load_string("""
Label:
    text:
        ('[b]Hello[/b] [color = ff0099]World[/color]\\n'
        '[color = ff0099]Hello[/color] [b]World[/b]\\n'
        '[b]Hello[/b] [color = ff0099]World:):)[/color]')
    markup: True
    font_size: '64pt'
""")

class MyFirstKivyApp(App):
    def build(self):
        return kv_file

if __name__ == '__main__':
    MyFirstKivyApp().run()
