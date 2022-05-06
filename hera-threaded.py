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
foo= SourceFileLoader("asr", "speech-recognition/asr.py").load_module()


#### SETTING UP TEXT TO SPEECH ###
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate",178)
#engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
##### CONSTANTS ################
fs = 22050
seconds = 2

model = load_model("./wake-word-detection/saved_model/WWD.h5")

##### LISTENING THREAD #########
def listener():
    while True:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        print("---Speak through Mic---")
        sd.wait()
        mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        prediction_thread(mfcc_processed)
        time.sleep(0.001)


def voice_thread():
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listen_thread.start()

##### PREDICTION THREAD #############
def prediction(y):
    prediction = model.predict(np.expand_dims(y, axis=0))
    if prediction[:, 1] > 0.98:
        print("---Wake word detected---")
        print("---Speech Recognition Initialized--")
      if engine._inLoop:
          engine.endLoop()
        
         speak("Hello, What can I do for you?")
         try:
             create_asr()
             print("called ASR")
         except Exception as e:
             print("Couldnt call",e)
            

    time.sleep(0.1)

def prediction_thread(y):
    pred_thread = threading.Thread(target=prediction, name="PredictFunction", args=(y,))
    pred_thread.start()
def create_asr():
    asr_thread = threading.Thread(target=foo.asr(),name="SpeechRecognition")
    asr_thread.start()

voice_thread()
