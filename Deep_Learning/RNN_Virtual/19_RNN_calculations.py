import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Step 1 : Load the data

train_setnatces = [
    "food was good",
    "food was bad",
    "food was excellent",
    "food was terrible",
    "service was good",
    "serice was bad",
    "service was excellent",
    "service was terrible",
    "ambience was good",
    "ambience was bad",
    "ambience was excellent",
    "ambience was terrible"
]

train_labels = [
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
    0
]

# Step 2 : Tokenisation

tokenizer = Tokenizer(oov_token = "<OOV>")

tokenizer.fit_on_texts(train_setnatces)

# Step 3 : Convert training data into sequance

train_sequance = tokenizer.texts_to_sequences(train_setnatces)

print("Training sequances : ")

for sentance, sequance in zip(train_setnatces,train_sequance):
    print(sentance, " -> ", sequance)

# Step 4 : Apply padding

max_length = 4

X_train = pad_sequences(
    train_sequance,
    maxlen = max_length,
    padding = "pre"
)

Y_train = np.array(train_labels)

print("Padded training data")
print(X_train)

print("Training labels : ")
print(Y_train)

# Step 5 : Calculate vocabulary size

vocab_size = len(tokenizer.word_index) + 1

print("Vocabulary size is : ",vocab_size)

# step 6 : Build RNN model

model = Sequential()

model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=8,
        input_length=max_length
    )
)

model.add(
    SimpleRNN(
        units = 8,
        activation = "tanh"
    )
)

model.add(
    Dense(
        units=1,
        activation="sigmoid"
    )
)

# Step 7 : Compile the model

model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

# Step 8 : Display model

model.build(input_shape = (None, max_length))

print("Model architecture")
model.summary()

# Stpe 9 : Train the model

history = model.fit(
    X_train,
    Y_train,
    epochs = 100,
    verbose = 1
)

print("Model training completed")

# step 10 : Create unseen data

test_sentances = [
    "service was amazing",
    "service was horrible",
    "experiance was excellent",
    "experiance was terrible"
]

# Step 11 : convert text to sequance

test_sequances = tokenizer.texts_to_sequences(test_sentances)

X_test = pad_sequences(
    test_sequances,
    maxlen = max_length,
    padding = "pre"
)

# Step 12 : Predict the enstiment

for text, sequance, padded in zip(test_sentances, test_sequances, X_test):
    input_data = np.array([padded])

    prediction = model.predict(input_data,verbose = 0)

    probablity = float(prediction[0][0])

    print("Sentance : ",text)
    print("Sequance : ",sequance)
    print("Padded sequance : ",padded)
    print("Prediction : ",probablity)

    if probablity >= 0.5:
        print("Sentiment : Positive")
    else:
        print("Sentiment : Negative")