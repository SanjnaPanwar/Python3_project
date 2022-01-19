import json
def  analyse_movies_language():
    file4=open("data_file_task5.json","r")
    h=json.load(file4)
    # print(h)
    list=[]
    for i in h:
        # print(i)
        # print(i["Original Language:"])
        if i["Original Language:"]not in list:
            list.append(i["Original Language:"])
            
    # print(list)

    dict={}
    # list9=[]
    for k in list:
        i=0
        count=0
        while i<len(h):
            if k==h[i]["Original Language:"]:
                count+=1
            i+=1
        dict.update({k:count})
        # print(dict)
    list.append(dict)
    with open("data_file_task6.json","w")as file:
        json.dump(dict,file,indent=4)
    return dict
analyse_movies_language()
