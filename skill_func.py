import time

def sender(pipe_end):
    """
    function to send messages to other end of pipe
    """
    msg = "Playing the song Faded"
    pipe_end.send(msg)
    print("Sent the message: {}".format(msg))
    pipe_end.close()
    time.sleep(5.0)