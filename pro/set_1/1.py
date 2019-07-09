def checkLongest(str1,str2):
        if(str1 in str2):
            return str1
        else:
            return checkLongest(str1[0:len(str1)-1],str2)
        

inp = int(input())
inpList= []
for _ in range(0,inp):
    inpList.append(input())
inpList.sort()
print(checkLongest(inpList[0],inpList[inp-1]))