class Arithmatic:
    
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
            
    def Addition(self):                   # instance method : since 1st parameter is self
        Ans= self.No1 + self.No2
        return Ans

    def Substarction(self):
        Ans= self.No1 - self.No2
        return Ans
    

print("Enter 1st number :")
Value1=int(input())

print("Enter 2nd number :")
Value2=int(input())
 
Aobj = Arithmatic(Value1,Value2)

ret= Aobj.Addition()
print("Addition is :",ret)

ret= Aobj.Substarction()
print("Substarction is :",ret)