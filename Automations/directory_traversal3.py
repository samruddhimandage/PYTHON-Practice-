import os
def main():
    for foldername,subfolder,filename in os.walk("marvellous"):
        print(foldername)
        
        for subf in subfolder:
            print("subfolder name :",subf)
            
        for fname in filename:
            print("file name :",fname)

if __name__=="__main__":
    main()