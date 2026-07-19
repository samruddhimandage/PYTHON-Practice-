import os
def main():
    ret = os.path.exists("demoo.txt")
    
    if ret==True:
        print("file is present in current directory ")
    else :
        print("there is no such file ")

if __name__=="__main__":
   main()