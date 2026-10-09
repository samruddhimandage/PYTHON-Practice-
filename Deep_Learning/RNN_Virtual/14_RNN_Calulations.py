# ht = tanh (wx * xt + wh * ht-1 +b)

# Xt  = current input
# wx  = weight of current input
# wh  = weight of previous hidden state
# b   = bias
# ht-1= previous hidden state
# tanh= activation function
# ht  = new hidden state

import numpy as np

def sigmoid(x):
    return 1 / ( 1 + np.exp(-x))

def marvellousRNN_prediction():
    print("Calculation if RNN")
    
    inputs =[1,2,5,3]
    # food was not good

    hidden_state = 0
    
    #RNN parameters
    wx = 0.5     #wt of X
    wh = 0.8     #wt of hidden
    bias =0.1    #bias
    
    for time_step , x in enumerate(inputs):
        previous_hidden_state = hidden_state
        
        weighted_input = wx * x

        weighted_memory = wh * previous_hidden_state
        
        total = weighted_input + weighted_memory + bias
        
        hidden_state = np.tanh(total)
        
        print("Time Step :",time_step + 1)
        print("Input :", x)
        print("Hidden State :", hidden_state)
        print("_"* 30)
        
    print("Final Hidden State :",hidden_state)
    
       
def main():
    marvellousRNN_prediction()
if __name__=="__main__":
    main()
    
