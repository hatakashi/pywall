import ctypes
import os
import config, download

cwd = os.getcwd()

def get_tags():
    tagsurl = ""
    tags = []
    while True:
        user_input = input("Want to search for specific tags? (Leave blank for random image or when finished adding tags.)\n")
        if user_input == "":
            break
        else:
            tags.append(user_input)
    for x in tags:
        tagsurl = tagsurl + x + ","
    tagsurl = tagsurl.replace(" ", "+")
    return tagsurl
    
# download and set wallpaper
def get_and_set():
    download.download_wp(config.width, config.height, get_tags())
    set_wp()

# set wallpaper to latest downloaded wallpaper
def set_wp():
    ctypes.windll.user32.SystemParametersInfoW(0x14, 0, download.latest_wp, 0x3)