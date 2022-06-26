import threading
import time
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock

Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
<KivyMDLayout>:
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
            on_release: root.executer()
""")


class KivyMDLayout(MDScreen):
    label_text = ""
    status = ObjectProperty(None)

    def executer(self):
        threading.Thread(target=self.script_run).start()

    def script_run(self):
        # First pass
        print('Starting first pass\n')
        time.sleep(3)
        self.label_text = "Play a song"
        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.update_label)

        # Second pass
        print('Starting second pass\n')
        time.sleep(3)
        self.label_text = "Playing a random song"
        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.update_label)

        # schedule the GUI update to clear label back on the main thread
        time.sleep(3)
        Clock.schedule_once(self.clear_label)

    def update_label(self, dt):
        print("Label updated: " + self.label_text + "\n")
        self.status.text = self.label_text

    def clear_label(self, dt):
        self.status.text = "..."
        print("Label cleared\n")


class Hera(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return KivyMDLayout()


if __name__ == '__main__':
    Hera().run()
