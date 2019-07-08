n = int(input())
inp = list(input().split())
inpSet =list(set(inp))

for i in inpSet:
    inp.remove(i)
output =sorted(set(inp))
if(len(output)!=0):
    print(' '.join(),end ='')
else:
    print("unique")
