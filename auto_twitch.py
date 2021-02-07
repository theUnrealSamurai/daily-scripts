#!/usr/bin/env python3

import os
from time import sleep 
import schedule

def open_stream_and_shutdown():
    os.system("google-chrome https://www.twitch.tv/brawlhalla")
    os.system("firefox https://www.twitch.tv/brawlhalla")
    os.system("shutdown +75")
    
    #An extray layer of fail safe shutdown 
    sleep(4500)
    os.system("shutdown -h now")

schedule.every().tuesday.at("23:27").do(open_stream_and_shutdown)
schedule.every().friday.at("23:27").do(open_stream_and_shutdown)

while True:
    schedule.run_pending()
    sleep(60)

