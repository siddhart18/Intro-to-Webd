print("enter the list")
n=input()
list=list(map(int,n.split()))
list.sort()
d={}
for item in list:
    if item in d:
        d[item]+=1
    else:
        d[item]=1
for k in d:
    print(k,":",d[k])

