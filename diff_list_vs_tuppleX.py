#_______________________________________
#                   list      tupple
#_______________________________________
#ordered            yes          yes
#indexed            yes          yes
#mutable            yes          No
#heterogeneous      yes          yes
#_______________________________________
def main():
    Data1=[10,3.14,True,"pune"]           #list
    Data2=[10,3.14,True,"pune"]           #tupple    
                                          #both r heterogenous
    print(Data1)
    print(Data2)
    
    print(Data1[0])
    print(Data2[0])
    
    
if __name__=="__main__":
   main()