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

def main():
    MarvellousClassifier("WinePredictor.csv")
    
if __name__=="__main__":
    main()
    