class number:
    
    def check(self,value=None):
        self.value=value
        if(self.value>0):
            print("Positive")
        elif(self.value<0):
            print("Negative")
        else:
            print("Zero")
try:  
    inp=int(input())
    obj=number()
    obj.check(inp)
except ValueError:
    print("Invalid Input")
