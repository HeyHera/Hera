# Code to execute in an independent thread
import time
  
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)
          
# Create and launch a thread
from threading import Thread
t = Thread(target = countdown, args =(10, ))
t.start()
for i in range(90, 100):
    print(i)
    time.sleep(1)