import os
from time import sleep 
import subprocess

def open_stream_and_shutdown():
    os.system("google-chrome https://www.twitch.tv/brawlhalla")
    os.system("firefox https://www.twitch.tv/brawlhalla")
    os.system("shutdown +75")


def time():
    pass


def failsafe_shutdown():
    sleep(4200)
    subprocess.Popen(['notify-send', "Yo! This thing haven't died yet"])
    print("shit executed man")


if __name__ == '__main__':
    open_stream_and_shutdown()
    failsafe_shutdown()    

