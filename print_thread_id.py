# SuperFastPython.com
# report pid and thread name for each worker process in the process pool
from time import sleep
from os import getpid
from os import getppid
from threading import current_thread
from concurrent.futures import ProcessPoolExecutor
 
# target task function
def work(value):
    sleep(0.1)
    # report the worker process details
    print(f'Worker pid={getpid()}, ppid={getppid()} thread={current_thread().name}')
 
# entry point
if __name__ == '__main__':
    # report the main process details
    print(f'Main pid={getpid()}, ppid={getppid()} thread={current_thread().name}')
    # create a process pool
    with ProcessPoolExecutor(2) as executor:
        # submit some tasks
        _ = executor.map(work, range(2))