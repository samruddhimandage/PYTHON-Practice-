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
    
