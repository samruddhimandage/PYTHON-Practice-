def main():
    Marks =list()
    Size =0
    
    print("enter the nuber of elements :")
    Size = int(input())
    
    print("entr the elements :")
    
    for no in range(Size):
        no = int (input())
        Marks.append(no)
 
    print(Marks)

if __name__=="__main__":
    main()