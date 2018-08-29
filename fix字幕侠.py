# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

baidu = []
magnet = []
emule = []

fix_url = input('请输入剧集地址\n格式为: http://www.zimuxia.cn/portfolio/[剧集名]\n')
#fix_url = 'http://www.zimuxia.cn/portfolio/%e6%9c%89%e5%ae%b6%e5%8f%af%e5%bd%92%e7%9a%84%e6%81%8b%e4%ba%ba%e4%bb%ac'
       
r = requests.get(fix_url, headers={'content-type': 'text/html; charset=UTF-8', 'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')


baidu_text = soup.find_all('a', text='百度网盘')
if baidu_text != None:
    for i in baidu_text:
        baidu_parent = i['href']
        baidu.append(baidu_parent)
        
magnet_text = soup.find_all('a', text='磁力下载')
if magnet_text != None:
    for i in magnet_text:
        magnet_parent = i['href']
        magnet.append(magnet_parent)

emule_text = soup.find_all('a', text='电驴下载')
if emule_text != None:
    for i in emule_text:
        emule_parent = i['href']
        emule.append(emule_parent)

        
fp = open(os.getcwd() + r'\\fix字幕组.txt', 'at+', encoding='utf-8')


        
        
if baidu == []:
    print('无百度云链接')
else:
    fp.write('百度网盘:' + '\n')
    for i in range(len(baidu)):
        fp.write(baidu[i] + '\n')

        
if magnet == []:
    print('无磁力链')
else:
    fp.write('磁力链:' + '\n')
    for j in range(len(magnet)):
        fp.write(magnet[j] + '\n')

if emule == []:
    print('无ed2k链接')
else:
    fp.write('ed2k链接:' + '\n')
    for k in range(len(emule)):
        fp.write(emule[k] + '\n')
        
        
        
fp.close()
