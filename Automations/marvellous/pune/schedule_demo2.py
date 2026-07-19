import schedule       #third party library
import time            #inbuilt library
import datetime

def display():
    print("jay ganesh..",datetime.datetime.now())
    
    
def main():
    print("automation script started")   
    
    schedule.every(1).minute.do(display)         #call display aft evry 1 minute 
    
    #issue
    
if __name__=="__main__":
   main()