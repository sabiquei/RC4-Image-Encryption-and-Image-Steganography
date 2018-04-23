import Util

def initial_perm(s, k):
    """ Initial permutation of array S using array U. """
    j = 0
    key_length = len(k)
    for i in range(256):
        j = (j + s[i] + k[i%key_length]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def prga(s):
    """
    Pseudo Random Generation Algorithm

    :param s: Permuted S Array
    :return: random int value ranging from 0 - 255
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = s[(s[i] + s[j]) % 256]
        yield t


def rc4(s, u):
    s = initial_perm(s, u)
    return prga(s)

def rc4_encryption(sec_image_name,key,output_path,encrypted_image_name):
    image = Util.get_image(image_path=sec_image_name)
    print "Encrypting..."
    # print image details
    # print("Image Shape: ", image.shape)
    img_width, img_height = image.shape[:2]
    # print('Image width: %i, height: %i ' % (img_width, img_height))

    # Convert external key
    dec_key = Util.get_dec_key(key)
    #print dec_key

    #print x0

    # Construct S Array
    s_array = Util.get_s_array()

    ran_gen = rc4(s_array, dec_key)

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

    Util.save_image(image, shape=image.shape, flag = 0, dest_dir=output_path, name="encrypted_image")
    print "Completed"

def rc4_decryption(encrypted_image_name, key, output_path, decrypted_image_name):
    image = Util.get_image(image_path=encrypted_image_name)

    print"Decrypting..."
    #print("Image Shape: ", image.shape)
    img_width, img_height = image.shape[:2]
    #print('Image width: %i, height: %i ' % (img_width, img_height))

    # Convert external key
    dec_key = Util.get_dec_key(key)
    # print dec_key

    # Construct S Array
    s_array = Util.get_s_array()

    ran_gen = rc4(s_array, dec_key)

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

    Util.save_image(image, shape=image.shape, flag = 1, dest_dir=output_path, name=decrypted_image_name)
    print "Completed"