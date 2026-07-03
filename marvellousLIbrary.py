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
        ret = Task(ret)
        
    result.append(ret)
    
    return result
        
def reduceX(Task , Element):
    sum =0
    
    for no in Element:
        sum = Task(sum , no)
    
    return sum 