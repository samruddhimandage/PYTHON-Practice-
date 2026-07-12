def main():
    
    Ans=0
    try:         
        print("enter 1st number :")
        no1=int(input())
        
        print("enter 2st number :")
        no2=int(input())
        
        Ans=no1 / no2 
        print ("division is successfull ")
        
    except Exception as Eobj:                                         # its generic exceptional handler
        print("Exception occured ", Eobj)
    #this will handle all type of exceptions 
    # we have to write it at bottom other wise remaining will be useless  
  
        
    print("division is :",Ans) 
    
    
if __name__=="__main__":
    main()