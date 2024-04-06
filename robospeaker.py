import pyttsx3
from colorama import Fore, Style, init

# Initialize colorama
init()

def select_voice():
    print(f"\n{Fore.GREEN}Select a voice:")
    print(f"{Fore.MAGENTA}[1]{Style.RESET_ALL} - Male")
    print(f"{Fore.MAGENTA}[2]{Style.RESET_ALL} - Female")
    choice = input(f"{Fore.GREEN}Enter your choice (1 or 2):{Style.RESET_ALL} ")
    return (choice)

def save_audio(output_file, text, voice):
    engine = pyttsx3.init()
    
    engine.setProperty('voice', id)  
    engine.save_to_file(text, output_file)
    engine.runAndWait()




def robospeaker():
    logo = r"""
_____  _____  ____   _____    __ _____ _____  ___  __ __ _____ _____    101
||_// ((   )) ||=)  ((   ))  ((  ||_// ||==  ||=|| ||<<  ||==  ||_//       
|| \\  \\_//  ||_))  \\_//  \_)) ||    ||___ || || || \\ ||___ || \\            
  """
    print(f"{Fore.MAGENTA}{logo}{Style.RESET_ALL}")
    print(f"{Fore.RED}\n\t\t█▒▓­░⡷⠂ DEVELOPED BY FADED ⠐⢾░▒▓█{Style.RESET_ALL}")
    print(f"{Fore.RED}\n\t★ 彡 https://github.com/anonfaded/robospeaker101 彡 ★ {Style.RESET_ALL}")
    choice = select_voice()
    
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()

    # Get all available voices
    voices = engine.getProperty('voices')

    # Set the voice based on user's choice
    if choice == "1":
        engine.setProperty('voice', voices[0].id)  # Select male voice
    elif choice == "2":
        engine.setProperty('voice', voices[1].id)  # Select female voice
    else:
        print(f"{Fore.YELLOW}Well, well, well... Are you trying to hack into my system, huh? 🤔 Using the default voice instead.{Style.RESET_ALL}")
        engine.setProperty('voice', voices[0].id)  # Use default male voice

    while True:
        user_input = input("\033[1;32m\nEnter What you want me to speak: \033[1;30m(or type q to exit)\033[1;35m\n>>> \033[0m")
        if user_input.strip() == "q":
            print("\n\t\033[1;31m<<< \033[1;31mBye >>>\n\033[0m")
            engine.say("See you soon")
            engine.runAndWait()
            break
        else:
            engine.say(user_input.strip())
            engine.runAndWait()

            # Prompt user to save the speech
            save_choice = input(f"{Fore.CYAN}\nDo you want to save this speech? {Fore.LIGHTYELLOW_EX}(y/n){Style.RESET_ALL}: ")
            if save_choice.lower() == "y":
                output_file = input(f"{Fore.CYAN}\nEnter the name of the output file {Fore.LIGHTYELLOW_EX}(e.g., speech.wav){Style.RESET_ALL}: ")
                save_audio(output_file, user_input.strip(), choice)  
                print(f"{Fore.YELLOW}\n\t<<< {Fore.GREEN}Speech saved as {Fore.MAGENTA}{output_file} 🎉 {Fore.YELLOW}>>> {Style.RESET_ALL}")


if __name__ == '__main__':
    robospeaker()


