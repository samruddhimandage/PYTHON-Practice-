no =11

print("before :",no)

def display():
    global no 
    no =21
    print("from display valu of no is:",no)
    
display()
print("after :",no)