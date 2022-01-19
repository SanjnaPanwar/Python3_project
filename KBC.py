que = [
    "1.How many continents are there?",              # pehla question
    "2.What is the capital of India?",            # doosra question
    "3.NG mei kaun se course padhaya jaata hai?"    # teesra question
]
option = [
    ["Four", "Nine", "Seven", "Eight"],#pehle question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],  #second question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"] #third question ke liye options
]
solution = [3, 4, 1]# har ek question ke liye, uski solution key (yeh index nahi hai)
answerlist=[
    ["2.Nine","3.Seven"],
    ["1.Chandigarh","4.Delhi"],
    ["1.Software Engineering","2.Counseling"]   #50-50 life line
]
print("SWAGAT HAI APKA :KAUN BANEGA CARORPATI:me")
# print("                 ","🙏"  )                       
# print("ye rha apka sawal apke computer 💻 💻 screen par")
i=0                    #indexing of questions
count=0                 
price=0  
# length=len(que)           #amount of winning
while i<len(que):  #this loop is use for indexing of questions
    print(que[i])
    serialno=0
    j=i             #it if for making value constant bcz printing of options
    while serialno<len(option[i]):  #for answer options
        k=option[j][serialno]
        print(serialno+1,k)  #increament from 1 is for serial number of option
        serialno+=1
    lifeline=input("do you want life line 🤓 yes/no:")
    if lifeline=="yes":
        print("you choose 50🔄50lifeline")
        if count<1:
            print(answerlist[j])
            answer=int(input("enter your answer🙃:"))
            if answer==solution[i]:
                price+=10000
                print("your answer is right😎CONGRATS you won",price)
            else:
                print("your answer is wrong,you loss the game and your winning amount rupees-",price)
                break
            count+=1
        else:
            print("you already use your life line")
            answer2=int(input("enter your answer:"))
            if answer2==solution[i]:
                print("congrats you choose right answer😊")
                price+=10000
                print("your winning amount is rupees-🤠",price)
            else:
                print("your answer is wrong and winning amount is-🥳",price)
                break
    else:
        pass
        k=int(input("enter your answer:"))
        if k==solution[i]:
            price+=10000
            print("congrats answer is right and your winning amount is🥳-",price)
        else:
            print("your answer is wrong and winning amount is -",price)
            break

    i+=1