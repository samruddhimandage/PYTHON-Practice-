#accept: multiple parameter   
#retrun: multiple vlaue

def marvellous(No1 , No2):
    print("age of son and father is s :",No1,No2)
    return 21,51
    
def main():
   ret1 , ret2 =marvellous(11 , 31) 
   print("return values are :",ret1 ,ret2)
    
if __name__=="__main__":
    main() 