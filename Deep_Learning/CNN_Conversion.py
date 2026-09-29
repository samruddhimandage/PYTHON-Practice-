from PIL import Image

img = Image.open("digit.png")
print(img.size)

img = img.convert("L")
img = img.resize((28,28))

img.save("digit_28X28.png")

print(img.size)
