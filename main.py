from audioop import mul
import time
from kivy.lang import Builder
from kivymd.app import MDApp
import multiprocessing
import skill_func as skill


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
        on_press: app.script()
'''
class Demo(MDApp):

    def build(self):

        # defining screen
        self.theme_cls.theme_style = "Dark"
        # self.msg = StringProperty()
        # self.msg = "Hello!"
        screen =  Builder.load_string(KV)
        return screen

    def change_word(self, r_msg): #What Parameters should I give after self?
        print("Got request to change word")
        self.root.ids.text_update.text=(r_msg)
        return(0)

    
    def script(self):
        msg = "None"
        pipe_begin, pipe_end = multiprocessing.Pipe()
        p1 = multiprocessing.Process(target=skill.sender, args=(pipe_end,))
        p1.start()
        msg = pipe_begin.recv()
        pipe_begin.close()
        print("Received the message: {}".format(msg))
        if msg != "None":
            print("Requesting to change word")
            chn_wrd = self.change_word(msg)
            # if chn_wrd == 0:
            #     self.change_word("...")
            # print("finished")
            # change_word_process = multiprocessing.Process(target=self.change_word, args=(msg,))
            # change_word_process.start()
            # change_word_process.join()
        # p1.join()
        # msg = "None"
        # self.change_word(msg)




if __name__ == "__main__":
    Demo().run()
