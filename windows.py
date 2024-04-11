import pyttsx3
from colorama import Fore, Style, init, Back
import os

# Initialize colorama
init()

clear_line = "\033[F\033[K"  # Escape codes for clearing one line

# Now, you can use clear_line in a print statement and multiply it as needed
# print(clear_line * 2)  # This will clear two lines
# print(clear_line * 3)  # This will clear three lines


def select_voice():
    print(f"\n{Fore.GREEN}\n\n\nSelect a voice:")
    print(f"{Fore.MAGENTA}[1]{Style.RESET_ALL} - Male")
    print(f"{Fore.MAGENTA}[2]{Style.RESET_ALL} - Female")
    choice = input(f"{Fore.GREEN}\nEnter your choice (1 or 2):{Style.RESET_ALL} ")
    if choice == '1':
        print(clear_line * 1000)
        header()
        print("\n"*2) # line breaks for alighnment
    elif choice == '2':
        print(clear_line * 1000)
        header()
        print("\n"*2)  # line breaks for alighnment
    elif choice not in ['1', '2']:
        print(clear_line * 1000)
        header()
        print(f"{Fore.YELLOW}\n\n\tWell, well, well... Are you trying to hack into my system, huh? 🤔\n\tUsing the default voice instead.\n{Style.RESET_ALL}")
        return '1'  # Use default male voice if invalid choice is entered
    return choice

def select_speed():
    print(f"{Fore.GREEN}Select speech speed:")
    print(f"{Fore.MAGENTA}[1]{Style.RESET_ALL} - Slow")
    print(f"{Fore.MAGENTA}[2]{Style.RESET_ALL} - Medium (Default)")
    print(f"{Fore.MAGENTA}[3]{Style.RESET_ALL} - Fast")
    speed_choice = input(f"{Fore.GREEN}\nEnter your choice (1, 2, or 3):{Style.RESET_ALL} ")
    if speed_choice == "1":
        print(clear_line * 1000) #terminal clear
        header()
        print("\n"*2) # line breaks for alignment
        return 130  # Slow
    elif speed_choice == "2":
        print(clear_line * 1000) #terminal clear
        header()
        print("\n"*2) # line breaks for alignment
        return 170 # Medium
    elif speed_choice == "3":
        print(clear_line * 1000) #terminal clear
        header()
        print("\n"*2) # line breaks for alignment
        return 207  # Fast
    else:
        print(clear_line * 1000) #terminal clear
        header()
        print(f"{Fore.YELLOW}\n\n\tUh-oh! Default speed (Medium) will be selected.{Style.RESET_ALL}")
        return 170  # Medium (Default)

def save_audio(output_file, text, voice):
    # Create the output folder if it doesn't exist
    audio_folder = "Audios"
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set the voice for the engine
    engine.setProperty('voice', voice)
    
    # Define the full path to the output file within the audio folder
    full_output_path = os.path.join(audio_folder, output_file)
    
    # Save the speech as an audio file
    engine.save_to_file(text, full_output_path)
    
    # Wait for the speech to be saved
    engine.runAndWait()

def header():
    # Print the logo
    logo = r"""
   __________      ___.           
   \______   \ ____\_ |__   ____  
    |       _//  _ \| __ \ /  _ \ 
    |    |   (  <_> ) \_\ (  <_> )
    |____|_  /\____/|___  /\____/ 
           \/           \/              __                 
            ____________   ____ _____  |  | __ ___________ 
            /  ___/\____ \_/ __ \\__  \ |  |/ // __ \_  __ \
            \___ \ |  |_> >  ___/ / __ \|    <\  ___/|  | \/
            /____  >|   __/ \___  >____  /__|_ \\___  >__|  101
                 \/ |__|        \/     \/     \/    \/      windows v2.1         
  """
    print(f"{Fore.MAGENTA}{logo}{Style.RESET_ALL}")
    print(f"{Fore.RED}\n\t\t█▒▓­░⡷⠂ DEVELOPED BY FADED ⠐⢾░▒▓█{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}\n\t\t🏴 彡 https://t.me/cyberhood  彡 🏴 {Style.RESET_ALL}")
    print(f"{Back.RED}\n\t ★ 彡 https://github.com/anonfaded/robospeaker101 彡 ★ {Style.RESET_ALL}") 



def robospeaker():
    while True:
        header() # Printing header part
        choice = select_voice()
        speed = select_speed()

        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # Get all available voices
        voices = engine.getProperty('voices')

        # Set the voice based on user's choice
        if choice == "1":
            engine.setProperty('voice', voices[0].id)  # Select male voice
        elif choice == "2":
            engine.setProperty('voice', voices[1].id)  # Select female voice

        while True:
            user_input = input(f"{Fore.GREEN}\nEnter What you want me to speak: {Fore.LIGHTBLACK_EX}(Enter q to quit or 0 for the main menu.){Fore.MAGENTA}\n>>> {Style.RESET_ALL}")
            if user_input.strip() == "q":
                print(f"\n\t{Fore.MAGENTA}<<< {Fore.YELLOW}Bye {Fore.MAGENTA}>>>\n{Style.RESET_ALL}")
                engine.say("Goodbye")
                engine.runAndWait()
                return
            elif user_input.strip() == "0":
                print(clear_line * 1000)
                break # Restat the tool
            elif not user_input.strip():  # Check if user input is empty
                print(clear_line * 1000)
                header()
                print(f"{Fore.RED}\n\n\t\tPlease enter something to speak.{Style.RESET_ALL}")
                continue
            else:
                engine.setProperty('rate', speed)  # Adjust the rate of speech
                engine.say(user_input.strip())
                engine.runAndWait()

                # Prompt user to save the speech
                save_choice = input(f"{Fore.CYAN}\nDo you want to save this speech? {Fore.YELLOW}(y/n){Style.RESET_ALL}: ")
                # print(clear_line * 7)
                if save_choice.lower() == "y":
                    
                    print(clear_line * 1000)
                    header()
                    output_file = input(f"{Fore.CYAN}\n\n\n\nEnter the name of the output file {Fore.YELLOW}(e.g., speech.wav){Style.RESET_ALL}: ")
                    save_audio(output_file, user_input.strip(), choice)  
                    print(clear_line * 1000)
                    header()
                    print(f"{Fore.MAGENTA}\n\n\t<<< {Fore.GREEN}Speech saved in folder: {Fore.YELLOW}Audios{Fore.MAGENTA}{Fore.GREEN}, as {Fore.YELLOW}{output_file} 🎉 {Fore.MAGENTA}>>> {Style.RESET_ALL}")
                elif save_choice.lower() != "y":
                    print(clear_line * 1000)
                    header()
                    print("\n"*2)   


if __name__ == '__main__':
    robospeaker()
