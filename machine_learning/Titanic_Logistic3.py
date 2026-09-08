import pandas as pd 
import numpy as np
import joblib 

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
# function name : PreprocessData
# Description : It performs Data analysis
# Input : DataFrame
# Output : Updated Dataframe
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------

def PreprocessData(df):
    df = df.drop([
        "zero",
        "Passengerid",
        "Name"
        ],
        errors = "ignore"
        )
    
    # Handle missing values
    df ["Age"]=df["Age"].fillna(df["Age"].median())
    df ["Fare"]=df["Fare"].fillna(df["Fare"].median())
    
    df ["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])   #One hot encoding
    
    # convert categoriacal to numeric data
    
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )
    
    print(df.head())
    print("Data Preprocessing Completed")
    return df 
#-----------------------------------------------------------------------
# function name : splitData
# Description : Performs spliting activity 
# Input : DataFrame
# Output : 4 Subset for training and testing
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------
def splitData(df):
    X = df.drop("Survived", axis = 1)
    
    Y =  df ["Survived"]
    
    X_train , X_test , Y_train ,Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )
   
    print("Dataset splitting completed succesfully")
    return X_train , X_test , Y_train , Y_test
   
#-----------------------------------------------------------------------
# function name : main
# Description : Entry point function
# Input : None
# Output : None
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------
def main():
    
    #step 1
    df = loadData("MarvellousTitanicDataset.csv")
    
    #step 2 : 
    df = PreprocessData(df)
    
    #step 3
    
    X_train , X_test , Y_train , Y_test = splitData(df)
    
if __name__=="__main__":
    main()