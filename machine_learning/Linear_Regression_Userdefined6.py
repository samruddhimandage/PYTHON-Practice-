import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def predictor():
    #Load the Data
    X =[1,2,3,4,5]
    Y =[3,4,2,4,5]
    
    print("values of independent variables X :",X)
    print("values of dependent variable Y :",Y)
    
    sum_X=0
    sum_Y=0
    
    for i in range(len(X)):
        sum_X= sum_X + X[i]
        sum_Y = sum_Y + Y[i]
        
    mean_X = sum_X / len(X)
    mean_Y = sum_Y / len(Y)
    
    print("mean_X is :",mean_X)
    print("mean_Y is :",mean_Y)
    
    n = len(X)       # 5
    
    numerator = 0
    denomenator = 0
     
    # m = sum(x - xbar)(y - ybar)/ sum (x-xbar)**2
    
    #calculate slope i.e m
    for i in range(n):
        
        numerator = numerator + ((X[i] - mean_X)*(Y[i]-mean_Y))
        
        denomenator = denomenator + ((X[i]-mean_X)**2)
        
    m = numerator / denomenator 
    print("Slope of line (m) is :",m)                            
    
    # y = mx + c
    # c = y_(mean) - m * x_(mean)
    
    c = mean_Y - m * mean_X
    print("Y intercept that is C is :",c)
    
    x = np.linspace(1,6,n)    
    y = (m*x) + c
    
    plt.plot(x,y,color = "g" ,label ="Regression line")
    plt.scatter(X,Y,color = "r",label = "Scatter Plot")
    
    plt.xlabel("Independent Variables")
    plt.ylabel("Dependent Variables")
    
    plt.legend()
    plt.show()
    
def main():
    
    predictor()
    
if __name__=="__main__":
    main()