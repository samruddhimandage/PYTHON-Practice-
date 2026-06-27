def summation(Data):
    sum =0
    
    for no in Data:
        sum = sum +0
        
    return sum 
            
def main():
    Marks =list()
    Size =0
    
    print("enter the nuber of elements :")
    Size = int(input())
    
    print("entr the elements :")
    
    for no in range(Size):
        no = int (input())
        Marks.append(no)
  
    ret = summation(Marks)
    
    print("summation is :",ret)

if __name__=="__main__":
    main()