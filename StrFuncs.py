from colorama import *
from datetime import datetime
   

init()

def evnt():
    return f"[{Fore.CYAN}~{Style.RESET_ALL}]"

def err():
    return f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Style.RESET_ALL}"

def timenow():
    now = datetime.now()
    nowtime = now.strftime("%H:%M:%S")
    return nowtime