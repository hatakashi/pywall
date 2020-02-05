import platform
import config, download, wallpaper
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q','--quick', help='Set a random wallpaper instantly!', action='store_true')
    # parser.add_argument('-c', '--collections', help='Download from a collection', action='store_true')
    args = parser.parse_args()
    
    if args.quick == True:
        # Download random wallpaper if quick tag chosen, TODO: add collections/double check arg
        try:
            config.parse_config()
            config.set_paths()
            download.download_wp(config.width, config.height, "")
            wallpaper.set_wp()
        except:
            print("Something went wrong - are you connected to the internet?")
            sys.exit(1)
    else:
        print("""
            
            ___       __    __      _ _ 
        / _ \_   _/ / /\ \ \__ _| | |
        / /_)/ | | \ \/  \/ / _` | | |
        / ___/| |_| |\  /\  / (_| | | |
        \/     \__, | \/  \/ \__,_|_|_|
                |___/                   

            An excellent application!
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
        collection_choice = input("Would you like to search (C)ollections or (T)ags?")
        if collection_choice.lower() == "c":
            collections = True
        else:
            collections = False
        wallpaper.get_and_set(collections)
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