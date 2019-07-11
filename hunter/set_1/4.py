n= int(input())
lis = sorted(list(map(int,input().split())))
temp = []
i=0
while i<n-1:
    if(lis[i]==lis[i+1]):
        i=i+2
    else:
        temp.append(lis[i])
        break
if(len(temp)==0):
    print(lis[n-1])
else:
    print(temp[0])
