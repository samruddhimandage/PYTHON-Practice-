def bigBazar():
    print("Inside BigBazar")
    
    def Amul():
        print("Inside Amul")
        
    Amul()                                     #we cannot call amul from main since it is in another function
    
def main():
    
    bigBazar()

if __name__=="__main__":
    main()
    