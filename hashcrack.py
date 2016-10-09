import os, sys ,hashlib

print "\n\nUsage: ./hash.py <hash algorithm > <hash> <wordlist>"
print "\n Example: /hash.py <md5 or sha1 or sha256 or sha384 or sha512> <hash> <wordlist>"
print ""
print "[+] ---------------------------------------------------- [+]"	
	
algo=raw_input('Enter Your Algo(md5|sha1|sha256) : ')
pw = raw_input('Enter Your Hash : ')
wordlistw = raw_input('Enter Your Wordlist : ')
try:
  words = open(wordlistw, "r")
except(IOError): 
  print "Error: Check your wordlist path\n"
  sys.exit(1)
words = words.readlines()
print "\n",len(words),"words loaded..."
file=open('cracked.txt','a')
if algo == 'md5':
	for word in words:
		hash = hashlib.md5(word[:-1])
		value = hash.hexdigest()
		if pw == value: 
			print "Password is:",word,"\n"
			file.write("\n Cracked Hashes\n\n")
			file.write(pw+"\t\t")
			file.write(word+"\n")
if algo == 'sha1':
	for word in words:
		hash = hashlib.sha1(word[:-1])
		value = hash.hexdigest()
		if pw == value: 
			print "Password is:",word,"\n"
			file.write("\n Cracked Hashes\n\n")
			file.write(pw+"\t\t")
			file.write(word+"\n")
if algo == 'sha256':
	for word in words:
		hash = hashlib.sha256(word[:-1])
		value = hash.hexdigest()
		if pw == value: 
			print "Password is:",word,"\n"
			file.write("\n Cracked Hashes\n\n")
			file.write(pw+"\t\t")
			file.write(word+"\n")

if algo == 'sha384':
	for word in words:
		hash = hashlib.sha384(word[:-1])
		value = hash.hexdigest()
		if pw == value: 
			print "Password is:",word,"\n"
			file.write("\n Cracked Hashes\n\n")
			file.write(pw+"\t\t")
			file.write(word+"\n")
	
	
if algo == 'sha512':
	for word in words:
		hash = hashlib.sha512(word[:-1])
		value = hash.hexdigest()
		if pw == value: 
			print "Password is:",word,"\n"
			file.write("\n Cracked Hashes\n\n")
			file.write(pw+"\t\t")
			file.write(word+"\n")


