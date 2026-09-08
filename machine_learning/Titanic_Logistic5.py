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
        test_size=0.7,
        random_state=42
    )
   
    print("Dataset splitting completed succesfully")
    return X_train , X_test , Y_train , Y_test
   
#-----------------------------------------------------------------------
# function name : TrainModel
# Description : it will perform Model Training
# Input : Training features
# Output : Trained Model
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------

def TrainModel(X_train,Y_train ):   # srep 4 : train the model
    
    model = LogisticRegression(max_iter=1000)
    
    model= model.fit(X_train,Y_train)
    
    print("Model Trained successfully")
    
    return model
    
#-----------------------------------------------------------------------
# function name : Evalute model
# Description : it will perfoem evalautaion
# Input : model
# Output : trained model
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------

def evaluatemodel(model,X_test,Y_test):
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(Y_test,y_pred)
    print("Accuracy is :",accuracy)
    
    print(confusion_matrix(Y_test,y_pred))
    
#-----------------------------------------------------------------------
# function name : PreserveModel
# Description : it will preseve the model into .pkl file
# Input : model
# Output : None
# Author : Samruddhi Mandage
# Date : 16/08/2026
#-----------------------------------------------------------------------
def PreserveModel(model,filename):              # step 6
    
    joblib.dump(model,filename)
    
    print("model preseerved with name :",filename)
    
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
    
    #step 4
    
    model = TrainModel(X_train, Y_train)
    
    #step 5
    
    evaluatemodel(model,X_test, Y_test)
    
    #step 6
    
    PreserveModel(model,"titanic.pkl")
    
if __name__=="__main__":
    main()