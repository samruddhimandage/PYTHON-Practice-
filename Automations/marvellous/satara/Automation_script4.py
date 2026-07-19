import sys

def main():
    if(len(sys.argv)==2):
        
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation script is use to travel the directory")
            print("for better usage please cheack --u flag")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as ")
            print("python Filename.py DirectoryName ")
            print("Directory name should be absolute path")
            
        DirectoryName=sys.argv[1]
        print("directory name is :",DirectoryName)
        
    else:
        print("invlide input")
        print("please use --h or --u for more info")
   
if __name__=="__main__":
    main()
    