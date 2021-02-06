import requests
from bs4 import BeautifulSoup
import platform
from selenium import webdriver

# https: // gogoanime.sh/great-teacher-onizuka-episode-1

# set chromedriver to interact with chrome.exe to scrape webpage
if (platform.system() == 'Windows'):
	driver = webdriver.Chrome("chromedriver/chromedriver_win32.exe")
elif (platform.system() == 'Linux'):
	driver = webdriver.Chrome("chromedriver/chromedriver_linux64")
else:
	print("\nqPull will not work with this operating system.")


def generate_links(anime_name, no_of_episodes):
    """This function generates the links by adding the gogoanime website domain anime name and the episode number and returns a list with all links"""
    domain = "https://gogoanime.sh/"
    for episode_number in range(no_of_episodes):
        link = domain + anime_name + "-episode-" + episode_number


if __name__ == '__main__':
    anime_name = input("Enter the name of the anime seperated by \"_\": ")
    no_of_episodes = input("Enter the number of episodes you want to download: ")
    links = generate_links(anime_name, no_of_episodes)

    