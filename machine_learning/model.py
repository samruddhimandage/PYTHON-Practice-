import pandas as pd
import joblib


# ---------------------------------------------------------
# Function Name : loadModel
# Description   : Load the trained model
# ---------------------------------------------------------
def loadModel(filename):

    model = joblib.load(filename)

    print("Model loaded successfully")
    print("Model features:", model.feature_names_in_)

    return model


# ---------------------------------------------------------
# Function Name : predictPassenger
# Description   : Take passenger information and predict
# ---------------------------------------------------------
def predictPassenger(model):

    print("\nEnter passenger information")

    pclass = int(input("Enter Pclass (1/2/3): "))
    sex = int(input("Enter Sex (0/1): "))
    age = float(input("Enter Age: "))
    sibsp = int(input("Enter SibSp: "))
    parch = int(input("Enter Parch: "))
    fare = float(input("Enter Fare: "))
    embarked = int(input("Enter Embarked (0/1/2): "))

    # Create passenger data
    passenger = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked_1": 1 if embarked == 1 else 0,
        "Embarked_2": 1 if embarked == 2 else 0
    }])

    # Arrange columns exactly like training data
    passenger = passenger[model.feature_names_in_]

    # Prediction
    result = model.predict(passenger)

    if result[0] == 1:
        print("Passenger Survived")
    else:
        print("Passenger Did Not Survive")


# ---------------------------------------------------------
# Function Name : main
# ---------------------------------------------------------
def main():

    model = loadModel("titanic.pkl")

    predictPassenger(model)


if __name__ == "__main__":
    main()