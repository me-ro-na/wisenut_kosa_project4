from bs4 import BeautifulSoup
import pandas as pd
import time, os, datetime
from selenium import webdriver

def del_html_tag(raw_text):
    return BeautifulSoup(raw_text, "lxml").text

boutique = []
browser = webdriver.Chrome(rf"{os.path.abspath('crawling/utils/chromedriver')}")

page_number = 1
run=True
while run:
  # 처음 접속해서 받아오는 정보, 상세정보에 들어가기 위한 url, pagination
  browser.get(f'https://ddmboutique9.modoo.at/?link=a5wuece6&page={page_number}')
  time.sleep(5)
  # pagenation
  last_page = 19

  html = browser.page_source
  soup = BeautifulSoup(html,'html.parser') 
  figs = soup.find_all("div", "area")
  for i in range(len(figs)):
    a = del_html_tag(str(figs[i].find_all("a")[0]).replace("비밀글", "")).strip()
    if("답글RE" not in a and a not in boutique):
    #     design.append(a)
      boutique.append(a)
  if int(last_page) == page_number:
    run = False
  else:
    page_number +=1


resultDict = dict(Questions = boutique)
df = pd.DataFrame(resultDict)

print("[BOUTIQUE9_HOTEL] data to csv file")

dt = datetime.datetime.now()
fName = f'crawling/datas/questions/hotel_boutique9_{dt.year}_{dt.month}_{dt.day}.csv'
fName = rf'{os.path.abspath(fName)}'

df.to_csv(fName, sep=',', encoding='utf-8-sig', index=False)
