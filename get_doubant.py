#使用BeautifulSoup获取豆瓣新片榜， 口碑榜， 票房榜

import re, urllib
from bs4 import BeautifulSoup

raw_url = 'http://movie.douban.com/chart'
html = urllib.urlopen(raw_url).read()


reg_name = r'<img src=".*" alt="(.*?)" class=""/>'
reg_introduction = r'<p class="pl">(.*)</p>'
reg_score= r'<span class="rating_nums">(.*?)</span>'
reg_evalute = r'<span class="pl">\((.*)\)</span>'

print '豆瓣新片排行榜'
print '-' * 80

class DBM(object):
    def __init__(self, reg, html):
        self.reg, self.html = reg, html
    def __iter__(self):
        return self  #instance self is iteration object, so return self
    
    def get(self):
        m_list = re.findall(self.reg, self.html)
        u_list =[]
        for abc in m_list:
            u_abc = abc.decode('utf-8')
            u_list.append(u_abc)
        return u_list

name = DBM(reg_name, html)
a = name.get

intro = DBM(reg_introduction, html)
b = intro.get

score = DBM(reg_score, html)
c = score.get

evaluate = DBM(reg_evalute, html)
d = evaluate.get


def index(num):
    print a()[num], ' ',  b()[num], ' ', 'Score:%s'%(c()[num]),' ', d()[num]
    print ''

nn = len(a())
for x in range(nn):
    index(x)


# use bs4
soup = BeautifulSoup(html)

#本周口碑榜
week = soup.find('div', id='ranking').find('ul', id='listCont2')
print '-' * 80
print '本周口碑榜....', soup.find('div', id='ranking').find('ul', id='listCont2') \
      .find('li').get_text()
for link in week.find_all('a'):
    print link.get_text()


#北美票房榜影名
week_name = soup.find('div', id='ranking').find('ul', id='listCont1')
america = []
for link in week_name.find_all('a'):
    america.append(link.get_text())

#票房榜的钱
money = soup.find('div', id='ranking').find('ul', id='listCont1')
dollar = []
for m in money.find_all('span'):
    dollar.append(m.get_text())
m_date = dollar.pop(0)

def split(num2):
    print america[num2], dollar[num2]


print '-' * 80
print '北美票房榜....', m_date

lens = len(america)
for num2 in range(lens):
    split(num2)



