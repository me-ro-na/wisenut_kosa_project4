from bs4 import BeautifulSoup
import pandas as pd
import time, os, datetime
from selenium import webdriver

def del_html_tag(raw_text):
    return BeautifulSoup(raw_text, "lxml").text

menupan = []

browser = webdriver.Chrome(rf"{os.path.abspath('crawling/utils/chromedriver')}")

page_number = 1
run=True
while run:
  # 처음 접속해서 받아오는 정보, 상세정보에 들어가기 위한 url, pagination
  browser.get(f'https://www.menupan.com/search/qna/qna_result.asp?sc=qna&kw=%uB9DB%uC9D1%20%uCD94%uCC9C&srt=rank&page={page_number}')
  time.sleep(5)
  last_page = 545
  
  html = browser.page_source
  soup = BeautifulSoup(html,'html.parser')
  figs = soup.find_all("dl")
  for i in range(len(figs)):
    a = del_html_tag(str(figs[i].find("a")))
    menupan.append(a)
    
  if int(last_page) == page_number:
    run = False
  else:
    page_number +=1

resultDict = dict(Questions = menupan)
df = pd.DataFrame(resultDict)
print("[MENUPAN_RESTAURANT] data to csv file")

dt = datetime.datetime.now()
fName = f'crawling/datas/restaurant_menupan_{dt.year}_{dt.month}_{dt.day}.csv'
fName = rf'{os.path.abspath(fName)}'

df.to_csv(fName, sep=',', encoding='utf-8-sig', index=False)

# %%
