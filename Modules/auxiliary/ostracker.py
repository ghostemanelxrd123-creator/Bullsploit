
#basic module description
def description():
    return "OS fingerprinter"

#basic module rank
def rank():
    return "Good"

#basic module date
def date():
    return "17.04.2026"

#set arguments
def depargs():
    return {
        "host": "IPv4 addr"
    }
#imports
from scapy.all import IP, ICMP, sr1
from StrFuncs import evnt, err, timenow
from colorama import Fore, Style
#main function
def main(ip):
    packet = IP(dst=ip)/ICMP()
    resp = sr1(packet, timeout=2, verbose=False)
    if resp:
        ttl = resp.getlayer(IP).ttl
        if ttl <= 64: return "Linux/Unix/macOS"
        if ttl <= 128: return "Windows"
        if ttl <= 255: return "Cisco/Network Device"
    return "unknown"
#launch func
def launch(args):
    target = args.get("host")
    print(f"{evnt()} Starting scan on {Fore.CYAN}{target}{Style.RESET_ALL} at {Fore.GREEN}{timenow()}{Style.RESET_ALL}")
    os = main(target)
    if os:
        print(f" Results for {target}:")
        print(" OS:", os)
