import time
import kivy
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.clock import Clock
import threading
kivy.require('2.1.0')


class GV:
    global_label_text = ""


class PrintHello(MDScreen):
    username = ObjectProperty(None)
    status = ObjectProperty(None)

    def display_hello_status(self):
        # Inform about process of generating hello text.
        # Pretend something is happening in the background. Actually make it happen on a background thread
        threading.Thread(target=self.do_something).start()

    def do_something(self):
        print('starting first')
        time.sleep(7)
        GV.global_label_text = "Play a song"

        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.something_finished)

        # Second itt
        print('starting second')
        time.sleep(7)
        GV.global_label_text = "Playing a random song"
        print('finished second')

        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.something_finished)
        time.sleep(3)
        Clock.schedule_once(self.clear_label)

    def something_finished(self, dt):
        print(GV.global_label_text)
        self.status.text = GV.global_label_text
        # Display information indicating successful printing.
        # self.status.text = "printed!"

    def something_finished_two(self, dt):
        # self.username.text = GV.global_label_text
        print(GV.global_label_text)
        self.status.text = GV.global_label_text
        # Display information indicating successful printing.
        # self.status.text = "printed!"

    def clear_label(self, dt):
        # Display information indicating successful printing.
        self.status.text = ""


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return PrintHello()


if __name__ == '__main__':
    MyApp().run()
