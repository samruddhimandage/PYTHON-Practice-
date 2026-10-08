sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

vocabulary = []

for sentence in sentences:
    words = sentence.split()  # Split the sentence into words
    
    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)  # Add unique words to the vocabulary    
            
for index , x in enumerate(vocabulary):
    print("positive ",index+1,":",x)
    print("---------------------------------------------")
    
    