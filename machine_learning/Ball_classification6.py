from sklearn import tree

def main():
    print("Ball Classification Case Study")

    Independent= [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]
    #independent variables for testing = [35,1],[95,0]
      
    Dependent= [1,1,2,1,2,1,2,1,1,1,2,1,2]
    # dependent variables for testing = 1,2
    
    model = tree.DecisionTreeClassifier()
    
    model = model.fit(Independent,Dependent)
    
    result = model.predict([[35,1],[95,0]])
    
    print("Predicted result of model is :",result)
    

if __name__=="__main__":
    main()