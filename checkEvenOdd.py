class number:
    
    def check(self,value=None):
        self.value=value
        if(self.value<1):
            print("Invalid")
        elif(self.value%2==0):
            print("Even")
        else:
            print("Odd")
try:  
    inp=int(input())
    obj=number()
    obj.check(inp)
except ValueError:
    print("Invalid Input")


        
