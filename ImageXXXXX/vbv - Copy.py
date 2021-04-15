from PIL import Image, ImageFilter

def all_are_dark_around(image, r, c):

    # range gives the bounds [-1, 0, 1]
    # you could use the list directly. Probably better for this especific case
    for i in range(-1,2):              
        for j in range(-1,2):
            # if the pixel is clear return False.
            # note that image[r+0][c+0] is always dark by definition
            if image[r+i][c+j] <= 128:  
                return False
    #the loop finished -> all pixels in the 3x3 square were dark
    return True


image = Image.open("puzzle.png")

