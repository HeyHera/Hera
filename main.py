from kivy.lang import Builder
from kivymd.app import MDApp
import random   


KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDScreen:
    MDLabel:
        id: text_update
        text: "Hello!"
        halign: "center"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("#f2dafe")
        font_style: 'H2'

    MDRectangleFlatButton:
        text: "ACTIVATE"
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        theme_text_color: "Custom"
        line_color: get_color_from_hex("#f2dafe")
        on_press: app.change_word()
'''
class Demo(MDApp):

    def build(self):

        # defining screen
        self.theme_cls.theme_style = "Dark"
        # self.msg = StringProperty()
        # self.msg = "Hello!"
        screen =  Builder.load_string(KV)
        return screen

    def change_word(self): #What Parameters should I give after self?
            site_list=['Google','Yahoo','Microsoft','APKpure','APKMB','Stackoverflow','Bing']
            text=random.choice(site_list)
            self.root.ids.text_update.text=(text)


if __name__ == "__main__":
    Demo().run()
