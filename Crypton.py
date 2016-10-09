#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# Toolname        : Crypton.py
# Coder           : Faid Amine < faid3200@gmail.com >
# Version         : 1.2
# greetz for all members of ex D3siprox, X_lucaerd
# 

import sys
import requests
import datetime
import useragent
import errno
import codecs
import time
import itertools
import  subprocess, socket, string, httplib, urlparse, urllib, re, urllib2, random, threading, cookielib
from xml.dom.minidom import parse, parseString
from urlparse import urlparse
from socket import gethostbyaddr
import binascii, sys, time
from time import sleep
import string, os





class colors():

    PURPLE = '\033[95m'

    CYAN = '\033[96m'

    DARKCYAN = '\033[36m'

    BLUE = '\033[94m'

    GREEN = '\033[92m'

    YELLOW = '\033[93m'

    RED = '\033[91m'

    ENDC = '\033[0m'



logo = """

 ######  ########  ##    ## ########  ########  #######  ##    ## 
##    ## ##     ##  ##  ##  ##     ##    ##    ##     ## ###   ## 
##       ##     ##   ####   ##     ##    ##    ##     ## ####  ## 
##       ########     ##    ########     ##    ##     ## ## ## ## 
##       ##   ##      ##    ##           ##    ##     ## ##  #### 
##    ## ##    ##     ##    ##           ##    ##     ## ##   ### 
 ######  ##     ##    ##    ##           ##     #######  ##    ##                                                                                            
 """



choicew = '''

  ######## Web Tools ##########

 1  - Dork Crawler ( collect searching results & test it )
 2  - Subdomain Checker
 3  - Dword to Url
 4  - SQL Fuzzer
 5  - RFI / LFI tester
 6  - Shellshock Auto-exploiter
 7  - Login Bruteforce
 8  - Port Scanner
 9  - XSS Checker
 0  - XSS Tracer
 A  - Auto SQLi Query Maker
 B  - Url Double Encoding or Single Encoding

  ######## Sys Tools ##############
  
 C  - Combine two files (exe files)
 D  - Backdoor Connect 

  ######## Crypto Tools ##############

 E  - Hash Cracker
 F -  Hash Type
 G  - Worlists Creator
 H  - Decode xored Strings
 I  - ShellCode Encoder / Decoder
 J  - Cisco Password Decode
 K  - One Time Cipher Decode
 L  - ROT 13 Decode
 
   ######## Forensic Tools ##############

 M  - Invert Image Color
 N  - Extract Image Data
 O  - DTMF Tones Detect

'''

xline = "#############################################################################################"

xline2 = "####################### Tool Creadted By @FaidAmine (xor00) ############################"



print(colors.BLUE + logo + colors.ENDC)

print (colors.RED + xline2 + colors.ENDC)

print ""

print choicew

print (colors.RED + xline + colors.ENDC)

print ""



user_input =raw_input("Enter your choice (1-10)(A-O) : ")


if "1" in user_input:
   from dorker0xor00 import *

if "2" in user_input:

    from subdomains import *


if "3" in user_input:

  from dword2url import * 



if "4" in user_input:

     from d3sqlfuzz import *


if "5" in user_input:

    from rfixlfi import *




if "6" in user_input:

   from shellshock import *



if "7" in user_input:

 from interfaceattack import * 

if "8" in user_input:
  
   from socket import * 
   import subprocess
   import sys
   from datetime import datetime

   if __name__ == '__main__':
      targetw = raw_input('Enter host to scan: ')
      targetIP = gethostbyname(targetw)
      print "-" * 60
      print "Please wait, Scanning Remote Host", targetIP
      print "-" * 60
      t1 = datetime.now()
       #scan reserved ports
      try:
        
        for port in range(20, 1025):
          s = socket(AF_INET, SOCK_STREAM)

          result = s.connect_ex((targetIP, port))

          if(result == 0) :
            print 'Port %d: OPEN' % (port,)
          s.close()
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



if "9" in user_input:

   from  xsschecker import *

if "0" in user_input:

  from xsstracer import *


if "A" in user_input:

   from autosqlquery import *


if "B" in user_input:
   from doubles import *

   dbl_sgl_encode = raw_input('Enter Your Url  : ')
   
   print "Your Double  Encoded Url " + double_urlencode(dbl_sgl_encode)
   print "Your Single Encoded Url" + single_urlencode(dbl_sgl_encode)


if "C" in user_input:

   var1 = input('1st file: ')
   var2 = input('2nd file: ')


   file1 = open(var1, 'rb')
   file2 = open(var2, 'rb')

   py_file = open('py_file.py', 'w')
   py_file.write('from subprocess import Popen')
   py_file.write('\n')
   py_file.write('file1 =' + str(file1.read()))
   py_file.write('''
   output_file1 = open('output_file1.exe', 'wb' )
   output_file1.write(file1)
   output_file1.close()
   Popen('output_file1.exe')

    ''')

   py_file.write('file2 =' + str(file2.read()))
   py_file.write('''
   output_file2 = open('output_file2.exe', 'wb' )
   output_file2.write(file2)
   output_file2.close()
   Popen('output_file2.exe') ''')


   file1.close()
   file2.close()
   py_file.close()


if "D" in user_input:
    from backconnect import *

    hostx= raw_input('Enter Your Host : ')
    portx= raw_input('Enter Your Port : ')





if "E" in user_input:
  
  from hashcrack import *

  algo=raw_input('Enter Your Algo(md5|sha1|sha256) : ')
  pw = raw_input('Enter Your Hash : ')
  wordlistw = raw_input('Enter Your Wordlist : ')


if "F" in user_input:
    from hashtype import *
    hash = raw_input(" HASH: ")

if "G" in   user_input:
 
   c = raw_input("Enter your character ['$_@125466+'] : ")
   x = raw_input("Enter your max lenth : ")
   file2 = open('dic.txt', 'w')
   res = itertools.product(c, repeat=int(x))
   for i in res:
      file2.write("\n"+"".join(i))
   file2.close()    



if "H" in user_input:
    
   encoded = raw_input('Enter Your Encoded Strings')

   for i in range(0,len(encoded)):
    sys.stdout.write(str(chr(ord(encoded[i])^i))) 
        
if "I" in  user_input:
    from shellcodeencdec import *
   

if "J" in  user_input:

   decrypt=lambda x:''.join([chr(int(x[i:i+2],16)^ord('dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87'[(int(x[:2])+i/2-1)%53]))for i in range(2,len(x),2)])
   cisco_input = raw_input('Enter Your Cisco Password to Crack : ')
   print decrypt(cisco_input)


if "K" in  user_input:
  onetime = raw_input('Decode or Encode : ')
  if "Encode" in onetime:
      ee = raw_input('Enter Your String : ') 
      key = 125
      plaintext = [ ord(x) for x in ee ]
      encode = [ x+key for x in plaintext ]
      print "Encoded String Is : " +"".join(str(x) for x in encode )

  if "Decode" in onetime:
     dd = raw_input('Enter Your String with spaces (xxx xxx xxx) : ')
     key = 125
     cipher = [ int(x) for x in dd.split(' ')]
     decode = [ x-key for x in cipher ]
     print "Decoded String Is : " + "".join(chr(x) for x in decode )


if "L" in  user_input:    
  rot13 = raw_input('Decode or Encode : ')
  if "Encode" in rot13:
    rot13_encode = raw_input('Enter Your String to Encode :')
    ee  = codecs.encode(rot13_encode, 'rot_13')
    print " Your Encoded String is : " + ee
  elif "Decode" in rot13:
    rot13_decode = raw_input('Enter Your String to Decode :')
    dd  = codecs.encode(rot13_decode, 'rot_13')
    print " Your Decoded String is : " +  dd

if "M" in  user_input:  
  import Image
  if __name__ == '__main__':
     yours = raw_input('Enter Your Image To Invert : ')
     img = Image.open(yours)
     in_pixels = list(img.getdata())
     out_pixels = list()
 
     for i in range(len(in_pixels)):
        r = in_pixels[i][0]
        g = in_pixels[i][1]
        b = in_pixels[i][2]
        out_pixels.append( (255-r, 255-g, 255-b) )
 
     out_img = Image.new(img.mode, img.size)
     out_img.putdata(out_pixels)
     out_img.save("output_inverted.png", "PNG")

if "N" in  user_input:
  import re,os
  m_image = raw_input('Enter Your Image : ')
  data = open(m_image, 'rb').read()

  def findndx(str, data):
    return [m.start() for m in re.finditer(str, data)]

  ext = {
    '.gif': 'GIF89a',
    '.png': '\x89PNG',
    '.bmp': 'BM',
    '.jpg': '\xFF\xD8\xFF\xE0'
  }
  os.system('mkdir ImageOutput')
  for ext, pat in ext.iteritems():
    for n in findndx(pat, data):
        open('ImageOutput/out.' + str(n) + ext, 'wb').write(data[n:])
  

if "O" in  user_input:
   from dtmf import *























