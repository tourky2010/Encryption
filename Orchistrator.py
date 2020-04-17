#!/usr/bin/python
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import Encrypt

class Orchistrator ():
    def __init__(self):
        self.encrypted_msg = b''


    def encrypt(self):
        option = 0
        while option != "1" and option != "2":
            option = input('Please choose the data type to encrypt 1 or 2:\n1- Message\n2- File\n')

        if option == "1":
            plain_msg = str(input("Please Enter the message, you need to encrypt: \n"))
            self.aes_mode_fuc(plain_msg)

        else:
            filename = self.choose_file()
            enc_msg = Encrypt.encrypt_file(filename)
            print(enc_msg)

    def aes_mode_fuc(self, msg):
        option2 = " "
        while option2 != "1" and option2 != "2":
            option2 = input('Please choose the AES Mode type 1 or 2:\n1- CBC\n2- ECB\n')

        if option2 == "1":
            self.encrypted_msg = Encrypt.tourky_encrypt_CBC(msg)
            print(self.encrypted_msg)
        else:
            self.encrypted_msg = Encrypt.tourky_encrypt_ECB(msg)
            print(self.encrypted_msg)

    def decrypt(self):
        option = 0
        while option != "1" and option != "2":
            option = input('Please choose the data type to decrypt 1 or 2:\n1- Message\n2- File\n')

        if option == "1":

            option1 = 0
            while option1 != "1" and option1 != "2":
                option1 = input('Please choose the AES Mode type 1 or 2:\n1- CBC\n2- ECB\n')
            if option1 == "1":
                try:
                    print(self.encrypted_msg)
                    print(Encrypt.tourky_decrypt_CBC(self.encrypted_msg))
                except(UnicodeDecodeError):
                    print('Key is Invalid')
            else:
                try:
                    print(self.encrypted_msg)
                    print(Encrypt.tourky_decrypt_ECB(self.encrypted_msg))
                except(UnicodeDecodeError):
                    print('Key is Invalid')

        else:
            filename = self.choose_file()
            try:
                Encrypt.decrypt_file(filename)
            except:
                print('Decryption failed, Key may be Invalid')


    def choose_file(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        return askopenfilename()  # show an "Open" dialog box and return the path to the selected file

def main():
    orc = Orchistrator()
    option3 = " "
    while option3 != "1" and option3 != "2":
        option3 = input('What do you need to do? type 1 or 2:\n1- Encryption\n2- Decryption\n')
    if option3 == "1":
        print("Encryption Module..\n")
        orc.encrypt()
    else:
        print("Decryption Module..\n")
        orc.decrypt()

if __name__ == '__main__':
    main()
