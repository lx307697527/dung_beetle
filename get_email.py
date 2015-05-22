#!/usr/bin/env python
import poplib
host = "pop3.163.com"
user = ""
password = ""

my = poplib.POP3(host)  #created a pop3 object, connected server at this time.
my.set_debuglevel(1)   #set the debug, you can see detail with the server.

my.user(user)
my.pass_(password)


'''
print my.stat()
#获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节.
    >>> *cmd* 'STAT'
    >>> *stat* ['+OK', '8', '154471']
    >>> (8, 154471)


print my.list()
#列出服务器上邮件信息，这个会对每一封邮件都输出id和大小,不象stat输出的是总的统计信息.
    >>> *cmd* 'LIST'
    >>> ('+OK 8 154471', ['1 2064', '2 21875',
    '3 2832', '4 2837', '5 22493', '6 21598', '7 58158', '8 22614'], 69)



for x in range(1, my.stat()[0]+1):
    mlist = zhan.top(x, 0)
    print len(mlist[1])
需要取出所有信件的头部，信件id是从1开始的
取出信件头部。注意：top指定的行数是以信件头为基数的，也就是说当取0行
其实是返回头部信息，取1行其实是返回头部信息之外再多1行
'''


down = my.retr(2)
'''取出一份完整的邮件，down[0]是返回状态信息， 邮件按行储存在down[1]
    print down    >>> ('+OK 2832 octets',[.....])
'''

for x in down[1]:  
    print x.decode('utf-8')
    
my.quit()
