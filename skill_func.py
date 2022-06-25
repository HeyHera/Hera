import random
import subprocess
import time
import multiprocessing

def play_vlc(s_path):
    vlc_path = "/usr/bin/vlc"
    subprocess.Popen([vlc_path, s_path], stderr=subprocess.STDOUT)
    print("Playing complete")


def sender(pipe_end):
    """
    function to send messages to other end of pipe
    """
    site_list=['Google','Yahoo','Microsoft','APKpure','APKMB','Stackoverflow','Bing']
    msg=random.choice(site_list)
    # msg = "Playing the song Faded"
    pipe_end.send(msg)
    pipe_end.close()
    print("Sleeping for 5 sec")
    time.sleep(5)
    print("Sleep finished")
    multiprocessing.Process(target=play_vlc, args=('../Music/sample.mp3',)).start()