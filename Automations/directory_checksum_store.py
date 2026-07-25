import sys
import os
import hashlib                                             #module / library which have checksums functions / for md file

def calculatechecksum(filename):
    
    fobj = open(filename,"rb")    # binary io
    
    hobj = hashlib.md5()          #object of md5 which is presnt in hashlib
    
    Buffer = fobj.read(1024)      #read 1000 bit and stored it in array name as buffer
    
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)          

    fobj.close()
    
    return hobj.hexdigest()   
def findduplicate(Directoryname):
    
    ret = False
    
    ret = os.path.exists(Directoryname)                                       # tells whether the path exist or not                           
    if ret == False:
        print("Path is invalid")
        return
    
    ret =os.path.isdir(Directoryname)                                         # tells whether the directory exist or not
    if ret == False:
        print("no such directory")
        return
    
    duplicate={}
    
    unique = 0
    same = 0  
    
    for foldername ,subfolder ,filename in os.walk(Directoryname):
        
        for fname in filename:                                                # fname will store name of file  
            fname = os.path.join(foldername,fname)                            # provides path  ie is marvellous/demo
            
            checksum=calculatechecksum(fname)
            
            print(f"file name is: {fname} and its checksum is :{checksum}")
            
            if checksum in duplicate:
                same = same + 1
                duplicate[checksum].append(fname)
            else:
                unique = unique + 1
                duplicate[checksum]=[fname]
                
                
    print("unique files found",unique)
    print("duplicate files found",same)
        
def main():
    findduplicate("test")
    
if __name__=="__main__":
    main()
    
  