from collections import Counter

def count(s):
    arr=list(Counter(s).values())
    temp=len(arr)*[0]
    print(arr, temp)
    print(max(arr) + 1)
    j=0

    for i in reversed(range(max(arr))):
       if(j<len(temp)):
           temp[j]=i
           j+=1
    # now temp=[3, 2, 1, 0, 0] possible unique count
    # sum(arr)-sum(temp) 12-6
    print(sum(arr)-sum(temp))

count("aaaabbbb")