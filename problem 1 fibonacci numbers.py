n=int(input("enter a number"))
a,b=0,1
if n==1:
    print(0)
if n>=2:
    print(0)
    print(1)
    for i in range(2,n):
        f=a+b
        a,b=b,f
        print(f)