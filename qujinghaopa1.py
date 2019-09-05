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
fp=open("D:\\qujinghao\\2018 12-00.txt","w",encoding='utf-8')
def qujingpa():
    r=browser.page_source
    soup = BeautifulSoup(r,'lxml')
    numbers=soup.find_all(class_="featured-image")
    #print(len(numbers))#查找有几篇文章
    end_num=len(numbers)+1
    for i in range(1,end_num):
        browser.find_element_by_xpath("/html/body/div/div/section/div[2]/div[%d]/article/div[2]/div[1]/h2/a"%i).click()
        time.sleep(3)
        r=browser.page_source          
        soup = BeautifulSoup(r,'lxml')
        titles=soup.find_all("p")
        for title in titles:
            #print(title)
            head=title.get_text(strip=True)
            if head!='' and "译者" not in head and "校对" not in head and '策划'not in head and "取经" not in head and "外刊" not in head and "Comment" not in head and "Name" not in head and "Email" not in head and "Website" not in head and "电子邮件地址不会被公开" not in head:#去除多余部分
                #print(head)#打印文章内容
                fp.write(head +'\n')
            if '❑' in head :
                #print(head)
                break
        browser.back()
browser = webdriver.Firefox()
#browser = webdriver.Chrome()
browser.get("https://qujinghao.com/")
r=browser.page_source
soup = BeautifulSoup(r,'lxml')
counts=soup.find_all('li')
print(len(counts))#有几个月的合集
end_yue=len(counts)+1
for n in range(1,2):#4是七月向下5是六月，
    browser.find_element_by_xpath("/html/body/div/div/aside/section[2]/ul/li[%d]/a"%n).click()
    #点击进入最上面那个月
    time.sleep(3)
    qujingpa()
    r=browser.page_source
    soup = BeautifulSoup(r,'lxml')
    if soup.find_all(class_="page-numbers")!=[]:
        num=soup.find_all(class_="page-numbers")
        page_num=len(num)-1
        print(page_num)
        for page in range(1,page_num):
            try:
                browser.find_element_by_css_selector(".next").click()
                qujingpa()
            except:pass
fp.close()
os.system('taskkill /im chromedriver.exe /F')           
