def CheckEven(no):
    return(no % 2==0)

def main():
    
    Data = [13,12,8,10,11,20]                         #Input Data/
    
    print("Input data is :",Data)
    
    FData = list(filter(CheckEven,Data))                                 #Fdata =Filtered Data
                                                                         #list(filter(Data,CheckEven))    = typecasting of filter function
    print("Data after filteration :",FData)
    
if __name__ =="__main__":
    main()



#filter( FUNCTION , ITERABLE )          
# Condition function should return boolean value 
# function should accept only one parameter