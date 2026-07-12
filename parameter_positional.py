def Area(Radius, Pi):
    Ans=Pi*Radius*Radius
    return Ans
    
def main():
    ret =Area(10.5,3.14)
    print("Area if circle is :",ret)
        
    ret =Area(12.6,7.12)
    print("Area if circle is :",ret)
    
    value1=int(input("enter 1st no :"))
    value2=int(input("enter 2nd no :"))
    ret=Area(value1,value2)
    print("Area if circle is :",ret)
        
if __name__=="__main__":
    main()