# Developed by Amith,Adhirath,Akhil,Sabique.
# RC4 ENCRYPTION AND SHUFFLING ON COLOUR IMAGES

from PIL import Image
import math
import Util
import RC4
import steganography

# Variables

SYSTEM_PARAMETER = 4.0
output_dir = "/Users/sabique/Desktop/output"
input_img_name = "input_image"
encrypted_image = "encrypted_image"
encrypted_image_input_path = "/Users/sabique/Desktop/output/"+encrypted_image+".png"
decrypted_image = "decrypted"
stego_name = "/Users/sabique/Desktop/output/stego_image.png"
decoded_secret = output_dir+"/secret_decoded.png"

def shuffle_unshuffle(input_name):

    im = Image.open(input_name,"r")
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

    BLKSZ = 64  # blocksize

    for i in range(2, BLKSZ + 1):
        for j in range(int(math.floor(float(xres) / float(i)))):
            for k in range(int(math.floor(float(yres) / float(i)))):
                rot(arr, i, j * i, k * i)
    for i in range(3, BLKSZ + 1):
        for j in range(int(math.floor(float(xres) / float(BLKSZ + 2 - i)))):
            for k in range(int(math.floor(float(yres) / float(BLKSZ + 2 - i)))):
                rot(arr, BLKSZ + 2 - i, j * (BLKSZ + 2 - i), k * (BLKSZ + 2 - i))

    # Saving the shuffled image over encrypted image
    im.save(encrypted_image_input_path)
    #Image._show(im)


def RC4_Encryption():

    # ---------------
    # ENCRYPTIONSTUFF
    # ---------------

    # get image

    key = raw_input("Enter the Key : ")

    #input image path
    input_image_path = "input_image/"
    input_image_path += raw_input("Enter the image name including extension : ")
    #print input_image_path

    print "Encrypting the Image using RC4..."

    image = Util.get_image(image_path=input_image_path)
    Util.show_image(image, shape=image.shape, dest_dir=output_dir, name=input_img_name)

    # print image details
    #print("Image Shape: ", image.shape)
    img_width, img_height = image.shape[:2]
    #print('Image width: %i, height: %i ' % (img_width, img_height))

    # Convert external key
    dec_key = Util.get_dec_key(key)
    #print dec_key

    # Generate initial value X0
    x0 = Util.get_x0(dec_key)
    print x0

    # Construct X, U, and S Array
    x_array = Util.get_x_array(x0, SYSTEM_PARAMETER)
    u_array = Util.get_u_array(x_array, img_width, img_height)
    s_array = Util.get_s_array()
    ran_gen = RC4.rc4(s_array, u_array)

    for i in range(img_width):
        for j in range(img_height):
            pixel = image[i, j]
            t = next(ran_gen)
            red = (pixel[0] + t) % 256
            t = next(ran_gen)
            green = (pixel[1] + t) % 256
            t = next(ran_gen)
            blue = (pixel[2] + t) % 256
            image[i, j] = (red, green, blue)

    Util.show_image(image, shape=image.shape, dest_dir=output_dir, name=encrypted_image)

    # Call Shuffle Function
    print "Shuffling ..."
    shuffle_unshuffle(encrypted_image_input_path)
    steganography.encode(encrypted_image_input_path, output_dir)

def RC4_Decryption():

    # ---------------
    # DECRYPTIONSTUFF
    # ---------------

    steganography.decode(stego_name,output_dir)

    key = raw_input("Enter the Key : ")

    # Unshuffling the shuffled Image
    print "Unshuffling ..."
    shuffle_unshuffle(decoded_secret)

    #Read Encrypted Image and print details
    image = Util.get_image(image_path=encrypted_image_input_path)

    print"Decrypting..."
    print("Image Shape: ", image.shape)
    img_width, img_height = image.shape[:2]
    print('Image width: %i, height: %i ' % (img_width, img_height))

    # Convert external key
    dec_key = Util.get_dec_key(key)
    print dec_key

    x0 = Util.get_x0(dec_key)
    # Construct X, U, and S Array
    x_array = Util.get_x_array(x0, SYSTEM_PARAMETER)
    u_array = Util.get_u_array(x_array, img_width, img_height)
    s_array = Util.get_s_array()
    ran_gen = RC4.rc4(s_array, u_array)

    for i in range(img_width):
        for j in range(img_height):
            pixel = image[i, j]
            t = next(ran_gen)
            red = (pixel[0] + 256 - t) % 256
            t = next(ran_gen)
            green = (pixel[1] + 256 - t) % 256
            t = next(ran_gen)
            blue = (pixel[2] + 256 - t) % 256
            image[i, j] = (red, green, blue)

    Util.show_image(image, shape=image.shape, dest_dir=output_dir, name=decrypted_image)


print "------------------------------\n" \
      " RC4 ENCRYPTION and SHUFFLING\n" \
      "------------------------------"
option = 0

while(option != 3):
    print "1.Encryption Procedure\n" \
          "2.Decryption Procedure\n" \
          "3.Exit"

    option = input("Enter your choice : ")

    if(option == 1 ):
        RC4_Encryption()

    elif(option == 2):
        RC4_Decryption()

    elif(option == 3):
        print"Exiting..."

    else:
        print"Invalid choice\n" \
             "Please give another input"