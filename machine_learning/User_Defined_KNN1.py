def MarvellousKNN_classifier():
    boarder = "_"*45
    
    data =[
        {'point':"A",'X':1,'Y':2,"lable":"red"},
        {'point':"B",'X':2,'Y':3,"lable":"red"},
        {'point':"C",'X':3,'Y':1,"lable":"blue"},
        {'point':"D",'X':5,'Y':6,"lable":"blue"}
    ]                                                 #list of dict
    
    print(boarder)
    print("User define KNN Classifier")
    print(boarder)
    
    for i in data:
        print(i)
        
    print(boarder)
    
def main():
    MarvellousKNN_classifier()
    
if __name__=="__main__":
    main()