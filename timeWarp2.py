#
#Created Date: Saturday, September 24th 2022, 8:52:25 pm
#Author: Prasanna R
#
import ctypes,sys
from asyncio import *
import time
import os

localhost = "127.0.0.1"
blocksite = ["www.facebook.com","m.facebook.com","www.youtube.com","m.youtube.com","m.google.com",
            "www.twitter.com",
            "twitter.com",
            "www.instagram.com",
            "www.snapchat.com",
            "www.swiggy.com",
            "www.zomato.com","news.google.com","www.amazon.in","www.flipkart.com"            
            ]
filepath = "C:\\Windows\\System32\\drivers\\etc"

#function for blocking websites
def block():
    with open(filepath+"\\hosts","a+") as file:
        file.seek(0)
        content = file.read()
        for website in blocksite:
                if website in content:
                    print("already blocked")
                    time.sleep(3)
                    break
                else:
                    # mapping hostnames to your localhost IP address
                    file.seek(0)
                    data = file.read(10)
                    if len(data) > 0:
                        file.write("\n")
                        file.write(localhost + " " + website)
    file.close()
    os.system('ipfonfig /flusdns')
    
#function for unblocking websites
def unblock():
    with open(filepath+"\\hosts",'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in blocksite):
                file.write(line)
                file.truncate()
                
            else:
                print("Allowed access!")
                time.sleep(3)
                break


#function for checking if the shell is in admin mode
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin() == True:
    passck ="$v53BCvo7vT7"
    passcks = input("enter your password:")
    if passck == passcks:
        unblock()
    else:
        print("password incorrect websites blocked")
        time.sleep(3)
        block()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    #block()