#seek(kuthe,kuthun)
#kuthun : 0/1/2

# 0 =start
# 1= current
# 2= End

def main():
    
    try:
        fobj= open("demo.txt","r")  
        print("file gets opened ") 
        
        fobj.seek(10,0)
        
        data = fobj.read()
        
        print(data)
        
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
    
if __name__=="__main__":
   main()