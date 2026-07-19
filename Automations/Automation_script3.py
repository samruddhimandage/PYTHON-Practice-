import sys

def main():
    if(len(sys.argv)==2):
        
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("Help")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("usage")
         
           
        DirectoryName=sys.argv[1]
        print("directory name is :",DirectoryName)
        
    else:
        print("invlide input")
        print("please use --h or --u for more info")
   
if __name__=="__main__":
    main()
    