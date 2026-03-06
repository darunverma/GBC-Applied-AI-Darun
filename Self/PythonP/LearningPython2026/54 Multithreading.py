# Multithreading & Multiprocessing | 54

"""
What is thread? 
Could be created by : Class or Function

A thread is a process, a lightweight process.

Why do we need threads?
To allow system to handle multiple work simultaneously as 1 thread could handle 1 work.


How thread works?



Multiprocessing/ Multi-core



"""

from threading import Thread        # External package, where Thread is actually a class.
from time import sleep,time

start = time()

class Hello(Thread):            # Just like in order to make a class an abstract class, just become the child of the abstract class. Similarly, inherit Thread class.
    def run(self):
        for i in range(4):
            print('Hello',i+1)
            sleep(0.3)          # To delay the processes manually

class Hi(Thread):
    def run(self):
        for i in range(4):
            print('Hi',i+1)
            sleep(0.2)


if __name__ == '__main__':
    obj1 = Hello()
    obj2 = Hi()

    obj1.start()            # For a thread to run : 1. Class must have run() method | 2. Thread must be started by calling using start() method > run() method.
    obj2.start()

    # I want the main thread to only work once these two threads would be completed.
    obj1.join()
    obj2.join()

    end = time()
    print('Threads completed, Time taken by processes : ',end-start)


# In case if I want these two functions to run parallely, I have to use multi-threading.

"""
Syntax of using Multi-Threading in Functional Programming where the classes aren't defined. 

obj3 = Thread(target=Hello.run())       # If class exist

obj3 = Thread(target=run)             # No class


"""

"""
If we are running multiple threads, it doesn not mean that the python code is being ran on multi-core as well.

Python has GIL (Global Infrential Lock) which would lock one thread and run another thread and this happens so one but it would take time for the switching. 

If our system would run the code at multi core/ multi process then multi threading would become extrememly fast.

Thread is a light weight process that shares memory and GIL; however, each process would have their own GIL and own memory.

"""
from multiprocessing import Process

def do1():
    for i in range(10):
        print("Process 1")


def do2():
    for i in range(10):
        print("Process 2")


if __name__ == '__main__':
        obj1 = Process(target=do1)
        obj2 = Process(target=do2)

        start = time()
        obj1.start()
        obj2.start()

        obj1.join()
        obj2.join()
        end = time()

        print('Processes completed, Time taken by processes : ',end-start)

"""
In depends which one to prefer, THREAD or PROCESS. 
"""
