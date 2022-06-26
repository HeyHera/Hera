import time
import kivy
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.clock import Clock
import threading
kivy.require('2.1.0')


class PrintHello(MDScreen):
    username = ObjectProperty(None)
    status = ObjectProperty(None)

    def display_hello_status(self):
        # Inform about process of generating hello text.
        self.status.text = "printing hello..."  # this text is never displayed.
        # Pretend something is happening in the background. Actually make it happen on a background thread
        threading.Thread(target=self.do_something).start()

    def do_something(self):
        print('starting something')
        time.sleep(5)
        print('finished something')
        
        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.something_finished)

    def something_finished(self, dt):
        self.username.text = f"Hello, {self.username.text}!"
        # Display information indicating successful printing.
        self.status.text = "printed!"


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return PrintHello()


if __name__ == '__main__':
    MyApp().run()