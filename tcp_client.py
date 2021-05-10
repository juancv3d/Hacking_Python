#! /usr/bin/python3

import socket

ports = [21,22,23,3306]
ip=input("IP Target:")

for port in ports:
    s=socket.socket()
    print("this is the banner for this port")
    print(port)
    
    try:
        s.connect((ip,port))
        answer = s.recv(1024)
        print(answer)
        s.close
    except:
        print("No answer...")

