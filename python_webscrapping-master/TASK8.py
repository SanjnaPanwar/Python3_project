# from os import link
import requests
from bs4 import BeautifulSoup
import pprint
import json
import os

def scrap_movie_details(l):
    data=l[34:]
    print(data)
    if os.path.exists(data+".json")==True:
        with open(data+".json",'r') as file:
            data1=file.read()
            print(json.loads(data1))
    else:
        url=requests.get(l)
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
        return dict1    
scrap_movie_details("https://www.rottentomatoes.com//m/black_panther_2018")
