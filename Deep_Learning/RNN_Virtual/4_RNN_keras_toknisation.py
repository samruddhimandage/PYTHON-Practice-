from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

# object = class()
tokenizer = Tokenizer()  

tokenizer.fit_on_texts(sentences)  # fit_on_texts() method is used to create the vocabulary

word_index = tokenizer.word_index  # word_index is a dictionary that contains the words and their corresponding index

for word , index in word_index.items():
    print("position ",index,":",word)
    print("---------------------------------------------")
    
    