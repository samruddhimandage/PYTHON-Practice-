checkEven = lambda no : no % 2 == 0   
    
   
def main():
    
    value =int (input("Enter a number:"))
    
    ret = checkEven(value)                         #aft compiltion ret = value % 2 == 0  
                                                   #since in lambda logic comes in main()
    if(ret == True) :
        print("number is even")
    else:
        print("number is odd")
        
if __name__ =="__main__":
    main()
    
