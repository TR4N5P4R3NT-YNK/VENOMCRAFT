#!/bin/bash
echo "[*] Updating package lists..."
pkg update -y && pkg upgrade -y

echo "[*] Installing dependencies..."
pkg install -y python git wget curl

echo "[*] Installing Metasploit Framework..."
curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfupdate.sh -o msfinstall.sh
chmod +x msfinstall.sh
./msfinstall.sh

echo "[*] Installing msfvenom and dependencies..."
# msfvenom comes with Metasploit but we verify
which msfvenom &>/dev/null && echo "[✔] msfvenom installed." || echo "[✘] msfvenom missing."

echo "[*] Setup complete. You can now run venomcraft.py"
