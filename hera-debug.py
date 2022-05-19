from importlib.machinery import SourceFileLoader
import time
import sounddevice as sd
import librosa
import numpy as np
from tensorflow.keras.models import load_model
from scipy.io.wavfile import write
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2`'

# LOCAL IMPORTS
asr_module = SourceFileLoader("asr", "speech-recognition/asr.py").load_module()
tts_module = SourceFileLoader(
    "espeak", "text-to-speech/espeak.py").load_module()
greeting_skill = SourceFileLoader(
    "greeting-skill", "skills/greetings.py").load_module()
music_playback_skill = SourceFileLoader(
    "music-playback-skill", "skills/music-playback.py").load_module()
launch_application_skill = SourceFileLoader(
    "launch-application", "skills/launch-application.py").load_module()

# CONSTANTS
fs = 22050
seconds = 2
print(sd.default.device)

model = load_model("wake-word-detection/saved_model/WWD.h5")

# print(sd.query_devices())


def listener():
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print("---Speak through Mic---")
    sd.wait()
    write('output.wav', fs, myrecording)  # Save as WAV file for debugging
    mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
    mfcc_processed = np.mean(mfcc.T, axis=0)
    prediction(mfcc_processed)
    time.sleep(0.001)


def prediction(y):
    prediction = model.predict(np.expand_dims(y, axis=0))
    print(prediction[:, 1])
    if prediction[:, 1] != 0.0:
        print("{} Wake Word Detected {}".format('='*20, '='*20))
        tts_module.tts(greeting_skill.greeting())
        try:
            print("{} Automatic Speech Recognition Initialized {}".format(
                '='*20, '='*20))
            spoken = asr_module.asr()
            print(spoken)
            matchSkill(spoken)

        except Exception as e:
            print("Couldn't connect with Automatic Speech Recognition", e)
    else:
        print("Recognition failed")
    time.sleep(0.1)


def matchSkill(statement):
    statement = statement.lower()
    rtn = None
    if "play music" in statement or "music" in statement or "song" in statement:
        rtn = music_playback_skill.music_playback(statement)
    elif statement.startswith("launch") or statement.startswith("open"):
        rtn = launch_application_skill.launch_applications(statement)
    if rtn != None:
        if rtn == 0:
            print("Success")
        elif rtn == 1:
            print("Fail")
        else:
            print("Return Prompt")
    else:
        print("I am sorry")


listener()
