from itertools import groupby

s = input()
for (key, occur) in groupby(s):
    print("(" + str(len(list(occur))) + ",", str(key), end=") ")
