import argparse
import configparser
import os
import platform
import sys
import ctypes
from pkg_resources import resource_string

width=0
height=0
wallpath = ''
confpath = ''
opsys = platform.system()


# initial config 

def initial_conf():
    try:
        global wallpath
        global confpath
        
        if opsys == "Windows":
            wallpath = os.path.expanduser("~\documents\pywall\images")
            confpath = os.path.expanduser("~\documents\pywall\conf")
        else:
            print("Incompitable OS - Exiting!")
            sys.exit(1)
        
        print("Checking Wallpapers Path Exists:")
        check_path(wallpath)
        
        print("Checking Configuation Path Exists:")
        check_path(confpath)
        
        print("Checking Configuration:")
        check_conf(confpath + '\config.conf')
        
        parse_config()
    except KeyboardInterrupt:
        sys.exit(1)
    

# detect system config

def detect_system_config():
    #################################################################

    #DPI AWARENESS SOLUTION FROM: https://stackoverflow.com/a/44422362

    # Query DPI Awareness (Windows 10 and 8)
    awareness = ctypes.c_int()
    errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))

    # Set DPI Awareness  (Windows 10 and 8)
    errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(1)

    # Set DPI Awareness  (Windows 7 and Vista)
    success = ctypes.windll.user32.SetProcessDPIAware()

    #################################################################

    # Monitor Resolution
    monwidth = ctypes.windll.user32.GetSystemMetrics(0)
    monheight = ctypes.windll.user32.GetSystemMetrics(1)

    # Operating System Information
    opsys = platform.system()
    oprel = platform.release()
    
    print("Detected OS: " + opsys + " " + oprel + "")
    print("Resolution: " + str(monwidth) + "x" + str(monheight) + "")
    print("\n")
    detect_config_changes(monwidth, monheight)
    
# detect any differences between system and config file
def detect_config_changes(monwidth, monheight):
    if monwidth != width or monheight != height:
        print("Config differences found:")
        print("Your resolution is: " + str(monwidth) + "x" + str(monheight) + " - Your configured resolution is: " + str(width) + "x" + str(height))
        while True:
            update_config = input("Would you like to update your configuration file? (Y/N)")        
            if update_config.lower() == "y":
                print("Updating Configuration File")
                update_config_file(monwidth, monheight)
                break
            elif update_config.lower() == "n":
                print("Ignoring Configuration Differences")
                break
            else:
                print("That is not a valid choice")
    else:
        print("No differences found in config")
            
# check path exists, otherwise create it

def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(path + " does not exist! - Creating\n")
    else:
        print("That path appears to exist - Continuing!\n")


# check config file exists, otherwise install default

def check_conf(filepath):
    if not os.path.isfile(filepath):
        print("Config file not present - setting up default")
        cfile = resource_string(__name__, 'conf/windows.conf')
        with open(filepath, 'wb') as f:
            f.write(cfile)
    else:
        print("Config file present - Continuing!")

# parse config from config file

def parse_config():
    global width
    global height
    
    config = configparser.ConfigParser()
    config.read(confpath + '\config.conf')
    
    width = config.getint('Options', 'width', fallback=1920)
    height = config.getint('Options', 'height', fallback=1080)
    
# updae config in config file
def update_config_file(monwidth, monheight):
    config = configparser.ConfigParser()
    config.read(confpath + '\config.conf')
    
    print("" + str(monwidth) + " x " + str(monheight) + "")
    config.set('Options', 'width', str(monwidth))
    config.set('Options', 'height', str(monheight))
    with open(confpath + '\config.conf', 'w') as configfile:
        config.write(configfile)
        
    parse_config()