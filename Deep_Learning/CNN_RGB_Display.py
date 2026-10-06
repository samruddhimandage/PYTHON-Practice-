from PIL import Image
import numpy as np

img = Image.open("color.png")

img = img.resize((28,28))

pixels = np.array(img)

print("Image Information :")
print("Image shape :",pixels.shape)
print("Height :",pixels.shape[0],"Rows")
print("width :",pixels.shape[1],"columns")
print("channels :",pixels.shape[2],"(R,G,B)")

total = pixels.shape[0] * pixels.shape[1] *  pixels.shape[2]
#            28         *       28        *        3

print("Total Pixel :",total)

print("Single Pixel Meaning :")

r = pixels[10][10][0]
g = pixels[10][10][1]
b = pixels[10][10][2]
print("Pixel details of 10,10 pixel is :")
print("Red",r)
print("Green",g)
print("Blue",b)


# Output :
#Image Information :
#Image shape : (28, 28, 3)
#Height : 28 Rows
#width : 28 columns
#channels : 3 (R,G,B)
#Pixel : 784  (of one cannel)
# total Pixel : 2352

