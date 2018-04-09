from PIL import Image
from scipy import misc
import binascii



def get_image(image_path):
    return misc.imread(image_path)


def show_image(image, shape, dest_dir=None, name=None):
    img = Image.fromarray((image.reshape(shape)).astype('uint8'), 'RGB')
    #img.show()
    img.save(dest_dir + '/' + name + ".png", "PNG")
    print("Image location: ", dest_dir + '/' + name + ".png", "PNG")

def get_x_array(x, sys_param):
    # Returns array X of seemingly random values obtained from CLM function
    x_array = []

    while len(x_array) < 256:
        x = sys_param * x * (1.0 - x)
        x_array.append(x)
    return x_array


def get_u_array(x_array, width, height):
    """ Build U array from X array """
    u_array = []
    for value in x_array:
        u_value = (value * width) / height
        u_array.append(int(round(u_value, 8) * (10 ** 8)))
    return u_array


def get_s_array():
    """ Build initial S array """
    s_array = []
    for _ in range(0, 256):
        s_array.append(_)
    return s_array


def get_dec_key(key):
    """ Convert external key from string to decimal """
    #hex_key = str(binascii.hexlify(key), 'ascii')
    hex_key = str(binascii.hexlify(key))
    dec_key = []
    print("Hexdecimal Key: ", hex_key)

    for _ in range(len(hex_key)):
        dec_key.append(ord(hex_key[_]))
    return dec_key


def get_x0(dec_key):
    """ Compute initial x from key to use in construction of X array """
    x_denum = 2 ** (len(dec_key) // 2)

    x01_num = []
    for i in range(0, len(dec_key) // 2):
        x01_num.append(dec_key[i] * (2 ** i))
    x01 = sum(x01_num) / float(x_denum)

    x02_num = []
    for i in range(len(dec_key) // 2, len(dec_key)):
        x02_num.append(dec_key[i] * (2 ** i))
    x02 = sum(x02_num) / float(x_denum)

    return (x01 + x02) % 1