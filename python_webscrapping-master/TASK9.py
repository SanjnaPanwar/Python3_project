from TASK1 import scrapped
import os
import requests
from bs4 import BeautifulSoup
import pprint
import json


list2=[ ]
for i in scrapped:
    list2.append(i["movieURL"])
def scrap_movie_details(l):
    list3=[]
    for mov in l:
        data=mov[33:]
        if os.path.exists(data+".json")==True:
            with open(data+".json",'r') as file:
                data1=file.read()
                dic=json.loads(data1)
            list3.append(dic)
        else:
            url=requests.get(mov)
            soup=BeautifulSoup(url.text,"html.parser")
            movie=soup.find_all("li",class_="meta-row clearfix")
            rating=soup.find_all("div",class_="meta-label subtle")
            value=soup.find_all("div",class_="meta-value")
            dict1={}
            for j in range(0,len(movie)):
                key=rating[j].get_text()
                values=value[j].get_text().replace("\n","").strip()
                dict1.update({key:values})
            with open(data+".json","w") as file1:
                json.dump(dict1,file1,indent=4) 
            list3.append(dict1)           
    return list3   
pprint.pprint(scrap_movie_details(list2[:20]))
