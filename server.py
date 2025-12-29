from tkinter import *
from tkinter import ttk
import socket
import threading

HOST = "127.0.0.1"
PORT = 8000
# ------------------------------- Server Start -------------------------------
def start_server():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST,PORT))
            s.listen()
            print (f"Listening on {HOST}:{PORT}\nWaiting for connection")

            conn, addr = s.accept()
            conn.sendall("This is just a text".encode())
            data = conn.recv(1024).decode()
            print(f"<Client> {data}")


            conn.close()
            s.close()
        except OSError:
            print("Server already busy")
# ------------------------------- Server Start -------------------------------

# -------------------------------- Server test --------------------------------
def server_test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall("This is a debug text\n".encode())
    data = s.recv(1024).decode()
    print (f"Message Recived and got responded with\n{data}")
# -------------------------------- Server test --------------------------------

# ------------------------------- Multi-Process -------------------------------
def start_server_threaded():
    threading.Thread(target=start_server, daemon=True).start()

def test_server_threaded():
    threading.Thread(target=server_test, daemon=True).start()
# ------------------------------- Multi-Process -------------------------------


def server_starter():
# ------------------------------------ GUI ------------------------------------
    root = Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    Label = ttk.Label(frame, text="GUI server starter")
    Label.grid(column=1, row=1)

    initiate_button = ttk.Button(frame, text="Initiate Server", command=start_server_threaded)
    initiate_button.grid(column=1, row=2)

    test_button = ttk.Button(frame, text="Server test", command=test_server_threaded)
    test_button.grid(column=1, row=5)

    kill_button = ttk.Button(frame, text="Kill", command=root.destroy)
    kill_button.grid(column=1, row=6)
    root.mainloop()
# ------------------------------------ GUI ------------------------------------

# ------------------------------- Debug section -------------------------------
debug = int(input("> "))
if debug == 1:
    start_server()
elif debug == 2:
    server_test()
elif debug == 3:
    server_starter()
else:
    print ("wrong debug")
# ------------------------------- Debug section -------------------------------
