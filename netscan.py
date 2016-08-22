import time
import sys
from subprocess import call

# run nmap scan to examine current network connections, OS, and device name
call(["sudo","nmap", "-sS", "-O","192.168.0.*"])

