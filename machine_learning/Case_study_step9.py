import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

Border ="_"*110

###########################################################
# step 1 : load the data set
###########################################################

print(Border)
print("step 1 : load the data set")
print(Border)

DataPath="iris.csv"

df = pd.read_csv(DataPath)       #df = dataframe

print("Dataset loaded successfully")

print("initial entry from dataset are :")
print(df.head())

###########################################################
# step 2 : Data Analysis (EDA)
###########################################################

print(Border)
print("step 2 : Data Analysis (EDA) ")
print(Border)

print("shape of dataset:",df.shape)               
print("Column name :",list(df.columns))            

print("Missing values per coloumn :")
print(df.isnull().sum())                          

print("Class distribution ( species count )")
print(df["species"].value_counts())               

print("Statistical report of dataset :")
print(df.describe())

###########################################################
# step 3 : Decide Independent & Dependent variable
###########################################################

print(Border)
print("step 3 : Decide Independent & Dependent variable ")
print(Border)

#X --> independent variables i.e features
#Y --> dependent variables i.e labels

feature_cols = ["sepal length (cm)",
                "sepal width (cm)",
                "petal length (cm)",
                "petal width (cm)",]

label_col=["species"]

X = df[feature_cols]            #df = dataframe i.e 2D Array
Y = df[label_col]

print("X shape :", X.shape)           # ------> (150 , 4)
print("Y shape :",Y.shape)            # ------> (150 , 1)

###########################################################
# step 4 : Visualization of Dataset
###########################################################

print(Border)
print("step 4 : Visualization of Dataset ")
print(Border)

#scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"]== sp ]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"], label = sp)

plt.title("Iris Case Study")

plt.xlabel("petal length (cm) ")
plt.ylabel("petal width (cm) ")

plt.legend()
plt.grid()
plt.show()

###########################################################
# step 5 : slit the dataset for training and testing
###########################################################

print(Border)
print("step 5 : slit the dataset for training and testing")
print(Border)

X_train , X_test , Y_train ,  Y_test  = train_test_split( X , Y , test_size=0.5 , random_state = 42)

print("Dataset sliting activity Done ")

print("X :",X.shape)                #(150,4)
print("Y :",Y.shape)                #(150,1)

print("X_train :",X_train.shape)      #(75,4)
print("X_test :",X_test.shape)        #(75,4)
print("Y_train :",Y_train.shape)      #()
print("Y_test :",Y_test.shape)

###########################################################
# step 6 : Built the model
###########################################################

print(Border)
print("step 6 : Built the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully ")

###########################################################
# step 7 : Train the model
###########################################################

print(Border)
print("step 7 : Train the model")
print(Border)

model.fit(X_train , Y_train)

print("Model trained successfully ")

###########################################################
# step 8 : Test the model
###########################################################

print(Border)
print("step 8 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model testing Done")

print("Expected answers :")
print(Y_test)

print("predicted answer :")
print(Y_pred)

###########################################################
# step 9 : Evaluate the Model performance
###########################################################

print(Border)
print("step 9 : Evaluate the Model performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print("accuracy of model is :",accuracy*100)

print("confusion matrix")
cm = confusion_matrix(Y_test , Y_pred)
print(cm)

print("Classification report")
print(classification_report(Y_test , Y_pred))