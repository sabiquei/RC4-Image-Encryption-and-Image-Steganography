from PIL import Image
from scipy import misc
import binascii



def get_image(image_path):
    return misc.imread(image_path)

# If Flag is one , display image, else do not display
def save_image(image, shape,flag, dest_dir=None, name=None):
    img = Image.fromarray((image.reshape(shape)).astype('uint8'), 'RGB')
    if(flag == 1):
        img.show()
    img.save(dest_dir + '/' + name + ".png", "PNG")
    #print("Image location: ", dest_dir + '/' + name + ".png", "PNG")

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

    #print("Hexdecimal Key: ", hex_key)

    for _ in range(len(hex_key)):
        dec_key.append(ord(hex_key[_]))
    return dec_key


