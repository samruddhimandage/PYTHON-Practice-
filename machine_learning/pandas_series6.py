import pandas as pd 

def main():
    
    sobj = pd.Series([11,21,51,101],index=["C","C++","JAVA","PYTHON"])     # series created 
    
    print(sobj)
    
    print(sobj["PYTHON"])
     
if __name__=="__main__":
    main()
    
