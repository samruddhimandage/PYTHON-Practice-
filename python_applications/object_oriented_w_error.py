class Arithmatic:
    
    def Addition(No1,No2):
        Ans=No1+No2
        return Ans

    def Substarction(No1,No2):
        Ans=No1-No2
        return Ans 
    

Aobj = Arithmatic()

print("enter 1st number :")
Value1=int(input())

print("enter 2nd number :")
Value2=int(input())
 
ret= Aobj.Addition(Value1,Value2)
print("addition is :",ret)

ret= Aobj.Substarction(Value1,Value2)
print("Substarction is :",ret)
