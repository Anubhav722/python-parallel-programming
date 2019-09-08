# processes that waste CPU cycles

import os
import multiprocessing as mp
import threading

# a simple function that wastes CPU cycles forever

def cpu_waster():
    while True:
        pass

if __name__ == '__main__':

    # display information about this process

    print ("Process ID: ", os.getpid())
    print ("Thread Count: ", threading.active_count())

    for thread in threading.enumerate():
        print (thread)

    print ("StartING 4 CPU wasters")
    for i in range(4):
        mp.Process(target=cpu_waster).start()

    # display information about this process
    print ("Process ID: ", os.getpid())
    print ("Thread Count: ", threading.active_count())
    for thread in threading.enumerate():
        print (thread)
