# %%
# from matplotlib.image import thumbnail
import pymysql
from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
import time
from selenium import webdriver


def del_html_tag(raw_text):
    return BeautifulSoup(raw_text, "lxml").text


# conn = pymysql.connect(host='localhost',
#                        user='root',
#                        password='root',
#                        db='pj4',
#                        charset='utf8')

# sql = "SELECT a_name, a_sub1_name, a_sub2_name FROM addr WHERE a_sub1_name IS NOT NULL OR a_sub2_name IS NOT NULL GROUP BY a_sub1_name, a_sub2_name"

# with conn:
#   with conn.cursor() as cur:
#     cur.execute(sql)
#     result = cur.fetchall()
#     for data in result:
#       print(data)

file_path = './mango_200.txt'

with open(file_path, 'rt', encoding='UTF8') as f:
  lines = f.readlines()

lines = [line.rstrip('\n') for line in lines]
print(lines)

name_list = []
rank_list = []

addr_list = [] # 주소
call_list = [] # 전화번호
type_list = [] # 음식종류
pran_list = [] # 가격대
park_list = [] # 주차
time_list = [] # 영업시간
break_list = [] # 쉬는시간
holi_list = [] # 휴일
menu_list = [] # 메뉴

review_list =[] 
thumbnail_list = [] 

food_list = []
food_url = []

#%%
browser = webdriver.Chrome('D:\chromedriver.exe')

# for idx, data in enumerate(lines):
# {data}?keyword={data}
for idx, data in enumerate(lines):
  page_number = 1
  run=True
  while run:
    # 처음 접속해서 받아오는 정보, 상세정보에 들어가기 위한 url, pagination
    browser.get(f'https://www.mangoplate.com/search/{data}?keyword={data}&page={str(page_number)}')
    time.sleep(5)
    # pagenation
    last_page = 10
    
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')
    figs = soup.find_all("figure", "restaurant-item")
    for i in range(len(figs)):
      food_list.append(figs[i].find("a")["href"])

    #print(food_list)
    if int(last_page) == page_number:
      run = False
    else:
      page_number +=1

    #중복 제거
    for i in food_list:
      if i not in food_url:
        food_url.append(i)
    print(len(food_url))

# df = pd.DataFrame({'food_url':food_url})
# def save_csv(df):
#   df.to_csv('food_url_50.csv',mode ='w',encoding='utf-8')
# save_csv(df)  
  
#%%

food_len = len(food_url)
addr_list = [0] * food_len # 주소
call_list = [0] * food_len # 전화번호
type_list = [0] * food_len # 음식종류
pran_list = [0] * food_len # 가격대
park_list = [0] * food_len # 주차
time_list = [0] * food_len # 영업시간
break_list = [0] * food_len # 쉬는시간
holi_list = [0] * food_len # 휴일
menu_list = [0] * food_len # 메뉴

# info_df = pd.DataFrame({'id':food_url})

# def save_csv(df):
#     df.to_csv('food_url.csv',mode ='w',encoding='utf-8')

# save_csv(info_df)  

# 한 페이지 안에 있는 맛집 상세정보 가져오기
for i in range(len(food_url)):
  print(f"i = {i}")
  url = "https://www.mangoplate.com" + food_url[i]
  browser.get(url)
  html = browser.page_source
  soup = BeautifulSoup(html, 'html.parser')
  
  # 맛집의 상세정보(이름, 평점, 주소, 전화번호, 휴일, 메뉴, 이미지, 리뷰)
  # 이름
  try:name_list.append(soup.select_one('span > h1').get_text())
  except:name_list.append("")

  # 평점
  try:rank_list.append(soup.select_one('span > strong > span').get_text())
  except:rank_list.append("")

  # 정보
  tbody = soup.find('tbody')
  print("done")

  trs = tbody.find_all("tr")
  # info1 = tags.find("th", text="주소")
  # info2 = tags.find("th", text="전화번호")
  # info3 = tags.find("th", text="음식 종류")
  # info4 = tags.find("th", text="가격대")
  # info5 = tags.find("th", text="주차")
  # info6 = tags.find("th", text="영업시간")
  # info7 = tags.find("th", text="쉬는시간")
  # info8 = tags.find("th", text="휴일")
  # info9 = tags.find("th", text="웹사이트")
  # info10 = tags.find("th", text="메뉴")
  
  # ths = tbody.find_all("th")
  for j in range(len(trs)):
    info1 = trs[j].find("th", text="주소")
    if(info1 is not None):
      info1_tr = info1.parent
      a = del_html_tag(str(info1_tr.find_all("td")))
      print(f"lists = {i}")
      addr_list[i] = a

    info2 = trs[j].find("th", text="전화번호")
    if(info2 is not None):
      info2_tr = info2.parent
      b = del_html_tag(str(info2_tr.find_all("td")))
      # call_list.append(b)
      call_list[i] = b
    # else: call_list.append(None)
    
    info3 = trs[j].find("th", text="음식 종류")
    if(info3 is not None):
      info3_tr = info3.parent
      c = del_html_tag(str(info3_tr.find_all("td")))
      # type_list.append(c)
      type_list[i] = c
    # else: type_list.append(None)
    
    info4 = trs[j].find("th", text="가격대")
    if(info4 is not None):
      info4_tr = info4.parent
      d = del_html_tag(str(info4_tr.find_all("td")))
      # pran_list.append(d)
      pran_list[i] = d
    # else: pran_list.append(None)
    
    info5 = trs[j].find("th", text="주차")
    if(info5 is not None):
      info5_tr = info5.parent
      e = del_html_tag(str(info5_tr.find_all("td")))
      park_list[i] = e
    # else: park_list.append(None)
    
    info6 = trs[j].find("th", text="영업시간")
    if(info6 is not None):
      info6_tr = info6.parent
      f = del_html_tag(str(info6_tr.find_all("td")))
      time_list[i] = f
    # else: time_list.append(None)
    
    info7 = trs[j].find("th", text="쉬는시간")
    if(info7 is not None):
      info7_tr = info7.parent
      g = del_html_tag(str(info7_tr.find_all("td")))
      break_list[i] = g
    # else: break_list.append(None)
    
    info8 = trs[j].find("th", text="휴일")
    if(info8 is not None):
      info8_tr = info8.parent
      h = del_html_tag(str(info8_tr.find_all("td")))
      holi_list[i] = h
    # else: holi_list.append(None)
    
    info9 = trs[j].find("th", text="메뉴")
    if(info9 is not None):
      info9_tr = info9.parent
      j = del_html_tag(str(info9_tr.find_all("td")))
      menu_list[i] = j
    # else: menu_list.append(None)

  #리뷰
  try:review_list.append(soup.select_one('li:nth-child(1) > a > div.RestaurantReviewItem__ReviewContent > div > p').get_text())
  except:review_list.append("")

  # 이미지
  try:
    a = soup.select_one('div:nth-child(1) > figure > figure > img')['src']
  except TypeError:
    a = None
  thumbnail_list.append(a)


print(len(food_url),len(name_list),len(rank_list),len(review_list),len(thumbnail_list),len(addr_list),len(call_list),len(type_list),len(pran_list),len(park_list),len(time_list),len(break_list),len(holi_list),len(menu_list))
  
food_df = pd.DataFrame({'id':food_url,'name':name_list,'rank':rank_list,'review':review_list,'thumbnail':thumbnail_list, 'addr':addr_list, 'call':call_list, 'type':type_list, 'price':pran_list, 'park':park_list, 'time':time_list, 'break':break_list, 'holiday':holi_list, 'menu':menu_list})
# food_df['id'] = food_df['id'].str[13:]
# def save_csv(df):
#     df.to_csv('food_test.csv',mode ='w',encoding='utf-8')

# save_csv(food_df)  


  #print(food_list)
  

# %%
