import cv2
import numpy as np
import tensorflow as tf


# ============================================================
# 1. LOAD YOUR TRAINED CRACK DETECTION MODEL
# ============================================================

MODEL_PATH = "Marvellous_Crack_Detection_Model.h5"

model = tf.keras.models.load_model(MODEL_PATH)

print("Crack detection model loaded successfully!")
print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)


# ============================================================
# 2. OPEN WEBCAM
# ============================================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam started.")
print("Press 'q' to quit.")


# ============================================================
# 3. REAL-TIME DETECTION
# ============================================================

while True:

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break


    # --------------------------------------------------------
    # Convert BGR → RGB
    # --------------------------------------------------------

    image = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # --------------------------------------------------------
    # Resize to the model's required size
    # Model expects: 128 × 128 × 3
    # --------------------------------------------------------

    image = cv2.resize(
        image,
        (128, 128)
    )


    # --------------------------------------------------------
    # Convert image to NumPy array
    # --------------------------------------------------------

    image = np.array(
        image,
        dtype=np.float32
    )


    # --------------------------------------------------------
    # Normalize pixel values
    # --------------------------------------------------------

    image = image / 255.0


    # --------------------------------------------------------
    # Add batch dimension
    #
    # Before:
    #     (128, 128, 3)
    #
    # After:
    #     (1, 128, 128, 3)
    # --------------------------------------------------------

    image = np.expand_dims(
        image,
        axis=0
    )


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(
        image,
        verbose=0
    )[0][0]


    # --------------------------------------------------------
    # CLASSIFICATION
    # --------------------------------------------------------

    if prediction >= 0.5:

        label = "CRACK"

        confidence = prediction * 100

    else:

        label = "NO CRACK"

        confidence = (1 - prediction) * 100


    # --------------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------------

    text = f"{label}: {confidence:.2f}%"


    # Red for crack
    # Green for no crack

    if label == "CRACK":
        text_color = (0, 0, 255)
    else:
        text_color = (0, 255, 0)


    cv2.putText(
        frame,
        text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        text_color,
        3,
        cv2.LINE_AA
    )


    # --------------------------------------------------------
    # SHOW WEBCAM
    # --------------------------------------------------------

    cv2.imshow(
        "Concrete Surface Crack Detection",
        frame
    )

    # --------------------------------------------------------
    # PRESS Q TO QUIT
    # --------------------------------------------------------

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ============================================================
# 4. CLEANUP
# ============================================================

cap.release()

cv2.destroyAllWindows()

print("Program stopped.")