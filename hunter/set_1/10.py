n,m = input().split()
nlist = sorted(list(map(int,input().split())))
mlist =sorted(list(map(int,input().split())))
ans=[]
for i in mlist:
    if i in nlist:
        ans.append(i)
if len(mlist)==len(ans):
    print("YES")
else:
    print("NO")