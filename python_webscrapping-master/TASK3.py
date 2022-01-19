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
    details={"movieName":"","year":"","rating":"","rank":'',"movieURL":""}
    def DividingName(a):
        b=a.split('(')
        return b[0]
    for i in range(0,len(tbody)):
        n=name[i].get_text()
        a=name[i].get_text().strip()
        result=DividingName(a)
        details["movieName"]=result
        details["year"]=n.split()[-1][1:5]
        details["rating"]=rating[i].get_text().strip()
        details["rank"]=review[i].get_text().strip()
        details["movieURL"]="https://www.rottentomatoes.com/"+name[i]["href"]
        Top_movies.append(details.copy())
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
# group_by_decade(GroupByYear)
pprint.pprint(group_by_decade(GroupByYear))