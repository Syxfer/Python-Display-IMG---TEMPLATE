import os
import sys
import subprocess
import multiprocessing
import time

def task_one():
    while True:
        time.sleep(1)

def task_two():
    while True:
        time.sleep(1)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=task_one)
    process2 = multiprocessing.Process(target=task_two)

    process1.start()
    process2.start()