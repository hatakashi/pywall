import argparse
import configparser
import os
import platform
import sys
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
    

# detect config matches system 

def detect_config():
    print("Not working yet!")
    sys.exit(1)
        
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