#!/usr/bin/env python
from pynput import keyboard
import socket
#IP
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
def on_press(key):
    try:
        #program getting the key user pressed
        print('{0}'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    #program storing the key in message to send to server.py file
    MESSAGE = '{0}'.format(
        key.char)
    s.send(MESSAGE.encode())
    print('Enter direction, followed by speed')
    #using if statements to check when the program should stop taking inputs
    if key.char != 'a' and key.char != 'w' and key.char != 's' and key.char != 'd' and key.char != '1' and key.char != '2' and key.char != '3' and key.char != '4' and key.char != '5':
        return False
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
data = s.recv(BUFFER_SIZE)


#data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
