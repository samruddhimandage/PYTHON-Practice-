import numpy as np

#Step 1 : Define input features as X
#                [ X1  , X2 , X3]
input = np.array([2.0 ,3.0 , 4.0])
print(" X : ",input)

#Step 2 : Define Weights as W
#                  [ W1  , W2 , W3]
Weights = np.array([0.5 ,0.3 ,0.2])
print("W : ",Weights)

#Step 3 : Define Bias
# b
Bias= 1.0
print("b : ",Bias
      )
#step  4 : Calculate Weighted sum i.e Z

#Z = x1w1 + x2w2 + x3w3 + b
#Z = (2.0*0.5) + (3.0*0.3) + (4.0*0.2) + 1.0

Z = np.dot(input,Weights) + Bias                   # dot = method of numpy Xn * Wn 
print("Z :",Z)

# Step 5:Activation function (ReLU)

def relu(x):
    return max(0,x)

#step 6 : Final Output

Y = relu(Z)

print("Output : ",Y)