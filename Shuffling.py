import Util
import matplotlib
import numpy


shuffled_image = "shuffled_image"
input_img_name = "input_image"
output_dir = "/Users/sabique/Desktop/output/shuffled"

big_image = list()

def shuffle(image):
    #getting image details
    img_width, img_height = image.shape[:2]
    image1 = image
    print img_width
    print img_height

    for i in range(img_width):
        for j in range(img_height):
            print""



    Util.show_image(image1, shape=image.shape, dest_dir=output_dir, name=shuffled_image)
    Util.show_image(image, shape=image.shape, dest_dir=output_dir, name=shuffled_image)


#input image path
input_image_path = "input_image/"
input_image_path += raw_input("Enter the image name including extension : ")
print input_image_path

image = Util.get_image(image_path=input_image_path)
Util.show_image(image, shape=image.shape, dest_dir=output_dir, name=input_img_name)

shuffle(image)

'''
Algorithm for shuffling

1)Divide the coloumns in to block of 2
    take first 2 blocks swap the first and second with first and second of next block , then take next 2 blocks and swap them and so on
2)increase block size in to 4
    swap first 2 blocks and swap them , then take 
'''