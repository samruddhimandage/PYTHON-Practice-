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
    
    #step 4: Elbow Method
    WCSS =[]
    for k in range(1,11):
        model = KMeans(
            n_clusters= k,
            random_state= 42,
            n_init=10,   
        )
        
        model.fit(X_scaler)
        
        WCSS.append(model.inertia_)
    
    print("Values of Wcss :")
    
    for i in range(len(WCSS)):
        print(f"{i+1}:{WCSS[i]}")
        
    #step 5: Visualization 
    
    plt.plot(
        range(1,11),
        WCSS,
        marker = "o",   
    )
    
    plt.xlabel("number of cluster : K")
    plt.ylabel("WCSS")
    plt.title("elbow method")
    plt.grid(True)
    plt.show()
    
    model = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )
    
    cluster = model.fit_predict(X_scaler)
    
    df["Cluser"] = cluster 
    
    print("Dataset with cluster")
    print(df.head(100))
if __name__=="__main__":
    main()