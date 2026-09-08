import pandas as pd 
import numpy as np
import joblib as jb

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#-----------------------------------------------------------------------
# function name : Load Data
# Description : Load the data from csv
# Input : Name of csv file
# Output : Data Frame
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------

def loadData(Datapath):
    
    df = pd.read_csv(Datapath)
    
    print("Dataset Loaded successfully")
    print(df.head())
    
    return df

#-----------------------------------------------------------------------
# function name : main
# Description : Entry point function
# Input : None
# Output : None
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------
def main():
    loadData("MarvellousTitanicDataset.csv")
    
if __name__=="__main__":
    main()