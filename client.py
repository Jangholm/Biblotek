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
        Display = data.decode() + "\n"
        gui.setTextArea("Data", Display)
        gui.clearEntry("Input")


def press(name):
    global client
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
client.connect(("192.168.1.227", 65432))
myThread = Thread(target=recive_from, args=(client,), daemon=True)
myThread.start()

gui.go()
