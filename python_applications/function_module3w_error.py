from marvellous import Addition

def main():
    print("Enter first number :")
    value1=int(input())
    
    print("Enter second number :")
    value2=int(input())
    
    ret = Addition(value1,value2)                 
    
    print("Addition is :",ret)
    
    ret=substartion(value1,value2)        #error since only addition is imported
    
    print("substartion is :",ret)
    
if __name__=="__main__":
    main()
    