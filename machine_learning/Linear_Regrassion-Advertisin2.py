import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
def regression(Datapath):
     # step 1 :load _ data
     
     boarder = "_"*40
     #################################################################
     print(boarder)
     print("step 1 :load the data")
     print(boarder)
     #################################################################

     
     df = pd.read_csv(Datapath)
     
     print(df.head())
     
     #################################################################
     print(boarder)
     print("step 2 :remove unwanted coloum")
     print(boarder)
     #################################################################
     
     if "Unnamed: 0" in df.columns:
         df = df.drop(columns=['Unnamed: 0'])
         
     print(df.head())
         

def main():
    regression("Advertising.csv")
    
if __name__=="__main__":
    main()
