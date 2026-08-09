import pandas as pd 

def main():
    
    sobj = pd.Series([27000,32000,32000],index=["Amit","Sagar","Sagar"])     # series created 
    
    print(sobj)
    
    print(sobj["Sagar"])
     
if __name__=="__main__":
    main()
    
