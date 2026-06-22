import marvellous            #imported by another file 

def main():
    print("Enter first number :")
    value1=int(input())
    
    print("Enter second number :")
    value2=int(input())
    
    ret = marvellous.Addition(value1,value2)                 
    
    print("Addition is :",ret)
    
if __name__=="__main__":
    main()
    