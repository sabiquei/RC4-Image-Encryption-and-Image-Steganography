import RC4
import shuffle
import steganography

# Variables
input_path = "/Users/sabique/Desktop/project/input_image/"
output_path = "/Users/sabique/Desktop/project/output_image"
encrypted_image_name = "encrypted_image.png"
stego_image_name = "stego_image.png"
decrypted_image_name="decrypted_image.png"
decrypted_image_name_without_extension ="decrypted_image"

def encryption_procedure(sec_image_name,cov_image_name,key):
    # Encryption Procedure
    sec_image_name = input_path+sec_image_name
    cov_image_name = input_path+cov_image_name
    RC4.rc4_encryption(sec_image_name,key,output_path,encrypted_image_name)
    shuffle.shuffle_unshuffle(output_path+"/"+encrypted_image_name)
    steganography.encode(output_path+"/"+encrypted_image_name,output_path,cov_image_name)

def decryption_procedure(stego_image_name,key):
    # Decryption Procedure
    stego_image_name = output_path+"/"+stego_image_name
    steganography.decode(stego_image_name,output_path)
    shuffle.shuffle_unshuffle(output_path+"/"+encrypted_image_name)
    RC4.rc4_decryption(output_path+"/"+encrypted_image_name, key, output_path, decrypted_image_name_without_extension)

def run_without_ui():
    print "------------------------------\n" \
          "     IMAGE SECURITY TOOL\n" \
          "------------------------------"
    option = 0

    while (option != 3):
        print "1.Encryption Procedure\n" \
              "2.Decryption Procedure\n" \
              "3.Exit"

        option = input("Enter your choice : ")

        if (option == 1):
            secret_image_name = raw_input("Enter the secret Image name : ")
            cover_image_name = raw_input("Enter the cover image name : ")
            key = raw_input("Enter the key : ")
            encryption_procedure(secret_image_name,cover_image_name,key)

        elif (option == 2):
            stego_image_name = raw_input("Enter the Stego Image name : ")
            key = raw_input("Enter the key : ")
            decryption_procedure(stego_image_name,key)

        elif (option == 3):
            print"Exiting..."

        else:
            print"Invalid choice\n" \
                 "Please give another input"

#run_without_ui()