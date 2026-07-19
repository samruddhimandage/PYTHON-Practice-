 
import time

def factorial(No):
    fact =1
    for i in range(1,No+1):
        fact=fact*i
        
    return fact
        
def main():
    value=int(input("enter a number :"))
    
    start_time=time.time()
    
    ret = factorial(value)
    
    end_time=time.time()
    
    print(f"factorial of {value} is :{ret}")    #formated printing
    
    print(f"time requreed :{end_time-start_time:.5f} seconds")
    
if __name__=="__main__":
    main()