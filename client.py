import socket
from threading import Thread
from appJar import gui
import json

gui = gui()

def recive_from(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        Display = "\n" + data.decode()
        print(data.decode())
        print(Display)
        gui.setTextArea("Data", Display)
        gui.clearEntry("Input")
    #client.close()

def press(name):
    #global client
    if name == "Close":
        client.close()
        gui.stop()

    elif name == "Send":
        input = gui.getEntry("Input")
        client.sendall(input.encode())



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.20.201.22", 65432))
myThread = Thread(target=recive_from, args=(client,), daemon=True)
myThread.start()


gui.addScrolledTextArea("Data",1,0,4,4)
gui.setTextAreaWidth("Data", 70)
gui.addEntry("Input", 5,0,4,5)
gui.addButtons(["Send", "Close"], press, 5,4)

welcome = f"\n1. Add an object.  2. Show Library.  3. Show Library by media type.  4. Close Library\n Select an option:"
gui.setTextArea("Data", welcome)

gui.go()