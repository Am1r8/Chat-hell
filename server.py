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
 
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8080
 
new_socket.bind((host_name, port))
print( "Binding successful!\n")
print("\nThis is your IP: ", s_ip, "\n")
 
name = input('\nEnter name: ')
 
new_socket.listen(1) 
 
 
conn, add = new_socket.accept()
 
print("\nReceived connection from ", add[0])
print('\nConnection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected...\n\n')
 
conn.send(name.encode())

def send():
    message = input('\nMe : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)


while True:
    try:
        send()
    except:
        print("there is a Problem in the script!")
        time.sleep(5)
        exit()