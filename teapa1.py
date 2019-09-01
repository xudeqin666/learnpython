# coding:utf-8 #
import time
import pickle
import re
from selenium import webdriver
from urllib import request
from http import cookiejar
import os
import sys
from urllib import parse
from http import cookiejar
from bs4 import BeautifulSoup
##filepath="C:\\Users\徐进\Desktop"
##filename="tea2015"
fp=open("D:\\tea\\2019 0420-0330tea.txt","w",encoding='utf-8')
#fp=open(filepath+filename+".txt","a",encoding='utf-8')
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#name=name.translate(non_bmp_map)
def tea_pa():
    #browser.find_element_by_xpath("/html/body/div[2]/div/div/p[1]/a[2]").click()#英文界面
    r=browser.page_source
    soup = BeautifulSoup(r,'lxml')
    #titles=soup.find_all("div",class_="col-md-12")
    titles=soup.find_all([re.compile(r'h\d'),"p"])
    for title in titles:
        head=title.get_text().translate(non_bmp_map)
        if head!=" " and "�" not in head and "©" not in head:
            fp.write(head + '\n')#写入标题
            #print(head)
    
browser = webdriver.Chrome()
#browser = webdriver.Firefox()
browser.get("https://tea.share2china.com/issue/2019")
browser.find_element_by_xpath('//*[@id="username"]').send_keys('xw64')
browser.find_element_by_xpath("/html/body/div[2]/div/div/form/div/div/span/button").click()
time.sleep(3)
all_list=browser.find_elements_by_class_name("btn-group")
all_number=len(all_list)  #2015年51期杂志 #2016年53期 2017第一个没有双语从第二开始53
print(all_number)
for n in range(3,7):
    time.sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[%d]/a/button"%n).click()#第几期杂志
    time.sleep(3)
    class_list=browser.find_elements_by_class_name("binode")#有几个双语文章
    long=len(class_list)+1
    #print(long)
    for i in range(1,long):
    #browser.find_elements_by_class_name("binode")[1].next.click()
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div/ol[1]/li[%d]/a"%i).click()
        browser.find_element_by_xpath("/html/body/div[2]/div/div/p[1]/a[2]").click()#英文界面
        time.sleep(3)#页面反应一下
        tea_pa()
        browser.back()#返回双语界面
        tea_pa()
        browser.back()#返回双语目录
    browser.back()#总界面
fp.close()
browser.close()
os.system('taskkill /im chromedriver.exe /F')

