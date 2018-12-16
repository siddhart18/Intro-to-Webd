n=int(input("enter no of strings"))
abb=""
for i in range(n):
    s=input()
    abb+=s[0]
    for j in range(len(s)):
        if s[j]==" ":
            abb+=s[j+1]
    print(abb)
    abb=""