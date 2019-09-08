# Threads that waste CPU cycles

import os
import threading

# a simple function that wastes cpu cycles forever
def cpu_waster():
    while True:
        pass


# display information about this process
print ("Process ID: ", os.getpid())
print ("Thread Count: ", threading.active_count())

for thread in threading.enumerate():
    print (thread)


print ("Starting 4 CPU wasters")

for i in range(4):
    threading.Thread(target=cpu_waster).start()

# display information about this process
print ("PROCESS ID: ", os.getpid())
print ("Thread Count: ", threading.active_count())

for thread in threading.enumerate():
    print (thread)
