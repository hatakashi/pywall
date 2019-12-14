import wget
import time

import config
latest_wp = ''

# download wallpaper from source.unsplash

def download_wp(width, height, tags):
    global latest_wp
    print("\n##############################################################################")
    if tags:
        print('https://source.unsplash.com/'+ str(width) +'x' + str(height) + '/?' + tags)
        latest_wp = wget.download('https://source.unsplash.com/'+ str(width) +'x' + str(height) + '/?' + tags, out=(config.wallpath + "\\image" + str(time.time()) +".jpg"))
    else:
        latest_wp = wget.download('https://source.unsplash.com/'+ str(width) +'x' + str(height), out=(config.wallpath + "\\image" + str(time.time()) +".jpg"))
    
    print("\n##############################################################################")