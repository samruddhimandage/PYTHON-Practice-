# ------------------------------------------------------------
# Marvellous Infosystems
# Surface Crack Detection using CNN
#
# Dataset folders:
# Positive = Crack Detected
# Negative = No Crack
# ------------------------------------------------------------

import os
import shutil
import random
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from sklearn.metrics import classification_report, confusion_matrix


# ------------------------------------------------------------
# Step 1: Dataset path
# ------------------------------------------------------------

original_dataset_path = "Concrete Crack Dataset"

positive_path = os.path.join(
    original_dataset_path,
    "Positive"
)

negative_path = os.path.join(
    original_dataset_path,
    "Negative"
)

base_dir = "CrackDataset"

train_dir = os.path.join(
    base_dir,
    "train"
)

test_dir = os.path.join(
    base_dir,
    "test"
)

train_crack_dir = os.path.join(
    train_dir,
    "Crack"
)

train_nocrack_dir = os.path.join(
    train_dir,
    "NoCrack"
)

test_crack_dir = os.path.join(
    test_dir,
    "Crack"
)

test_nocrack_dir = os.path.join(
    test_dir,
    "NoCrack"
)


# ------------------------------------------------------------
# Step 2: Create required folder structure
# ------------------------------------------------------------

for folder in [
    train_crack_dir,
    train_nocrack_dir,
    test_crack_dir,
    test_nocrack_dir
]:
    os.makedirs(folder, exist_ok=True)


# ------------------------------------------------------------
# Step 3: Split dataset into training and testing
# ------------------------------------------------------------

def Split_Data(
    source_folder,
    train_folder,
    test_folder,
    split_ratio=0.8
):

    files = os.listdir(source_folder)

    files = [
        file for file in files
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        )
    ]

    random.shuffle(files)

    train_size = int(
        len(files) * split_ratio
    )

    train_files = files[:train_size]
    test_files = files[train_size:]

    for file in train_files:

        src = os.path.join(
            source_folder,
            file
        )

        dst = os.path.join(
            train_folder,
            file
        )

        if not os.path.exists(dst):
            shutil.copy(src, dst)

    for file in test_files:

        src = os.path.join(
            source_folder,
            file
        )

        dst = os.path.join(
            test_folder,
            file
        )

        if not os.path.exists(dst):
            shutil.copy(src, dst)


Split_Data(
    positive_path,
    train_crack_dir,
    test_crack_dir
)

Split_Data(
    negative_path,
    train_nocrack_dir,
    test_nocrack_dir
)

print("Dataset split completed successfully.")


# ------------------------------------------------------------
# Step 4: Display dataset count
# ------------------------------------------------------------

print(
    "Training Crack Images:",
    len(os.listdir(train_crack_dir))
)

print(
    "Training No Crack Images:",
    len(os.listdir(train_nocrack_dir))
)

print(
    "Testing Crack Images:",
    len(os.listdir(test_crack_dir))
)

print(
    "Testing No Crack Images:",
    len(os.listdir(test_nocrack_dir))
)


# ------------------------------------------------------------
# Step 5: Image preprocessing
# ------------------------------------------------------------

image_size = 128
batch_size = 32

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=15,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(
    rescale=1.0 / 255
)


train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(image_size, image_size),
    batch_size=batch_size,
    class_mode="binary"
)

test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=(image_size, image_size),
    batch_size=batch_size,
    class_mode="binary",
    shuffle=False
)

print(
    "Class Indices:",
    train_data.class_indices
)


# ------------------------------------------------------------
# Step 6: Display sample images
# ------------------------------------------------------------

sample_images, sample_labels = next(train_data)

plt.figure(figsize=(10, 6))

for i in range(6):

    plt.subplot(2, 3, i + 1)

    plt.imshow(sample_images[i])

    plt.title(
        "Crack"
        if sample_labels[i]
        == train_data.class_indices["Crack"]
        else "No Crack"
    )

    plt.axis("off")

plt.suptitle("Sample Training Images")

plt.show()


# ------------------------------------------------------------
# Step 7: Build CNN model
# ------------------------------------------------------------

model = Sequential()


# First convolution block

model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation="relu",
        input_shape=(
            image_size,
            image_size,
            3
        )
    )
)

model.add(
    MaxPooling2D(
        pool_size=(2, 2)
    )
)


# Second convolution block

model.add(
    Conv2D(
        filters=64,
        kernel_size=(3, 3),
        activation="relu"
    )
)

model.add(
    MaxPooling2D(
        pool_size=(2, 2)
    )
)


# Third convolution block

model.add(
    Conv2D(
        filters=128,
        kernel_size=(3, 3),
        activation="relu"
    )
)

model.add(
    MaxPooling2D(
        pool_size=(2, 2)
    )
)


# Flatten layer

model.add(
    Flatten()
)


# Fully connected layer

model.add(
    Dense(
        128,
        activation="relu"
    )
)


# Dropout

model.add(
    Dropout(0.5)
)


# Output layer

model.add(
    Dense(
        1,
        activation="sigmoid"
    )
)


# ------------------------------------------------------------
# Step 8: Compile model
# ------------------------------------------------------------

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# ------------------------------------------------------------
# Step 9: Train model
# ------------------------------------------------------------

history = model.fit(
    train_data,
    epochs=10,
    validation_data=test_data
)


# ------------------------------------------------------------
# Step 10: Plot training accuracy
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.xlabel("Epochs")
plt.ylabel("Accuracy")

plt.title(
    "Training and Validation Accuracy"
)

plt.legend()

plt.show()


# ------------------------------------------------------------
# Plot training loss
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.title(
    "Training and Validation Loss"
)

plt.legend()

plt.show()


# ------------------------------------------------------------
# Step 11: Evaluate model
# ------------------------------------------------------------

loss, accuracy = model.evaluate(test_data)

print(
    "Testing Loss:",
    loss
)

print(
    "Testing Accuracy:",
    accuracy * 100
)


# ------------------------------------------------------------
# Step 12: Confusion Matrix
# ------------------------------------------------------------

predictions = model.predict(test_data)

predicted_classes = (
    predictions > 0.5
).astype(int).reshape(-1)

actual_classes = test_data.classes

print("Confusion Matrix:")

print(
    confusion_matrix(
        actual_classes,
        predicted_classes
    )
)


# ------------------------------------------------------------
# Classification Report
# ------------------------------------------------------------

print("Classification Report:")

print(
    classification_report(
        actual_classes,
        predicted_classes
    )
)


# ------------------------------------------------------------
# Step 13: Save model
# ------------------------------------------------------------

model.save(
    "Marvellous_Crack_Detection_Model.h5"
)

print(
    "Model saved successfully."
)


# ------------------------------------------------------------
# Step 14: Predict single image
# ------------------------------------------------------------

def Predict_Crack(image_path):

    img = load_img(
        image_path,
        target_size=(
            image_size,
            image_size
        )
    )

    img_array = img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    result = model.predict(
        img_array
    )

    crack_index = (
        train_data.class_indices["Crack"]
    )

    print(
        "Prediction Value:",
        result[0][0]
    )

    if crack_index == 1:

        if result[0][0] > 0.5:
            print("Final Result: Crack Detected")
        else:
            print("Final Result: No Crack")

    else:

        if result[0][0] > 0.5:
            print("Final Result: No Crack")
        else:
            print("Final Result: Crack Detected")

    plt.imshow(
        load_img(image_path)
    )

    plt.title("Input Image")

    plt.axis("off")

    plt.show()


# ------------------------------------------------------------
# Step 15: Test single image
# ------------------------------------------------------------

# Change this path according to your image.

# Example:
#
# Predict_Crack(
#     "CrackDataset/test/Crack/00100.jpg"
# )