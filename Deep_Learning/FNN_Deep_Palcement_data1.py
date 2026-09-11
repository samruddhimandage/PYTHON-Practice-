#----------------------------------------------------------------------
# Deep Learning Pipeline
# 1. read the data from CSV
# 2. data analysis
# 3. preprocessing
# 4. train test split
# 5. feature scaling
# 6. FNN model training
# 7. model evaluation
# 8. graphical representation
# 9. model preservation
# 10.model loading and preserve
# 11.Test unseen Data
#----------------------------------------------------------------------

import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#----------------------------------------------------------------------
# 1. read the data from CSV
#----------------------------------------------------------------------
 
print("read the data from CSV")

data = pd.read_csv("placement_data.csv")
print("complete dataset :")
print(data)

#----------------------------------------------------------------------
# 2. data analysis
#----------------------------------------------------------------------

print("data analysis")
print("first 5 rows")
print(data.head())

print("name of columns")
print(data.columns)

print("shape of dataset")
print(data.shape)

print("desvription :")
print(data.describe())

#----------------------------------------------------------------------
#  3. preprocessing
#----------------------------------------------------------------------

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]

Y = data[['Placed']]

print("input features :")
print(X.head())

print("Target :")
print(Y.head())

#----------------------------------------------------------------------
#  4. train test split
#----------------------------------------------------------------------

print("train test split")

x_train , x_test , y_train,y_test = train_test_split(X,Y, test_size=0.3,random_state=42)

print("trainig input shape:")
print(x_train.shape)
print("testing input shape :")
print(x_test.shape)
print("trainig output shape :")
print(y_train.shape)
print("trainig output shape :")
print(y_test.shape)

#----------------------------------------------------------------------
# 5. feature scaling
#----------------------------------------------------------------------

print("feature scaling")

scalar = StandardScaler()

x_train_scaled = scalar.fit_transform(x_train)
x_test_scaled = scalar.fit_transform(x_test)

print("scaled trainig data :")
print(x_train_scaled)

#----------------------------------------------------------------------
# 6. FNN model training
#----------------------------------------------------------------------

print("FNN model creation")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print("Train the model")
model.fit(x_train_scaled,y_train)
print("model training completed")

#----------------------------------------------------------------------
# 7. model evaluation
#----------------------------------------------------------------------
print("evaluation of model")
y_pred = model.predict(x_test_scaled)

accuracy = accuracy_score(y_test,y_pred)
print("accuracy is ",accuracy)

cm = confusion_matrix(y_test,y_pred)
print("confusion matrix ",cm)

print("Predict the Probability")
y_prob = model.predict_proba(x_test_scaled)

print(y_prob[:5])
#----------------------------------------------------------------------
# model preserve
#----------------------------------------------------------------------

print("model preserve")

joblib.dump(model,"palcement_FNN_model.pkl")   #python pickel file = pkl
joblib.dump(scalar,"palcement_scalar.pkl")

print("Model and Scalar gets dumped Successfully")

#----------------------------------------------------------------------
# 10.model loading and preserve
#----------------------------------------------------------------------

print("model loading and preserve")

loaded_model = joblib.load("palcement_FNN_model.pkl")
loaded_scaler=joblib.load("palcement_scalar.pkl")

print("Model gets Loaded successfully ")

#----------------------------------------------------------------------
# 11.Test unseen Data
# Aptitude : 70
# coding :   75
# communication : 80
# acadimics :  85
# internship : 1
#----------------------------------------------------------------------

new_student = pd.DataFrame([[70,75,80,85,1]],columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scaler.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probalilty = loaded_model.predict_proba(new_student_scaled)



print("New student Data :")
print(new_student)

print("prediction probability :",new_probalilty)

if new_prediction[0]==1:
    print("prediction is placed")

else :
    print("prediction is Not placed")


#to preserve the object of any class is serialization
#to use the preserved model we use deserialization
#to preserve the model we use dump () method by joblib

