import pandas as pd 

def main():
    Data={ 
          "Name":["Sagar","Amit","Pooja"],
          "Age":[27,28,29],
          "City":["Pune","Kolhapur","satara"]
          }
    
    dobj = pd.DataFrame(Data)
    
    print(dobj[["Age","Name"]])  # allowed
    
if __name__=="__main__":
    main()