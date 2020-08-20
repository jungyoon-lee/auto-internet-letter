from getpass import getpass
import requests
from bs4 import BeautifulSoup

from constants import *


class Myinfo:
    def __init__(self):
        self.email = ""
        self.password = ""

        self.login_session = None
        self.my_name = ""


    def make_login_request(self, email   : str = 'leejungyoon@gmai.com',
                                 password: str = 'bobforever'):
        return {
            "userId": email,
            "userPwd": password,
            "state": "email-login",
            "autoLoginYn": "N",
            "withdrawDate": "",
            "telecomCd": "",
            "telecomNm": "",
            "osType": "",
            "osVersion":"",
            "deviceModel": "",
            "appVersion": "",
            "deviceWidth": "",
            "deviceHeight": "",
            "resultCd": "",
            "resultMsg": ""
        }


    def check_login(self, soup):
        try:
            myname = soup.find('span', {'class', 'name'}).text
        except:
            print('-----------------로그인 실패------------------')
            return False

        return myname
    

    def login(self):
        while True:
            # self.email    = input('이메일을 입력하세요   : ')
            # self.password = getpass('비밀번호를 입력하세요 : ')                

            with requests.Session() as sess:
                login_request = self.make_login_request(email   =self.email,
                                                        password=self.password)
                res = sess.post(THE_CAMP_LOGIN_URL, headers=REAQUEST_HEADERS, data=login_request)

                login_get = sess.get(THE_CAMP_MEMBER_URL, headers=REAQUEST_HEADERS)
                login_soup = BeautifulSoup(login_get.text, 'html.parser')
                username = self.check_login(login_soup)

                if username != False:
                    print("로그인 성공 : {}".format(username))
                    print('')

                    self.login_session = sess
                    self.my_name = username
                    return sess
