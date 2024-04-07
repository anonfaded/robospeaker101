<div align="center">

# RoboSpeaker 101

**RoboSpeaker 101 is a Python tool for text-to-speech conversion, offering voice selection and audio file saving options.🔥**

[![GitHub all releases](https://img.shields.io/github/downloads/anonfaded/robospeaker101/total?label=Downloads&logo=github)](https://github.com/anonfaded/robospeaker101/releases/)

</div>

---

## 📱 Screenshots

<div align="center">
<img src="/img/1.jpg" style="width: 700px; height: auto;" >
</div>

## ⬇️ Download

Download the linux and macOS scripts from the [releases page](https://github.com/anonfaded/robospeaker101/releases/tag/v1.0).


## Features

- Text-to-Speech Conversion: Convert typed text into spoken words.
- Voice Selection: Choose between male and female voices for the speech output.
- Speech Speed Control: Adjust the speech speed from slow to high according to preference.
- Easy Navigation: Use intuitive input options like 'q' to exit or '0' to return to the main menu for enhanced user experience.
- Save Speech Output: Option to save the generated speech as a file for future reference or sharing.


## Prerequisites

Before running RoboSpeaker 101, ensure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/)
- pip (usually comes installed with Python)
- [Git](https://git-scm.com/downloads)

## Prerequisites & Installation Guide

### Linux, macOS, Android, (Windows optional)
1. Open `Terminal`.

    (For android, install Termux from [F-Droid app store](https://f-droid.org/F-Droid.apk))

2. Install the required Python packages: 
   ```bash
   pip install colorama gTTS
   ```
   (For android, first install python and git by `pkg install python git` then use the pip command)

3. Clone the repository: 
   ```bash
   git clone https://github.com/anonfaded/robospeaker101.git
   ```

4. Navigate to the project directory: 
   ```bash
   cd robospeaker101
   ```

5. Run the script:
   ```bash
   python linux+all_platforms.py
   ```
   (For linux, use `python3 linux+all_platforms.py` )
   
### Windows

1. Install Python from [python.org](https://www.python.org/downloads/).

2. Open Command Prompt or PowerShell.

3. Install the required Python packages:
   ```bash
   pip install colorama pyttsx3
   ```

4. Clone the repository:
    ```bash
    git clone https://github.com/anonfaded/robospeaker101.git
    ```

5. Navigate to the project directory:
    ```bash
    cd robospeaker101
    ```

6. Run the script:
    ```bash
    python windows.py
    ```