def Area(Radius, Pi):
    Ans=Pi*Radius*Radius
    return Ans
    
def main():
    ret =Area(Pi=3.14,Radius=10.5 )
    print("Area if circle is :",ret)
           
if __name__=="__main__":
    main()