import multiprocessing
import skill_func as skill

if __name__ == "__main__":
    pipe_begin, pipe_end = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=skill.sender, args=(pipe_end,))
    p1.start()
    msg = pipe_begin.recv()
    pipe_begin.close()
    print("Received the message: {}".format(msg))
    p1.join()