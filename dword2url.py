#!/usr/bin/env python


from urlparse import urlparse
from socket import gethostbyaddr

print """----- menu -----
1: dword -> url
2: url -> dword
3: quit
----------------"""
choicea = raw_input("Choice: ")

if choicea=="1":
    # DWORD->URL
    url = raw_input("DWORD to convert? Valid examples are\n http://1079984325/foo/bar or just 1079984325: ")
    scheme = urlparse(url).scheme
    host = urlparse(url).netloc
    path = urlparse(url).path
    if host == '':
        # scheme not specified (http, https, ftp, ...) e.g. "1079984325"
        (scheme, host, path) = ('http', path, '')
    hx = "%X" % int(host)
    ip = []
    for i in range(0, 4):
        ip.append(str(int(hx[i*2:i*2+2], 16)))
    print "==> %s://%s%s" % (scheme, ".".join(ip), path)

elif choicea=="2":
    # URL->DWORD
    url = raw_input("URL to convert? (e.g. http://www.dword.com/foo/bar/): ")
    scheme = urlparse(url).scheme
    host = urlparse(url).netloc
    path = urlparse(url).path
    ip = gethostbyaddr(host)[2][0]
    print "==> %s resolves to: %s" % (host, ip)
    hx = ''
    for i in ip.split('.'):
        if len("%X" % int(i))==1:
            hx += "0%X" % int(i)
        else:
            hx += "%X" % int(i)
    print "==> %s://%s%s" % (scheme, int(hx, 16), path)

elif choicea=="3":
    print "Good bye!\n"

