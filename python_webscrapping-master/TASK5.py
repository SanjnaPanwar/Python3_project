from os import link
import requests
from bs4 import BeautifulSoup
import pprint
import json

url=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
soup=BeautifulSoup(url.text,'html.parser')
def scrap_top_list():
    table=soup.find("table",class_="table")
    name=table.find_all("a",class_="unstyled articleLink")
    tbody=table.find_all('td',class_="bold")
    review=table.find_all("td",class_="right hidden-xs")
    rating=table.find_all("span",class_="tMeterScore")
    Top_movies=[]
    details={"position":"","movieName":"","year":"","rating":"","rank":'',"movieURL":""}
    def DividingName(a):
        b=a.split('(')
        return b[0]
    c=1
    for i in range(0,len(tbody)):
        n=name[i].get_text()
        a=name[i].get_text().strip()
        result=DividingName(a)
        details["position"]=c
        details["movieName"]=result
        details["year"]=n.split()[-1][1:5]
        details["rating"]=rating[i].get_text().strip()
        details["rank"]=review[i].get_text().strip()
        details["movieURL"]="https://www.rottentomatoes.com/"+name[i]["href"]
        Top_movies.append(details.copy())
        c+=1
    with open("data_file_task1.json", "w") as read_content:
            print(json.dump(Top_movies ,read_content, indent=4))
    return Top_movies
scrapped=scrap_top_list()
# pprint.pprint(scrapped)




# 2nd task
def group_by_year(movies):
    years=[]
    for a in movies:
        year=a['year']
        if year not in years:
            years.append(year)
    movie_dict={a:[]for a in years}
    for a in movies:
        year=a["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(a)
    with open("data_file_task2.json", "w") as read_content:
            print(json.dump(movie_dict ,read_content, indent=4))
    return movie_dict
GroupByYear=group_by_year(scrapped)
# pprint.pprint(GroupByYear)


# 3rd task
def group_by_decade(movies):
    moviedec={}
    list1=[]
    # print(movies)
    for index in movies:
        # print(index,'index hain')
        module=int(index)%10  #remainder
        decade=int(index)-module
        decade=int(decade)
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if int(x)<=dec10 and int(x)>=i:
                for a in movies[x]:
                    moviedec[i].append(a) 
    with open("data_file_task3.json", "w") as read_content:
            print(json.dump(moviedec ,read_content, indent=4))
    return moviedec
GroupByDecade=(group_by_decade(GroupByYear))
# pprint.pprint(group_by_decade(GroupByYear))


#4TH TASK

def scrap_movie_details():

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
    with open("data_file_task4.json", "w") as read_content:
        json.dump(dict1 ,read_content, indent=4)  
    return dict1    
ScrapMovieDetails=(scrap_movie_details())


# 5th task

def scrap_movie_details_list():
    with open("data_file_task1.json","r") as f:
        data=json.load(f)
    k=1
    main=[]
    for i in data:
        if k==i["position"]:
            a=str(i["movieURL"])
            link=requests.get(a)
            soup=BeautifulSoup(link.text,"html.parser")
            movie=soup.find_all("li",class_="meta-row clearfix")
            rating=soup.find_all("div",class_="meta-label subtle")
            value=soup.find_all("div",class_="meta-value")
            dict1={}
            for j in range(0,len(movie)):
                key=rating[j].get_text()
                values=value[j].get_text().replace("\n","").strip()
                dict1.update({key:values})
            main.append(dict1)
            pprint.pprint(main)
            with open("data_file_task5.json", "w") as read_content:
                json.dump(main ,read_content, indent=4) 
        k+=1
        # return main
scrap_movie_details_list()
