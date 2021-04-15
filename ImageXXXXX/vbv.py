from PIL import Image, ImageFilter
image = Image.open("puzzle.png")
mask=image.convert("L")
th=150 # the value has to be adjusted for an image of interest 
mask = mask.point(lambda i: i < th and 255)
mask.show()