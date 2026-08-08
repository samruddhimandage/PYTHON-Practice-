from sklearn.datasets import load_iris     

def main():
    print("-"*35)
    print("Iris Classifiaction Case Study")
    print("-"*35)
    
    Dataset = load_iris()
    
    for i in range(len(Dataset.target)):
        print("ID %d, features %s , lable %s" % ( i , Dataset.data[i] , Dataset.target[i]))

    
if __name__=="__main__":
    main()