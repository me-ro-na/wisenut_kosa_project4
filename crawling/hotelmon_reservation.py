from bs4 import BeautifulSoup
import os, datetime
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(rf"{os.path.abspath('crawling/utils/chromedriver')}")
def del_html_tag(raw_text):
    return BeautifulSoup(raw_text, "lxml").text
titles = []
page = 1
while (page <= 5):
    url = f"http://www.mondavihotel.com/board/bbs/board.php?bo_table=m71&page={page}"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    tbody = soup.find('tbody')
    trs = tbody.select("tr")
    for tags in trs[4:len(trs)-2:2]:
        td = tags.select("td")[1]
        title = del_html_tag(str(tags.select("td")[1].select("nobr>a>span")[0])).strip()
        if title not in titles:
            titles.append(title)
    page +=1

resultDict = dict(Questions = titles)
df = pd.DataFrame(resultDict)

print("[HOTELMON_HOTEL] data to csv file")

dt = datetime.datetime.now()
fName = f'crawling/datas/questions/hotel_hotelmon_{dt.year}_{dt.month}_{dt.day}.csv'
fName = rf'{os.path.abspath(fName)}'

df.to_csv(fName, sep=',', encoding='utf-8-sig', index=False)
