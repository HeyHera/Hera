import multiprocessing
import subprocess
import threading
import kivy
from kivy.config import Config
import time
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock

kivy.require('2.1.0')

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
        threading.Thread(target=self.running_script).start()

    def running_script(self):
        pipe_begin, pipe_end = multiprocessing.Pipe()

        # CALLING AUTOMATIC-SPEECH-RECOGNITION TO RECOGNIZE COMMAND
        try:
            print("\n{} Automatic Speech Recognition initializing {}".format(
                '='*20, '='*20))
            self.label_text = "..."
            # SCHEDULE THE GUI UPDATE BACK ON THE MAIN THREAD
            Clock.schedule_once(self.update_label)
            time.sleep(0.5)
            spoken = asr_module.asr()
            spoken = str(spoken).lower()
            print("\nASR: " + spoken)
            self.label_text = spoken.capitalize()
            # SCHEDULE THE GUI UPDATE BACK ON THE MAIN THREAD
            Clock.schedule_once(self.update_label)
            time.sleep(0.5)
        except Exception as e:
            print(
                "\nError encountered. Couldn't connect with Automatic Speech Recognition.\n" + str(e))\

        # AUDIBLE PROCESSING SOUND
        subprocess.call(["mpg321", 'assets/audible-feedback/Assistant-Module_Assets_processing.mp3'], stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)

        # PASSING THE COMMAND TO INTENT CLASSIFIER
        print("\n{} Classifying Intent {}".format(
            '='*20, '='*20))
        matched_intent = intent_classifier_module.classify(spoken)
        print("Matched Intent: {}".format(matched_intent))

        # MATCHING THE INTENT WITH CORRESPONDING SKILL
        statement = spoken.lower()
        skill_response = None
        pipe_output = None
        print("\n{} Skill match starting {}".format(
            '='*20, '='*20))
        # POSSIBLE LABELS {'LAUNCH_APPLICATION', 'MUSIC_PLAYBACK_RANDOM_SONG','MUSIC_PLAYBACK_ALBUM_SONG', 'UNDEFINED'} etc

        if matched_intent == 'UNDEFINED':
            print("Nothing received as command")
            # AUDIBLE FALLBACK SOUND
            subprocess.call(["mpg321", 'assets/audible-feedback/Assistant-Module_Assets_fallback.mp3'], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)

        elif matched_intent in ['MUSIC_PLAYBACK_ALBUM_SONG', 'MUSIC_PLAYBACK_SPECIFIC_SONG', 'MUSIC_PLAYBACK_RANDOM_SONG']:
            print("Matched Skill: {}".format(matched_intent))
            status = multiprocessing.Value('i', -1)
            p1 = multiprocessing.Process(target=music_playback_skill.music_playback, args=(
                status, pipe_end, statement, matched_intent,))
            p1.start()
            pipe_output = pipe_begin.recv()
            pipe_begin.close()
            if str(pipe_output) != None:
                self.label_text = str(pipe_output).capitalize()
                # SCHEDULE THE GUI UPDATE BACK ON THE MAIN THREAD
                Clock.schedule_once(self.update_label)
                time.sleep(0.5)
            p1.join()
            skill_response = status.value
        elif matched_intent == 'LAUNCH_APPLICATION':
            print("Matched Skill: {}".format(matched_intent))
            status = multiprocessing.Value('i', -1)
            p1 = multiprocessing.Process(
                target=launch_application_skill.launch_applications, args=(status, pipe_end, statement,))
            p1.start()
            pipe_output = pipe_begin.recv()
            pipe_begin.close()
            if str(pipe_output) != None:
                self.label_text = str(pipe_output).capitalize()
                # SCHEDULE THE GUI UPDATE BACK ON THE MAIN THREAD
                Clock.schedule_once(self.update_label)
                time.sleep(0.5)
            p1.join()
            skill_response = status.value
        print("Skill response: {}" .format(skill_response))
        if skill_response == 0:
            print("Success")
        elif skill_response == 1:
            print("Fail")
        elif skill_response == 2:
            print("Return prompt")
        elif skill_response != None or "NO_MATCH" in matched_intent:
            subprocess.call(["mpg321", 'assets/audible-feedback/Assistant-Module_Assets_fallback.mp3'], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
            tts_module.tts("Sorry! I did't understood that.")

        time.sleep(2)
        Clock.schedule_once(self.clear_label)

    def update_label(self, dt):
        self.status.text = self.label_text

    def clear_label(self, dt):
        self.status.text = "Hello!"


class Hera(MDApp):
    def build(self):
        self.icon = 'Hera-Logo-128x128.ico'
        self.theme_cls.theme_style = "Dark"
        return KivyMDLayout()


if __name__ == '__main__':
    Hera().run()
