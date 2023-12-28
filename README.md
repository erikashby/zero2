# Zero2 node

## Device Description
Raspberry Pi Zero 2 W

Operating System: 32 Bit default "Raspberry PI OS" minimal with no desktop

Hostname: ashbypi-zero2
Current IP: (Store) 192.168.1.170

Main account: erika
PwdHint: As**0

Folder structure

main applications /home/erika/app/zero2

## Setup Activity:
- Confirmed RPI was updated
    - sudo app-get update
    - sudo apt-get upgrade
 
    - 
- Established Remote access
    - SSH - On by default from OS setting

## Setup git folder
    - from /home/erika/app
    - git clone "http://github.com/erikashby/rpi1"

    - tested git folder
    - created this README.md
    - from /home/erika/app/rpi1
    - git pull "https://github.com/erikashby/rpi1"


## Installed Flask
    - made sure there was a virtual enviornment
    - from /home/erika/app
    -   sudo apt install python3-venv  << to install virtual enviornment >>
    -    python3 -m venv app << to create the virtual enviornment called app>>
    -   . app/bin/activate  << to activate the virtual enviornment >>

    - Installed flask
        pip install Flask

    - Tested flask
        - added hello.py (see file) and updated raspberry pi
        - from /home/erika/app/rpi1
        - flask --app hello run --host=0.0.0.0
