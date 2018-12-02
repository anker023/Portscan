#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
#Note: Edit loop for checking ports..
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_menu():
    print bcolors.OKGREEN + " _____           _      _____                 "
    print bcolors.OKGREEN + "|  __ \         | |    / ____|                "
    print bcolors.OKGREEN + "| |__) |__  _ __| |_  | (___   ___ __ _ _ __  "
    print bcolors.OKGREEN + "|  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \ "
    print bcolors.OKGREEN + "| |  | (_) | |  | |_   ____) | (_| (_| | | | |"
    print bcolors.OKGREEN + "|_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|"
    print bcolors.OKGREEN + "Simple Port scan by Diogo V1T0R"
    print bcolors.HEADER + "1337. Port Scan"
    print bcolors.HEADER + "quit. It's nice to scan why you left"

loop=True

while loop:
    print_menu()
    choice = raw_input("Menu options: ")
    if choice=="1337":

	subprocess.call('clear', shell=True)

	remoteServer    = raw_input("Enter a remote host to scan: ")
	remoteServerIP  = socket.gethostbyname(remoteServer)
	
	print "-" * 60
	print "Please wait, scanning remote host", remoteServerIP
	print "-" * 60

	t1 = datetime.now()


	try:
	    for port in range(1,512): 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.05)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
		    print "Port {}: 	 Open  |  IP: {} ".format(port, remoteServerIP)
		sock.close()

	except KeyboardInterrupt:
	    print "You pressed Ctrl+C"
	    sys.exit()

	except socket.gaierror:
	    print 'Hostname could not be resolved. Exiting'
	    sys.exit()

	except socket.error:
	    print "Couldn't connect to server"
	    sys.exit()

	t2 = datetime.now()

	total =  t2 - t1

	print 'Scanning Completed in: ', total
        #1loop=False
    elif choice=="quit":
        loop=False
    else:
        raw_input("Try again...")
