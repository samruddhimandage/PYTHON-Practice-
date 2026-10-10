import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score,mean_squared_error
import matplotlib.pyplot as plt
#------------------------------------------------------------
# Step 1 : load the Data
#------------------------------------------------------------

df = pd.read_csv("california_housing.csv")

print("Shape of dataset :",df.shape)

print("First few entres :")
print(df.head())

#------------------------------------------------------------
# Step 2 : Seperate Features and labels
#------------------------------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

print("shape of X :",X.shape)
print("shape of y :",Y.shape) 

#------------------------------------------------------------
# Step 3 : Split the Data
#------------------------------------------------------------

X_Train , X_Test , Y_Train , Y_Test = train_test_split(
    X,
    Y,
    test_size= 0.2,
    random_state= 42
)

#------------------------------------------------------------
# Step 4 : Create the model
#------------------------------------------------------------

Model = DecisionTreeRegressor(random_state= 42)

#------------------------------------------------------------
# Step 5 : Train the model
#------------------------------------------------------------

Model = Model.fit(X_Train,Y_Train)

#------------------------------------------------------------
# Step 6 : Test the model
#------------------------------------------------------------

Y_pred = Model.predict(X_Test)

#------------------------------------------------------------
# Step 7 : Evaluate the model
#------------------------------------------------------------

print("Mean Squ Error",mean_squared_error(Y_Test,Y_pred))
print("R2 :",r2_score(Y_Test,Y_pred))

plt.plot(
    Y_Test,
    Y_pred,
    'o'
)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Decision Tree Regressor")
plt.show()