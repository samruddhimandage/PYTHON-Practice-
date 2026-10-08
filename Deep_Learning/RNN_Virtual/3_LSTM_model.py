##############################################################

# step 1:import re libraries
##############################################################

from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

##############################################################
# step 2: configuration of values 
##############################################################

vocab_size = 10000 # consider most frequent 10000 unique words
max_lenght = 200 # consider max 200 words from review

##############################################################
# step 3: load the imdb dataset
##############################################################
print("-"*40)
print("Movie review sentiment analysis using LSTM")
print("-"*40)

print("loading the dataset")
print("-"*40)

(x_train , y_train),(x_test , y_test) = imdb.load_data(num_words = vocab_size)

print("imdb Dataset Loaded Successfully")

print("number of training reviews :",len(x_train))
print("number of testing reviews :",len(x_test))

##############################################################
# x_ tarin = reviews use for training
# y_ train = actual sentiments of traninig
# x_test = reviewas use for testng
# y_train = actual sentiments of testing

# sentiments :-
# 0 : negative
# 1 : possitive
###############################################################

###############################################################
# step 4 :load the word dictionory
###############################################################

word_index = imdb.get_word_index()

# dictonary contains mapping of words and its corresponding number 
# drisham is good movie --> (20 26 78 43)
# drisham - 20
# is - 26
# good - 78
# movie - 43

###############################################################
# step 5 :create reverse dictonary
##############################################################

reverse_word_index = {}

for word , index in word_index.items():
    reverse_word_index[index+3] = word
    
###############################################################
# step 6 : Function to decode the review (number to word)
##############################################################
def decodedReview(encoded_review):
    words=[]
    
    for number in encoded_review:
        if number >= 3:                    # ignore 1st 3
            word = reverse_word_index.get(number,"?")
            words.append(word)
            
    return " ".join(words)

print("decoded 1st tarinig review :")
print(decodedReview(x_train[0]))
###############################################################
# step 7 : display sample reviews
##############################################################

print("-"*40)
print("----------------------sample reviews----------------------")
print("-"*40)

for i in range(4):
    review = decodedReview(x_train[i])
    
    print("-"*40)
    print("review number :",i+1)
    print("review :")
    print(review)
    
    print("-"*40)
    if y_train[i]==1:
        print("sentiment is positive")
        
    else :
        print("sentiment is negative")
    
###############################################################
# step 8 : padding 
##############################################################

x_train_padded = pad_sequences(
    x_train ,
    maxlen= max_lenght,
)

x_test_padded = pad_sequences(
    x_test,
    maxlen = max_lenght,
)

print("training data shape :",x_train_padded.shape)
print("testing data shape :",x_test_padded.shape)

###############################################################
# step 9 : Create LSTM Model 
##############################################################

model = Sequential()

model.add(
    Embedding(
    input_dim = vocab_size,
    output_dim = 32,            # each word will be represented by 32 dimensional vector 
    input_length = max_lenght
)
)

model.add(
    LSTM(
      units = 64   # size of hidden state
    )
)

model.add(
    Dense(
      units= 1,       # one output
      activation = "sigmoid"   # use to produce probability 
    )
)

# Project Architecture 
# review --> embedding --> LSTM --> Dense --> Sidmoid --> positive /negative

###############################################################
# step 10 : complie LSTM Model 
############################################################## 


model.compile( 
    optimizer = "adam",   # algo to update weights
    loss = "binary_crossentropy",   # loss function
    metrics = ["accuracy"]     # measure classification accuracy
)

print("Model compiled successfully")

###############################################################
# step 11 : train LSTM Model 
##############################################################

print("Model trainig")

model.fit(
    x_train_padded,   # input trainig reviewa
    y_train,          # actual sentiment labels
    epochs = 3,       # complete dataset gets processes 3 times
    batch_size =  64, #process 64 reviews in one batch
    validation_split = 0.2 #use 20 percent training for validation
)

print("Model trainig gets completed")

###############################################################
# step 12 : evaluate the model
##############################################################

accuracy = model.evaluate(
                        x_test_padded,    # testing reviews
                        y_test,           # actual testing labels
                        verbose = 0       # don't display the progress bar
                    )

print("Testing Accuracy :",accuracy)

###############################################################
# step 13 : Predict the review 
##############################################################

test_review_number = 0
original_review = x_test[test_review_number]
decodedReview = decodedReview(original_review)

print("review given to the model :")
print(decodedReview)

###############################################################
# step 14 : Get the actual Sentiment
##############################################################

actual_value = y_test[test_review_number]

if actual_value ==1:
    actual_sentiment = "positive"
else:
    actual_sentiment="negative"

print("Actual sentiment :",actual_sentiment)

###############################################################
# step 15 :Predict the sentiment
##############################################################

review_for_prediction = x_test_padded[test_review_number : test_review_number + 1]

prediction =model.predict(
                    review_for_prediction,
                    verbose = 0
                )

probability = prediction[0][0]

if probability >= 0.5 :
    predicted_sentiment ="positive"
else :
    predicted_sentiment ="negative"
    
print("final result :")

print("predicted probability :",probability)
print("actual sentiment :",actual_sentiment)
print("predictec sentiment :",predicted_sentiment)

print("-"*40)




