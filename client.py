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
        elif data == b'quit':
            break
        Display = "\n" + data.decode()
        gui.setTextArea("Data", Display)
        gui.clearEntry("Input")
    #client.close()

def press(name):
    #global client
    if name == "Close":
        client.sendall(b'quit')
        myThread.join()
        client.close()
        gui.stop()

    elif name == "Send":
        input = gui.getEntry("Input")
        client.sendall(input.encode())

gui.addScrolledTextArea("Data",1,0,4,4)
gui.setTextAreaWidth("Data", 70)
gui.addEntry("Input", 5,0,4,5)
gui.addButtons(["Send", "Close"], press, 5,4)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.20.201.140", 65432))
myThread = Thread(target=recive_from, args=(client,), daemon=True)
myThread.start()

gui.go()
