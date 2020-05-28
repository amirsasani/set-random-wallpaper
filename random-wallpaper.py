# usr/bin/python3

# wget -O /home/amir/Pictures/Wallpapers/wallpaper.jpg https://unsplash.it/2560/1440/?random
# gsettings set org.gnome.desktop.background picture-uri file:///home/amir/Pictures/Wallpapers/wallpaper.jpg

import shutil
import requests
import os
import tkinter
import urllib.request
import subprocess
import sys
import platform


base_url = "https://picsum.photos/"

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

random_image_url = f"{base_url}{width}/{height}/?random"

home_directory = os.getenv("HOME")

response = urllib.request.urlopen(random_image_url)
print(response.getcode())
if response.getcode() == 200:
    image = urllib.request.urlretrieve(
        random_image_url, f"{home_directory}/local-filename.jpg")


def set_wallpaper(file_loc):
    pass


def detection():

    if platform.system == 'Linux':
        desktops = {'gnome':'/usr/bin/gnome-session', 'mate':'/usr/bin/mate-session', 'lxde':'/usr/bin/lxsession', 'jwm':'/usr/bin/icewm-session'}
        current_desktop = None
        for key, value in desktops.items():
            if os.path.exists(value):
                current_desktop = key

        if(current_desktop == 'gnome'):
            pass
    else:
        print("Not Linux. Shame on you.")



if __name__ == "__main__":
    print(platform.system())
