# usr/bin/python3

import os
import tkinter
import urllib.request
import subprocess
import platform


def download_wallpaper():
    base_url = "https://picsum.photos/"

    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    random_image_url = f"{base_url}{width}/{height}/?random"

    home_directory = os.getenv("HOME")

    response = urllib.request.urlopen(random_image_url)
    if response.getcode() == 200:
        urllib.request.urlretrieve(
            random_image_url, f"{home_directory}/Pictures/Wallpapers/wallpaper.jpg")
        return f"{home_directory}/Pictures/Wallpapers/wallpaper.jpg"


def set_wallpaper(file_location):
    desktop_environment = detection()

    if desktop_environment == "gnome":
        command = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{file_location}"]
        subprocess.Popen(command).communicate()


def detection():
    if platform.system() == 'Linux':
        desktops = {
            'gnome': '/usr/bin/gnome-session',
            'mate': '/usr/bin/mate-session',
            'lxde': '/usr/bin/lxsession',
            'jwm': '/usr/bin/icewm-session'
        }

        for key, value in desktops.items():
            if os.path.exists(value):
                return key
    else:
        return platform.system()


if __name__ == "__main__":
    image_uri = download_wallpaper()
    set_wallpaper(image_uri)
