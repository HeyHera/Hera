import random
import subprocess
import time
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock

# LOCAL IMPORTS
try:
    # import wake_word_detection.wake_word_detection_script as wwd_module
    import automatic_speech_recognition.automatic_speech_recognition_script as asr_module
    import nlu.intent_classification.intent_classifier as intent_classifier_module
    import tts.speak as tts_module
    import skills.greetings as greeting_skill
    import skills.music_playback as music_playback_skill
    import skills.launch_application as launch_application_skill
    import skill_func
    print("\nLocal imports successful")
except Exception as e:
    print("\nLocal imports unsuccessful.\n" + str(e))


Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
<MySec>:
    MDScreen:
        MDLabel:
            id: text_update
            text: root.seconds_string
            halign: "center"
            theme_text_color: "Custom"
            text_color: get_color_from_hex("#f2dafe")
            font_style: 'H2'

        MDRectangleFlatButton:
            text: "ACTIVATE"
            pos_hint: {"center_x": 0.5, "center_y": 0.25}
            theme_text_color: "Custom"
            line_color: get_color_from_hex("#f2dafe")
            on_release: app.script()
""")


class MySec(MDScreen):
    seconds_string = StringProperty('Hello!')


class Hera(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Clock.schedule_interval(lambda dt: self.script(), 1)
        return MySec()

    def script(self):
        # site_list=['Google','Yahoo','Microsoft','APKpure','APKMB','Stackoverflow','Bing']
        # msg=random.choice(site_list)
        # self.root.seconds_string = msg
        # site_list=['2Google','2Yahoo','2Microsoft','2APKpure','2APKMB','2Stackoverflow','2Bing']
        # msg=random.choice(site_list)
        # self.root.seconds_string = msg
        try:
            print("\n{} Automatic Speech Recognition initializing {}".format(
                '='*20, '='*20))
            spoken = asr_module.asr()
            spoken = str(spoken).lower()
            print(spoken)
            # self.change_word(spoken)
            self.seconds_string = spoken
        except Exception as e:
            print(
                "\nError encountered. Couldn't connect with Automatic Speech Recognition.\n" + str(e))
        spoken = asr_module.asr()
        self.seconds_string = "spoken"


if __name__ == '__main__':
    Hera().run()
