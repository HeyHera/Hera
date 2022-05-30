from importlib.machinery import SourceFileLoader
from scipy.io.wavfile import write
# from tts.nix.models.TTS import NixTTSInference
import os

# Initiate Nix-TTS
NixTTSInference_module = SourceFileLoader(
        "NixTTSInference-Module", "tts/nix/models/TTS.py").load_module()


nix = NixTTSInference_module.NixTTSInference(model_dir = "tts/nix/models/nix-ljspeech-stochastic-v0.1")
def tts(text):
    print("\n" + text)
    # Tokenize input text
    c, c_length, phoneme = nix.tokenize(text)
    # Convert text to raw speech
    xw = nix.vocalize(c, c_length)

    # Listen to the generated speech
    # Audio(xw[0,0], rate = 22050)
    wav_file_path = "tts/audio_out/"
    path_exist = os.path.exists(wav_file_path)
    if not path_exist:
        # Create a new directory because it does not exist 
        os.makedirs(wav_file_path)
        print("{} directory is created".format(wav_file_path))

    write(wav_file_path+"voice.wav", 22050, xw[0,0])
    wav_file = wav_file_path+"voice.wav"
    os.system(f'aplay {wav_file}')
    os.remove(wav_file_path+"voice.wav")

if __name__ == '__main__':
    tts("I'll always love you 'cause we grew up together and you helped make me who I am. I just wanted you to know there will be a piece of you in me always, and I'm grateful for that. Whatever someone you become, and wherever you are in the world, I'm sending you love. You're my friend to the end")
