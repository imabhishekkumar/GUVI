a,b = input().split()
lenA = len(a)
lenB = len(b)
cost=0
if(lenA<lenB):
    for i in range(0,lenA):
        if a[i] != b[i]:
            cost+=1
    cost+=(lenB-lenA)
else:
    for i in range(0,lenB):
        if b[i] != a[i]:
            cost+=1
    cost+=(lenA-lenB)

    

print(cost)