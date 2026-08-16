import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    boarder="_"*60
    print(boarder)
    print("step 1: Load the dataset from CSV file")
    print(boarder)
    
    df = pd.read_csv(Datapath)
    
    print(boarder)
    print("Some entries from Datasets :")
    print(df.head())
    print(boarder)

def main():
    MarvellousClassifier("WinePredictor.csv")
    
if __name__=="__main__":
    main()
    