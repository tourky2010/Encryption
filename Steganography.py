#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

# need PIL and stepic packages
import stepic
import stegano
from PIL import Image
from tkinter.filedialog import askopenfilename
from tkinter import Tk
 """"""
def choose_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    return askopenfilename(title="Please Select a Text File", initialdir= "C:\\Users\\ZGKW5367\\Desktop\\")  # show an "Open" dialog box and return the path to the selected file

#i = Image.open("any_rules.jpg")
#i.show()
#  could open a file here
f = open(choose_file(), "r")
text = f.read()
#text=str(input('please enter you stegano text \n'))

steg = stegano.lsb.hide("C:\\Users\\ZGKW5367\\Desktop\\map.png", text)
# steg = stepic.encode(i, text)

steg.save("steg.png")

i2 = Image.open("steg.png")
i2.show()

clear_message = stegano.lsb.lsb.reveal("steg.png")
print(clear_message)


def choose_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    return askopenfilename()  # show an "Open" dialog box and return the path to the selected file