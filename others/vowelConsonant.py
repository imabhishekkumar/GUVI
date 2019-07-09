class word:
    
    def check(self,value=None):
        self.value=value
        vowels="aeiou"
        consonant="qwrtypsdfghjklzxcvbnm"
        if(self.value.lower() in vowels):
            print("Vowel")
        elif(self.value.lower() in consonant):
            print("Consonant")
        else:
            print("invalid")
class main:
    inp=input()
    obj=word()
    obj.check(inp)
