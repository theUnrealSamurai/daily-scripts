"""
use this tool to remove all the json files in the backup that you take from the google photos.
"""


import os  
from glob import glob
from tqdm import tqdm

path = '/home/roshan/Pictures/test/*/*'

log = open('log.txt', 'w')
log.write("The list of deleted files:\n")

count = 0

for file in tqdm(glob(path)):
    if file.split('.')[-1] == 'json':
        log.write(file + '\n')
        os.remove(file)
        count += 1

log.write("\nTotal number of files deleted: " + str(count))
log.close()
