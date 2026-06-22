
print("________________________________________________________________________")
print("______________________ticket pricing software___________________________")
print("________________________________________________________________________") #industrial banner


print("please enter ur age :")
Age= int(input())

if(Age <= 5):
    print("free entry ")
    
elif(Age>5 and Age<=18):
    print("price is 900/-")
    
elif(Age>18 and Age<=40):
    print("price is 1200/-")
    
else:
    print("price is 500/-")
    
