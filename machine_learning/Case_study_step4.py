import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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