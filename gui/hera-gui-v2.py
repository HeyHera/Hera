from importlib.machinery import SourceFileLoader
import threading
import time
from functools import partial

import sys
from PyQt5 import QtGui,QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap



def hera():
    main_pass_no = 0
    while(True):
        main_pass_no += 1
        print("\n[__main__] Pass #{}".format(main_pass_no))
        try:
            # CALLING WAKE-WORD-DETECTION IN A SEPARATE THREAD
            print("\n{} Wake Word Detection thread starting {}".format(
                '='*20, '='*20))
            wwd_thread = threading.Thread(
                target=wwd_module.listener(), name="Wake-Word-Detection-Thread")
            wwd_thread.start()
            wwd_thread.join()  # WAITING wwd_thread TO STOP EXECUTING
        except Exception as e:
            print("An error occurred while starting Wake Word Detection thread")

        # WHILE WAKE WORD IS NOT WORKING
        #start_char = input("Press Enter to continue: ")
        #if start_char != "":
        #    print("Exiting")
        #    exit()
        #else:

            # CALLING TEXT-TO-SPEECH FOR GREETING THE USER
            tts_module.tts(greeting_skill.greeting())

            # CALLING AUTOMATIC-SPEECH-RECOGNITION TO RECOGNIZE COMMAND
            try:
                print("\n{} Automatic Speech Recognition initializing {}".format(
                    '='*20, '='*20))
                spoken = asr_module.asr()
                print(spoken)
            except Exception as e:
                print(
                    "\nError encountered. Couldn't connect with Automatic Speech Recognition.\n" + str(e))

            # MATCHING THE COMMAND WITH CORRESPONDING SKILL
            statement = spoken.lower()
            skill_response = None
            print("\n{} Skill match starting {}".format(
                '='*20, '='*20))
            if statement == "":
                print("Nothing received as command")
                # PLAY AN AUDITORY ERROR BELL
            if "play" in statement or "music" in statement or "song" in statement:
                print("Matched: music_playback_skill")
                skill_response = music_playback_skill.music_playback(statement)
            elif statement.startswith("launch") or statement.startswith("open"):
                print("Matched: launch_application_skill")
                skill_response = launch_application_skill.launch_applications(
                    statement)
            print("Skill response: {}" .format(skill_response))
            if skill_response == 0:
                print("Success")
            elif skill_response == 1:
                print("Fail")
            elif skill_response == 2:
                print("Return prompt")
            elif skill_response != None:
                tts_module.tts("Sorry! I did't understood that.")



class HeraGui(QMainWindow):
    def __init__(self):
        super(HeraGui, self).__init__()
        self.initUI()

    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        #cursor.insertText(str(self.process.readAll()))
        cursor.insertText(self.process.readAll().data().decode())
        self.output.ensureCursorVisible()

    def callProgram(self):
        # run the process
        # `start` takes the exec and a list of arguments
        self.process.start('python',['-u','sample.py'])
        

    def keyPressEvent(self, e):
        if (e.key() == 16777299):
           print("enter key")
        
    def initUI(self):
        # Layout are better for placing widgets
        
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

        # QProcess object for external app
        self.process = QtCore.QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: self.runButton.setEnabled(False))
        self.process.finished.connect(lambda: self.runButton.setEnabled(True))

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(55)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)


    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')


    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

def sample():
    while(True):
        print("hello")
        time.sleep(5)



ERROR_MSG = 'ERROR'
# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result



class HeraCtrl:
    """Hera Controller class."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        #result = self._evaluate(expression=self._view.displayText())
        
        result="Hello"
        print("result1",result)
        while(True):
            print("result2",result)
            self._view.setDisplayText(result)
            time.sleep(5)
            self._view.clearDisplay

    def _buildExpression(self, sub_exp):
        """Build expression."""
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)




#Function Main Start
def main():
    app =QApplication(sys.argv)
    view=HeraGui()
    view.show()

    model = evaluateExpression
    HeraCtrl(model=model, view=view)

    sys.exit(app.exec_())
#Function Main END

if __name__ == '__main__':
    main() 