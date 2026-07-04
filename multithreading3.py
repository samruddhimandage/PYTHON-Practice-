import threading

def display(No):
    print(f"inside display: {No}",threading.get_ident())     #identifiction of current thread
    

def main():
    print("inside main :",threading.get_ident())
    
    tobj = threading.Thread(target = display,args=(11,))
    
    tobj.start()
    

if __name__=="__main__":
    main()