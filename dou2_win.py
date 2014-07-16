#-*- coding: cp936 -*
#cp936
import urllib
import urllib2
import re
import time
import random

print '*'*20+'开始采集代理'+'*'*20
f = open('proxy_list.txt','w')
exp1 = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
exp2 = re.compile("(?isu)<td[^>]*>(.*?)</td>")
proxy_ua = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
proxyHtml = urllib2.Request(url="http://www.getproxy.jp/cn",headers=proxy_ua)
proxySocket = urllib2.urlopen(proxyHtml)
htmlSource = proxySocket.read()
for row in exp1.findall(htmlSource):
   for col in exp2.findall(row)[:1]:
    f.write(col+'\n')
f.close()

print '*'*20+'代理采集完成'+'*'*20
##########################################################################################3
print '/'*50
print '本程序主要采集豆瓣<请不要害羞>小组的图片'
print '采集的图片在文件夹Doubanimg内.'
print '代理采集程序没有验证，所以如果不成功请重新运行本程序.'
print '#'*50
print '#'*20 + 'By 肾虚公子' + '#'*20
print '#'*50

f0=open('proxy_list.txt','r')
dat0=f0.readlines()
f0.close()
proxy_SJ = random.choice(dat0)

proxy_handler = urllib2.ProxyHandler({'http':'%s'%proxy_SJ})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

print '请输入小组代码,默认害羞组[haixiuzu]'
Douban_group = raw_input('请输入小组ID(默认按回车继续):')or 'haixiuzu'
Douban_group_url = 'http://www.douban.com/group/'

def gethtml2(url2):
    Douban_ua = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
    Douban_Html = urllib2.Request(url=(url2),headers=Douban_ua)
    Douban_Socket = urllib2.urlopen(Douban_Html)
    html2 = Douban_Socket.read().decode('utf-8')
    return  html2

def gettoimg(html2):
    reg2 = r'http://www.douban.com/group/topic/\d+'
    toplist = re.findall(reg2,html2)
    x = 0
    for topicurl in toplist:
        x+=1
    return topicurl

def download(topic_page):
    reg3 = r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg'
    imglist = re.findall(reg3,topic_page)
    i = 1
    download_img = None
    for imgurl in imglist:
        img_numlist = re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            download_img = urllib.urlretrieve(imgurl,'Doubanimg/%s.jpg'%img_num)
            time.sleep(1)
            i+=1
            print (imgurl)
    return download_img

print '-'*50
print '请输入采集页码数,默认采集[10]页'
page_end = int(raw_input('请输入需要采集的页数(默认按回车继续):')or 10)
print '-'*50
print '正在采集图片中，请您耐心等待,程序可能用较长时间'
print '-'*50
print '如出现错误，请重新运行'
print '-'*50
num_end = page_end*25
num = 0
page_num = 1
while num<=num_end:
    html2 = gethtml2(Douban_group_url+Douban_group+"/discussion?start=%d"%num)
    topicurl = gettoimg(html2)
    topic_page = gethtml2(topicurl)
    download_img=download(topic_page)
    num = page_num*25
    page_num+=1

else:
    print('程序采集完成')