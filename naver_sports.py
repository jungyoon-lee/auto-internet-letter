import requests
import json
from bs4 import BeautifulSoup

from constants import *


def main_board():
    urls = list()

    res = requests.get(naver_sports_news)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    dives = soup.findAll('a', {'class', 'title'})[:10]
    
    for div in dives:
        urls.append('https://sports.news.naver.com' + div['href'])
    
    return urls


def parse_article(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')

    article_title = soup.find('h4', {'class', 'title'}).text
    article_content = soup.find('div', {'class', 'news_end'}).text.replace("\n", "")

    return article_title, '<b>' + article_title + '</b><br><br>' + article_content


def sports_start():
    urls = main_board()
    
    title_list = list()
    content_list = list()
    for url in urls:
        title, content = parse_article(url)
        title_list.append(title)
        content_list.append(content)

    return title_list, content_list