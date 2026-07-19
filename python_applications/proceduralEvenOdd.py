def checkEven(no):
    
    if (no % 2 == 0):
        print("number is even")
    else:
        print("number is odd")
      
def main():
    
    value =int (input("Enter a number:"))
    
    checkEven(value)
    
if __name__ =="__main__":
    main()
    
