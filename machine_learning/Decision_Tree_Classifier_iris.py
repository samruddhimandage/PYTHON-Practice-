
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

def main():
    iris_data =load_iris()
    
    X = iris_data.data
    
    Y = iris_data.target
    
    X_train, X_test , Y_train , Y_test =train_test_split(X,Y,test_size=0.5,random_state=42)
    
    model = DecisionTreeClassifier()
    
    model = model.fit(X_train,Y_train)
    
    Y_pred= model.predict(X_test)
    
    result = accuracy_score(Y_test,Y_pred)
    
    print("accuracy is :",result*100)
    
    #visualization
    
    plt.figure(figsize=(12,8))
    
    plot_tree(model , filled= True , feature_names= iris_data.feature_names,class_names=iris_data.target_names)
    
    plt.title("Decision tree Classifier")
    
    plt.show()
    
if "__name__"=="__name__":
    main()
    