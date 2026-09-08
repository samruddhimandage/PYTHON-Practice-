import pandas as pd
import joblib
def loadmodel(filename):
    model = joblib.load(filename)
    
    print("model loaded successfully")
    
    print(model.feature_names_in_)
    
    return model
 
def predictpassenger(model):
    
    print("Enter the informtion")
    
    pclass=int(input("enter pclass (1/2/3):"))
    sex=int(input("enter sex (0/1):"))
    Age=float(input("enter Age :"))
    sibsp=int(input("enter sibsp :"))
    parch=int(input("enter parch :"))
    fare=int(input("enter Fare :"))
    embarked=float(input("enter embarked (0/1/2):"))
    
    passenger = pd.DataFrame([{
       "pclass" : pclass,
       "sex" : sex,
       "Age":Age,
       "sibsp":sibsp,
       "parch":parch,
       "fare":fare,
       "embarked_1.0": 1 if embarked ==1 else 0,
       "embarked_2.0": 1 if embarked ==2 else 0,
    }])
    
    passenger = passenger[model.feature_names_in_]
    
    result = model.predict(passenger)
    
    return result

def main():
    model = loadmodel("titanic.pkl")

    result = predictpassenger(model)

    print("Prediction:", result)

if __name__ == "__main__":
    main()