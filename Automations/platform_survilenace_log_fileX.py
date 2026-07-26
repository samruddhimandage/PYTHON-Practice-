# pyhton  process_survilence.py    2       marvellousLogs
# pyhton  file name.py            time     foldername
#                   0             1           2


import psutil        # third party dependency ie module
import sys           # for  command line 
import os            # for file handling
import time          # for perticular time

def platform_survilace(foldername):
    border="-"*67
    
    ret = False
    
    ret = os.path.exists(foldername)                            # is there is directory of this name
    
    if ret == True:
        
        ret = os.path.isdir(foldername)                         # is it a directory
        
        if ret == True:
            print("directory exists")
            
        else :
            print("unable to process since there exixts something of this name but its not directory")
            return 
        
    else :
        os.mkdir(foldername)                                    # create the folder
        print("directory for log file created successfully")
        
    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")                                   # it provide time in string format
      
    file_name = os.path.join(foldername,"marvellous_%s.log"%time_stamp) 
    
    fobj=open(file_name,"w")
    
    print(f"log file gets successfully created with name{file_name} in folder {foldername}")
                    
def main():
    border="-"*67
    print(border)
    print("----marvellous platform survilence system----")
    print(border)
    
    if (len(sys.argv)==2):                  # handling of --h and --u
       if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
           print("this automation script is used to perform ")
           print("1 : if will fetc info of running processes")
           print("2 : it eill fetch info abt primary storage as ram")
           print("3 : it eill fetch info abt secondary storage as HDD")
           print("5 : it eill tech info abt cpu")
           print("6 : it maintail all records into  log file")
           print("7 : it will send log file through mail periodically")
           
       elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
           print("use the automation script as :")
           print(f"python {sys.argv[0]} time_interval folder_name")
           print("time_interval : time in minute for periodic execution")
           print("folder_name : name of folder where we can store the file")
  
    elif (len(sys.argv)==3):                # actual logic after passing Arguments
        platform_survilace(sys.argv[2])
    
    else:
        print("invalide number of arguments")
        print("unable to proceed as arguments are not passing")
        print("please use --u and --h for more info")
    
    print(border)
    print("----thank you for using marvellous platform survilence system----")
    print(border)
if __name__=="__main__":
    main()