a=[
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]]
i=0
rowsum=0
while i<len(a):
    j=0
    while j<len(a):
        rowsum+=a[i][j]
        j+=1
    i+=1
    print(rowsum)
i=0
colomnsum=0
while i<len(a):
    j=0
    while j<len(a):
        colomnsum+=a[i][j]
        j+=1
    i+=1
    print(colomnsum)
i=0
leftdiagonal=0
while i<len(a):
    j=0
    n=0
    while j<len(a):
        leftdiagonal+=a[j][n]
        j+=1
        n+=1
    i+=1
    print(leftdiagonal)
i=0
rightdiagonal=0
while i<len(a):
    j=1
    n=1
    while j<=len(a):
        rightdiagonal+=a[-j][-n]
        j+=1
        n+=1
    i+=1
    print(rightdiagonal)
if rowsum==colomnsum==leftdiagonal==rightdiagonal:
    print("magic square")