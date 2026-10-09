import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# step 1 : load the data
train_sentences =[
    "food was good",
    "food was bad",
    "food was excellent",
    "food was terible",
    "service was good",
    "service was bad ",
    "service was excellent",
    "service was terrible"
    "ambience was good",
    "ambience was bad ",
    "ambience was excellent",
    "ambience was terrible"
]


train_labels =[
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
]

#step 2: tokenization

tokenizer = Tokenizer(oov_token ="<OOV>")

tokenizer.fit_on_text(train_sentences)

# step 3 : convert training data in sequance

train_sequance = tokenizer.texts_to_sequences(train_sentences)

print("training sequences :")

for sentance , sequance in zip (train_sentences , train_sequance):
    print(sentance,"->",sentance)
    
#step 4 : Apply Padding

max_length = 4

x_train = pad_sequance(
    train_sequance,
    maxlen = max_length,
    padding="pre"
)

y_train=np.array(train_labels)

print("padded training data")

print(x_train)

print("trainig lables")
print(y_train)
