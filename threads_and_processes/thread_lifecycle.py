# Two threads cooking soup

import threading
import time

# another way to create a thread
class ChefOlivia(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print ("Olivia started and waiting for the sausage to thaw..")
        time.sleep(3)
        print ("Olivia is done cutting sausage")

# main thread aka Barron
if __name__ == "__main__":
    # new thread started
    print ("Barron started and is rquesting Olivia's help")
    olivia = ChefOlivia()
    print ("Olivia alive? ", olivia.is_alive())

    # new thread running
    print ("Barron tells olivia to start")
    olivia.start()
    print ("Olivia alive? :", olivia.is_alive())

    print ("Barron continues cooking soup")
    time.sleep(0.5)
    print ("Olivia alive? ", olivia.is_alive())
    # thread is blocked

    print ("Barron patiently waits for Olivia to finish and join")
    olivia.join()
    print ("Olivia alive? ", olivia.is_alive())

    print ("Barron and Olivia are both done")
    # thread is terminated
