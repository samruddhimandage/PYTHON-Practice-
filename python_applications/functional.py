addition = lambda no1 , no2 : no1 + no2
substraction = lambda no1 , no2 : no1 - no2

print("enter 1st number :")
Value1=int(input())

print("enter 2nd number :")
Value2=int(input())

ret=addition(Value1,Value2)
print("addition is :",ret)

ret=substraction(Value1,Value2)
print("Substarction is :",ret)