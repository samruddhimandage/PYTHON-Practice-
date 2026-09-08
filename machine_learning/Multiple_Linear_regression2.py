import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    
     X= np.array([
         [1,7],
         [2,6],
         [3,7],
         [4,6],
         [5,8]
     ])
     
     Y = np.array([50,55,60,65,70])
     
     model = LinearRegression()
     
     model = model.fit(X,Y)
     
     print(model.predict([[6,5]]))
     
     print("Coefficient :",model.coef_)
     
     print("intercept :",model.intercept_)
     
if __name__=="__main__":
    main()
    