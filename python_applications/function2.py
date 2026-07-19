def Addition(No1,No2):
    Ans=0 
    Ans = No1 + No2   
    return Ans               
    
def main():
    print("Enter first number :")
    value1=int(input())
    
    print("Enter second number :")
    value2=int(input())
    
    ret = Addition(value1,value2)                    
    
    print("Addition is :",ret)
    
if __name__=="__main__":
    main()
    