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
        # pprint.pprint(details)
    # return Top_movies
    with open("data_file_task1.json", "w") as read_content:
            print(json.dump(Top_movies ,read_content, indent=4))
    return Top_movies
scrapped=scrap_top_list()
# pprint.pprint(scrapped)




# 2nd task
def group_by_year(movies):
    years=[]
    print(movies)
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
    # return movie_dict
    with open("data_file_task2.json", "w") as read_content:
            print(json.dump(movie_dict ,read_content, indent=4))
    return movie_dict
GroupByYear=group_by_year(scrapped)
pprint.pprint(GroupByYear)
