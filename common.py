from os import path, listdir
import time
from sys import exit

def directory_scan(input_dir):
    running_file_list = []

    while path.exists(input_dir):
        current_file_list = listdir()
        #Unit in seconds
        time.sleep(5)
        for i in current_file_list:
            print(f'Found a new file: {i}')
    else:
        exit("Input directory does not exist.")