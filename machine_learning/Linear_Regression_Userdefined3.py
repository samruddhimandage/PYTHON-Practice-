import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def predictor():
    #Load the Data
    X =[1,2,3,4,5]
    Y =[3,4,2,4,5]
    
    print("values of independent variables X :",X)
    print("values of dependent variable Y :",Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    
    print("mean_X is :",mean_X)
    print("mean_Y is :",mean_Y)
    
    
def main():
    
    predictor()
    
if __name__=="__main__":
    main()