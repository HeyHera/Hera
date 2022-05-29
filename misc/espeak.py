import pyttsx3

# initialize Text-to-speech engine
try:
    # Comment out these lines if you don't want sound output
    engine = pyttsx3.init()
    # print("\n{} Text To Speech engine initialized {}".format(
    #     '='*20, '='*20))
    engine.setProperty("rate", 140)
    # -------------------------
    # checking voices
    # voices = engine.getProperty("voices")
    # set another voice
    # engine.setProperty("voice", voices[10].id)
    # -------------------------
    engine.setProperty('voice', 'english_rp+f3')  # female
except Exception as e:
    print("\nAn error occurred while initializing Text To Speech engine.\n" + str(e))


def tts(text):
    print("\n" + text)
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    tts("It's good to be with somebody, that's excited about life.")
