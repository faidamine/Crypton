


import sys, os, time, socket

if sys.platform == 'linux' or sys.platform == 'linux2':
	clearing = 'clear'
else:
	clearing = 'cls'
os.system(clearing)


subdomains = ['adm','admin','admins','agent','aix','alerts','av','antivirus','app','apps','appserver','archive','as400','auto','backup','banking','bbdd','bbs','bea','beta','blog','catalog','cgi','channel','channels','chat','cisco','client','clients','club','cluster','clusters','code','commerce','community','compaq','conole','consumer','contact','contracts','corporate','ceo','cso','cust','customer','cpanel','data','bd','db2','default','demo','design','desktop','dev','develop','developer','device','dial','digital','dir','directory','disc','discovery','disk','dns','dns1','dns2','dns3','docs','documents','domain','domains','dominoweb','download','downloads','ecommerce','e-commerce','edi','edu','education','email','enable','engine','engineer','enterprise','error','event','events','example','exchange','extern','external','extranet','fax','field','finance','firewall','forum','forums','fsp','ftp','ftp2','fw','fw1','gallery','galleries','games','gateway','gopher','guest','gw','hello','helloworld','help','helpdesk','helponline','hp','ibm','ibmdb','ids','ILMI','images','imap','imap4','img','imgs','info','intern','internal','intranet','invalid','iphone','ipsec','irc','ircserver','jobs','ldap','link','linux','lists','listserver','local','localhost','log','logs','login','lotus','mail','mailboxes','mailhost','management','manage','manager','map','maps','marketing','device','media','member','members','messenger','mngt','mobile','monitor','multimedia','music','my','names','net','netdata','netstats','network','news','nms','nntp','ns','ns1','ns2','ns3','ntp','online','openview','oracle','outlook','page','pages','partner','partners','pda','personal','ph','pictures','pix','pop','pop3','portal','press','print','printer','private','project','projects','proxy','public','ra','radio','raptor','ras','read','register','remote','report','reports','root','router','rwhois','sac','schedules','scotty','search','secret','secure','security','seri','serv','serv2','server','service','services','shop','shopping','site','sms','smtp','smtphost','snmp','snmpd','snort','solaris','solutions','support','source','sql','ssl','stats','store','stream','streaming','sun','support','switch','sysback','system','tech','terminal','test','testing','testing123','time','tivoli','training','transfers','uddi','update','upload','uploads','video','vpn','w1','w2','w3','wais','wap','web','webdocs','weblib','weblogic','webmail','webserver','webservices','websphere','whois','wireless','work','world','write','ws','ws1','ws2','ws3','www1','www2','www3']

R = "\033[31m";
G = "\033[32m";


domaino = raw_input("Enter Your Taget : ")

def logo():
	print G+"\n|---------------------------------------------------------------|" 
	print "    |                SubDomain Brute Forcing Tool                   |"
        print "|---------------------------------------------------------------|\n"
	print "\n[-] %s\n" % time.strftime("%X")
	
	
logo()

w00t = 0
print "Checking for subdomains\n"
for sub in subdomains:
	subdomain = sub + '.' + domaino
	try:
		targeto = socket.gethostbyname(subdomain)
		w00t = w00t+1
		print R+subdomain
	except:
		pass
print G+"\nFound %s subdomain(s)." % w00t
