from PyQt5.QtWidgets import (QPushButton, QWidget, QLabel,
                             QTextEdit, QGridLayout, QApplication)
from PyQt5.QtGui import QFont, QPalette, QPixmap
from PyQt5.QtCore import *
import os
import sys
from datetime import datetime
import subprocess
import speech_recognition as sr
import colorama
from termcolor import cprint

from gtts import gTTS


class GV:
    pathDelimiter = "././"
    try:
        file_list = os.listdir(pathDelimiter+"Internal")
    except:
        pathDelimiter = ".././"
    greeting = ""


def gtts(text):
    file = GV.pathDelimiter+"Internal/gTTS/gtts-audio.mp3"
    tts = gTTS(text=text, lang="en", tld="com")
    tts.save(file)
    subprocess.call(["/usr/bin/mpg123", file], stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    os.remove(file)


def activate():
    gtts(text=GV.greeting)
    sample_rate = 48000
    chunk_size = 2048
    text = ""
    while True:
        r = sr.Recognizer()
        with sr.Microphone(device_index=6, sample_rate=sample_rate,
                        chunk_size=chunk_size) as source:
            r.adjust_for_ambient_noise(source)
            print("\n")
            display_statements_list = ["I'M LISTENING"]
            width = len(display_statements_list[0])
            colorama.init()
            print('+-' + '-' * width + '-+')
            for s in display_statements_list:
                cprint('| {0:^{1}} |'.format(s, width), color='cyan')
                print('+-' + '-'*(width) + '-+')
            subprocess.call(["/usr/bin/mpg123", GV.pathDelimiter+"Internal/Assistant-Module/Assets/listen.mp3"], stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
            audio = r.listen(source, timeout=5.0)
            try:
                text = r.recognize_google(audio)
                subprocess.call(["/usr/bin/mpg123", GV.pathDelimiter+"Internal/Assistant-Module/Assets/processing.mp3"], stdout=subprocess.DEVNULL,
                                stderr=subprocess.STDOUT)
                break
            except sr.WaitTimeoutError:
                print(
                    "Mic timeout. Google Speech Recognition could not understand audio")
                subprocess.call(["/usr/bin/mpg123", GV.pathDelimiter+"Internal/Assistant-Module/Assets/fallback.mp3"], stdout=subprocess.DEVNULL,
                                stderr=subprocess.STDOUT)
            except sr.UnknownValueError:
                print(
                    "Mic timeout. Google Speech Recognition could not understand audio")
                subprocess.call(["/usr/bin/mpg123", GV.pathDelimiter+"Internal/Assistant-Module/Assets/fallback.mp3"], stdout=subprocess.DEVNULL,
                                stderr=subprocess.STDOUT)
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service", e)
                subprocess.call(["/usr/bin/mpg123", GV.pathDelimiter+"Internal/Assistant-Module/Assets/fallback.mp3"], stdout=subprocess.DEVNULL,
                                stderr=subprocess.STDOUT)
    update_label(str(text).capitalize())
    command = str(text).lower()
    print("\nCommand: ", command.capitalize())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("Hera")
    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.white)
    qp.setColor(QPalette.Window, Qt.black)
    w.setPalette(qp)

    # LOGO
    logo = QLabel()
    logo_pix = QPixmap(
        GV.pathDelimiter+"Internal/Assistant-Module/Assets/logo.png")
    logo_pix_scaled = logo_pix.scaledToHeight(400)
    logo.setPixmap(logo_pix_scaled)
    logo.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    # OUTPUT FIELD
    output_field = QTextEdit()
    output_field.setReadOnly(True)
    output_field.setStyleSheet(
        "background-color: black; color: white; padding : 10px")
    output_field.setTextColor(Qt.white)
    now = datetime.now()
    current_time = now.strftime("%H")
    if int(current_time) >= 0 and int(current_time) < 12:
        greet_day_condition = "Good Morning"
    elif int(current_time) >= 12 and int(current_time) < 16:
        greet_day_condition = "Good Afternoon"
    else:
        greet_day_condition = "Good Evening"
    output_field.setFont(QFont('Calibri', 25))
    GV.greeting = greet_day_condition+" Gokul"
    output_field.setText(GV.greeting)

    # BUTTON
    button = QPushButton("Activate")
    button.setStyleSheet(
        "border-radius : 15; border : 2px solid grey; color : white; padding : 7px; margin-bottom : 10px;")
    button.setFont(QFont('Calibri', 16))
    button.clicked.connect(activate)

    grid = QGridLayout()
    grid.setSpacing(10)

    grid.addWidget(output_field, 0, 0, 5, 1)
    grid.addWidget(logo, 0, 1, 3, 1)
    grid.addWidget(button, 3, 1, 2, 1)

    w.setLayout(grid)

    w.setFixedSize(720, 480)
    w.show()

    def update_label(text):
        output_field.clear()
        output_field.setText(text)

    sys.exit(app.exec_())
