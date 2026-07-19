def main():
    
    try:
        fobj= open("demo.txt","w")  
        print("file gets opened ") 
        fobj.write("marvellous infosystem...")
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()