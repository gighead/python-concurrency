from threading import Thread
from multiprocessing import Process

from multiprocessing.managers import BaseManager
from queue import Queue
import time
import multiprocessing


class SumUpClass:

    def __init__(self):
        self.counter = 0

    def add_integers(self, start, end):
        for i in range(start, end+1):
            self.counter += i

    def get_counter(self):
        return self.counter


def single_thread():
    #instantiate objects
    obj = SumUpClass()
    start = time.time()
    obj.add_integers(1, 30000000)
    end = time.time() - start
    print(f"Single Threaded Execution time: {end} seconds and summed to {obj.counter}")


def multiple_threads():
    obj1 = SumUpClass()
    obj2 = SumUpClass()
    start = time.time()

    t1 = Thread(target=obj1.add_integers, args=(1, 1500000,), name='thread1')
    t2 = Thread(target=obj1.add_integers, args=(15000001, 30000000), name='thread2')

    t1.start()
    t2.start()

    t1.join() #waits untill the thread terminates
    t2.join()
    combined_sum = obj1.counter + obj2.counter
    end = time.time() - start
    print(f"multiple threads Execution time: {end} seconds and summed to {combined_sum}")


# def single_process(obj1, start, end):
#     obj1.add_integers(start, end)
if __name__ == "__main__":
    single_thread()
    multiple_threads()