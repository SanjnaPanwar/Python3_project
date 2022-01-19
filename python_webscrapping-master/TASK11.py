import json
from typing import Counter


file=open("data_file_task5.json","r")
data=json.load(file)
def analyse_movies_genre(data):
    # file=open("data_file_task5.json","r")
    # data=json.load(file)
    # # print(data)
    list1=[]
    list2=[]
    for i in data:
        file2=i["Genre:"].split()
        # if file2 not in list1:
        for l in file2:
            if l[-1]==",":
                l=l[:-1]
            list1.append(l)

    for i in list1:
        if i not in list2:
            list2.append(i)
            
    # print(list2)
    dict1={}
    for j in list2:
        count=0
        k=0
        while k<len(list1):
            if j==list1[k]:
                count+=1
            k+=1
        dict1.update({j:count})
        # dict1[j]=count
    # print(dict1)
    with open ("data_file_task11_.json","w")as file:
        json.dump(dict1,file,indent=4) 
analyse_movies_genre(data) 
