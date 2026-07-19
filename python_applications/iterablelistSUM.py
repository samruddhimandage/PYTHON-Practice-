def main():
    Marks=[78,90,56,98,77]
    
    for no in Marks:
        print(no)
        
    Marks[2]=59
    print("--------------------------------------")
    
    for no in Marks:
        print(no)
    
if __name__ =="__main__":
    main()