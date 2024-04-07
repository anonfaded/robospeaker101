from gtts import gTTS
from colorama import Fore, Style, init, Back
import os

# Initialize colorama
init()

clear_line = "\033[F\033[K"  # Escape codes for clearing one line

def select_voice():
    print(f"\n{Fore.GREEN}\n\n\nSelect a voice:")
    print(f"{Fore.MAGENTA}[1]{Style.RESET_ALL} - Male")
    print(f"{Fore.MAGENTA}[2]{Style.RESET_ALL} - Female")
    choice = input(f"{Fore.GREEN}\nEnter your choice (1 or 2):{Style.RESET_ALL} ")
    if choice == '1':
        print(clear_line * 1000)
        header()
        print("\n"*3) # line breaks for alignment
        return 'en'  # Male voice
    elif choice == '2':
        print(clear_line * 1000)
        header()
        print("\n"*3)  # line breaks for alignment
        return 'ar'  # Female voice
    else:
        print(clear_line * 1000)
        header()
        print(f"{Fore.YELLOW}\n\nInvalid choice. Using the default male voice.\n{Style.RESET_ALL}")
        return 'en'  # Default to male voice

def select_speed():
    print(f"{Fore.GREEN}Select speech speed:")
    print(f"{Fore.MAGENTA}[1]{Style.RESET_ALL} - Slow")
    print(f"{Fore.MAGENTA}[2]{Style.RESET_ALL} - Medium (Default)")
    print(f"{Fore.MAGENTA}[3]{Style.RESET_ALL} - Fast")
    speed_choice = input(f"{Fore.GREEN}\nEnter your choice (1, 2, or 3):{Style.RESET_ALL} ")
    if speed_choice == "1":
        print(clear_line * 1000) #terminal clear
        header()
        return 0.5  # Slow
    elif speed_choice == "2":
        print(clear_line * 1000) #terminal clear
        header()
        return 1.0 # Medium
    elif speed_choice == "3":
        print(clear_line * 1000) #terminal clear
        header()
        return 1.5  # Fast
    else:
        print(clear_line * 1000) #terminal clear
        header()
        print(f"{Fore.YELLOW}\n\nInvalid choice. Default speed (Medium) will be selected.{Style.RESET_ALL}")
        return 1.0  # Medium (Default)

def save_audio(output_file, text):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

def header():
    # Print the logo
    logo = r"""
_____  _____  ____   _____    __ _____ _____  ___  __ __ _____ _____    101
||_// ((   )) ||=)  ((   ))  ((  ||_// ||==  ||=|| ||<<  ||==  ||_//       
|| \\  \\_//  ||_))  \\_//  \_)) ||    ||___ || || || \\ ||___ || \\            
  """
    print(f"{Fore.MAGENTA}{logo}{Style.RESET_ALL}")
    print(f"{Fore.RED}\n\t\t█▒▓­░⡷⠂ DEVELOPED BY FADED ⠐⢾░▒▓█{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}\n\t\t🏴 彡 https://t.me/cyberhood/  彡 🏴 {Style.RESET_ALL}")
    print(f"{Back.RED}\n\t ★ 彡 https://github.com/anonfaded/robospeaker101 彡 ★ {Style.RESET_ALL}") 

def robospeaker():
    while True:
        speed = select_speed() # Select the speech speed
        header() # Printing header part
        lang = select_voice() # Select the language based on voice choice

        while True:
            user_input = input(f"{Fore.GREEN}\nEnter What you want me to speak: {Fore.LIGHTBLACK_EX}(Enter q to quit or 0 for the main menu.){Fore.MAGENTA}\n>>> {Style.RESET_ALL}")
            if user_input.strip() == "q":
                print(f"\n\t{Fore.YELLOW}<<< {Fore.MAGENTA}Bye {Fore.YELLOW}>>>\n{Style.RESET_ALL}")
                return
            elif user_input.strip() == "0":
                print(clear_line * 1000)
                break # Restart the tool
            else:
                tts = gTTS(text=user_input.strip(), lang=lang, slow=False) # Use slow=False to handle speed
                tts.speed = speed # Apply selected speed
                tts.save("temp_audio.mp3")
                os.system("mpv temp_audio.mp3")

                # Prompt user to save the speech
                save_choice = input(f"{Fore.CYAN}\nDo you want to save this speech? {Fore.YELLOW}(y/n){Style.RESET_ALL}: ")
                if save_choice.lower() == "y":
                    print(clear_line * 1000)
                    header()
                    output_file = input(f"{Fore.CYAN}\n\n\n\nEnter the name of the output file {Fore.YELLOW}(e.g., speech.mp3){Style.RESET_ALL}: ")
                    save_audio(output_file, user_input.strip())  
                    print(clear_line * 1000)
                    header()
                    print(f"{Fore.YELLOW}\n\n\t<<< {Fore.GREEN}Speech saved as {Fore.MAGENTA}{output_file} 🎉 {Fore.YELLOW}>>> {Style.RESET_ALL}")
                elif save_choice.lower() != "n":
                    print(clear_line * 1000)
                    header()

if __name__ == '__main__':
    robospeaker()
