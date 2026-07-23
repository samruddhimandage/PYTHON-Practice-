import sys
import os
import hashlib      #module / library which have checksums functions

def calculatechecksum(filename):
    
    fobj = open(filename,"rb")    # binary io
    
    hobj = hashlib.md5()          #object of md5
    
    Buffer = fobj.read(1000)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    
    return hobj.hexdigest()   
    

def main():
    ret= calculatechecksum("DEMOX.txt")
    print("checksum of file is :",ret)
    
if __name__=="__main__":
    main()
    