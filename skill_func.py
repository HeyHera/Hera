import random
import subprocess
import time

def sender(pipe_end):
    """
    function to send messages to other end of pipe
    """
    site_list=['Google','Yahoo','Microsoft','APKpure','APKMB','Stackoverflow','Bing']
    msg=random.choice(site_list)
    # msg = "Playing the song Faded"
    pipe_end.send(msg)
    print("Sent the message: {}".format(msg))
    pipe_end.close()
    print("Sleeping 5 sec")
    vlc_path = "/usr/bin/vlc"
    time.sleep(5)
    subprocess.call([vlc_path, '../Music/sample.mp3'], stderr=subprocess.STDOUT) 

    print("Sleep finished")