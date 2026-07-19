import os
def main():
    for foldername,subfolder,filename in os.walk("marvellous"):
        print(foldername)

if __name__=="__main__":
    main()