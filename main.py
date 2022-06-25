import subprocess
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
import multiprocessing
import threading

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


KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDScreen:
    MDLabel:
        id: text_update
        text: root.chang
        halign: "center"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("#f2dafe")
        font_style: 'H2'

    MDRectangleFlatButton:
        text: "ACTIVATE"
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        theme_text_color: "Custom"
        line_color: get_color_from_hex("#f2dafe")
        on_press: app.script()
'''


class Hera(MDApp):

    chang = StringProperty('')

    def build(self):

        # defining screen
        self.theme_cls.theme_style = "Dark"
        # self.msg = StringProperty()
        # self.msg = "Hello!"
        screen = Builder.load_string(KV)
        return screen

    def change_word(self, r_msg):  # What Parameters should I give after self?
        print("Got request to change word")
        self.root.ids.text_update.text = (r_msg)
        return(0)

    def script(self):
        # start_char = input("Press Enter to continue: ")
        start_char = "" # Remove this line later
        if start_char != "":
            print("Exiting")
            exit()
        else:
            # try:
            #     # CALLING WAKE-WORD-DETECTION IN A SEPARATE THREAD
            #     print("\n{} Wake Word Detection thread starting {}".format(
            #         '='*20, '='*20))
            #     wwd_thread = threading.Thread(
            #         target=wwd_module.listener, name="Wake-Word-Detection-Thread")
            #     wwd_thread.start()
            #     wwd_thread.join()  # WAITING wwd_thread TO STOP EXECUTING
            # except Exception as e:
            #     print("An error occurred while starting Wake Word Detection thread")

            # CALLING TEXT-TO-SPEECH FOR GREETING THE USER
            # tts_module.tts(greeting_skill.greeting())
            subprocess.call(["mpg321", 'assets/Assistant-Module_Assets_listen.mp3'], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)

            # CALLING AUTOMATIC-SPEECH-RECOGNITION TO RECOGNIZE COMMAND
            try:
                print("\n{} Automatic Speech Recognition initializing {}".format(
                    '='*20, '='*20))
                spoken = asr_module.asr()
                spoken = str(spoken).lower()
                print(spoken)
                # self.change_word(spoken)
                self.chang = spoken
            except Exception as e:
                print(
                    "\nError encountered. Couldn't connect with Automatic Speech Recognition.\n" + str(e))
            spoken = asr_module.asr()
            self.chang = "spoken"


            # msg = "None"
            # pipe_begin, pipe_end = multiprocessing.Pipe()
            # p1 = multiprocessing.Process(target=skill_func.sender, args=(pipe_end,))
            # p1.start()
            # msg = pipe_begin.recv()
            # pipe_begin.close()
            # if msg != "None":
            #     chn_wrd = self.change_word(msg)
            #     # if chn_wrd == 0:
            #     #     self.change_word("...")
            #     # print("finished")
            #     # change_word_process = multiprocessing.Process(target=self.change_word, args=(msg,))
            #     # change_word_process.start()
            #     # change_word_process.join()
            # # p1.join()
            # # msg = "None"
            # # self.change_word(msg)


if __name__ == "__main__":
    Hera().run()
