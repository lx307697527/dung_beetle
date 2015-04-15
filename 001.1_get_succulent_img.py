import re, urllib, random

list_1=["http://www.yuhuagu.com/duorou/2012/0704/3534.html",]
for n in range(1,8):
    raw_s = "http://www.yuhuagu.com/duorou/2012/0704/3534_%s.html" % n
    list_1.append(raw_s)
print list_1


for n in list_1:
    s = urllib.urlopen(n)
    html = s.read()
    def getImg(html):
        reg = r'<p align=.*? src="(.*?)" \/></p>'
        com_reg = re.compile(reg)
        url_list = re.findall(com_reg, html)
        for x in url_list:
            urllib.urlretrieve(x, './succulent/%s.jpg' % random.randint(100,1000))
        
    getImg(html)

