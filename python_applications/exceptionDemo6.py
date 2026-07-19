def main():
    
    Ans=0
    try:         
        print("enter 1st number :")
        no1=int(input())
        
        print("enter 2st number :")
        no2=int(input())
        
        Ans=no1 / no2 
        print ("division is successfull ")
        
    except ZeroDivisionError as zobj:      # ZeroDivisionError = name of perticular error class 
                                           #zobj = object of that class                            
        print("Exception occur due to 2nd operand is zero :",zobj) 
        
    except ValueError as v:
        print("Exception occur due to 2nd operand is invalide datatype :",v)
    
    except Exception as Eobj:                                         
        print("Exception occured ", Eobj)
        
    finally :
        print("inside finally block ")
  
        
    print("division is :",Ans) 
    
    
if __name__=="__main__":
    main()