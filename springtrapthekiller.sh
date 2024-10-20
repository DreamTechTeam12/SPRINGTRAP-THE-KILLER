#!/bin/bash

check_ffmpeg() {
    # Check if FFmpeg is installed.
    if command -v ffmpeg &> /dev/null; then
        echo "FFmpeg is already installed."
    else
        echo "FFmpeg is not found. Please ensure it is installed correctly."
        exit 1
    fi
}

play_audio() {
    local audio_path="$1"
    local speed="$2"
    # Play audio with speed using ffplay.
    ffplay -nodisp -autoexit -af "atempo=${speed}" "${audio_path}"
}

check_ffmpeg

audio_path='line.wav'
audio_speed=1.0

play_audio "${audio_path}" "${audio_speed}"

# Clear the terminal screen
clear

echo -e "\033[33m" # Set text color to yellow
cat << "EOF"
███████╗██████╗ ██████╗ ██╗███╗   ██╗ ██████╗████████╗██████╗  █████╗ ██████╗     ████████╗██╗  ██╗███████╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██║  ██║██╔════╝    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
███████╗██████╔╝██████╔╝██║██╔██╗ ██║██║  ███╗  ██║   ██████╔╝███████║██████╔╝       ██║   ███████║█████╗      █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██╗██║██║╚██╗██║██║   ██║  ██║   ██╔══██╗██╔══██║██╔═══╝        ██║   ██╔══██║██╔══╝      ██╔═██╗ ╚═╝██║     ██║     ██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║██║ ╚████║╚██████╔╝  ██║   ██║  ██║██║  ██║██║            ██║   ██║  ██║███████╗    ██║  ██╗██╗███████╗███████╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                          

                                                                                                -İntikam, soğuk yenen bir yemektir!
EOF

echo -e "\033[32m" # Set text color to green
cat << "EOF"
1.SMS BOMBER (SIM Söktüren 2.0)
2.EMAIL BOMBER
3.SSH LOGIN
4.ZAYIFLIK TARAYICI (WEB)
5.DATA CHECKER
6.SQL AÇIĞI BULUCU
7.Modülleri Yükle
EOF

read -p ">>>" inputs1

# tools dizinindeki dosyaların tam yollarını kullanın
tool_path="tools/"

if [[ "${inputs1}" == "1" ]]; then
    python3 "${tool_path}simsokturen.py"
elif [[ "${inputs1}" == "2" ]]; then
    python3 "${tool_path}Email_Bombe.py"
elif [[ "${inputs1}" == "3" ]]; then
    python3 "${tool_path}ssh_login.py"
elif [[ "${inputs1}" == "4" ]]; then
    python3 "${tool_path}browser.py"
elif [[ "${inputs1}" == "5" ]]; then
    python3 "${tool_path}data_check.py"
elif [[ "${inputs1}" == "6" ]]; then
    python3 "${tool_path}sqlfinder.py"
elif [[ "${inputs1}" == "7" ]]; then
    pip3 install -r requirements.txt --break-system-packages
fi
