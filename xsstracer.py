#!/usr/bin/python

import socket
import time
import sys, getopt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main(argv):
	

	target = raw_input('Enter Your Target : ') # SET TARGET
	port = raw_input('Enter Your Port : ')  # SET PORT

	buffer1 = "TRACE / HTTP/1.1"
	buffer2 = "Test: <script>alert(1);</script>"
	buffer3 = "Host: " + target

	print ""
	print bcolors.OKBLUE + "+ -- --=[Target: " + target + ":" + port + "]=-- -- +"

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result=s.connect_ex((target,int(port)))
	s.settimeout(1.0)

	if result == 0:
		s.send(buffer1 + "\n")
		s.send(buffer2 + "\n")
		s.send(buffer3 + "\n\n")
		data = s.recv(1024)
		script = "alert"
		if script.lower() in data.lower():
			print bcolors.FAIL + "+ -- --=[Site vulnerable to XST!" + bcolors.ENDC
			print ""
			print bcolors.WARNING + data + bcolors.ENDC
		else:
			print bcolors.OKGREEN + "+ -- --=[Site not vulnerable to XST!"
			print ""
			print ""

	else:
		print bcolors.WARNING + "+ -- --=[Port is closed!" + bcolors.ENDC

	s.close()

main(sys.argv)
