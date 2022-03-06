#%%
from bs4 import BeautifulSoup
import datetime, os
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver.exe')
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
    # if(len(tbody.select("tr")) == 2):
    #     break
    # print("1: ", tbody.select("tr"))

    trs = tbody.select("tr")
    for tags in trs[4:len(trs)-2:2]:
        td = tags.select("td")[1]
        title = del_html_tag(str(tags.select("td")[1].select("nobr>a>span"))).strip()
        # title = del_html_tag(str(tags.select("td>nobr>a>span")[1])).strip()
        print(title)


        if title not in titles:
            titles.append(title)
    page +=1

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
