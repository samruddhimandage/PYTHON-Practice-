words = ["food","was","not","good"]

hidden_state="empty memory"

print("Input Tokens :",words)
print("Initial Hidden state :",hidden_state)

for index , word in enumerate(words):
    print("Timestep :",index+1)
    print("Current word :",word)
    print("previous memory :",hidden_state)
    
    hidden_state="memory after reading " + " ".join(words[:index+1]) + " "
    
    print("updated memory :","hidden_state")
    
    print("_"*30)