from PIL import Image
import numpy as np

img = Image.open("digit_28X28.png")
img = img.convert("L")

img = img.resize((28,28))
pixels = np.array(img)

print("Image Size :",pixels.shape)

print("pixel Values :",pixels)

# 0  = pure balck
# 255 = pure white
# 50 = dark grey
# 120 = medium grey
# 200 = light grey