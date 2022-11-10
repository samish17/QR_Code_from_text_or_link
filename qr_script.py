#! /venv/bin/python3.10
import sys
from tkinter import *  # pip3 install python-tk
from tkinter import messagebox
from tkinter import ttk

import pyqrcode  # pip3 install pyqrcode
from pyqrcode import *
import png  # pip3 install pypng

import os
import sys
import shutil  # <----- This module helps to move/copy file from another directory to other
import psutil  # pip3 install psutil

# Creating the foreground color, background color and scale size names for combobox-tkinter
module_fg_color_combo_values = ['Black', 'Blue', 'Purple', 'Pink', 'Blue',
                                'Red', 'Green', 'Coral', 'Lemon Chiffon']
background_color_combo_values = ['White', 'Light Grey', 'Light Pink', 'Light Blue', 'Light Purple']

#   Getting the device info of the user in UPPER CASE using sys module # e.g.LINUX, WINDOWS
users_platform = sys.platform.upper()


def quit_program():
    quit()
    sys.exit(0)  # <-- exits the program with exit value '0' when the exit button is clicked.


class QR_Code_app(Tk):
    def __init__(self):
        """ Creating a GUI using tkinter."""
        self.window = Tk()
        self.window.title("Samish's QR Code Generator")
        self.window.maxsize(height=340, width=500)  # <------ Maximum size of the window
        self.window.minsize(height=340, width=450)  # <------ Minimum size of the window
        # Putting a background image to an application
        # back_photo = PhotoImage(file='image_name.png')
        # label = Label(self.window, image=back_photo)
        # label.image = back_photo
        # label.place(x=-50, y=-350)
        self.window.configure(bg='#C5CDE8')
        # self.window.iconbitmap('icon.ico')

        # Welcome Label
        Label(self.window, text='Welcome !', fg='black', bg='#C5CDE8', cursor='heart',
              font='Times 24 bold italic underline').place(x=120, y=5)

        # Enter the text label and its entry box
        Label(self.window, text='Enter your text/link here :-', bg='#C5CDE8').place(x=15, y=50)
        self.link_input = StringVar()
        Entry(self.window, width=40, bg='skyblue', textvariable=self.link_input).place(x=20, y=80)

        # Foreground/Module color label and its combo box
        Label(self.window, text='Choose the module color :-', bg="#C5CDE8").place(x=15, y=110)
        self.qr_module_color = StringVar()
        fg_combo = ttk.Combobox(self.window, width=10, cursor='exchange', values=module_fg_color_combo_values,
                                textvariable=self.qr_module_color)
        fg_combo.current(0)
        fg_combo.state = 'read and write'
        fg_combo.place(x=200, y=110)

        # Background color label and its combo box
        Label(self.window, text='Choose the background color :-', bg='#C5CDE8').place(x=15, y=140)
        self.qr_back_color = StringVar()
        bg_combo = ttk.Combobox(self.window, width=10, cursor='exchange', values=background_color_combo_values,
                                textvariable=self.qr_back_color)
        bg_combo.current(0)
        bg_combo.place(x=225, y=140)

        # File name label and its entry box
        Label(self.window, text='Rename a file:- ', bg='#C5CDE8').place(x=15, y=170)
        self.file_name = StringVar()
        Entry(self.window, width=20, bg='skyblue', textvariable=self.file_name).place(x=140, y=170)

        # a button for creating a qr code
        Button(self.window, text='Create Qr Code', bg='#B589A3', fg='black', bd=3, padx=5, pady=5,
               cursor='based_arrow_down', command=self.creating_a_qr_code).place(x=160, y=220)

        # Quit button
        Button(self.window, text='Exit', bg='red', fg='black', bd=3, padx=2, cursor='pirate',
               command=quit_program).place(x=400, y=282)

        # get the working dir button
        Button(self.window, text='Get', bg='#B7CED9', fg='black', bd=3, cursor='right_tee',
               command=self.get_file_dir).place(x=7, y=282)

        # directory label
        self.file_dir = Entry(self.window, width=38)
        self.file_dir.place(x=65, y=290)
        # placeholder for a file location box
        self.file_dir.insert(0, " Click 'Get' to get file location of your Qr Code")

        self.window.mainloop()  # <-------- Running this tkinter app in a loop (it is compulsory)

    # creating a qr code with a click of a button named 'create a qr code'
    def creating_a_qr_code(self):
        """ Tt is a command function creating a qr code with a click of a button named 'Create Qr Code' """
        # Conditional Statement for  Message box when any of the entry box is left empty and if the values of fb, bg
        # and scale are unmatched with the per-provided values .
        if len(self.link_input.get()) == 0 and len(self.file_name.get()) == 0:
            messagebox.showerror('Error!', 'Please input text and the file name.')
            return mainloop()

        elif len(self.link_input.get()) == 0:
            messagebox.showerror('Error!', 'Please input text.')
            return mainloop()

        elif len(self.file_name.get()) == 0:
            messagebox.showerror('Error!', 'Please enter the file name.')
            return mainloop()

        else:
            pass

        # Creating a New folder if not exists and not creating a folder if it already exists
        if 'WINDOW' in users_platform:
            if not os.path.exists("C:\\Samish's Qr Code Generator"):
                os.mkdir("C:\\Samish's Qr Code Generator")
            else:
                pass

        elif 'LINUX' in users_platform:
            home_directory_of_the_user = psutil.Process().username()
            if not os.path.exists("/home/{}/Samish's QR Code Generator".format(home_directory_of_the_user)):
                os.mkdir("/home/{}/Samish's QR Code Generator".format(home_directory_of_the_user))
            else:
                pass

        # making the foreground and background color variable global to use it in a global way
        global background_qr_color, foreground_qr_color
        # Foreground/Module color Hex value
        my_fg = self.qr_module_color.get()
        if my_fg == 'Black':  # black_color
            foreground_qr_color = '#000000'
        elif my_fg == 'Blue':  # Blue color
            foreground_qr_color = '#0000FF'
        elif my_fg == 'Purple':  # Purple
            foreground_qr_color = '#800080'
        elif my_fg == 'Pink':  # Pink_color
            foreground_qr_color = '#ffc0cb'
        elif my_fg == 'Navy Blue':  # navy blue color
            foreground_qr_color = '#000080'
        elif my_fg == 'Red':  # red color
            foreground_qr_color = '#FF0000'
        elif my_fg == 'Green':  # Green color
            foreground_qr_color = '#008000 '
        elif my_fg == 'Coral':  # coral
            foreground_qr_color = '#FF7F50'
        elif my_fg == 'Lemon Chiffon':  # lemon chiffon
            foreground_qr_color = '#FFFACD'
        else:
            pass

        #  Background color Hex value
        my_bg = self.qr_back_color.get()
        if my_bg == 'White':  # white_color
            background_qr_color = '#FFFFFF'
        elif my_bg == 'Light Grey':  # Light Grey
            background_qr_color = '#b8a399'
        elif my_bg == 'Light Pink':  # Light Pink
            background_qr_color = '#fbb291'
        elif my_bg == 'Light Blue':  # Light Blue
            background_qr_color = '#909be9'
        elif my_bg == 'Light Purple':  # Light purple
            background_qr_color = '#ac50e1'
        else:
            pass

        # Creating a qr code using the text, fg & bg color values
        my_qr = pyqrcode.create(self.link_input.get())
        valid_file_name = (self.file_name.get() + '.png')
        my_qr.png(valid_file_name, scale=5, module_color=foreground_qr_color,
                  background=background_qr_color)

        # changing the location of the file using shutil module, Note:- this only works when the get button is clicked.
        if 'WINDOW' in users_platform:
            png_file_location = os.getcwd()
            png_file_full_location = png_file_location + '\\' + self.file_name.get() + '.png'
            shutil.move(png_file_full_location, "C:\\Samish's Qr Code Generator")  # <------- using shutil module

        elif 'LINUX' in users_platform:
            png_file_location = os.getcwd()
            png_file_full_location = png_file_location + '/' + self.file_name.get() + '.png'
            #   Getting the home directory of the user
            home_directory_of_the_user = psutil.Process().username()  # <--- using psutil module

            #  Using shutil module to move the created qr code into the Samish's QR Code Generator folder.
            shutil.move(png_file_full_location,
                        "/home/{}/Samish's QR Code Generator".format(home_directory_of_the_user))

    def get_file_dir(self):
        """ This function displays the location of the qr image in the device. """
        # Conditional Statement for  Message box
        # showing error if the user clicks get button before creating a qr code
        if len(self.link_input.get()) == 0 or len(self.file_name.get()) == 0:
            messagebox.showerror('Error!', 'Please create the qr code first.')
            return mainloop()
        else:
            pass

        self.file_dir.delete(0, 'end')  # <---- clearing the entry widget after the button is pressed

        # Providing the location of the created qr code after clearing the previous text in the entry box
        if 'WINDOW' in users_platform:
            png_file_location_new = "C:\\Samish's Qr Code Generator"
            self.file_dir.insert(0, png_file_location_new)

        elif 'LINUX' in users_platform:
            # Getting the home directory of the user
            home_directory_of_the_user = psutil.Process().username()
            png_file_location_new = "/home/{}/Samish's QR Code Generator".format(home_directory_of_the_user)
            self.file_dir.insert(0, png_file_location_new)


QR_Code_app()  # <------ Calling the Class function
