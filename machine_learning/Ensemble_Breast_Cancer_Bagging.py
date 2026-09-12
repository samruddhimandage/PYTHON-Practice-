import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix

##########################################
#Step 1: load the data set
##########################################
df = pd.read_csv("breast_cancer.csv")
print("shape of dataset :",df.shape)

print("first few records :")
print(df.head())

##########################################
#Step 2: Seperate features and labels
##########################################

X = df.drop("target", axis=1)
Y = df["target"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

#######################################################
#Step 3: Split dataset for training and testing
#######################################################

X_Train , X_Test , Y_Train ,Y_Test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

#######################################################
#Step 4: Scale the Features
#######################################################

scaler = StandardScaler()

X_Train = scaler.fit_transform(X_Train)
X_Test = scaler.fit_transform(X_Test)

#######################################################
#Step 5a:Create the Base Model
#######################################################

Base_Model = DecisionTreeClassifier(random_state=42)

#######################################################
#Step 5b:Create the Bagging Model
#######################################################

Model = BaggingClassifier(
    estimator= Base_Model,
    n_estimators= 10 ,                                  # create 10 model of base model and then perfoem bagging
    random_state= 42
)

#######################################################
#Step 6 :Train the Model
#######################################################

Model = Model.fit(X_Train,Y_Train)
 
#######################################################
#Step 7 :Test the Model
#######################################################

Y_pred  =  Model.predict(X_Test)

#######################################################
#Step 8 :Evaluate the Model
#######################################################

print("Accuracy :",accuracy_score(Y_Test,Y_pred))
print("Confusion matrix :")
print(confusion_matrix(Y_Test,Y_pred))