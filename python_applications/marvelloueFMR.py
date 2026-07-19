
CheckEven = lambda no :(no % 2==0)

increament = lambda no : no + 1

Addition = lambda no1 , no2 : no1 + no2

def filterX( Task,Elements):          # user define filter function 
    Result = list()                   #empty list
    
    for no in Elements:
        Ret = Task (no)               # task (no)= checkeven (no)
        
        if Ret == True:
            Result.append(no)
            
    return Result

def mapX(Task , Elements):
    result=list()
    
    for no in  Elements:
        ret = Task(no)
        
    result.append(ret)
    
    return result
        
def reduceX(Task , Element):
    sum =0
    
    for no in Element:
        sum = Task(sum , no)
    
    return sum 
           
def main():
    
    Data = [13,12,8,10,11,20]                        
    print("Input data is :",Data)
    
    FData = list(filterX(CheckEven,Data))                                
    print("Data after filteration :",FData)
    
    MData = list(mapX(increament , FData))
    print("data after map :",MData)
    
    RData = (reduceX(Addition,MData))
    print("data after reduce :", RData)
    
if __name__ =="__main__":
    main()
    




