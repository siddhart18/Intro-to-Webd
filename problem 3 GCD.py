def euclid(a,b):
    if b==0:
        return a
    rem=a%b
    return euclid(b,rem)
print("enter 2 numbers")
a=int(input())
b=int(input())
print(euclid(a,b))

