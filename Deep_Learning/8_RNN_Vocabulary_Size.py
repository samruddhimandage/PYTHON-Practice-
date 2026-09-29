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

vocab_size = len(word_index)+1

print("number of unique words :",len (word_index))
print("Padding index : 0")
print("vocabulary size :",vocab_size)