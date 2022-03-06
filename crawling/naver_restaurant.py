from bs4 import BeautifulSoup
import datetime, os, time
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(rf"{os.path.abspath('crawling/utils/chromedriver')}")

detail_url = []
title_list = []
page = 1
url = f"https://search.naver.com/search.naver?query=%EB%A7%9B%EC%A7%91%20%EC%B6%94%EC%B2%9C&nso=&where=article&sm=tab_opt"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

last_height = driver.execute_script("return document.body.scrollHeight")
# cnt = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(1)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # cnt += 1
    titles = soup.find_all('a', "api_txt_lines")
    if(len(titles) >= 2000):
        break

cnt = 0
while True:
    titles = soup.find_all('a', "api_txt_lines")
    
    for i in titles:
        title = i.text
        if(title not in title_list):
            title_list.append(title)

    if cnt == len(titles) :
        break
    cnt += 1

print("[NAVER_RESTAURANT] data to csv file")
resultDict = dict(Questions = title_list)

dt = datetime.datetime.now()
fName = f'crawling/datas/questions/restaurant_naver_{dt.year}_{dt.month}_{dt.day}.csv'
fName = rf'{os.path.abspath(fName)}'
df = pd.DataFrame(resultDict)

df.to_csv(fName, sep=',', encoding='utf-8-sig', index=False)