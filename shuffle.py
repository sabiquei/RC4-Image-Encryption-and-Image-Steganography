from PIL import Image
import math

def shuffle_unshuffle(input_name):

    im = Image.open(input_name,"r")
    print "Shuffling.."
    arr = im.load()  # pixel data stored in this 2D array

    def rot(A, n, x1, y1):  # this is the function which rotates a given block
        temple = []
        for i in range(n):
            temple.append([])
            for j in range(n):
                temple[i].append(arr[x1 + i, y1 + j])
        for i in range(n):
            for j in range(n):
                arr[x1 + i, y1 + j] = temple[n - 1 - i][n - 1 - j]

    xres, yres = im.size

    BLKSZ = 16  # blocksize

    for i in range(2, BLKSZ + 1):
        for j in range(int(math.floor(float(xres) / float(i)))):
            for k in range(int(math.floor(float(yres) / float(i)))):
                rot(arr, i, j * i, k * i)
    for i in range(3, BLKSZ + 1):
        for j in range(int(math.floor(float(xres) / float(BLKSZ + 2 - i)))):
            for k in range(int(math.floor(float(yres) / float(BLKSZ + 2 - i)))):
                rot(arr, BLKSZ + 2 - i, j * (BLKSZ + 2 - i), k * (BLKSZ + 2 - i))

    # Saving the shuffled image over encrypted image
    im.save(input_name)
    print "Completed.."
    #Image._show(im)
