import os
import time
from multiprocessing import Process, current_process


def square(numbers):
    for number in numbers:
        time.sleep(0.005)
        result = number * number
        print(f"The {number} square is {result}")


if __name__=='__main__':
    processes=[]
    numbers=range(100)

    for i in range(50):
        process = Process(target=square, args=(numbers,))
        processes.append(process)
        # the created process will start using start()
        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing Complete")
