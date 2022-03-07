from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import os, time, datetime

def del_html_tag(raw_text):
    return BeautifulSoup(raw_text, "lxml").text

design = []
browser = webdriver.Chrome(rf"{os.path.abspath('crawling/utils/chromedriver')}")

page_number = 1
run=True
while run:
  # 처음 접속해서 받아오는 정보, 상세정보에 들어가기 위한 url, pagination
  browser.get(f'https://designersincheon.modoo.at/?link=09g0im5w&page={page_number}')
  time.sleep(5)
  # pagenation
  last_page = 14

  html = browser.page_source
  soup = BeautifulSoup(html,'html.parser') 
  figs = soup.find_all("div", "area")
  for i in range(len(figs)):
    a = del_html_tag(str(figs[i].find_all("a")[0]).replace("비밀글", "")).strip()
    if("답글RE" not in a and a not in design):
        design.append(a)

  if int(last_page) == page_number:
    run = False
  else:
    page_number +=1

resultDict = dict(Questions = design)
df = pd.DataFrame(resultDict)

print("[DESIGNERS_HOTEL] data to csv file")

dt = datetime.datetime.now()
fName = f'crawling/datas/questions/hotel_designersincheon_{dt.year}_{dt.month}_{dt.day}.csv'
fName = rf'{os.path.abspath(fName)}'

df.to_csv(fName, sep=',', encoding='utf-8-sig', index=False)
