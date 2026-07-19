def main():
    
    try:
        fobj= open("demo.txt","r")  
        print("file gets opened ") 
        
        print("file offset is :",fobj.tell())
        data =fobj.read(10)
        print(data)
        print("file offset is :",fobj.tell())
        
        fobj.seek(1)
        
        data =fobj.read(10)
        print(data)
        print("file offset is :",fobj.tell())
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()