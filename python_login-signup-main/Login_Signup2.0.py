import json
import os
def storng_password(password):
    if len(password)>6 and len(password)<16:
        if ("#" in password or "@" in password):
            if "1"in password or"2"in password or"3"in password or"4"in password or"5"in password or "6"in password or "7"in password or "8"in password or"9"in password or"0" in password :
                return True
            else:
                print(password,"At least password should contain one number")
                password1=input("enter your 1st password : ")
                storng_password(password1)
        else:
            print(password,"At least password should contain one special character")
            password1=input("enter your 1st password : ")
            storng_password(password1)   
    else:
            print(password,"At least password should length 6 to 16 digit")
            password1=input("enter your 1st password :")
            storng_password(password1)

def checkpassword(password1,password2):
    if password1==password2:
        print(" your is password created.")
    else:
        print("your both password are not same")
        password2=input("enter your password : ")
        checkpassword(password1,password2)
print("Welcome to login and sign up page")
login_signup=input("what you choose login or signup : ")
file=os.path.exists("your_data.json")
if file==False:
    if login_signup=="signup":
        user_name=input("enter your user name : ")
        password1=input("enter your 1st password : ")
        storng_password(password1)
        password2=input("enter your 2nd password : ")
        checkpassword(password1,password2)
        print("congrats",user_name,"you are Signed  up Successfully.")       
        description=input("Information about you :")
        date_of_birth=input("enter your date of birth : ")
        hobbies=input("enter your hobies : ")
        gender=input("enter your gender (male or female) :")
        mylist=[]
        your_data={}
        list1=["username","password","description","dob","hobbies","gender"]
        list2=[user_name,password1,description,date_of_birth,hobbies,gender]
        for i in range(len(list1)):
            your_data.update({list1[i]:list2[i]})
        mylist.append(your_data)

        with open ("your_data.json","a")as p:
            json.dump(mylist,p,indent=4,)

elif file==True:
    if login_signup=="signup":
        user_name=input("enter your user name : ")
        password1=input("enter your 1st password : ")
        storng_password(password1)
        password2=input("enter your password : ")
        checkpassword(password1,password2)
        
        m=open("your_data.json","r")
        usname=m.read()
        if user_name in usname:
            print("This account is already exists")
        else:
            print("congrats",user_name,"you are Signed  up Successfully")
            description=input("Information about you : ")
            date_of_birth=input("enter your date of birth : ")
            hobbies=input("enter your hobies : ")
            gender=input("enter your gender (male or female) :")
            
            user_data={}
            list1=["username","password","description","dob","hobbies","gender"]
            list2=[user_name,password1,description,date_of_birth,hobbies,gender]
            for i in range(len(list1)):
                user_data.update({list1[i]:list2[i]})
            with open("your_data.json","r")as k:
                data=json.load(k)
            data.append(user_data)
            with open("your_data.json","w")as p:
                json.dump(data,p,indent=4)
    elif login_signup=="login":
        login_name=input("enter the name : ")
        login_password=input("enter the password : ")
        with open("your_data.json","r")as p:
            data=json.load(p)
            for i in data :
                if i["username"]==login_name:
                    if i["password"]==login_password:
                            print("login successfully")
                
                            for x,y in i.items():
                                print("your",x,"is",y)
                            break
                    else:
                        print("password is incorrect")
                        break
            else:
                print("invalid account")
