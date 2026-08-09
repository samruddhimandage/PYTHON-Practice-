import pandas as pd 

def main():
    Data=[11,21,51,101]
    
    print(Data)
    
    sobj = pd.Series(Data)     # series created 
    
    print(sobj)
    
    
if __name__=="__main__":
    main()