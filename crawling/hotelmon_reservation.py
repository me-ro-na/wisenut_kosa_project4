<<<<<<< HEAD
#%%
from bs4 import BeautifulSoup
import datetime, os
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver.exe')
=======
from bs4 import BeautifulSoup
import os, datetime
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(rf"{os.path.abspath('crawling/utils/chromedriver')}")
>>>>>>> e14ae926640bd5802609950a5e54163ba27b2e4d
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
<<<<<<< HEAD
    # if(len(tbody.select("tr")) == 2):
    #     break
    # print("1: ", tbody.select("tr"))

=======
>>>>>>> e14ae926640bd5802609950a5e54163ba27b2e4d
    trs = tbody.select("tr")
    for tags in trs[4:len(trs)-2:2]:
        td = tags.select("td")[1]
        title = del_html_tag(str(tags.select("td")[1].select("nobr>a>span"))).strip()
<<<<<<< HEAD
        # title = del_html_tag(str(tags.select("td>nobr>a>span")[1])).strip()
        print(title)

=======
>>>>>>> e14ae926640bd5802609950a5e54163ba27b2e4d

        if title not in titles:
            titles.append(title)
    page +=1

<<<<<<< HEAD
#%%

print("[HOTELMON] data to csv file")

hotelmon = pd.DataFrame({'title':titles})

def save_csv(df):
    df.to_csv('hotelmon.csv',mode ='w',encoding='utf-8')

save_csv(hotelmon)  

#%%
# resultDict = dict(Questions = titles)

# dt = datetime.datetime.now()
# fName = f'hotelmon_rs_{dt.year}_{dt.month}_{dt.day}.csv'
# fName = rf'{os.path.abspath(fName)}'
# df = pd.DataFrame(resultDict)

# df.to_csv(fName, sep=',', encoding='utf-8-sig', index=False)
=======
df = pd.DataFrame({'title':titles})

print("[HOTELMON_HOTEL] data to csv file")

dt = datetime.datetime.now()
fName = f'crawling/datas/questions/hotel_hotelmon_{dt.year}_{dt.month}_{dt.day}.csv'
fName = rf'{os.path.abspath(fName)}'

df.to_csv(fName, sep=',', encoding='utf-8-sig', index=False)
>>>>>>> e14ae926640bd5802609950a5e54163ba27b2e4d
