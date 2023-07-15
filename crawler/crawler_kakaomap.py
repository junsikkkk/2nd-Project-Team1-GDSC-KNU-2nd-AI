import re
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import csv
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
################
list = []
url = "https://map.kakao.com"
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
#chromedriver_path = 'chromedriver'
#os.getcwd() # 내 경로 찾기
driver = webdriver.Chrome(executable_path = '/Users/kimjunsik/chromedriver') # chrmedriver 넣은 위치
driver.get(url)
searchloc = input('찾고싶은 음식종류 : ')
filename = input('파일이름 영어로치기 : ')

search_area = driver.find_element(By.XPATH, r'//*[@id="search.keyword.query"]') # 검색창 XPath로 접근
search_area.send_keys(searchloc) # 검색어 입력
driver.find_element(By.XPATH, '//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER) # Enter로 검색
time.sleep(2)
# 장소 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER)
storeNamePrint()
page = 1 #진짜 페이지
page2 = 0 #넘기는용
for i in range(0,35):
    try:
        page2+=1
        print('**',page,'**')
        xpath = f'//*[@id="info.search.page.no{page2}"]'
        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
        storeNamePrint()      
        if (page2)%5 == 0:
            driver.find_element(By.XPATH,r'//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            page2 = 0      
        page+= 1
    except:
        break
print('**크롤링완료**')
