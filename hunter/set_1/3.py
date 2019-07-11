n= int(input())
lis = list(map(str,input().split()))
ans=[]
for i in range(n):
    if int(lis[i])==i:
        ans.append(lis[i])
if(len(ans)==0):
    print(-1)
else:
    print(" ".join(ans))