from login import Myinfo
from letter import Letter
from naver_news import *
from naver_sports import *


if __name__ == '__main__':
    myinfo = Myinfo()
    myinfo.login()

    letter = Letter(session=myinfo.login_session)
    letter.find_army()
    
    title_list, content_list = naver_start()
    
    # title_list, content_list = sports_start()
    
    for i in range(len(title_list)):
        print(title_list[i])
        letter.send_letter(title_list[i], content_list[i])