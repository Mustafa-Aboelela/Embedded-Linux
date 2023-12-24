import keyboard
import subprocess
def on_triggered():
    subprocess.run(['nautilus','/home/mustafa_mohamed/'])

def listen_shortcut():
    shortcut = "ctrl + alt + s"
    keyboard.add_hotkey(shortcut,on_triggered)
    
    #listen for keyboard
    keyboard.wait()
    
listen_shortcut()        