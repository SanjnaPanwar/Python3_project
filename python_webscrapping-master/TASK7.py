def analyse_movie_directors():
    file=open("data_file_task5.json","r")
    data=json.load(file)
    # print(data)
    list1=[]
    list2=[]
    dict1={}
    for i in data:
        file2=(i["Director:"])
        # if file2 not in list1:
        list1.append(file2)

    for i in list1:
        if i not in list2:
            list2.append(i)
            
    # print(list2)
    dict1={}
    for j in list2:
        cont=0
        k=0
        while k<len(data):
            if j==data[k]["Director:"]:
                cont+=1
            k+=1
        dict1[j]=cont
    # print(dict1)
    with open ("data_file_task7_.json","w")as file:
        json.dump(dict1,file,indent=4) 
analyse_movie_directors() 
