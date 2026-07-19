import threading

def display(No1,No2,No3):
    print(f"inside display: {No1},{No2},{No3}",threading.get_ident())     #identifiction of current thread
    

def main():
    print("inside main :",threading.get_ident())
    
    tobj = threading.Thread(target = display,args=(11,21,51,))
    
    tobj.start()
    

if __name__=="__main__":
    main()