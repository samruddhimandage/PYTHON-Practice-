from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

# object = class()
tokenizer = Tokenizer()  

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

print("Original Sequences :")
for sequence in sequences:
    print(sequence,"Length :",len(sequence))
    
print("All sequences are of diffrent lengths")

max_length = 4

padded_seqeunces = pad_sequences(
                                    sequences,
                                    maxlen = max_length,
                                    padding="pre"
                                )

for sentence , sequence , padded in zip(sentences,sequences,padded_seqeunces):
    print("sentence :",sentence)
    print("Original sequence :",sequence)
    print("padded seqeunce :",padded)
    print("______________________________________")
    