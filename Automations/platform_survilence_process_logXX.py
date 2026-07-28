
import psutil        # third party dependency ie module
import sys           # for  command line 
import os            # for file handling
import time          # for perticular time
import schedule      # for periodic execution
def process_scan():
    list_process =[]
    for proc in psutil.process_iter():                             # use to itrate running processses
        info= proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"]=proc.cpu_percent(None)
        info["memory_percent"]=proc.memory_percent()
        
        list_process.append(info)
        
    return list_process

def platform_survilace(foldername):
    
    border="-"*67
    
    ret = False
    
    ret = os.path.exists(foldername)                                                 # is there is directory of this name
    
    if ret == True:
        
        ret = os.path.isdir(foldername)                                              # is it a directory
        
        if ret == True:
            print("directory exists")
            
        else :
            print("unable to process since there exixts something of this name but its not directory")
            return 
        
    else :
        os.mkdir(foldername)                                                         # create the folder
        print("directory for log file created successfully")
        
    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")                                  # it provide time in string format
      
    file_name = os.path.join(foldername,"marvellous_%s.log"%time_stamp) 
    
    fobj=open(file_name,"w")
    
    print(f"log file gets successfully created with name{file_name} in folder {foldername}")
    
    fobj.write(border +"\n")  
    fobj.write("----marvellous platform survilence system----\n")  
    fobj.write("log file gets created at :"+time_stamp+"\n")
    fobj.write(border +"\n\n")
    
    fobj.write("-----------------------system report------------------------\n") 
    fobj.write(border +"\n")
    
    #CPU information
    fobj.write("active cpu cores : %s \n"%psutil.cpu_count())
    fobj.write(border +"\n")
    fobj.write("cpu usage : %s %%\n"%psutil.cpu_percent())
    
    fobj.write(border +"\n")
    #RAM information
    memory = psutil.virtual_memory()
    fobj.write("RAM usage : %s %%\n" %memory.percent)
    fobj.write(border +"\n")
    fobj.write("Total RAM available  : %s \n" %memory.total)
    fobj.write(border +"\n")
    
    #network usage
    netobj=psutil.net_io_counters()
    
    fobj.write("network usage report\n")
    fobj.write("sent : %.2f MB\n" %(netobj.bytes_sent / (1024*1024)))
    fobj.write("receive : %.2f MB\n" %(netobj.bytes_recv / (1024*1024)))
    fobj.write(border +"\n")
    fobj.write(border +"\n")
    
    #process logs
    data = process_scan()
    
    for info in data:
        fobj.write("pid : %s\n"%info.get("pid"))
        fobj.write("name : %s\n"%info.get("name"))
        fobj.write("username : %s\n"%info.get("username"))
        fobj.write("status : %s\n"%info.get("status"))
        fobj.write("cpu percent usage: %.2f\n"%info.get("cpu_percent"))
        fobj.write("ram usage : %.2f\n"%info.get("memory_percent"))
        fobj.write(border +"\n")
        
    fobj.write(border +"\n")
    
    fobj.write(border +"\n")
    fobj.write("-----------------------end of log file-----------------------\n") 
    fobj.write(border +"\n")
    
    fobj.close()
           
def main():

    
    border="-"*67
    print(border)
    print("--------------marvellous platform survilence system--------------")
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
           
    # actual logic after passing Arguments
    elif (len(sys.argv)==3):
        
        
        print("scheduler started successfully")
        print("press ctrl + c to abort the automation script")
        
        schedule.every(int(sys.argv[1])).minutes.do(platform_survilace,sys.argv[2])
        
        while(True):
            schedule.run_pending()
            time.sleep(1)
            
    else:
        print("invalide number of arguments")
        print("unable to proceed as arguments are not passing")
        print("please use --u and --h for more info")
    
    print(border)
    print("----thank you for using marvellous platform survilence system----")
    print(border)
if __name__=="__main__":
    main()