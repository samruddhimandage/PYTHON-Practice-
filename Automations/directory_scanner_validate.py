import sys
import os
import time
import schedule

def directory_sscanner(Directory_path ="marvellous"):
    Border = "-"*60
  
    timestamp=time.ctime()
    logfilename="marvellous%s.log"%(timestamp)
    
    logfilename=logfilename.replace(" ","_")
    logfilename=logfilename.replace(":","_")
    
    ret=False
    
    ret =os.path.exists(directory_sscanner)
    
    if (ret==False):
        print("marvellous automation Error: there is no such directory with name ",Directory_path)
        return
    
    ret = os.path.isdir(Directory_path)
    if (ret==False):
        print("marvellous automation Error : it is not a director ")
        return
    
    print("log file gets created with name :",logfilename)
    
    fobj=open(logfilename ,"w")
    
    fobj.write(Border+"/n")
    fobj.write("Welcome to marvellous Automation script \n")
    fobj.write(Border+"/n/n")
        
    fobj.write("files from the directory are :\n\n")
    fobj.write(Border+"/n")
    
    for foldername,subfolder,filename in os.walk(Directory_path):
        for fname in filename:
            fobj.write(fname+"\n")

    fobj.close()
    
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
            
            schedule.every(10).seconds.do(directory_sscanner,sys.argv[1])         
            
            while True:
                schedule.run_pending()
                time.sleep(10)
    else:
        print("invalide input")
        print("for more info provide --u or --h")
    
    print(Border)
    print("Thank you for using marvellous Automation script")
    print(Border)

if __name__=="__main__":
    main()
    