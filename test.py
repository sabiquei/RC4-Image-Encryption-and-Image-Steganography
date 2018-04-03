import cv2
import sys
import numpy
print cv2.__version__


#rc4 CODE HERE

def KSA(key):
    keylength = len(key)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)

def convert_key(s):
    return [ord(c) for c in s]


#END RC4 CODE

#read an image
img = cv2.imread("clouds.jpg",0)

#get height ,width and number of channels in the image
height , width  = img.shape

print "Height of the image : ",height
print "Width of the image : ",width
print ""

plaintext = list()
#thefile = open('test.txt', 'w')

for x in range(0,height):
    #print("Row: %d") %x # print row number
    #thefile.write(" \n Row: %d \n" % x) #writing to file to check
    for y in range(0,width):
        #print "coloum %d : " %y ,img[x,y]
        #thefile.write("%d " % img[x,y]) #writing to file to check
        plaintext.append(img[x,y])

#read key
key = raw_input("Enter the key : ")

#convert key in to required format
key = convert_key(key)

#generate key stream
keystream = RC4(key)

relength = len(plaintext)

plaintextstr = str(plaintext)

#print plaintextstr

# append dimensions of image for reconstruction after decryption
#plaintextstr += "h" + str(height) + "h" + "w" + str(width) + "w"

ciphertextstr =""

#XOR and generate cipher
for c in plaintextstr:
    # print("%02X" % (ord(c) ^ keystream.next()))
    #print("%d" % (ord(c) ^ keystream.next()))
    ciphertextstr = ciphertextstr + " %d" % (ord(c) ^ keystream.next())
print

print ciphertextstr

#print type(ciphertextstr)



# -----------------
    # construct encrypted image
# -----------------
#test

enc_img = img



h = 0
w = 0

thefile = open('test.txt', 'w')
for s in ciphertextstr.split():
    if s.isdigit():
        thefile.write("%s " %s)
        #if(h < height):
         #   if(w < width):
          #     w = w+1
           # elif(w == width):
            #    w=0
             #   h = h+1
        #enc_img[h,w] = int(s)
        #thefile.write("%d " % enc_img[x, y])  # writing to file to check
        #else:
         #   print "out of bounds"

'''
thefile = open('test.txt', 'w')
for x in range(0,height):
    thefile.write(" \n Row: %d \n" % x) #writing to file to check
    for y in range(0,width):
        thefile.write("%d " % enc_img[x,y]) #writing to file to check

'''

#cv2.imshow("encrypted Image",enc_img)

#cv2.imshow("new",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
