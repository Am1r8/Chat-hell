print("""\n\n
        __          __     __         ____
  _____/ /_  ____ _/ /_   / /_  ___  / / /
 / ___/ __ \/ __ `/ __/  / __ \/ _ \/ / / 
/ /__/ / / / /_/ / /_   / / / /  __/ / /  
\___/_/ /_/\__,_/\__/  /_/ /_/\___/_/_/   
                                          
\n\n\n""")



import time
import socket
import sys
 
socket_server = socket.socket()
server_host = socket.gethostname()

ip = socket.gethostbyname(server_host)

port = 8080

print('This is your IP address: ',ip)
server_host = input('Enter host\'s IP address: ')
name = input('Enter your username: ')
 
 
socket_server.connect((server_host, port))
 
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' has joined...\n\n')

def send():
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("\nMe : ")
    socket_server.send(message.encode())  

while True:
    try:
        send()
    except:
        print("there is a Problem in the script!")
        time.sleep(5)
        exit()