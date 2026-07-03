from marvellousLIbrary import filterX , mapX , reduceX

CheckEven = lambda no :(no % 2==0)

increament = lambda no : no + 1

Addition = lambda no1 , no2 : no1 + no2

           
def main():
    
    Data = [13,12,8,10,11,20]                        
    print("Input data is :",Data)
    
    FData = list(filterX(CheckEven,Data))                                
    print("Data after filteration :",FData)
    
    MData = list(mapX( increament , FData))
    print("data after map :",MData)
    
    RData = (reduceX(Addition,MData))
    print("data after reduce :", RData)
    
if __name__ =="__main__":
    main()
    




