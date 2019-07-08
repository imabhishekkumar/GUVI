n = int(input())
inp = sorted(list(input().split()),reverse= True)
output = "".join(inp)
if int(output) !=0:
    print(output)
else:
    print(0)