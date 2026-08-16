import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    boarder="_"*60
    
    #################################################################
    # step 1: Load the dataset from CSV file
    #################################################################
 
    print(boarder)
    print("step 1: Load the dataset from CSV file")
    print(boarder)
    
    df = pd.read_csv(Datapath)
    
    print(boarder)
    print("Some entries from Datasets :")
    print(df.head())
    print(boarder)

    #################################################################
    # step 2 : clean the Dataset
    #################################################################
    
    print(boarder)
    print("step 2 : clean the Dataset")
    print(boarder)
    
    df.dropna(inplace=True)       # dropna = remove all missing value     |   inplace =True - remove all in that place only
   
    print("Shape of Dataset :",df.shape)
    print("Total Records :",df.shape[0])
    print("Ttotal Coloumns :",df.shape[1])
    
    print(boarder)
    
    #################################################################
    # step 3 : Seperate dependent and independent variables
    #################################################################
    
    print(boarder)
    print("step 3 : Seperate dependent and independent variables")
    print(boarder)
    
    X= df.drop(columns=["Class"])         # independent variable
    
    Y= df["Class"]                        # dependent variable
    
    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)
    
    print(boarder)
    print("Input columns :",X.columns.tolist())
    print("Output columns : class")  
    
    print(boarder) 
    
    #################################################################
    # step 4 : Split dataset for training and testing 
    #################################################################
    
    print(boarder)
    print("step 4 : Split dataset for training and testing ")
    print(boarder) 
    
    X_train , X_test , Y_train ,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)   # training =80 and testing = 20

    print(boarder)
    print("Details of training and testing data")
    
    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)
    print("Shape of Y_train :",Y_train.shape)
    print("Shape of Y_test :",Y_test.shape)
    
    print(boarder)
    
def main():
    MarvellousClassifier("WinePredictor.csv")
    
if __name__=="__main__":
    main()
    
    