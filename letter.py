from bs4 import BeautifulSoup

from constants import *


class Letter:
    def __init__(self, session):
        self.session         = session

        self.trainUnitCd     = "" 
        self.trainUnitEduSeq = ""
        self.traineeMgrSeq   = ""
    

    def first_find(self):
        res = self.session.get(THE_CAMP_2, headers=REAQUEST_HEADERS)
        soup = BeautifulSoup(res.text, 'html.parser')

        aries = soup.findAll('div', {'class', 'cafe-card-box'})
        
        for idx, army in enumerate(aries):
            print(idx+1, '-', army.find('div', {'class', 'id'}).text.replace(" ", "").replace("\n", ""))

        choose_num = int(input('번호 : '))
            
        army = aries[choose_num-1].find('a', {'class', 'btn-green'})['href'][26:-1]

        self.trainUnitEduSeq = eval(army)[0]
        self.trainUnitCd = eval(army)[1]

    
    def second_find(self):
        request_data = {
            'divType'            : '1',
            'noticeMgrSeq'       : '',
            'trainUnitCd'        : self.trainUnitCd,
            'trainUnitTypeCd'    : '',
            'trainUnitEduSeq'    : self.trainUnitEduSeq,
            'trainCafeContentSeq': '', 
            'enterPageType'      : 'main'
        }

        req = self.session.post(THE_CAMP_VIEW_CONSOLE_LETTER, headers=REAQUEST_HEADERS, data=request_data)
        
        soup = BeautifulSoup(req.text, 'html.parser')
            
        self.traineeMgrSeq = soup.find('a', {'class', 'letter-card-box'})['href'][26:-3]

    
    def find_army(self):
        self.first_find()
        self.second_find()

    
    def send_letter(self, title, content):
        data = {
            'boardDiv'                        : 'sympathyLetter',
            'tempSaveYn'                      : 'N',
            'sympathyLetterEditorFileGroupSeq': '',
            'fileGroupMgrSeq'                 : '',
            'fileMgrSeq'                      : '',
            'sympathyLetterMgrSeq'            : '',
            'traineeMgrSeq'                   : self.traineeMgrSeq,
            'sympathyLetterContent'           : content,
            'sympathyLetterSubject'           : title
        }

        req = self.session.post(THE_CAMP_SEND_LETTER, headers=REAQUEST_HEADERS, data=data)