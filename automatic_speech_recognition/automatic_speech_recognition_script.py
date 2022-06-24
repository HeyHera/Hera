import os
import queue
import sounddevice as sd
import vosk
import sys
import json

q = queue.Queue()

device_info = sd.query_devices(device=None, kind='input')
samplerate = int(device_info['default_samplerate'])

model_path = "automatic_speech_recognition/vosk-models/vosk-model-en-in-0.4"
if not os.path.exists(model_path):
    print(
        "Please download a model for your language from https://alphacephei.com/vosk/models.")
    exit()

model = vosk.Model(model_path)


def callback(indata, frames, time, status):
    # This is called (from a separate thread) for each audio block
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def asr():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=None, dtype='int16',
                           channels=1, callback=callback):
        # int16: 16-bit audio format
        print("I'M LISTENING")
        # Audio in wav mono format
        rec = vosk.KaldiRecognizer(model, samplerate)
        spoken_words = []
        while len(spoken_words) != 1:
            data = q.get()
            if rec.AcceptWaveform(data):
                spoken_words.append(rec.Result())
                y = json.loads(spoken_words[0])
                return(y['text'])
            # else:
            #     print(rec.PartialResult())


if __name__ == '__main__':
    start_char = input("Press Enter to start: ")
    if start_char != "":
        print("Exiting")
        exit()
    else:
        spoken = asr()
        print(spoken)
