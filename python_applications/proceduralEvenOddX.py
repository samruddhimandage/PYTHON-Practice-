def checkEven(no):
    
    if (no % 2 == 0):
        return True
    else:
        return False
      
def main():
    
    value =int (input("Enter a number:"))
    
    ret = checkEven(value)
    
    if(ret == True) :
        print("number is even")
    else:
        print("number is odd")
        
if __name__ =="__main__":
    main()
    
