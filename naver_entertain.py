import requests
import bs4
from bs4 import BeautifulSoup
from datetime import datetime

from constants import *


def bring_top_rank_urls(main_url=naver_entertain):
    res = requests.get(main_url)
    content = BeautifulSoup(res.content, 'html.parser')
    rankList = content.find('div', class_="rank_lst")

    ass = rankList.find_all('a')

    urls = []
    for a in ass:
        urls.append(main_url[:-8] + a.get('href'))
    
    return urls


def parsing(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    title = soup.find('h2', class_="end_tit").text
    author = soup.find('span', class_="author").find('em').text
    body = soup.find('div', id="articeBody").text

    bodybody = list()

    return title[4:], body, author


def naver_entertain():
    # 10개가 최대
    now = datetime.now()

    urls = bring_top_rank_urls()

    for i in range(10):
        title, content, author = parsing(urls[i])

        filename = './letter/entertain/' + str(now.year)[2:] + str(now.month) + str(now.day) + '_' + str(i + 1) + '.txt'

        f = open(filename, 'w')
        f.write('<p>' + title + '</p><br>')

        f.write('<p>')
        for q in content:
            f.write(q)
            if q == '.':
                f.write('</p><br>\n<p>')
        f.write('</p>')

        f.close()