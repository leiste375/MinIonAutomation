from os import path, listdir
import time
from sys import exit

def directory_scan(input_dir):
    running_set = set()

    while path.exists(input_dir):
        time.sleep(1)
        current_set = frozenset(listdir())
        #Unit in seconds
        for i in current_set:
            if i not in current_set.intersection(running_set):
                print(f'Found new file: {i}')
                running_set.add(i)
            else:
                #print(f'Item {i} already found')
                pass
    else:
        exit("Input directory does not exist.")