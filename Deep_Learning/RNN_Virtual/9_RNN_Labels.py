sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]
labels = [1, 0, 0]  # 1 for positive sentiment, 0 for negative sentiment

for sentence , label in zip(sentences, labels):
    
    print("Sentence:",sentence)
    print("label :",label)
    
    if label==1:
        print("meaning : positive sentiment")
    else:
        print("meaning : negative sentiment")
    print("---------------------------------------------")

    