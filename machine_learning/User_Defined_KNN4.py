import numpy as np
import math
def MarvellousEucDistance( P1 , P2 ):
    
    Ans = np.sqrt( (P1["X"]-P2["X"])**2 + (P1["Y"]-P2["Y"])**2 )
    
    return Ans  
def MarvellousKNN_classifier():
    boarder = "_"*45
    
    data =[
        {'point':"A",'X':1,'Y':2,"lable":"red"},
        {'point':"B",'X':2,'Y':3,"lable":"red"},
        {'point':"C",'X':3,'Y':1,"lable":"blue"},
        {'point':"D",'X':5,'Y':6,"lable":"blue"}
    ]                                                 #list of dict
    
    new_point ={'X':3,"Y":3}
        
    print(boarder)
    print("User define KNN Classifier")
    print(boarder)

        
    for d in data:
        d['distance']= MarvellousEucDistance(d,new_point)       
    print(boarder)
    
    for i in data:
        print(d['distance'],d["lable"])
    

    
    print("distances of all points")
    print(boarder)
    
def main():
    MarvellousKNN_classifier()
    
if __name__=="__main__":
    main()