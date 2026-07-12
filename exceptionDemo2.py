def main():
    
    Ans=0
    try:         
        print("enter 1st number :")
        no1=int(input())
        
        print("enter 2st number :")
        no2=int(input())
        
        Ans=no1 / no2 
        print ("division is successfull ")
        
    except ZeroDivisionError as zobj:                                #as is nickname
        print("Exception occur due to 2nd operand is zero :",zobj) 
        # pvm will give the type of issue in zobj
        
    print("division is :",Ans) 
    
    
if __name__=="__main__":
    main()