def main():
    
    try:
        fobj= open("demo.txt","a")  
        print("file gets opened ") 
        fobj.write(" pune maharastra ")
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()