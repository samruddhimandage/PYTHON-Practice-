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
    sumeven(1000000)
    
    sumodd(10000000) 

if __name__=="__main__":
    main()