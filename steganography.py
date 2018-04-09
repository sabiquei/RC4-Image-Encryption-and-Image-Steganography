from PIL import Image
import scipy.misc
import numpy as np
import Util

# Variables

def encode(input_image_path, output_dir,cov_image_name):
    print "Encoding..."

    # Read Cover Image
    cov_image = Util.get_image(image_path=cov_image_name)
    cov_img_width, cov_img_height = cov_image.shape[:2]
    #print('Image width: %i, height: %i ' % (cov_img_width, cov_img_height))

    # Read Secret Image
    sec_image = Util.get_image(image_path=input_image_path)
    sec_img_width, sec_img_height = sec_image.shape[:2]
    #print('Image width: %i, height: %i ' % (sec_img_width, sec_img_height))

    # Get Height and width of secret image in bits
    sec_img_width_bits = format(sec_img_width, "016b")  # convert it in to 16 bit data to store in 2 pixels
    #print sec_img_width_bits
    sec_img_height_bits = format(sec_img_height, "016b")  # convert it in to 16 bit data to store in 2 pixels
    #print sec_img_height_bits

    img_bit_stream = sec_img_width_bits
    img_bit_stream += sec_img_height_bits

    #print img_bit_stream

    sec_bit_stream = ""

    # Converting the secret image in to bit stream
    for i in range(sec_img_width):
        for j in range(sec_img_height):
            pixel = sec_image[i, j]
            sec_bit_stream += format(pixel[0], "08b")
            sec_bit_stream += format(pixel[1], "08b")
            sec_bit_stream += format(pixel[2], "08b")

    # Convert bit stream length in to 32 bits
    sec_bit_stream_length = format(len(sec_bit_stream), "032b")

    # Getting final bit stream
    # Adding bit stream length and then bit stream itself
    img_bit_stream += sec_bit_stream_length
    #print img_bit_stream
    img_bit_stream += sec_bit_stream

    # Final length for encoding
    img_bit_stream_length = len(img_bit_stream)

    #print img_bit_stream_length

    stream_pointer = 0
    flag = 1

    # Embed this bit stream in the image
    # 8 Bits per pixel 3 in red, 3 in green and 3 in blue
    for i in range(cov_img_width):
        if (flag == 0):
            break
        for j in range(cov_img_height):
            if (stream_pointer == img_bit_stream_length):
                flag = 0
                break

            pixel = cov_image[i, j]

            red = format(pixel[0], "08b")
            red = list(red)
            green = format(pixel[1], "08b")
            green = list(green)
            blue = format(pixel[2], "08b")
            blue = list(blue)

            for k in range(0, 3):
                red[5 + k] = img_bit_stream[stream_pointer]
                stream_pointer += 1

            for k in range(0, 3):
                green[5 + k] = img_bit_stream[stream_pointer]
                stream_pointer += 1

            for k in range(0, 2):
                blue[6 + k] = img_bit_stream[stream_pointer]
                stream_pointer += 1

            red = ''.join(str(e) for e in red)
            green = ''.join(str(e) for e in green)
            blue = ''.join(str(e) for e in blue)

            green = int(green, 2)
            blue = int(blue, 2)
            red = int(red, 2)

            pixel[0] = red
            pixel[1] = green
            pixel[2] = blue

            cov_image[i, j] = pixel

    if flag == 1:
        print "Image not Large enough to hold all the data"
    else:
        Util.show_image(cov_image, shape=cov_image.shape, dest_dir=output_dir, name="stego_image")
        print "Complete.."

    #print stream_pointer


    '''sec_stream_img_data_bits = img_bit_stream

    i = 61440
    while (i < 61680):
        print sec_stream_img_data_bits[i], sec_stream_img_data_bits[i + 1], sec_stream_img_data_bits[i + 2], \
        sec_stream_img_data_bits[i + 3], sec_stream_img_data_bits[i + 4], sec_stream_img_data_bits[i + 5], \
        sec_stream_img_data_bits[i + 6], sec_stream_img_data_bits[i + 7] 
        i += 8 '''

        # Expects cover_image_path, input_image path
    # Opens cover_image, input_image
    # Get height and width of cover image
    # Convert image in to bit stream
    # get length of bit stream
    # // Expecting to encode 3 bits in red,3 bits in green and 2 bits in blue
    # embed height in first pixel of cover image - store the value as a 8 bit number
    # embed width in second pixel of cover image - store the value as a 8 bit number
    # embed length in third & fourth pixel of cover image - store the value as a 16 bit number
    # embed bit by bit in each of the pixels of cover image from it's 5th pixel
    # The expectation is that each pixel value (R,G,B) will be converted to it's binary equivalent and r will be stored in first pixel of cover,g in second and b in third and this pattern repeats until the whole image is done.
    # form the stego_image and then store it as stego image and return the stego image_path

def decode(stego_image_path,output_path):
    print "Decoding....."

    # Read Stego Image
    cov_image = Util.get_image(image_path=stego_image_path)
    cov_img_width, cov_img_height = cov_image.shape[:2]
    #print('Image width: %i, height: %i ' % (cov_img_width, cov_img_height))



    # Get secret image binary width
    sec_img_width_bits = ""
    for i in range(0, 2):
        pixel = cov_image[0, i]
        red = format(pixel[0], "08b")
        #print red
        green = format(pixel[1], "08b")
        #print green
        blue = format(pixel[2], "08b")
        #print blue
        for j in range(0,3):
            sec_img_width_bits += red[5+j]
        for j in range(0,3):
            sec_img_width_bits += green[5+j]
        for j in range(0,2):
            sec_img_width_bits += blue[6+j]

    #print sec_img_width_bits

    sec_img_width = int(sec_img_width_bits,2)
    #print sec_img_width

    # Get secret image binary height
    sec_img_height_bits = ""
    for i in range (2, 4):
        pixel = cov_image[0, i]
        red = format(pixel[0], "08b")
        #print red
        green = format(pixel[1], "08b")
        #print green
        blue = format(pixel[2], "08b")
        #print blue
        for j in range(0,3):
            sec_img_height_bits += red[5+j]
        for j in range(0,3):
            sec_img_height_bits += green[5+j]
        for j in range(0,2):
            sec_img_height_bits += blue[6+j]

    #print sec_img_height_bits

    sec_img_height = int(sec_img_height_bits, 2)
    #print sec_img_height


    # Get stream length from the next 32 bits that is 4 pixels
    sec_stream_length_bits = ""
    for i in range (4, 8):
        pixel = cov_image[0, i]
        red = format(pixel[0], "08b")
        #print red
        green = format(pixel[1], "08b")
        #print green
        blue = format(pixel[2], "08b")
        #print blue
        for j in range(0,3):
            sec_stream_length_bits += red[5+j]
        for j in range(0,3):
            sec_stream_length_bits += green[5+j]
        for j in range(0,2):
            sec_stream_length_bits += blue[6+j]

    #print sec_stream_length_bits
    sec_stream_length = int(sec_stream_length_bits,2)
    #print sec_stream_length

    # since the first 8 pixels has been already considered we do not need to consider them
    # We need to extract 8 bit per pixels from 9th pixel until the end

    sec_stream_img_data_bits =""

    # Extracting the first row from the 9th pixel
    for i in range(8,cov_img_height):
        pixel = cov_image[0, i]
        red = format(pixel[0], "08b")
        # print red
        green = format(pixel[1], "08b")
        # print green
        blue = format(pixel[2], "08b")
        # print blue
        for j in range(0, 3):
            sec_stream_img_data_bits += red[5 + j]
        for j in range(0, 3):
            sec_stream_img_data_bits += green[5 + j]
        for j in range(0, 2):
            sec_stream_img_data_bits += blue[6 + j]

    #print len(sec_stream_img_data_bits)
    #print sec_stream_length


    # Extracting for the remaining pixels

    flag = 1
    stream_pointer = len(sec_stream_img_data_bits)

    for i in range(1,cov_img_width):
        if (flag == 0):
            break
        for j in range(cov_img_height):
            if (stream_pointer == sec_stream_length):
                flag = 0
                break
            pixel = cov_image[i, j]
            red = format(pixel[0], "08b")
            # print red
            green = format(pixel[1], "08b")
            # print green
            blue = format(pixel[2], "08b")
            # print blue
            for k in range(0, 3):
                sec_stream_img_data_bits += red[5 + k]
                stream_pointer += 1
            for k in range(0, 3):
                sec_stream_img_data_bits += green[5 + k]
                stream_pointer += 1
            for k in range(0, 2):
                sec_stream_img_data_bits += blue[6 + k]
                stream_pointer += 1

    #print len(sec_stream_img_data_bits)
    #print stream_pointer

    '''i = 614400
    while (i < 614640):
        print sec_stream_img_data_bits[i], sec_stream_img_data_bits[i + 1], sec_stream_img_data_bits[i + 2], \
        sec_stream_img_data_bits[i + 3], sec_stream_img_data_bits[i + 4], sec_stream_img_data_bits[i + 5], \
        sec_stream_img_data_bits[i + 6], sec_stream_img_data_bits[i + 7] 
        i += 8 '''

    # Image size
    width = sec_img_width
    height = sec_img_height
    channels = 3

    # Create an empty image
    img = np.zeros((width, height, channels), dtype=np.uint8)

    stream_pointer = 0

    # Set the RGB values
    for y in range(sec_img_width):
        for x in range(sec_img_height):
            # get red
            red = ""
            for i in range(0,8):
                red += sec_stream_img_data_bits[stream_pointer]
                stream_pointer += 1
            # get green
            green = ""
            for i in range(0, 8):
                green += sec_stream_img_data_bits[stream_pointer]
                stream_pointer += 1
            #get blue
            blue =""
            for i in range(0,8):
                blue += sec_stream_img_data_bits[stream_pointer]
                stream_pointer +=1

            red = int(red, 2)
            green = int(green, 2)
            blue = int(blue, 2)

            pixel = [red, green, blue]
            img[y][x] = pixel

    # Display the image
    #scipy.misc.imshow(img)

    # Save the image
    output_path += "/encrypted_image.png"
    scipy.misc.imsave(output_path, img)
    print"Complete.."


    # Expects the path of stego image
    # Get the height from first pixel of stego image
    # Get the width from second pixel of stego image
    # Get the length of the image bit stream from 3rd & 4th pixel of stego image
    # Form an image shape using Image.formaarray() with height and width which was obtained before
    # Repeat for i in range 0,length
        # Retrieve 24 bits and then convert them in to RGB of 8 each
        # Store it as pixel
        # Always check for proper width and height
    # Once the image is completely constructed , store it as decoded secret image
    # return the decoded stego image path


#encode("","")
#decode("")