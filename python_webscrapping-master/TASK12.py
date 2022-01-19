import requests
from bs4 import BeautifulSoup
import pprint
import json
import os
def scrap_movie_cast():

    with open("data_file_task1.json","r") as f:
        data=json.load(f)
    l="https://www.rottentomatoes.com//m/black_panther_2018"
    link=requests.get(l)
    soup=BeautifulSoup(link.text,"html.parser")
    movie=soup.find_all("li",class_="meta-row clearfix")
    rating=soup.find_all("div",class_="meta-label subtle")
    value=soup.find_all("div",class_="meta-value")
    dict1={}
    for j in range(0,len(movie)):
        key=rating[j].get_text()
        values=value[j].get_text().replace("\n","").strip()
        dict1.update({key:values})
    lis=[]
    cast_div=soup.find("div", class_="castSection")
    a2=cast_div.find_all("div", recursive=False)
    for i in a2:
        a1=i.find("div", class_="media-body")
        lis.append(a1.a.span.get_text().strip())
    # print(lis)
    dict1.update({"actors":lis})
    with open("data_file_task12.json", "w") as read_content:
        json.dump(dict1 ,read_content, indent=4)  
    return dict1    
ScrapMovieDetails=(scrap_movie_cast())
