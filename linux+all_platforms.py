from gtts import gTTS
from colorama import Fore, Style, init, Back
import subprocess


# Initialize colorama
init()

clear_line = "\033[F\033[K"  # Escape codes for clearing one line

def select_voice():
    print(f"\n{Fore.GREEN}\n\n\nSelect a voice:")
    print(f"{Fore.MAGENTA}[1]{Style.RESET_ALL} - English (US accent)")
    print(f"{Fore.MAGENTA}[2]{Style.RESET_ALL} - English (Indian accent)")

    choice = input(f"{Fore.GREEN}\nEnter your choice (1 or 2):{Style.RESET_ALL} ")

    if choice == '1':
        print(clear_line * 1000) #terminal clear
        header()
        print("\n"*2) # line breaks for alignment
        return 'en', 'us'  # US accent
    elif choice == '2':
        print(clear_line * 1000) #terminal clear
        header()
        print("\n"*2)  # line breaks for alignment
        return 'en', 'co.in'  # Indian voice
    

    else:
        print(clear_line * 1000) #terminal clear
        header()
        print(f"{Fore.YELLOW}\n\n\tInvalid choice. Using the default US voice.{Style.RESET_ALL}")
        return 'en', 'us'  # Default to US voice
    


def save_audio(output_file, text, lang, tld):
    tts = gTTS(text=text, lang=lang, tld=tld)
    tts.save(output_file)

def header():
    # Print the logo
    logo = r"""
   __________      ___.           
   \______   \ ____\_ |__   ____  
    |       _//  _ \| __ \ /  _ \ 
    |    |   (  <_> ) \_\ (  <_> )
    |____|_  /\____/|___  /\____/ 
           \/           \/        
                                        __                 
            ____________   ____ _____  |  | __ ___________ 
            /  ___/\____ \_/ __ \\__  \ |  |/ // __ \_  __ \
            \___ \ |  |_> >  ___/ / __ \|    <\  ___/|  | \/
            /____  >|   __/ \___  >____  /__|_ \\___  >__|   101
                \/ |__|        \/     \/     \/    \/        linux v2.0         
  """
    print(f"{Fore.MAGENTA}{logo}{Style.RESET_ALL}")
    print(f"{Fore.RED}\n\t\t█▒▓­░⡷⠂ DEVELOPED BY FADED ⠐⢾░▒▓█{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}\n\t\t🏴 彡 https://t.me/cyberhood/  彡 🏴 {Style.RESET_ALL}")
    print(f"{Back.RED}\n\t ★ 彡 https://github.com/anonfaded/robospeaker101 彡 ★ {Style.RESET_ALL}") 

def robospeaker():
    while True:
        # speed = select_speed() # Select the speech speed
        header() # Printing header part
        lang, tld = select_voice()  # Get selected language and top-level domain 

        while True:
            user_input = input(f"{Fore.GREEN}\nEnter What you want me to speak: {Fore.LIGHTBLACK_EX}(Enter q to quit or 0 for the main menu.){Fore.MAGENTA}\n>>> {Style.RESET_ALL}")
            if user_input.strip() == "q":
                print(f"\n\t{Fore.YELLOW}<<< {Fore.MAGENTA}Bye {Fore.YELLOW}>>>\n{Style.RESET_ALL}")
                return
            elif user_input.strip() == "0":
                print(clear_line * 1000)
                break # Restart the tool
            elif not user_input.strip():  # Check if user input is empty
                print(clear_line * 1000)
                header()
                print(f"{Fore.RED}\n\n\tPlease enter something to speak.{Style.RESET_ALL}")
                continue
            else:
                tts = gTTS(text=user_input.strip(), tld=tld, lang=lang, slow=False) # Use slow=False to handle speed
                # Pipe the audio data directly to mpv
                mpv_process = subprocess.Popen(['mpv', '--no-terminal', '-'], stdin=subprocess.PIPE)
                tts.write_to_fp(mpv_process.stdin)
                mpv_process.stdin.close()

                # Wait for mpv to finish playing
                mpv_process.wait()
                # Add a delay to allow mpv to consume the data before closing the pipe                # tts.speed = speed # Apply selected speed
                # tts.save("temp_audio.mp3")
                # os.system("mpv temp_audio.mp3")

                # Prompt user to save the speech
                save_choice = input(f"{Fore.CYAN}\nDo you want to save this speech? {Fore.YELLOW}(y/n){Style.RESET_ALL}: ")
                if save_choice.lower() == "y":
                    print(clear_line * 1000)
                    header()
                    output_file = input(f"{Fore.CYAN}\n\n\n\nEnter the name of the output file {Fore.YELLOW}(e.g., speech.mp3){Style.RESET_ALL}: ")
                    save_audio(output_file, user_input.strip(), lang, tld)  
                    print(clear_line * 1000)
                    header()
                    print(f"{Fore.YELLOW}\n\n\t\t<<< {Fore.GREEN}Speech saved as {Fore.MAGENTA}{output_file} 🎉 {Fore.YELLOW}>>> {Style.RESET_ALL}")
                elif save_choice.lower() != "y":
                    print(clear_line * 1000)
                    header()
                    print("\n"*2)


if __name__ == '__main__':
    robospeaker()
