# Invisible Backdoor

## What's about this python3 project:
Backdoor with shell access with python (Using lib subproccess as main functions...), in the main mode (.py) you can execute by terminal and it will make the cmd/prompt VERY, VERY SMALL, but there's the executable in .pyw, who makes the proccess running invisible, like a real backdoor needs to be.

## Usage for server-owner
> Remember, use it for educational purposes and sockets learning/python3.

```
python Serverzeira.py (starts the server, and waits for a connection from the client)
```

## Usage for client-side
### First Way
```
Open CMD.exe
python ClientTCPIP.py
```
### Second Way (Easily and 100% hidden)
```
Double click at ClientTCPIP.pyw
```

## Requirements

Python3 instaled in both machines.

## Configuration

Serverzeira.py - Where are s.bind(('192.168.1.7')) you change it for another people external ip
ClientTCPIP.py - Where are s.connect((192.168.1.7)) change for your external ip.

Work better in some closed network with dhcp, 192.168.1.2 ~ 192.168.1.24 in home/corporative networks.


