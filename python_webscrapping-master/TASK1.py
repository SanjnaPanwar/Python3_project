import requests
from bs4 import BeautifulSoup
import pprint
import json
url=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
soup=BeautifulSoup(url.text,'html.parser')
# print(soup)
def scrap_top_list():
    table=soup.find("table",class_="table")
    name=table.find_all("a",class_="unstyled articleLink")
    # pprint.pprint(main)
    tbody=table.find_all('td',class_="bold")
    # print(tbody)
    review=table.find_all("td",class_="right hidden-xs")
    # # print(review)
    rating=table.find_all("span",class_="tMeterScore")
    # # print(rating)
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
        # # print(n)
        # b=n.split()
        # c=b[-1][1:5]
        # # print(c)
        # l="https://www.rottentomatoes.com/"+name[i]["href"]
        Top_movies.append(details.copy())
        # print(l)
        pprint.pprint(details)
    with open("data_file.json", "w") as read_content:
            print(json.dump(Top_movies ,read_content, indent=4))
scrap_top_list()