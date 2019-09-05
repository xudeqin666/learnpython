from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
from bs4 import BeautifulSoup
import requests
import re
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#name=name.translate(non_bmp_map)
fp=open("D:\\微信爬\\LearnAndRecord.txt","a",encoding='utf-8')
with open ("LearnAndRecord.txt" ,'r') as f:
    for url in f:
#url="http://mp.weixin.qq.com/s?__biz=MzU1MDQwNTgzMg==&mid=2247485713&idx=1&sn=df1586ee476dca8908188f5b691bf4c9&chksm=fba05ab6ccd7d3a0da3c03c8038ed7f63eef331f75bffe274a4fd32ac8c1943d7f28423530f1#rd"
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers={'User-Agent':user_agent}
        r = requests.get(url,headers=headers)  #客运网页'https://ks.wjx.top/m/27600317.aspx#'
        #print (r.text)
        soup = BeautifulSoup(r.text,'lxml')
        titles=soup.find_all("p")
        for title in titles:
            #print(title)
            head=title.get_text(strip=True)
            head=head.translate(non_bmp_map)
            if head!='' and "微信号" not in head and "听力" not in head and "功能介绍" not in head and '导读'not in head and head!="1" and head!="2":
                fp.write(head + '\n')
                print(head)
            if '翻译组' in head :
                        #print(head)
                break
