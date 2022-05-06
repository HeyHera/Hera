import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
#text = "Good morning Arjun"
text = "How are you Arjun, nandu, gokul and jithin"
engine.setProperty("rate", 105)
# checking voices
voices = engine.getProperty("voices")
# set another voice
#engine.setProperty("voice", voices[10].id)
engine.setProperty('voice', 'english_rp+f3') #female
#engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
engine.say(text)
engine.runAndWait()
