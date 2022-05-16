def asr():

    import argparse
    import os
    import queue
    import sounddevice as sd
    import vosk
    import sys
    import json

    q = queue.Queue()

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    device_info = sd.query_devices(device=None, kind='input')
    samplerate = int(device_info['default_samplerate'])
    try:
        model = "speech-recognition/vosk-models/vosk-model-en-in-0.4"
        if not os.path.exists(model):
            print(
                "Please download a model for your language from https://alphacephei.com/vosk/models")
        model = vosk.Model(model)

        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=None, dtype='int16',
                               channels=1, callback=callback):
            # int16: 16-bit audio format
            print('#' * 80)
            print('Press Ctrl+C to stop the recording')
            print('#' * 80)
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

    except KeyboardInterrupt:
        print('\nDone')
    except Exception as e:
        print("Exception: {}".format(e))


if __name__ == '__main__':
    print("\n")
    start_char = input("{} Press Enter to start {}".format('='*20, '='*20))
    if start_char != "":
        print("Please press Enter")
    else:
        spoken = asr()
        print(spoken)
