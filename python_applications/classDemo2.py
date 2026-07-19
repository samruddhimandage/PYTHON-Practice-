class Demo:        #class creation
    def __init__(self):
        
        print("inside contructor")
        
    def __del__(self):
        
        print("inside distructor")

obj1=Demo()    # object creation
obj2=Demo()

print("end of application")