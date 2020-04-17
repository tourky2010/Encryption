#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

# need PIL and stepic packages
import stepic
import stegano
from PIL import Image



#i = Image.open("any_rules.jpg")
#i.show()
#  could open a file here
f = open("route details.txt", "r")
text = f.read()
#text=str(input('please enter you stegano text \n'))
steg = stegano.lsb.hide("map.png", text)
# steg = stepic.encode(i, text)

steg.save("steg.png")

i2 = Image.open("steg.png")
i2.show()

clear_message = stegano.lsb.lsb.reveal("steg.png")
print(clear_message)