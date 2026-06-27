def sumation(Data):
    Sum=0
    for no in Data:
        Sum = Sum + no 
        
    return Sum 
        
def main():
    
    Marks=[78,90,56,98,77]           #local variable
    
    ret = sumation(Marks)
    
    print("Sum of marks:", ret)

if __name__ =="__main__":
    main()