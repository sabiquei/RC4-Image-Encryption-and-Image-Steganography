from Tkinter import *
#from tkFileDialog import *
import tkMessageBox

def info_button_action():
    tkMessageBox.showinfo("Information", "Developed by Amith,Adhirath,Akhil,Sabique\n"
                                         "\n\n"
                                         "How to use\n"
                                         "----------\n"
                                         "1.All Input Images are to be stored in the folder desktop/project/input_image\n"
                                         "2.All Output Images will be stored to the folder desktop/project/output_image\n"
                                         "3.Always enter the image names including extension\n"
                                         "4.Do not leave/close the window in the middle of Encryption or Decryption procedure\n"
                                         "\n"
                                         "\n"
                                         "Version - 0.1\n")

def main_page_ui():

    def encryption_button_action():
        window.destroy()
        encryption_ui()

    def decryption_button_action():
        window.destroy()
        decryption_ui()

    # Create main window
    window = Tk()
    window.title("IMAGE SECURITY TOOL")
    window.geometry('350x350')

    # Creating Frames inside the root window
    header = Frame(window,width = 350,height = 40,bg='khaki')
    body = Frame(window,width = 350,height = 270,bg='white')
    footer = Frame(window,width=350,height=40,bg='khaki')

    # Layout for all Frames
    header.pack(side=TOP,fill = X)
    body.pack(fill = X)
    footer.pack(side=BOTTOM,fill = X)

    # Contents in top frame
    name = Label(header,text='IMAGE SECURITY TOOL',fg='black',bg='khaki',font='none 20 bold')

    # Layout for top frame
    name.pack()

    # Contents in body frame
    encryption_button = Button(body,text='ENCRYPTION PROCEDURE',font='none 15 bold',command =encryption_button_action)
    decryption_button = Button(body,text='DECRYPTION PROCEDURE',font='none 15 bold',command =decryption_button_action)

    # Layout for body frame
    encryption_button.pack(pady = 45)
    decryption_button.pack(pady = 15)

    # Contents in footer frame
    info_button = Button(footer,highlightbackground='khaki',text='info',font='none 15 bold', command=info_button_action)

    # Layout for footer frame
    info_button.pack(side= RIGHT)

    # Running window
    window.mainloop()

def encryption_ui():
    window = Tk()
    window.title("IMAGE SECURITY TOOL")
    window.geometry('350x350')

    def back_button_action():
        window.destroy()
        main_page_ui()

    # Creating Frames inside the root window
    header = Frame(window, width=350, height=40, bg='khaki')
    body = Frame(window, width=350, height=270, bg='white')
    footer = Frame(window, width=350, height=40, bg='khaki')

    # Layout for all Frames
    header.pack(side=TOP, fill=X)
    body.pack(fill=X)
    footer.pack(side=BOTTOM, fill=X)

    # Contents in top frame
    back_button = Button(header, text='Go Back',highlightbackground='khaki',command=back_button_action)
    name = Label(header, text='IMAGE SECURITY TOOL', fg='black', bg='khaki', font='none 20 bold')

    # Layout for top frame
    back_button.pack(side = LEFT)
    name.pack()

    # Contents in body frame
    message_label = Label(body, text='')

    secret_img_label = Label(body, text='Input the secret Image name : ')
    secret_img_name = Entry(body,width=15)

    cover_img_label = Label(body, text='Input the cover Image name : ')
    cover_img_name = Entry(body, width=15)

    key_label = Label(body, text='Enter the Key for Encryption : ')
    key_name = Entry(body, width=15)

    encryption_button = Button(body, text='ENCRYPT', font='none 10 bold')

    # Layout for body frame
    message_label.grid(row=0, column=0,columnspan=2,sticky="ew")

    secret_img_label.grid(row=1, column=0, sticky=W)
    secret_img_name.grid(row=1, column =1, sticky=W)

    cover_img_label.grid(row=2, column=0, sticky = W)
    cover_img_name.grid(row=2, column =1, sticky = W)

    key_label.grid(row=3, column=0, sticky=W)
    key_name.grid(row=3, column=1, sticky=W)

    encryption_button.grid(row=3,column =0,columnspan=2,sticky="ew")


    # Contents in footer frame
    info_button = Button(footer, highlightbackground='khaki', text='info', font='none 15 bold',command=info_button_action)

    # Layout for footer frame
    info_button.pack(side=RIGHT)

    # Running window
    window.mainloop()

def decryption_ui():
    window = Tk()
    window.title("IMAGE SECURITY TOOL")
    window.geometry('350x350')

    def back_button_action():
        window.destroy()
        main_page_ui()

    # Creating Frames inside the root window
    header = Frame(window, width=350, height=40, bg='khaki')
    body = Frame(window, width=350, height=270, bg='white')
    footer = Frame(window, width=350, height=40, bg='khaki')

    # Layout for all Frames
    header.pack(side=TOP, fill=X)
    body.pack(fill=X)
    footer.pack(side=BOTTOM, fill=X)

    # Contents in top frame
    back_button = Button(header, text='Go Back', highlightbackground='khaki', command=back_button_action)
    name = Label(header, text='IMAGE SECURITY TOOL', fg='black', bg='khaki', font='none 20 bold')

    # Layout for top frame
    back_button.pack(side=LEFT)
    name.pack()

    # Contents in body frame
    message_label = Label(body, text='')

    stego_img_label = Label(body, text='Input the Stego Image name : ')
    stego_img_name = Entry(body, width=15)

    key_label = Label(body, text='Enter the Key for Encryption : ')
    key_name = Entry(body, width=15)

    decryption_button = Button(body, text='DECRYPT', font='none 10 bold')

    # Layout for body frame
    message_label.grid(row=0, column=0, columnspan=2, sticky="ew")

    stego_img_label.grid(row=1, column=0, sticky=W)
    stego_img_name.grid(row=1, column=1, sticky=W)

    key_label.grid(row=2, column=0, sticky=W)
    key_name.grid(row=2, column=1, sticky=W)

    decryption_button.grid(row=3, column=0, columnspan=2, sticky="ew")

    # Contents in footer frame
    info_button = Button(footer, highlightbackground='khaki', text='info', font='none 15 bold', command=info_button_action)

    # Layout for footer frame
    info_button.pack(side=RIGHT)

    # Running window
    window.mainloop()


main_page_ui()
#encryption_ui()
#decryption_ui()