n = int(input())
inp = list(map(int,input().split()))
ans=[]
for i in range(n):
    if i%2==0 and inp[i]%2!=0:
        ans.append(str(inp[i]))
    elif i%2!=0 and inp[i]%2==0:
        ans.append(str(inp[i]))
print(" ".join(ans))