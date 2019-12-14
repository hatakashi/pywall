import platform
import config, download, wallpaper
import sys


def main():
    print("""
        
        ___       __    __      _ _ 
       / _ \_   _/ / /\ \ \__ _| | |
      / /_)/ | | \ \/  \/ / _` | | |
     / ___/| |_| |\  /\  / (_| | | |
     \/     \__, | \/  \/ \__,_|_|_|
            |___/                   

        """)

    config.initial_conf()
    config.detect_system_config()
    menu()

# display the main menu
def menu():
    menu_input = input("""
########################################################                       
Choose an option:\n
1: Get and Set a Wallpaper
2: Detect Config

Q/Quit/Cancel/Exit to exit the program
########################################################\n""")
    
    if menu_input == "1":
        wallpaper.get_and_set()
        menu()
    elif menu_input == "2":
        config.detect_system_config()
        menu()
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