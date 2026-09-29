from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Embedding
import numpy as np

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()  

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

max_length = 4

x = pad_sequences(
                                    sequences,
                                    maxlen = max_length,
                                    padding="pre"
                                )

vocab_size = len(tokenizer.word_index)+1

embedding_model = sequential()

embedding_model.add(Embedding(input_dim=vocab_size,output_dim=4))

embedding_model.build(input_shape=(None,max_length))

embedding_model.summary()

embedding_output = embedding_model.predict(x,verbose=0)

print("embedding vectors for 1st sentence")
print("Sentence :",sentences[0])
print("Padded sequence :",x[0])

for position , token in enumerate(x[0]):
    print("position :",position+1)
    print("token :",token)
    print("vector :",np.round(embedding_output[0],[position],4))