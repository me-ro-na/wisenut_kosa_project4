#%%
import pymysql
from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
import time
from selenium import webdriver


def del_html_tag(raw_text):
    return BeautifulSoup(raw_text, "lxml").text

menupan = []

browser = webdriver.Chrome('D:\chromedriver.exe')

page_number = 1
run=True
while run:
  # 처음 접속해서 받아오는 정보, 상세정보에 들어가기 위한 url, pagination
  browser.get(f'https://www.menupan.com/search/qna/qna_result.asp?sc=qna&kw=%uB9DB%uC9D1%20%uCD94%uCC9C&srt=rank&page={page_number}')
  time.sleep(5)
  # pagenation
  last_page = 545
  
  html = browser.page_source
  soup = BeautifulSoup(html,'html.parser')
  figs = soup.find_all("dl")
  for i in range(15):
    a = del_html_tag(str(figs[i].find("a")))
    menupan.append(a)
    print(a)
    print(len(menupan))
    
  if int(last_page) == page_number:
    run = False
  else:
    page_number +=1


# %%
df = pd.DataFrame({'list':menupan})
def save_csv(df):
    df.to_csv('Menupan.csv',mode ='w',encoding='utf-8')

save_csv(df)  

