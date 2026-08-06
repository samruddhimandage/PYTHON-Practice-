import pandas as pd

Border ="_"*45

################################
# step 1 : load the data set
################################

print(Border)
print("step 1 : load the data set")
print(Border)

DataPath="iris.csv"

df = pd.read_csv(DataPath)       #df = dataframe

print("Dataset loaded successfully")

print("initial entry from dataset are :")
print(df.head())












#                                     pandas  
#                                       |
#                                       |
#                 -----------------------------------------------
#                 |                      |                      |
#             series id            Data farme id              panel id