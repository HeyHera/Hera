import pyttsx3

# initialize Text-to-speech engine


def tts(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 140)
    # checking voices
    # voices = engine.getProperty("voices")
    print(text)
    # set another voice
    #engine.setProperty("voice", voices[10].id)
    engine.setProperty('voice', 'english_rp+f3')  # female
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    tts("Fire Fox")
