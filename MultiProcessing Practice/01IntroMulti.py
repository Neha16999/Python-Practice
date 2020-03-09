import os
from multiprocessing import Process, current_process


def square(number):
    result = number * number
    process_id=os.getpid()
    print(f"Process ID : {process_id}")
    print(f"The {number} square is {result}")
    process_name=current_process().name
    print(f"Process Name : {process_name}")


if __name__=='__main__':
    processes=[]
    numbers=[1,2,3,4]

    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)
        # the created process will start using start()
        process.start()

