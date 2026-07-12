from functools import reduce

def CheckEven(no):
    return(no % 2==0)

def increament(no):
    return no + 1

def Addition (no1 , no2):
    return no1 + no2

def main():
    
    Data = [12,8,10,11,20]                        
    print("Input data is :",Data)
    
    FData = list(filter(CheckEven,Data))                                
    print("Data after filteration :",FData)
    
    MData = list(map( increament , FData))
    print("data after map :",MData)
    
    RData = (reduce (Addition,MData))
    print("data after reduce :", RData)
    
if __name__ =="__main__":
    main()
    




