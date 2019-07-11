n = int(input())
inp = list(input().split())
ans=[]
for i in range(n):
    if inp[i] not in ans:
        ans.append(inp[i])
    else:
        print(inp[i])
        break
        


