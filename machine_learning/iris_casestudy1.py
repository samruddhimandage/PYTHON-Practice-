from sklearn.datasets import load_iris     


def main():
    print("-"*50)
    print("Iris Classifiaction Case Study")
    print("-"*50)
    
    Dataset = load_iris()
    print(Dataset)
    
if __name__=="__main__":
    main()