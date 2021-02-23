#!/usr/bin/env python3
#this above line is called the shebang line, which allows you to run the script on background with the nohup command
# you also gotta change the permission for the file which is "chmod +x auto_twitch.py" navigate to the folder where the file is present then type the command
# this whole thing was the command for me "nohup python3 /home/samurai/Code/daily-scripts/auto_twitch.py &"

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

# yet another fail safe shutdown
schedule.every().wednesday.at("00:35").do(os.system, "shutdown -h now")
schedule.every().saturday.at("00:35").do(os.system, "shutdown -h now")


while True:
    schedule.run_pending()
    sleep(60)

