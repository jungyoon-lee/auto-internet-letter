import requests
import json
from bs4 import BeautifulSoup

from constants import *


def main_board():
    res = requests.get(naver_popular_news)
    news_soup = BeautifulSoup(res.content, 'html.parser')
    
    num1_list = news_soup.findAll('li', {'class', 'num1'})
    num2_list = news_soup.findAll('li', {'class', 'num2'})
    num3_list = news_soup.findAll('li', {'class', 'num3'})
    num4_list = news_soup.findAll('li', {'class', 'num4'})
    num5_list = news_soup.findAll('li', {'class', 'num5'})

    news_list = num1_list + num2_list + num3_list + num4_list + num5_list
    # news_list = num1_list

    link_list = list()
    for article in news_list:
        try:
            link_list.append(naver_news + article.find('dt').find('a')['href'])
        except:
            pass
    
    return link_list


def parse_article(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')

    article_title = soup.find('div', {'class', 'article_info'}).find('h3').text
    article_content = soup.find('div', {'class', '_article_body_contents'}).text

    return article_title, '<b>' + article_title + '</b><br><br>' + article_content


def naver_start():
    link_list = main_board()
    
    title_list = list()
    article_list = list()
    for link in link_list:
        title, article = parse_article(link)
        title_list.append(title)
        article_list.append(article)
    
    return title_list, article_list