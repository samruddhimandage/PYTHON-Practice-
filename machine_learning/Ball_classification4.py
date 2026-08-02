from sklearn import tree

def main():
    print("Ball Classification Case Study")

    Independent= [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    
    Dependent= [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
 
    print("Independent variables are :",Independent)
    print("Dependent variables are :",Dependent)
    
if __name__=="__main__":
    main()
    
#encoding word to number conversion