a,b = input().split()
lenA = len(a)
lenB = len(b)
cost=0
for i in range(0,lenA):
    if a[i] != b[i]:
        cost+=1
    
cost+=(lenB-lenA)
print(cost)