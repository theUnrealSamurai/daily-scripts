import requests
from bs4 import BeautifulSoup
import platform
from selenium import webdriver

# https: // gogoanime.sh/great-teacher-onizuka-episode-1

# set chromedriver to interact with chrome.exe to scrape webpage
# if (platform.system() == 'Windows'):
# 	driver = webdriver.Chrome("chromedriver/chromedriver_win32.exe")
# elif (platform.system() == 'Linux'):
# 	driver = webdriver.Chrome("chromedriver/chromedriver_linux64")
# else:
# 	print("\nqPull will not work with this operating system.")


def generate_links(anime_name, no_of_episodes):
    """This function generates the links by adding the gogoanime website domain anime name and the episode number and returns a list with all links"""
    
    page_links = [] #list to store the address of the main anime webpage
    domain = "https://gogoanime.sh/"
    for episode_number in range(no_of_episodes):
        page_link = domain + anime_name + "-episode-" + str(episode_number+1) #adding 1 cause the python index starts from 0 
        page_links.append(page_link)
    return page_links


def scrape_download_page_link(page_links):
    """Takes in the main anime page link and returns the download page links"""
    pass 


if __name__ == '__main__':
    anime_name = input("Enter the name of the anime seperated by \"-\": ")
    no_of_episodes = int(input("Enter the number of episodes you want to download: "))
    page_links = generate_links(anime_name, no_of_episodes)
    print(page_links[3])