sentence = "food was good"

words = sentence.split()

print("Actual sentence is :",sentence)

for index , word in enumerate(words):
    print("Timestep :",index+1,":",word)