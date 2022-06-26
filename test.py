import threading
import time
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock


class GV:
    global_label_text = ""


Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
<MySec>:
    status: status_label
    MDScreen:
        MDLabel:
            id: status_label
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
            on_release: root.display_hello_status()
""")


class MySec(MDScreen):
    status = ObjectProperty(None)

    def display_hello_status(self):
        threading.Thread(target=self.do_something).start()

    def do_something(self):
        # First pass
        print('starting first')
        time.sleep(7)
        GV.global_label_text = "Play a song"
        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.something_finished)

        # Second pass
        print('starting second')
        time.sleep(7)
        GV.global_label_text = "Playing a random song"
        print('finished second')
        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.something_finished)

        # schedule the GUI update to clear label back on the main thread
        time.sleep(3)
        Clock.schedule_once(self.clear_label)

    def something_finished(self, dt):
        print(GV.global_label_text)
        self.status.text = GV.global_label_text

    def clear_label(self, dt):
        self.status.text = "..."


class Hera(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MySec()


if __name__ == '__main__':
    Hera().run()
