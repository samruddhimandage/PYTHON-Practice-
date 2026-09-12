import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

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
#Step 5A:Create the Individual Models
#######################################################

Model_D = DecisionTreeClassifier(random_state= 42)

Model_L = LogisticRegression(max_iter=1000)

Model_K = KNeighborsClassifier(n_neighbors=5)

#######################################################
#Step 5B:Create the voting Model
#######################################################

Model = VotingClassifier(                               # serial workingS
    
    estimators=[('decision_tree',Model_D),              #tuple of MODEL_LITERAL and MODEL 
                ('knn',Model_K),
                ('logistic',Model_L)],
    
    voting='soft'
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