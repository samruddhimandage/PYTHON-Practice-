def bigBazar():
    print("Inside BigBazar")
    
    def Amul():
        print("Inside Amul")

def main():
    
    bigBazar()
    Amul()                      #error
    bigBazar.Amul()             #error  (this will allowed in oop)
   

if __name__=="__main__":
    main()
    