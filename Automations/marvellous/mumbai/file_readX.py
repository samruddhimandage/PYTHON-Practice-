def main():
    
    try:
        fobj= open("demo.txt","r")  
        print("file gets opened ") 
        
        data =fobj.read()
        
        print(data)
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()