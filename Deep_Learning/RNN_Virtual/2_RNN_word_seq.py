sentence =["food was not good"]

words = sentence[0].split()  # Split the sentence into words

for index , word in enumerate(words):
    print("positive ",index+1,":",word)
    print("---------------------------------------------")