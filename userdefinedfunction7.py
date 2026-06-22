def calculation(no1,no2):
    multi=no1*no2
    div=no1/no2
    return multi , div 

def main():
    value1 = int(input("enter first number :"))
    value2 = int(input("enter second number :"))
    
    ret1 ,ret2 =calculation(value1,value2)
    
    print("multiplaction is :",ret1)
    print("division is :",ret2)

if __name__=="__main__":
    main()
    