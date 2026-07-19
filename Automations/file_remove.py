import os
def main():
    
    try:
       
        os.remove("demo.txt")     #fobj.remove()   -> not applicable
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()