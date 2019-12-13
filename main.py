import platform
import config, download, wallpaper
import ctypes
import sys

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

def main():
    print("""
        
        ___       __    __      _ _ 
       / _ \_   _/ / /\ \ \__ _| | |
      / /_)/ | | \ \/  \/ / _` | | |
     / ___/| |_| |\  /\  / (_| | | |
     \/     \__, | \/  \/ \__,_|_|_|
            |___/                   

        """)

    print("Detected OS: " + opsys + " " + oprel + "")
    print("Resolution: " + str(monwidth) + "x" + str(monheight) + "")
    print("\n")
    config.initial_conf()
    menu()

# display the main menu
def menu():
    menu_input = input("""Choose an option:\n
1: Get and Set a Wallpaper
2: Detect Config\n""")
    
    if menu_input == "1":
        wallpaper.get_and_set()
        menu()
    elif menu_input == "2":
        config.detect_config()
    elif menu_input.lower() == "cancel" or menu_input.lower() == "quit" or menu_input.lower() == "q" or menu_input.lower() == "exit":
        print("Bye bye!")
        sys.exit
    else:
        print("That wasn't one of the options!")
        print("Try again!")
        menu()
try:
    main()
except KeyboardInterrupt:
        sys.exit(1)