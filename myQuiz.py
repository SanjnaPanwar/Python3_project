q1="""1.Is Python case sensitive when dealing with Identifiers?
a.yes
b.no
c.machine dependent
d.none"""
q2="""2.Which of the following is not a keyword?
a.eval
b.assert
c.local
d.pass"""
q3="""3.Which one of these is floor division?
a./
b.//
c.%
d.none"""
q4="""4.What is the output of this 3*1**3?
a.27
b.9
c.3
d.1"""
q5="""5.".a"+"bc"=?
a.a
b.bc
c.bca
d.abc"""
questions={q1:"a",q2:"a",q3:"b",q4:"c",q5:"d"}
name =input("enter your name:")
print("hello",name,"welcome to my quiz")
score=1
for i in questions:
    print()
    print(i)
    opt=input("do you waant skip this question..yes/no:")
    if opt=="yes":
        continue
    ans=input("enter the ans(a/b/c/d):")
    if ans==questions[i]:
        print("correct answer,you got",score,"point")
        score+=1
    else:
        print("wrong answer,you lost 1 point and your score is",score)
        score-=1
    quit=input("do you want to quit this quiz..yes/no:")
    if quit=="yes":
        break
print("final score is",score-1)