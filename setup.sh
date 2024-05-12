#!/bin/bash

echo
printf "\033[1;31m"
echo "<<---------------------------------------------------------------------------------->>"
printf '\033[92m'
echo "                   Checking installation......!! Please Wait"
printf "\033[1;31m"
echo "<<---------------------------------------------------------------------------------->>"
sleep 2

# Function to check and install Python 3 if not present
check_python3() {
    if ! command -v python3 &> /dev/null; then
        echo "Python 3 is not installed. Installing Python 3..."
        apt install python3
        echo "Python installation - Done !!"
    fi
}

# Function to check and install the termcolor Python module
check_img2txt() {
    if ! command -v python3 &> /dev/null; then
        echo "Img2Txt is not installed. Installing..."
        apt install jp2a
        echo "Img2Txt installation - Done !!"
    fi
}

check_python3
check_img2txt

echo
echo


echo "All requirements is Satisfied !!"
sleep 1
printf '\033[0;35m'
echo "Setup completed. Enjoy Script Shift Tool!"
printf '\033[91m'
echo -n "Run the "
printf '\033[1;36m'
echo -n "main.py "
printf '\033[91m'
echo -n "file to start script-shift........"
echo
echo
