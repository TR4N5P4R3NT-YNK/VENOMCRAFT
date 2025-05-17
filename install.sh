#!/bin/bash

echo "[*] Updating package lists..."
pkg update -y && pkg upgrade -y

echo "[*] Installing dependencies..."
pkg install -y wget git curl python

echo "[*] Installing Metasploit Framework from community script..."
cd $HOME
wget https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh -O metasploit.sh

chmod +x metasploit.sh
bash metasploit.sh

echo "[*] Checking if msfvenom is installed..."
if command -v msfvenom >/dev/null 2>&1; then
    echo "[✔] msfvenom installed successfully."
else
    echo "[✘] msfvenom not found."
    echo "Try running: bash metasploit.sh manually, or restart Termux and try again."
fi

echo "[*] Setup complete. Run: python venomcraft.py"
