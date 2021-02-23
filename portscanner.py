# -*- coding: utf-8 -*- 
"""
Created on Tuesday February 23 19:33 2021

@author: root_sphinx
"""
import socket
import os
import json
os.system("apt install figlet")
os.system("clear")
os.system("figlet Sphinx")

print("""
Bu Araçla Hızlı Bir Şekilde Port Tarayabilirsiniz
""")
print("""
[1] Port Denetleyicisi
[2] Port Tarayıcısı
[3] Exit
""")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Option = int(input("Option>> "))
if(Option == 3):
    print("Exit...")
    exit
elif(Option == 1):
    Target = input("[+] Target Website / Ip>> ")
    Port = int(input("[+] Port>> "))
    try:
        s.connect((Target, Port))
        print("[+] Port Açık>> "+str(Port))
    except:
        print("[-] Port Kapalı>> "+str(Port))
elif(Option == 2):
    Target = input("[+] Target WebSite / Ip>> ")
    Min = int(input("[+] Minimum Port>> "))
    Max = int(input("[+] Maximum Port>> "))
    for Port in range(Min, Max + 1):
        try:
            s.connect((Target , Port))
            print("[+] Port Açık>> "+str(Port))
            break
        except:
            print("[-] Port Kapalı>> "+str(Port))
else:
     print("[-] Error")
     exit    
