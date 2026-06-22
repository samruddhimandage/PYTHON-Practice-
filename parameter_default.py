def Area(Radius, Pi=3.14):
    Ans=Pi*Radius*Radius
    return Ans
    
def main():
    ret =Area(10.5)
    print("Area if circle is :",ret)
    
    ret =Area(10.5,7.12)
    print("Area if circle is :",ret)
           
if __name__=="__main__":
    main()