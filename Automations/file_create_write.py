def main():
    
    try:
        fobj= open("demo.txt","w")  
        print("file gets opened ") 
        fobj.write("jay ganesh..")
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()