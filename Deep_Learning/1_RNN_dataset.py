sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]
labels = [1, 0, 0]  # 1 for positive sentiment, 0 for negative sentiment

for sentence , label in zip(sentences, labels):
    sentiments = "positive" if label == 1 else "negative"
    print("Sentence:",sentence)
    print("label :",label)
    print("meaning :",sentiments)
    print("---------------------------------------------")

    