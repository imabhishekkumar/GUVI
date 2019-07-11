from itertools import permutations
n = int(input())
inp = sorted(list(map(int,input().split())))
per=list(permutations(inp,3))
for i in per:
    if(i[0]+i[1]==i[2] and i[0]<i[1]<i[2] ):
        print(str(i[0])+" "+str(i[1])+" "+str(i[2]))
