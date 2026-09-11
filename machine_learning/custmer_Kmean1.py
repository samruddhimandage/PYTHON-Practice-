import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
boarder = "-"*55
def KMean(Datapath):
    df = pd.read_csv(Datapath)
    
    print(boarder)
    print("Dataset Loaded with values")
    print(boarder)

    print(df.head())

    print(boarder)    
    print("Missing values :")
    print(boarder)
    print(df.isnull().sum())
    

def main():
    #step 1
    KMean("Mall_Customers.csv")
    
if __name__=="__main__":
    main()