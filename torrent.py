# 种子搜索


import requests
import bs4
import re #re库是正则表达式库
import os #os库是文件夹操作
from bs4 import BeautifulSoup
import time
import shutil

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_options.add_experimental_option("prefs",prefs)


fp = open(os.getcwd() + r'\\种子.txt', 'at+', encoding='utf-8')
no = ['ARM-598', 'GVG-481','REXD-309','TPPN-151','REAL-632', 'HQIS-026', 'CEAD-217', 'MEYD-250']
for t in no:
    pagelink = 'http://www.aoyoso.cc/search/' + t +'_ctime_1.html'
    r = requests.get(pagelink, headers={'content-type': 'text/html; charset=UTF-8', 'User-Agent': 'Mozilla/5.0'})
    time.sleep(2)
    soup = BeautifulSoup(r.text, "html.parser", from_encoding="utf-8")
    dl = soup.find_all('div', class_='panel-body')


    #cookies = {'Cookie': '123'}

    for i in dl:
        title = i.find('h5').get_text()  #标题
        print(title)
        fp.write(title + '\n')
        content = i.find('table').get_text()   #种子信息
        print(content)
        fp.write(content + '\n')
        link2 = 'http://www.aoyoso.cc' + i.find('a')['href']
        print(link2)
        time.sleep(1)
        r = requests.get(link2, headers={'content-type': 'text/html; charset=UTF-8', 'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, "html.parser", from_encoding="utf-8")
        magnet = soup.find('textarea', class_='well magnet center').get_text() #磁力链接
        fp.write(magnet + '\n')
        fp.write('-----------------------------------------------------------------------------------------------------' + '\n' + '\n')
        print(magnet)
        
    fp.write('#########################################################################################################' + '\n' + '\n')

fp.close()