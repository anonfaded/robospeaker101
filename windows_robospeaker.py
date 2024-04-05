import os
import platform
from colorama import Fore, Style, init

# pip install colorama
def robospeaker():
    init()  # Initialize colorama
    if platform.system() == "Windows":
        from win32com.client import Dispatch
        speaker = Dispatch("SAPI.SpVoice")
    else:
        def speaker(text):
            os.system(f"espeak '{text}'")

    logo = f"""{Fore.RED}
    _____  _____  ____   _____    __ _____ _____  ___  __ __ _____ _____    101
    ||_// ((   )) ||=)  ((   ))  ((  ||_// ||==  ||=|| ||<<  ||==  ||_//       
    || \\\  \\\_//  ||_))  \\\_//  \_)) ||    ||___ || || || \\\ ||___ || \\\            
    \033[1;31m\n\t\t\tDeveloped by Faded\033[0m
    \033[1;35m\n\t✨ {Style.UNDERLINE}https://github.com/anonfaded/robospeaker101 ✨\033[0m
                                                                 \033[0m"""
    print(logo)
    while True:
        user_input = input(f"{Fore.GREEN}\nEnter What you want me to speak: {Fore.LIGHTBLACK_EX}(or type q to exit){Fore.MAGENTA}\n>>> {Style.RESET_ALL}")
        if user_input.strip() == "q":
            print(f"{Fore.RED}\n\t<<< Bye >>>{Style.RESET_ALL}\n")
            speaker('See you soon')
            break
        else:
            speaker(user_input.strip())

if __name__ == '__main__':
    robospeaker()
