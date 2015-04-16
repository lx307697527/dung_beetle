import re, urllib

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
