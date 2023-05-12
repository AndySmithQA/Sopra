from multiprocessing import Process, Queue
import os
def my_funct(*args):
    queue = args[0]

    word = ""
    while word != "END":
        word = queue.get()
        if len(word) == 15:
            print(os.getpid(), ':', word)

def main():
    queue = Queue()

    p1 = Process(target=my_funct, args=(queue, "1"))
    p2 = Process(target=my_funct, args=(queue, "2"))

    p1.start()
    p2.start()

    for line in open("words.txt"):
        queue.put(line[:-1])

    queue.put("END")
    queue.put("END")

    p1.join()
    p2.join()
    print("ALL DONE")

if __name__ == "__main__":
    main()


# def myfunct(*args):
#     print("From Proc", args)
#
# def main():
#     p1 = Process(target=myfunct, args="1")
#     p2 = Process(target=myfunct, args="2")
#
#     p1.start()
#     p2.start()
#
#     print("From Main")
#
#     p1.join()
#     p2.join()
#
# if __name__ == "__main__":
#     p1 = Process(target=myfunct, args="1")
#     p1.start()
#     p1.join()