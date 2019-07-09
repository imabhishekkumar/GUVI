inp = int(input())
inpList= []
n=1
for i in range(0,inp):
    inpList.append(input())
for i in range(1,inp):
    temp = inpList[0][0:i]
    print(temp)
    if(temp not in inpList[i]):
        break
print(temp)

    