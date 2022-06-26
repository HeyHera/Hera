import time
import kivy
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.clock import Clock
import threading
kivy.require('2.1.0')


class WindowManager(ScreenManager):
    pass

class PrintHello(Screen):
    username = ObjectProperty(None)
    status = ObjectProperty(None)

    def display_hello_status(self):
        # Inform about process of generating hello text.
        self.status.text = "printing hello..."  # this text is never displayed.
        # Pretend something is happening in the background. Actually make it happen on a background thread
        threading.Thread(target=self.do_somehing).start()

    def do_somehing(self):
        print('starting something')
        time.sleep(5)
        print('finished something')
        
        # schedule the GUI update back on the main thread
        Clock.schedule_once(self.something_finished)

    def something_finished(self, dt):
        self.username.text = f"Hello, {self.username.text}!"
        # Display information indicating successful printing.
        self.status.text = "printed!"


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()