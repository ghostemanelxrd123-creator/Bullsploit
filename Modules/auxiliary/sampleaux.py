
#basic module description
def description():
    return "Standard auxiliary (Multithread scaner)"

#basic module rank
def rank():
    return "Good"

#basic module date
def date():
    return "08.03.2026"

#set arguments
def depargs():
    return {
        "host": "IPv4 addr",
        "range": "Port diapasone",
        "threads": "Number of threads"
    }
#imports
from StrFuncs import evnt, err, timenow
import socket
from colorama import Fore, Style
from threading import Semaphore, Thread
import json
import os

#main function
def main(ip, port, semaphore, services):
    with semaphore:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            res = s.connect_ex((ip, port))
            if res == 0:
                servicename = services.get(str(port), "UNKNOWN")
                print(f"{Fore.YELLOW}[{Style.RESET_ALL}{timenow()}{Fore.YELLOW}] {Style.RESET_ALL}Port{Fore.CYAN} {port} {Style.RESET_ALL}is opened on service{Fore.GREEN} {servicename}{Style.RESET_ALL}")
            s.close()
        except:
            pass
#launch func
def launch(args):
    try:
        basepath = os.path.dirname(__file__)
        servpath = os.path.join(basepath, "Services.json")
        if not os.path.exists(servpath):
            print(f"{err()} Services data not found!")
            return
        try:
            with open(servpath, "r", encoding="utf-8") as f:
                services = json.load(f)
        except Exception as b:
            print(f"{err()} {b}")
            services = {}
        target = args.get("host")
        portrange = args.get("range")
        threadcount = int(args.get("threads", 10))
        try:
            startp, endp = map(int, portrange.split("-"))
        except:
            print(f"{err()} Invalid range format")
        print(f"{evnt()} Starting scan on {Fore.CYAN}{target}{Style.RESET_ALL} at {Fore.GREEN}{timenow()}{Style.RESET_ALL}")
        sem = Semaphore(threadcount)
        threads = []
        for port in range(startp, endp + 1):
            t = Thread(target=main, daemon=True, args=(target, port, sem, services))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
        print(f"{evnt()} Scan successfully finished!")
    except RuntimeError:
        pass