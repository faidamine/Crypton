#!/usr/bin/python

import binascii, sys, time

RED = '\033[31m'
WHITE = '\033[37m'
RESET = '\033[0;0m'

def main():
	print "shellcode hex encode decoder"
	print "what do you want to do ? %sencode%s / %sdecode%s" % (RED, RESET, WHITE, RESET)
	q = raw_input("=> ")

	if q == "encode": 
		inputtype = raw_input("Please input data : ")
		print "shellcode => ",
		for encoded in inputtype:
			print "\b\\x"+encoded.encode("hex"),
			sys.stdout.flush()
			time.sleep(0.5)
			print RESET

	elif q == "decode":
		inputtype = raw_input("Please input data : ")
		cleaninput = inputtype.replace("\\x","")
		print "hex       => ",cleaninput
		print "plaintext => ",
		print "\b"+cleaninput.decode("hex")

	else:
		print "wrong answer ! your choice is %sencode%s or %sdecode%s" % (RED, RESET, WHITE, RESET)
		sys.exit(1)		

main()
