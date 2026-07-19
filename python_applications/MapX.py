def CheckEven(no):
    return(no % 2==0)

def increament(no):
    return no + 1

def main():
    
    Data = [13,12,8,10,11,20]                         #Input Data/
    print("Input data is :",Data)
    
    FData = list(filter(CheckEven,Data))                                
    print("Data after filteration :",FData)
    
    MData= list(map( increament , FData))
    print("data after map :",MData)
    
if __name__ =="__main__":
    main()
    
# in MAP the function should return integer



