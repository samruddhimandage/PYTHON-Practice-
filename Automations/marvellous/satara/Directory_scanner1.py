import sys
import os
def directory_sscanner(Directory_path):
    
    print("files form directory are:")
    
    for foldername,subfolder,filename in os.walk(Directory_path):
        for fname in filename:
            print(fname)

def main():
    Border = "-"*60
    print(Border)
    print("Welcome to marvellous Automation script")
    print(Border)

    if(len(sys.argv)==2):
        
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation script is use to travel the directory")
            print("for better usage please cheack --u flag")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as ")
            print("python Filename.py DirectoryName ")
            print("Directory name should be absolute path")
                       
        else:
            directory_sscanner(sys.argv[1]) 
    
    print(Border)
    print("Thank you for using marvellous Automation script")
    print(Border)

if __name__=="__main__":
    main()
    