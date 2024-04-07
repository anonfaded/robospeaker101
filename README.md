<div align="center">

# RoboSpeaker 101

**RoboSpeaker 101 is a multi-platform Python tool for text-to-speech conversion with voice selection and audio file saving options. Available for Linux, macOS, Windows, and Android.**

[![GitHub all releases](https://img.shields.io/github/downloads/anonfaded/robospeaker101/total?label=Downloads&logo=github)](https://github.com/anonfaded/robospeaker101/releases/)

</div>

---

## 📱 Screenshots

<div align="center">
    <img src="/img/1.png" style="width: 700px; height: auto;" >
    <br>
    <em>Windows version</em>
    <br><br>
    <img src="/img/2.png" style="width: 700px; height: auto;" >
    <br>
    <em>Linux version</em>
    <br><br>
    </div>
    <details>
        <summary><strong>More Screenshots</strong></summary>
        <img src="/img/3.png" style="width: 700px; height: auto;" >
        <br>
        <img src="/img/4.png" style="width: 700px; height: auto;" >
        <br>
        <img src="/img/5.png" style="width: 700px; height: auto;" >
    </details>


## ⬇️ Download

Download the linux and macOS scripts from the [releases page](https://github.com/anonfaded/robospeaker101/releases/tag/v2.0).


## Features

- **Text-to-Speech Conversion:** Convert typed text into spoken words.
- **Easy Navigation:** Use intuitive input options like 'q' to exit or '0' to return to the main menu.
- **Save Speech Output:** Option to save the generated speech as a file for future reference or sharing.

### windows.py Script Specific Features

- **Engine:** Utilizes pyttsx3.
- **Voice Selection:** Choose between male and female voices.
- **Speech Speed Control:** Adjust the speech speed from slow to high.
- **Platform Compatibility:** Windows only.

### linux+all_platforms.py Script Specific Features

- **Engine:** Utilizes Google Text-to-Speech (gTTS).
- **Voice Selection:** Offers accents for US English and Indian English only.
- **Limited Voice Options**: Only provides male voices.
- **Speech Speed Control:** Not available.
- **Multi-Platform Compatibility:** Can be run on Android, Linux, macOS, and Windows.


## Prerequisites & Installation Guide


### Windows _(windows.py script)_

You can download Python from [python.org](https://www.python.org/downloads/), Git from [git-scm.com](https://git-scm.com/downloads), and MPV from [mpv.io](https://mpv.io/installation/), or just do it directly form the terminal, see next steps:
1. Open Terminal/PowerShell.
2. Install Python, Git, and MPV using the following command:
   ```bash
   winget install Python Git mpv
   ```
3. Agree to the terms of service by typing 'Y' and then pressing Enter.
4. Once the installations are complete, close and reopen Terminal/PowerShell to continue with the next steps, such as cloning the repository.
5. Install the required Python packages:
   ```bash
   pip install colorama pyttsx3
   ```

6. Clone the repository:
    ```bash
    git clone https://github.com/anonfaded/robospeaker101.git
    ```

7. Navigate to the project directory:
    ```bash
    cd robospeaker101
    ```
    **(Tip: In Powershell when you type `cd r`, press the `TAB` button to autocomplete the command)**

8. Run the script:
    ```bash
    python windows.py
    ```


### Linux, macOS, Android, [Windows optional] _(linux+all_platforms.py script)_
1. Open `Terminal`.
    (For android, install Termux from [F-Droid app store](https://f-droid.org/F-Droid.apk))
2. For Debian/Ubuntu-based distributions(using apt), run:

   ```bash
   sudo apt-get install python3 git mpv
   ```
   (For windows, use `winget install Python Git mpv` and for android run `pkg install python git mpv`)

3. Install the required Python packages: 
   ```bash
   pip install colorama gTTS
   ```

4. Navigate to your desktop and clone the repository:

   ```bash
   cd ~/Desktop && git clone https://github.com/anonfaded/robospeaker101.git
   ```
   (For windows, use this instead ` cd ~/Desktop; git clone https://github.com/anonfaded/robospeaker101.git`)

5. Navigate to the project directory: 
   ```bash
   cd robospeaker101
   ```

6. Run the script:
   ```bash
   python linux+all_platforms.py
   ```
   (For linux, use `python3 linux+all_platforms.py` )
   

## Moving Audio Files on Android

If you're using Termux on Android and want to move your RoboSpeaker101 generated audio files, you can use the following command:
(First go to phone `settings` and give `storage permission to Termux` app)

```bash
mv /data/data/com.termux/files/home/robospeaker101 /storage/emulated/0/Download
```
This command will move the entire `robospeaker101` directory to the `Download` folder in your device's internal storage, making it easier to access and manage your audio files.



## Contributions

Contributions to RoboSpeaker 101 are welcomed! Feel free to submit pull requests or open issues to contribute to the project.

