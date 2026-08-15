import numpy as np
from sklearn.neighbors import KNeighborsClassifier   #scikit-learn

def main():
    
    #independent
    X = np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6],   
    ])
    
    #dependent
    Y = np.array([
        "red",
        "red",
        "blue",
        "blue"
        ])
    
    #To Predict
    new_point = np.array([[3,3]])
    
    print("Independent variables are :",X)
    print("Dependent variables are :",Y)
    print("testing point is :",new_point)
    
if __name__=="__main__":
    main()