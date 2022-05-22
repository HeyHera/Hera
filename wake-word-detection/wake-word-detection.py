import sounddevice as sd
import librosa
import numpy as np
from tensorflow.keras.models import load_model
from scipy.io.wavfile import write
# import os
import threading

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2`'
# print(sd.query_devices())
# print(sd.default.device)

# CONSTANTS
fs = 22050
seconds = 2
model = load_model("wake-word-detection/saved_model/WWD.h5")


def listener():
    pass_number = 0
    while True:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        pass_number += 1
        print("[WWD] Pass #{}".format(pass_number))
        print("Waiting for wake word")
        sd.wait()
        mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        y = mfcc_processed
        prediction = model.predict(np.expand_dims(y, axis=0))
        write('wake-word-detection/recordings/output'+str(pass_number) +
              '.wav', fs, myrecording)  # Save as WAV file for debugging
        if prediction[:, 1] != 0.0:
            print("Wake word detected")
            break
        else:
            print("Recognition failed")


if __name__ == '__main__':

    start_char = input("Press Enter to start: ")
    if start_char != "":
        print("Exiting")
        exit()
    else:
        wwd_thread = threading.Thread(
            target=listener, name="Wake-Word-Detection-Thread")
        wwd_thread.start()
        wwd_thread.join()
    print("\nComplete")
