import pyttsx3

# initialize Text-to-speech engine


def tts(text):
    try:
        print("\n" + text)
        # Comment out these lines if you don't want sound output

        engine = pyttsx3.init()
        print("\n{} Text To Speech engine initialized{}".format(
            '='*20, '='*20))
        engine.setProperty("rate", 140)
        # -------------------------
        # checking voices
        # voices = engine.getProperty("voices")
        # set another voice
        # engine.setProperty("voice", voices[10].id)
        # -------------------------
        engine.setProperty('voice', 'english_rp+f3')  # female
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("\nAn error occurred while initializing Text To Speech engine.\n" + str(e))


if __name__ == '__main__':
    tts("Firefox")
