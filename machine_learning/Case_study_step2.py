import pandas as pd

Border ="_"*45

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

print("shape of dataset:",df.shape)                # complete shape of matrix  --> (150,5)          

print("Column name :",list(df.columns))            #headeer of all column      -->  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']

print("Missing values per coloumn :")
print(df.isnull().sum())                           # is there is any null value and all sum

print("Class distribution ( species count )")
print(df["species"].value_counts())               # complete values from species column

print("Statistical report of dataset :")
print(df.describe())                               


#Output :
#Statistical report of dataset :
#       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
#count         150.000000        150.000000         150.000000        150.000000
#mean            5.843333          3.057333           3.758000          1.199333
#std             0.828066          0.435866           1.765298          0.762238
#min             4.300000          2.000000           1.000000          0.100000
#25%             5.100000          2.800000           1.600000          0.300000
#50%             5.800000          3.000000           4.350000          1.300000
#75%             6.400000          3.300000           5.100000          1.800000
#ax             7.900000          4.400000           6.900000          2.500000



