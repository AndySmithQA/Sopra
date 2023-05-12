from threading import Thread, Lock
import time

csListBuilder = Lock()

list_to_build = []

def list_builder(*elements):
    global list_to_build

    csListBuilder.acquire() #Initiate the lock

    list_to_build.extend(elements)
    print(list_to_build)

    csListBuilder.release() #Allows other processes and threads

th1 = Thread(target=list_builder, args=(1,2,3))
th2 = Thread(target=list_builder, args=(4,5,6))
th3 = Thread(target=list_builder, args=(7,8,9))
th4 = Thread(target=list_builder, args=(10,11,12))

th1.start()
th2.start()
th3.start()
th4.start()

list_builder(13,14,15)

th1.join()
th2.join()
th3.join()
th4.join()

print("The Final list: ", list_to_build)
