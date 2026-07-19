def summation(Data):
    sum =0
    
    for no in Data:         #here no have each element of data
     
        sum = sum +0          #iteration logic
        
    return sum 
            
def main():
    Marks =list()
    Size =0
    
    print("enter the nuber of elements :")
    Size = int(input())
    
    print("entr the elements :")
    
    for i in range(Size):     #here i will tell iteration
        no = int (input())    #this is the process which will iterqate for the i times
        Marks.append(no)       #this is the process which will iterqate for the i times
  
    ret = summation(Marks)
    
    print("summation is :",ret)

if __name__=="__main__":
    main()