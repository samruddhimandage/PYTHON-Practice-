from sklearn.datasets import load_iris     

def main():
    print("-"*35)
    print("Iris Classifiaction Case Study")
    print("-"*35)
    
    Dataset = load_iris()
    
    #meta data of the dataset
    print("independent variables are :")
    print(Dataset.feature_names) 
    print("length of independent variable :",len(Dataset.feature_names))
    
     
    print("dependent variables are :")
    print(Dataset.target_names)
    print("length of dependent variable :",len(Dataset.target_names))
      
if __name__=="__main__":
    main()