import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
def regression(Datapath):
     # step 1 :load _ data
     
     boarder = "_"*55
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
     
     #################################################################
     print(boarder)
     print("step 3 :check missing values")
     print(boarder)
     #################################################################     
     
     print("Total missing values :")
     print(df.isnull().sum())
     
     #################################################################
     print(boarder)
     print("step 4 :statistical summary")
     print(boarder)
     #################################################################   
     
     print(df.describe())  
     
     #################################################################
     print(boarder)
     print("step 5 :Correlation")
     print(boarder)
     #################################################################  
     
     print(df.corr())                                                   # correlation matrix

     #################################################################
     print(boarder)
     print("step 6 :Split independent and dependent variables")
     print(boarder)
     #################################################################
     
     X = df[["TV","radio","newspaper"]]
     
     Y = df["sales"]
     
     print("independet variables :",X.head())
     print("independet variables :",Y.head())

     #################################################################
     print(boarder)
     print("step 7 :Split the dataset")
     print(boarder)
     #################################################################    
     
     X_train,X_test,Y_train,Y_test =train_test_split(
         X,
         Y,
         test_size=0.2,
         random_state=42
     )
     
     print("training data :",X_train.shape)
     print("testing data :",X_test.shape)
     
     #################################################################
     print(boarder)
     print("step 8 :Create and train the model")
     print(boarder)
     #################################################################
     
     model = LinearRegression()
     model = model.fit(X_train,Y_train)
     
     print("model trained successfully")

     #################################################################
     print(boarder)
     print("step 9 :Test the model")
     print(boarder)
     #################################################################     
     
     y_pred = model.predict(X_test)
     
     print("Expected Ans :")
     print(Y_test[:3])                                          #slicing that is first 5 records
     
     print("predicted Ans :")
     print(y_pred[:3])

     #################################################################
     print(boarder)
     print("step 10 :evaluate the model")
     print(boarder)
     #################################################################
     
     MSE = mean_squared_error(Y_test,y_pred)
     RMSE = np.sqrt(MSE)
     
     R2 = r2_score(Y_test,y_pred)
     
     print("Mean squared error :",MSE)
     print("Mean squared error :",RMSE)
     print("R2:",R2)
     
     #################################################################
     print(boarder)
     print("step 11 :Display the coefficient")
     print(boarder)
     #################################################################    
     
     print("TV coefficient :",model.coef_[0])
     print("radio coefficient :",model.coef_[1])
     print("newspaper coefficient :",model.coef_[2])
     
     print("intercept is :",model.intercept_)
def main():
    regression("Advertising.csv")
    
if __name__=="__main__":
    main()
