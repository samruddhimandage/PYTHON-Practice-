def main():
    try:
        open("demo.txt","w")  
        
        print("file gets opened ") 
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()