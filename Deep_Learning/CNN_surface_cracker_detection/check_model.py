import tensorflow as tf

MODEL_PATH = "Marvellous_Crack_Detection_Model.h5"

print("Loading crack detection model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("\n========== MODEL INFORMATION ==========")

print("Input shape:")
print(model.input_shape)

print("\nOutput shape:")
print(model.output_shape)

print("\nNumber of layers:")
print(len(model.layers))

print("\n========== MODEL SUMMARY ==========")

model.summary()