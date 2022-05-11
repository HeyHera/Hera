###### IMPORTS ###################
from importlib.machinery import SourceFileLoader
import time
import sounddevice as sd
import librosa
import numpy as np
from tensorflow.keras.models import load_model
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

asrmod = SourceFileLoader("asr", "speech-recognition/asr.py").load_module()
ttsmod = SourceFileLoader("espeak", "tts/espeak.py").load_module()
sksmod = SourceFileLoader("skills", "skills/skills.py").load_module()


#from Hera.skills.greeting import greeting


##### CONSTANTS ################
fs = 22050
seconds = 2

model = load_model("wake-word-detection/saved_model/WWD.h5")

print(sd.query_devices())
# device_info = sd.query_devices(args.device, 'input')

##### LISTENING THREAD #########


def listener():

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print("---Speak through Mic---")
    sd.wait()
    print("Mic waited")
    mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
    mfcc_processed = np.mean(mfcc.T, axis=0)
    prediction(mfcc_processed)
    time.sleep(0.001)


def prediction(y):
    prediction = model.predict(np.expand_dims(y, axis=0))
    if prediction[:, 1] > 0.98:
        print("---Wake word detected---")
        print("---Speech Recognition Initialized--")

        ttsmod.tts(greeting())
        try:
            spoken = asrmod.asr()
            print(spoken)
            matchSkill(spoken)

        except Exception as e:
            print("Couldnt call", e)

    time.sleep(0.1)


def matchSkill(statement):
    statement = statement.lower()

    if "play music" in statement or "music" in statement or "song" in statement:
        ttsmod.tts('Playing a random music')
        sksmod.music_playback(statement)
    elif statement.startswith("launch") or statement.startswith("open"):
        sksmod.launch_applications(statement)
        # os.system('randommusic')


def greeting():
    t = time.localtime()
    current_time = time.strftime("%H", t)

    if int(current_time) >= 0 and int(current_time) < 12:
        greet_day_condition = "Good Morning"
    elif int(current_time) >= 12 and int(current_time) < 16:
        greet_day_condition = "Good Afternoon"
    else:
        greet_day_condition = "Good Evening"

    return(greet_day_condition)


listener()
