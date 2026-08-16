import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    boarder="_"*60
    
    #################################################################
    # step 1: Load the dataset from CSV file
    #################################################################
    print(boarder)
    print(boarder)
    print("step 1: Load the dataset from CSV file")
    print(boarder)
    
    df = pd.read_csv(Datapath)
    
    print(boarder)
    print("Some entries from Datasets :")
    print(df.head())
    print(boarder)

    #################################################################
    # step 2 : clean the Dataset
    #################################################################
    
    print(boarder)
    print("step 2 : clean the Dataset")
    print(boarder)
    print(boarder)
    
    df.dropna(inplace=True)       # dropna = remove all missing value     |   inplace =True - remove all in that place only
   
    print("Shape of Dataset :",df.shape)
    print("Total Records :",df.shape[0])
    print("Ttotal Coloumns :",df.shape[1])
    
    print(boarder)
    
    #################################################################
    # step 3 : Seperate dependent and independent variables
    #################################################################
    
    print(boarder)
    print("step 3 : Seperate dependent and independent variables")
    print(boarder)
    print(boarder)
    
    X= df.drop(columns=["Class"])         # independent variable
    
    Y= df["Class"]                        # dependent variable
    
    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)
    
    print(boarder)
    print("Input columns :",X.columns.tolist())
    print("Output columns : class")  
    
    print(boarder) 
    
    #################################################################
    # step 4 : Split dataset for training and testing 
    #################################################################
    
    print(boarder)
    print("step 4 : Split dataset for training and testing ")
    print(boarder) 
    
    X_train , X_test , Y_train ,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)   # training =80 and testing = 20

    print(boarder)
    print("Details of training and testing data")
    
    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)
    print("Shape of Y_train :",Y_train.shape)
    print("Shape of Y_test :",Y_test.shape)
    
    print(boarder)
    
    #################################################################
    # step 5 : Feature Scaling
    #################################################################
    
    print(boarder)
    print("step 5 : Feature Scaling")
    print(boarder) 
    print(boarder)
        
    scaler = StandardScaler()
    
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Feature scaling done")
    print(boarder)
    
    #################################################################
    # step 6 :Hyper parameter tunning
    #################################################################
    
    print(boarder)
    print("step 6 :Hyper parameter tunning")
    print(boarder) 
    print(boarder)   
    
    accuracy_scores=[]
    
    k_values = range(1,21)
    
    for k in k_values:
        model = KNeighborsClassifier(n_neighbors = k)
        model = model.fit(X_train_scaled,Y_train)
        
        Y_pred = model.predict(X_test_scaled)
        
        accuracy = accuracy_score(Y_test,Y_pred)
        
        accuracy_scores.append(accuracy)
        
    print("accuracy report is :")
    for no in accuracy_scores:
        print(no)
       
    print(boarder)  
    
    print(boarder)
    print("Graphical representation")
    print(boarder)
    
    plt.figure(figsize=(8.5))
    plt.plot(k_values,accuracy_scores,marker="o")
    plt.title("k values vs accuracy")
    plt.xlabel("values of k")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(k_values))
    plt.show()
    
def main():
    MarvellousClassifier("WinePredictor.csv")
    
if __name__=="__main__":
    main()
    
    