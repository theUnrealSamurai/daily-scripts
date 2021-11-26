import requests
from bs4 import BeautifulSoup
import platform
from selenium import webdriver

# https: // gogoanime.sh/great-teacher-onizuka-episode-1


def generate_links(anime_name, no_of_episodes):
    """This function generates the links by adding the gogoanime website domain anime name and the episode number and returns a list with all links"""
    
    page_links = [] #list to store the address of the main anime webpage
    domain = "https://gogoanime.pe/"
    for episode_number in range(no_of_episodes):
        page_link = domain + anime_name + "-episode-" + str(episode_number+1) #adding 1 cause the python index starts from 0 
        page_links.append(page_link)
    return page_links


def scrape_download_page_link(page_link):
    """Takes in the main anime page link and returns the download page link"""
    
    page = requests.get(page_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    temp_soup = soup.find("li", class_="dowloads")
    download_page_link = temp_soup.find('a')['href']

    return download_page_link


def trigger_download(download_page_link):
    page = requests.get(download_page_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    temp_soup = soup.find_all("div", class_ = "mirror_link")
    result = temp_soup[0].find_all('a')
    for i in result:
        print(i['href'])
    print(result)
    return result



if __name__ == '__main__':
    # anime_name = input("Enter the name of the anime seperated by \"-\": ")
    # no_of_episodes = int(input("Enter the number of episodes you want to download: "))
    # page_links = generate_links(anime_name, no_of_episodes)

    downloadpage = scrape_download_page_link("https://gogoanime.pe/great-teacher-onizuka-episode-1")
    trigger_download(downloadpage)