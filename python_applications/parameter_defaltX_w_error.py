#error
def Area(Pi=3.14 , Radius):           #default argument should always be at last 
    Ans=Pi*Radius*Radius
    return Ans
    
def main():
    ret =Area(10.5)
    print("Area if circle is :",ret)
    
    ret =Area(10.5,7.12)
    print("Area if circle is :",ret)
           
if __name__=="__main__":
    main()