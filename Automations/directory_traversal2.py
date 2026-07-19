import os
def main():
    for foldername,subfolder,filename in os.walk("marvellous"):
        print(foldername)
        
        for subf in subfolder:
            print("subfolder name :",subf)

if __name__=="__main__":
    main()