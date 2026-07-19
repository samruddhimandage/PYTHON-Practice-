import sys


def main():
    if(len(sys.argv)==2):
        DirectoryName=sys.argv[1]
        print("directory name is :",DirectoryName)
        
    else:
        print("invlide input")
   
if __name__=="__main__":
    main()
    