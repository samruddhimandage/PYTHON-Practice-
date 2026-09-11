import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
boarder = "-"*55

def main():
    #step 1

    df = pd.read_csv("Mall_Customers.csv")
        
    print(boarder)
    print("Dataset Loaded with values")
    print(boarder)
    
    print(df.head())
    
    print(boarder)    
    print("Missing values :")
    print(boarder)
    print(df.isnull().sum())
        
    
    #step2 : Feature selection
    
    X = df [["AnnualIncome","SpendingScore"]]
    print(X.head())
    
    #step 3 : Scale the data 
    
    scalar = StandardScaler()
    
    X_scaler = scalar.fit_transform(X)
    
    print("Scaled Data :")
    
    print(X_scaler[:5])
if __name__=="__main__":
    main()