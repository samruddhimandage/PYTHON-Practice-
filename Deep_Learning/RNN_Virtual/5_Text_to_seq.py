from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

# object = class()
tokenizer = Tokenizer()  

tokenizer.fit_on_texts(sentences)

sequeances = tokenizer.texts_to_sequences(sentences)

for sentence, sequeance in zip(sentences,sequeances):
    print("sentences :",sentence)
    print("sequances :",sequeance)
    print("---------------------------------")
    