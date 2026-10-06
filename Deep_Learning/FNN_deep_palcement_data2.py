import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#----------------------------------------------------------------------
# step 1: read the data from CSV
#----------------------------------------------------------------------
def read_data(datapath):
    
    data = pd.read_csv(datapath)
    
    print("first 5 rows from the csv",data.head())
    
    analysis(data)
    
#----------------------------------------------------------------------
# 2. data analysis
#----------------------------------------------------------------------
def analysis(data):
    print("data analysis")
    print("first 5 rows")
    print(data.head())

    print("name of columns")
    print(data.columns)

    print("shape of dataset")
    print(data.shape)

    print("desvription :")
    print(data.describe())
    
    divide(data)
    
#-----------------------------------------------------------------------
# step 3: divide the data into features and labels
#-----------------------------------------------------------------------
def divide(data):
    
    X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
    
    Y = data[["palced"]]
    
    print("input features :")
    print(X.head())

    print("Target :")
    print(Y.head())
    
    test_train(X,Y)

#-----------------------------------------------------------------------
# step 4: train test split
#----------------------------------------------------------------------- 

def test_train(X,Y):
    
    x_train ,x_test , y_train  ,y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
    
    print("trainig input shape:")
    print(x_train.shape)
    print("testing input shape :")
    print(x_test.shape)
    print("trainig output shape :")
    print(y_train.shape)
    print("trainig output shape :")
    print(y_test.shape)  
    
       

def main():
    read_data("placement_data.csv")
if __name__=="__main__":
    main()