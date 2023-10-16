from PIL import Image, ImageFilter

# There is a code in word_matrix.png 
# figure it with mask.png

im1 = Image.open("word_matrix.png")
im2 = Image.open('mask.png').resize(im1.size)

mask = Image.new("L", im1.size, 100)
im = Image.composite(im1, im2, mask)

print(im)