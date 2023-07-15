#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def storeNamePrint() :
    
    time.sleep(0.2)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    cafe_lists = soup.find_all(name='li', attrs={"class": "PlaceItem clickArea"})
    #s = len(cafe_lists)
    count = 1
    for cafe in cafe_lists :
        temp = []
        cafe_name = cafe.find(name = 'a', attrs={"class" : "link_name"}).text
        food_score = cafe.find(name = 'em', attrs={"data-id" : "scoreNum"}).text
        score_num = cafe.find(name = 'a', attrs={"data-id" : "numberofscore"}).text
        #review = soup.find(name = 'em', attrs={"class" : "num"})
        reviewnum = cafe.find(name = 'em', attrs={"data-id" : "numberofreview"}).text
        addr = cafe.find(name = 'p', attrs={"data-id" : "address"}).text
        cate = cafe.find(name = 'span', attrs={"data-id" : "subcategory"}).text
        open1 = cafe.find(name = 'a', attrs={"data-id" : "periodTxt"}).text
               
        temp.append(cafe_name)
        temp.append(food_score)
        temp.append(score_num)
        #temp.append(review)
        temp.append(reviewnum)
        temp.append(addr)
        temp.append(cate)
        temp.append(open1)
        
        list.append(temp)
    f = open(filename+'.csv','w',encoding='utf-8-sig',newline="")
    writercsv=csv.writer(f)
    header=['Name','food_Score','Score_num','Review','Addr','Category', 'OpenTime']
    writercsv.writerow(header)
    
    for i in list:
        writercsv.writerow(i)

