from threading import Thread
import time
def myfunct(*args):
    print("From Thread: ", args)
    time.sleep(1)

def myOther(*args):
    time.sleep(5)
    print("From Thread: ", args )

th1 = Thread(target=myfunct, args="1")
th2 = Thread(target=myfunct, args="2")
th3 = Thread(target=myOther, args="3")
th1.start()
th2.start()
th3.start()
print("From Main")
th3.join()
th1.join()
th2.join()
print("The End")
