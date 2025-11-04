import os

import platform

import socket

import shutil

def main():
    versjon, maskin = operativsystem()   
    diskPlass = diskspace()
    bruker = user()
    ipAddress = ip()


    if not os.path.isdir("c:\\maskin\\"):
        os.mkdir("c:\\maskin\\")

    fil = open(f"c:\\maskin\\{bruker.strip("\n")}.txt","w")
    fil.write(diskPlass+maskin+versjon+bruker+ipAddress)
    fil.close()



def operativsystem():
    
    uname_info = platform.uname()

    print("Machine Hardware Identifier:", uname_info.machine)

    print("OS Version:", uname_info.version)
    return (f"Machine Hardware Identifier: {uname_info.machine}\n", f"OS Version: {uname_info.version}")


def diskspace():

    path = '/'

    usage = shutil.disk_usage(path)

    def bytes_to_gigabytes(bytes_value):
        return bytes_value / (1024**3)

    print("Disk Usage Information:")
    print(f"Total Space: {bytes_to_gigabytes(usage.total):.2f} GB")
    print(f"Used Space: {bytes_to_gigabytes(usage.used):.2f} GB")
    print(f"Free Space: {bytes_to_gigabytes(usage.free):.2f} GB")

    return f"Free Space: {bytes_to_gigabytes(usage.free):.2f} GB\n"

def user():
    uname_info = platform.uname() 
    print("User of machine", uname_info.node)
    return uname_info.node+"\n"


def ip():


    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f"Local IP Address: {local_ip}")
    return local_ip+"\n"


main()

print("hei joost")