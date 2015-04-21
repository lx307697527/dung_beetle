#模拟登录豆瓣，bs4截取 http://www.douban.com/doumail/ 豆邮

import urllib
import urllib2
import cookielib
import re
import random
from bs4 import BeautifulSoup


class DB(object):
    def __init__(self, email, passwd):
        self.url = "http://www.douban.com/accounts/login"
        self.post = {
            'form_email':email,
            'form_password':passwd,
            'source':'index_nav'
            }
        cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        self.response = self.opener.open(self.url, urllib.urlencode(self.post))

    def login(self):
        if self.response.geturl() == self.url:
            print 'logining...'
            html = self.response.read()
            reg = r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>'
            imglist = re.findall(reg, html)
            urllib.urlretrieve(imglist[0], '%d.jpg' % random.randint(1,100))
            captcha = raw_input('captcha is: ')
            regid = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
            ids = re.findall(regid, html)
            self.post["captcha-solution"] = captcha
            self.post["captcha-id"] = ids[0]
            self.post["user_login"] = "登录"
            self.post["redir"] = 'http://www.douban.com/doumail/'
            self.response = self.opener.open(self.url, urllib.urlencode(self.post))
            if self.response.geturl() == "http://www.douban.com/doumail/":
                print 'login success !'
                soup = BeautifulSoup(self.response.read())
                tag = soup.find_all('span', attrs={'class':'from'})
                tag2 =  soup.find_all('a', attrs={'class':'url'})
                a = []
                for x in tag:
                    a.append(x.get_text())
                b = []
                for y in tag2:
                    b.append(y.get_text())

                def split(num):
                    print a[num] + '  ' +  b[num]
                    print 
                    
                print '-'*30, '豆瓣豆邮', '-'*30
                for x in range(len(a)):
                    split(x)
                print '-'*80

email = raw_input('Your email: ')
passwd = raw_input('Your passwd: ')   
my = DB(email, passwd)         
my.login()


