import tensorflow as tf

inputs = tf.constant([1.0,2.0,3.0])

weights = tf.constant([0.5,-0.2,0.8])

bias = tf.constant(0.1)

weighted_sum = tf.reduce_sum(inputs * weights) + bias

print("Inputs : ",inputs.numpy())
print("Weights : ",weights.numpy()) 
print("Bias :",bias.numpy()) #1.0
print("Weighted Sum :",weighted_sum.numpy()) #2.6

output = tf.sigmoid(weighted_sum) #0.93

print("Output is : ", output.numpy())