#factorial 
def factorial(No):
    fact =1
    for i in range(1,No+1):
        fact=fact*i
        
    return fact
        

def main():
    value=int(input("enter a number :"))
    
    ret = factorial(value)
    
    print("factorial is :",ret)
    
if __name__=="__main__":
    main()