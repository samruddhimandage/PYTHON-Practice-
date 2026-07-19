def checkEven(no):
    
   return (no % 2 == 0)         #if we pass input as 11 then mode is 1 which is not == 0 therefore it will return FAlSE else it will return true 
                                #which will return to if condition from main
      
def main():
    
    value =int (input("Enter a number:"))
    
    ret = checkEven(value)
    
    if(ret == True) :
        print("number is even")
    else:
        print("number is odd")
        
if __name__ =="__main__":
    main()
    
