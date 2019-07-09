class word:
    
    def check(self,value=None):
        self.value=value
        if(self.value.isalpha()):
            print("Alphabet")
        else:
            print("invalid")
class main:
    inp=input()
    obj=word()
    obj.check(inp)