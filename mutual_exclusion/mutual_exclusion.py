# Two shoppers adding items to a shared notepad

import threading
import time

garlic_count = 0
pencil = threading.Lock()


def shopper():
    global garlic_count
    pencil.acquire()
    for i in range(15):
        print (threading.current_thread().getName(), " is thinking")
        time.sleep(0.5)
        garlic_count += 1
    pencil.release()

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print ("No of garlic we need to buy: ", garlic_count)
