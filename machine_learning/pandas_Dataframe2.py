import pandas as pd 

def main():
    Data={ 
          "Name":["Sagar","Amit","Pooja"],
          "Age":[27,28,29],
          "City":["Pune","Kolhapur","satara"]
          }
    
    dobj = pd.DataFrame(Data)
    print(dobj)
    
    # print(dobj[0])    # not allowed
    
    print(dobj["Age"])  # allowed
    
if __name__=="__main__":
    main()