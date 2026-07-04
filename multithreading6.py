import time
def sumeven(No):
    sum=0
    for i in range(2,No,2):
        sum=sum+i
        
    print("summation of even :",sum)
    
    
def sumodd(No):
    sum=0
    for i in range(1,No,2):
        sum=sum+i
        
    print("summation of odd :",sum)
    
def main():
    
    start_time=time.perf_counter()
    sumeven(100000000)
    sumodd(100000000) 
    end_time=time.perf_counter()
    
    print(f"time req is :{end_time-start_time:.4f}")

if __name__=="__main__":
    main()