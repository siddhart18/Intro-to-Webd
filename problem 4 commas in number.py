def commas(s):
    if len(s)<=3:
        return s
    else:
        d=s[len(s)-3:]
        r=s[:len(s)-3]
        return commas(r)+","+d
n=int(input("number of integers"))
for i in range(n):
    print(commas(input()))

