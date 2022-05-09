###### IMPORTS ###################
import threading
import time
import sounddevice as sd
import librosa
import numpy as np
from tensorflow.keras.models import load_model
import pyttsx3
import os

from importlib.machinery import SourceFileLoader
asrmod= SourceFileLoader("asr", "speech-recognition/asr.py").load_module()
ttsmod=SourceFileLoader("espeak", "tts/espeak.py").load_module()



##### CONSTANTS ################
fs = 22050
seconds = 2

model = load_model("./wake-word-detection/saved_model/WWD.h5")

##### LISTENING THREAD #########
def listener():
    
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        print("---Speak through Mic---")
        sd.wait()
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
            spoken=asrmod.asr()
            print(spoken)
        except Exception as e:
            print("Couldnt call",e)
            

    time.sleep(0.1)


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
