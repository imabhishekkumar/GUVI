from itertools import combinations
n,k= input().split()
k=int(k)
arr=[]
j= combinations(n,len(n)-k)
for d in j:
    arr.append(''.join(d))
print(min(arr))