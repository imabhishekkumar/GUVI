def getAns(s1,s2):
    summ=ord(s1)+ord(s2)-96
    if summ>122:
        return chr(summ-26)
    else:
        return chr(summ)

s1= str(input())
s2= str(input())
l = len(s1)
s3=[]
for i in range(l):
    s3.append(getAns(s1[i],s2[i]))
print("".join(s3))