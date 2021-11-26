from glob import glob
import subprocess
from tqdm import tqdm


def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

total_time = 0
for video in tqdm(glob("/media/samurai/Code/GATE/8. TOC & Compiler Design/*/*/*.mp4")):
    total_time += get_length(video)


print(f"There are {total_time/3600} hours of content")
# videos = glob("/media/samurai/Code/GATE/*/*/*/*.mp4")
