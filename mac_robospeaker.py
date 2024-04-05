import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Faded")
    while True:
        x = input("Enter What you want me to speak: \n")
        if x == "q":
            print("bye")
            os.system("espeak 'See you soon'")
            break
        command = f"espeak {x}"
        os.system(command)
