import os

def robospeaker():
    logo = """\033[31m
_____  _____  ____   _____    __ _____ _____  ___  __ __ _____ _____    101
||_// ((   )) ||=)  ((   ))  ((  ||_// ||==  ||=|| ||<<  ||==  ||_//       
|| \\\  \\\_//  ||_))  \\\_//  \_)) ||    ||___ || || || \\\ ||___ || \\\            
  \033[1;31m\n\t\t\tDeveloped by Faded\033[0m
\033[1;35m\n\t\t✨ https://github.com/anonfaded/robospeaker101 ✨\033[0m
                                                             \033[0m"""
    print(logo)
    while True:
        user_input = input("\033[1;32m\nEnter What you want me to speak: \033[1;30m(or type q to exit)\033[1;35m\n>>> \033[0m")
        if user_input.strip() == "q":
            print("\n\t\033[1;31m<<< \033[1;31mBye >>>\n\033[0m")
            os.system("espeak 'See you soon'")
            break
        else:
            os.system(f"espeak '{user_input.strip()}'")

if __name__ == '__main__':
    robospeaker()






# import os

# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1 Created by Faded")
#     while True:
#         x = input("Enter What you want me to speak: \n")
#         if x == "q":
#             print("bye")
#             os.system("espeak 'See you soon'")
#             break
#         command = f"espeak {x}"
#         os.system(command)








# This below code is only for macOS 
#         if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1 Created by Faded")
#     while True:
#         x = input("Enter What you want me to speak: ")
#         if x == "q":
#             os.system("say 'Bye bye friend'")
#             break
#         command = f"say {x}"
#         os.system(command)