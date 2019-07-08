n = int(input())
inp = list(input().split())
inpSet =list(set(inp))
output =[]
for i in inpSet:
    inp.remove(i)
print(' '.join(sorted(set(inp))),end ='')

